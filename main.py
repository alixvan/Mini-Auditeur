import argparse

from scanner.scanner import scan_ports
from utils.helpers import parse_ports
from http_checker.headers import analyze_headers
from utils.helpers import security_level
from report.report import generate_report


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

    results = scan_ports(args.host, [80])

    for port, status in results:
        print(f"Port {port} : {status}")

    
    print("\n===== SCAN EN COURS =====")

    ports = parse_ports(args.ports)

    results = scan_ports(args.host, ports)

    print("\n===== PORTS OUVERTS =====\n")

    for numero, statut in results:

        if statut == "OUVERT":
           print(f"Port {numero:<5} : {statut}")

    ouverts = sum(1 for _, statut in results if statut == "OUVERT")
    fermes = sum(1 for _, statut in results if statut == "FERMÉ")
    filtres = sum(1 for _, statut in results if statut == "FILTRÉ")

    print("\n===== STATISTIQUES =====")
    print(f"Ports ouverts : {ouverts}")
    print(f"Ports fermés  : {fermes}")
    print(f"Ports filtrés : {filtres}")

    print("\n===== ANALYSE HTTP =====\n")

    http_result = analyze_headers(args.url)

    if "error" in http_result:

        print("Erreur :", http_result["error"])

    else:

        print("Code HTTP :", http_result["status"])

        print()

        for header, value in http_result["headers"].items():

            if value:

                print(f"✔ {header}")

            else:

                print(f"✘ {header}")

        print()

        print(
            f"Score : {http_result['score']}/5"
        )

        niveau = security_level(http_result["percentage"])

        print(
            f"Soit {http_result['percentage']:.0f}%"
        )

        print(f"Niveau : {niveau}")

        print("\n===== GÉNÉRATION DU RAPPORT =====")

    generate_report(
        args.host,
        args.url,
        results,
        http_result,
        args.output
    )

    print(f"Rapport enregistré dans : {args.output}")


if __name__ == "__main__":
    main()

    