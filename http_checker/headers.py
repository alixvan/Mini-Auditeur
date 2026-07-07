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

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/138.0 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=5,
            allow_redirects=True
        )

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

    except requests.exceptions.ConnectionError:

        return {
            "error": (
                "Le serveur a fermé la connexion. "
                "Cette cible ne permet pas l'analyse HTTP via requests."
            )
        }

    except Exception as e:

        return {
            "error": str(e)
        }   