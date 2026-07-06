import socket


def scan_port(host, port, timeout=1):
    """
    Vérifie si un port TCP est ouvert.

    Paramètres :
        host (str) : nom de domaine ou adresse IP
        port (int) : numéro du port
        timeout (int) : délai maximal en secondes

    Retour :
        tuple (port, état)
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(timeout)

    try:

        result = sock.connect_ex((host, port))

        if result == 0:
            status = "OUVERT"

        else:
            status = "FERMÉ"

    except socket.timeout:
        status = "FILTRÉ"

    except socket.gaierror:
        status = "HÔTE INTROUVABLE"

    except Exception as e:
        status = f"ERREUR : {e}"

    finally:
        sock.close()

    return port, status