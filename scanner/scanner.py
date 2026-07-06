from concurrent.futures import ThreadPoolExecutor

from scanner.tcp import scan_port


def scan_ports(host, ports, max_workers=100):
    """
    Scanne plusieurs ports en parallèle.

    Paramètres
    ----------
    host : str
        Adresse IP ou nom d'hôte.

    ports : iterable
        Liste ou range de ports.

    max_workers : int
        Nombre maximum de threads.

    Retour
    ------
    list
        Liste de tuples (port, statut).
    """

    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:

        futures = [
            executor.submit(scan_port, host, port)
            for port in ports
        ]

        for future in futures:

            results.append(future.result())

    return sorted(results)