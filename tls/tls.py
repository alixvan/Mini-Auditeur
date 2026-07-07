import ssl
import socket
from datetime import datetime
from urllib.parse import urlparse


def check_tls(url):
    """
    Vérifie le certificat TLS d'une URL HTTPS.
    """

    parsed = urlparse(url)

    if parsed.scheme != "https":

        return {
            "valid": False,
            "error": "Le site n'utilise pas HTTPS."
        }

    host = parsed.hostname

    context = ssl.create_default_context()

    try:

        with socket.create_connection((host, 443), timeout=5) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=host
            ) as secure_socket:

                cert = secure_socket.getpeercert()

        expiration = datetime.strptime(
            cert["notAfter"],
            "%b %d %H:%M:%S %Y %Z"
        )

        today = datetime.utcnow()

        days_left = (expiration - today).days

        issuer = ""

        for group in cert["issuer"]:

            for key, value in group:

                if key == "organizationName":

                    issuer = value

        return {

            "valid": True,

            "issuer": issuer,

            "expires": expiration.strftime("%d/%m/%Y"),

            "days_left": days_left

        }

    except socket.timeout:

        return {

            "valid": False,

            "error": "Connexion TLS expirée (timeout)."

        }

    except ssl.SSLError:

        return {

            "valid": False,

            "error": "Certificat SSL invalide."

        }

    except Exception as e:

        return {

            "valid": False,

            "error": str(e)

        }