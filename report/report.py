from datetime import datetime


def generate_report(
    host,
    url,
    port_results,
    http_result,
    output_file
):
    """
    Génère un rapport Markdown.
    """

    now = datetime.now()

    with open(output_file, "w", encoding="utf-8") as report:

        report.write("\n")
        report.write("# Rapport d'audit de sécurité\n\n")

        report.write(f"**Date :** {now.strftime('%d/%m/%Y %H:%M:%S')}\n\n")

        report.write(f"**Cible :** {host}\n\n")

        report.write(f"**URL analysée :** {url}\n\n")

        report.write("---\n\n")

        report.write("## Scanner TCP\n\n")

        ouverts = 0
        fermes = 0
        filtres = 0

        for port, status in port_results:

            if status == "OUVERT":
                ouverts += 1
                report.write(f"- Port {port} : {status}\n")

            elif status == "FERMÉ":
                fermes += 1

            elif status == "FILTRÉ":
                filtres += 1


        report.write("### Statistiques\n\n")

        report.write(f"- Ports ouverts : {ouverts}\n")
        report.write(f"- Ports fermés : {fermes}\n")
        report.write(f"- Ports filtrés : {filtres}\n\n")

        report.write("---\n\n")

        report.write("## Analyse HTTP\n\n")

        if http_result is None:

            report.write("Analyse HTTP non effectuée.\n")

        elif "error" in http_result:

            report.write(f"Erreur : {http_result['error']}\n")

        else:

            report.write(
                f"Code HTTP : {http_result['status']}\n\n"
            )

            for header, value in http_result["headers"].items():

                if value:

                    report.write(f"✔ {header}\n")

                else:

                    report.write(f"✘ {header}\n")

            report.write("\n")

            report.write(
                f"Score : {http_result['score']}/5\n"
            )

            report.write(
                f"Soit {http_result['percentage']:.0f}%\n"
            )

        report.write("\n---\n\n")

        report.write("Rapport généré automatiquement par Mini-Auditeur.\n")