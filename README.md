# Mini Auditeur de Sécurité

## Présentation

Mini Auditeur de Sécurité est une application développée en Python permettant de réaliser un audit réseau simple sur des cibles autorisées.

Le projet a été réalisé dans le cadre du module **Python pour la cybersécurité et le pentesting**.

Les fonctionnalités principales sont :

- Scan TCP d'une plage de ports
- Scan multithread pour améliorer les performances
- Analyse des principaux en-têtes HTTP de sécurité
- Vérification des certificats TLS
- Génération automatique d'un rapport Markdown
- Interface en ligne de commande

---

## Architecture du projet

```
Mini-Auditeur/
│
├── http_checker/
├── report/
├── scanner/
├── serveur_local/
├── tls/
├── utils/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Cloner le dépôt :

```bash
git clone https://github.com/alixvan/Mini-Auditeur.git

cd Mini-Auditeur
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Démarrer le serveur local

Le projet contient un serveur Flask utilisé comme cible locale pour les analyses HTTP.

Depuis le dossier `serveur_local` :

```bash
python app.py
```

Le serveur sera disponible sur :

```
http://127.0.0.1:5000
```

---

## Exécution

### Scanner TCP

```bash
python main.py --host scanme.nmap.org --ports 20-100
```

Cette démonstration utilise **scanme.nmap.org**, une cible officiellement autorisée par le projet Nmap.

---

### Analyse HTTP

Dans un premier terminal :

```bash
cd serveur_local
python app.py
```

Dans un second terminal :

```bash
python main.py --host 127.0.0.1 --ports 5000 --url http://127.0.0.1:5000
```

Cette démonstration utilise **localhost**, conformément au cahier des charges.

---

## Rapport généré

Le rapport est automatiquement enregistré dans :

```
rapports/rapport.md
```

Il contient notamment :

- la liste des ports ouverts ;
- les statistiques du scan ;
- les en-têtes HTTP détectés ;
- les résultats de la vérification TLS ;
- la date de l'audit.

---

## Technologies utilisées

- Python 3
- socket
- requests
- ssl
- argparse
- Flask
- colorama
- concurrent.futures

---

## Cibles autorisées

Conformément au cahier des charges, les démonstrations ont été réalisées uniquement sur des cibles autorisées :

- **scanme.nmap.org** (scan TCP)
- **localhost (127.0.0.1)** via un serveur Flask local (analyse HTTP)

Aucun test n'a été exécuté contre un système tiers sans autorisation.

---

## Auteur

Projet réalisé dans le cadre du module **Python pour la cybersécurité et le pentesting**.
