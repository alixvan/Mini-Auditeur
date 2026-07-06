def parse_ports(port_range):
    """
    Convertit une chaîne comme '20-100'
    en une liste de ports.
    """

    try:

        start, end = port_range.split("-")

        start = int(start)
        end = int(end)

        if start > end:
            raise ValueError

        return range(start, end + 1)

    except ValueError:
        raise ValueError(
            "Format invalide. Utilisez par exemple : 20-100"
        )
    

def security_level(score):

    if score >= 80:
        return "EXCELLENT"

    if score >= 60:
        return "BON"

    if score >= 40:
        return "MOYEN"

    return "FAIBLE"    