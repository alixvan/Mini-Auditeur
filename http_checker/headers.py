import requests

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy"
]


def analyze_headers(url):
    """
    Analyse les en-têtes HTTP d'une URL.
    """

    try:

        response = requests.get(url, timeout=5)

        headers = response.headers

        print("\nHEADERS REÇUS :")

        for key, value in response.headers.items():
            print(f"{key}: {value}")

        results = {}

        score = 0

        for header in SECURITY_HEADERS:

            if header in headers:
                results[header] = headers[header]
                score += 1
            else:
                results[header] = None

        percentage = (score / len(SECURITY_HEADERS)) * 100

        return {
            "url": url,
            "status": response.status_code,
            "headers": results,
            "score": score,
            "percentage": percentage
        }

    except requests.exceptions.Timeout:

        return {
            "error": "Timeout"
        }

    except requests.exceptions.ConnectionError as e:

        print("\nERREUR COMPLÈTE :")
        print(e)

        return {
            "error": str(e)
        }

    except Exception as e:

        return {
            "error": str(e)
        }   