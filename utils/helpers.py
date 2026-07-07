def parse_ports(port_range):
    """
    Convertit un port unique (ex : 80)
    ou une plage de ports (ex : 20-100)
    en une liste de ports.
    """

    try:

        # Cas d'un seul port
        if "-" not in port_range:

            port = int(port_range)

            if port < 1 or port > 65535:
                raise ValueError

            return [port]

        # Cas d'une plage
        start, end = port_range.split("-")

        start = int(start)
        end = int(end)

        if start > end:
            raise ValueError

        if start < 1 or end > 65535:
            raise ValueError

        return list(range(start, end + 1))

    except ValueError:

        raise ValueError(
            "Format invalide. Utilisez par exemple : 80 ou 20-100"
        )
    
def security_level(score):

    if score >= 80:
        return "EXCELLENT"

    if score >= 60:
        return "BON"

    if score >= 40:
        return "MOYEN"

    return "FAIBLE"