import ssl
import socket
from datetime import datetime


def check_tls(host, port=443):
    """
    Vérifie le certificat TLS d'un serveur.
    """

    context = ssl.create_default_context()

    try:

        with socket.create_connection((host, port), timeout=5) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=host
            ) as secure_socket:

                certificate = secure_socket.getpeercert()

        expiration = datetime.strptime(
            certificate["notAfter"],
            "%b %d %H:%M:%S %Y %Z"
        )

        today = datetime.utcnow()

        days_left = (expiration - today).days

        issuer = certificate["issuer"]

        issuer_name = ""

        for item in issuer:

            for key, value in item:

                if key == "organizationName":

                    issuer_name = value

        return {

            "valid": True,

            "issuer": issuer_name,

            "expires": expiration.strftime("%d/%m/%Y"),

            "days_left": days_left

        }

    except ssl.SSLError:

        return {

            "valid": False,

            "error": "Certificat invalide"

        }
    except socket.timeout:

        return {
            "valid": False,
            "error": "Le serveur n'a pas répondu avant le délai imparti."
        }

    except Exception as e:

        return {

            "valid": False,

            "error": str(e)

        }