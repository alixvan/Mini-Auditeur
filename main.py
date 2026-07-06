import argparse

from scanner.tcp import scan_port

def create_parser():
    """
    Crée et configure les arguments de la ligne de commande.
    """

    parser = argparse.ArgumentParser(
        description="Mini Auditeur de Sécurité"
    )

    parser.add_argument(
        "--host",
        required=True,
        help="Nom de domaine ou adresse IP à scanner"
    )

    parser.add_argument(
        "--ports",
        default="1-1024",
        help="Plage de ports à scanner (exemple : 20-100)"
    )

    parser.add_argument(
        "--url",
        required=True,
        help="URL à analyser"
    )

    parser.add_argument(
        "--output",
        default="rapports/rapport.md",
        help="Nom du fichier de rapport"
    )

    return parser


def main():

    parser = create_parser()

    args = parser.parse_args()

    print("\n===== PARAMÈTRES REÇUS =====")

    print(f"Cible : {args.host}")
    print(f"Ports : {args.ports}")
    print(f"URL : {args.url}")

    print("\n===== TEST D'UN PORT =====")

    port, status = scan_port(args.host, 80)

    print(f"Port {port} : {status}")


if __name__ == "__main__":
    main()