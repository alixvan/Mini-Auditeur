from flask import Flask, make_response

app = Flask(__name__)


@app.route("/")
def accueil():

    response = make_response(
        "Bienvenue sur le serveur local du Mini Auditeur."
    )

    # En-têtes de sécurité
    response.headers["Strict-Transport-Security"] = "max-age=31536000"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin"

    return response


@app.route("/health")
def health():
    return {
        "status": "OK",
        "application": "Mini Auditeur",
        "version": "1.0"
    }


if __name__ == "__main__":

    print(__file__)
    
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )