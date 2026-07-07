# Mini Auditeur de Sécurité

## Description

Mini Auditeur de Sécurité est un outil développé en Python dans le cadre du projet
« Python pour les tests d'intrusion ».

L'application permet de réaliser un audit défensif d'une cible autorisée en effectuant :

- un scan TCP multithread ;
- une analyse des en-têtes HTTP ;
- une vérification du certificat TLS (bonus) ;
- la génération automatique d'un rapport Markdown.

---

## Fonctionnalités

### Scanner TCP

- Scan d'une plage de ports
- Détection des ports ouverts
- Multithreading

### Analyse HTTP

Vérification des en-têtes :

- Strict-Transport-Security
- Content-Security-Policy
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy

Calcul d'un score de sécurité.

### Vérification TLS

- Validité du certificat
- Date d'expiration
- Nombre de jours restants
- Autorité de certification

### Rapport

Génération automatique d'un rapport Markdown.

---

## Prérequis

Python 3.10 ou supérieur.

---

## Installation

Créer un environnement virtuel :

```bash
python -m venv venv
```

Activer l'environnement :

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Utilisation

Exemple :

```bash
python main.py ^
--host scanme.nmap.org ^
--ports 20-100 ^
--url http://scanme.nmap.org ^
--output rapports/rapport.md
```

Exemple HTTPS :

```bash
python main.py ^
--host example.com ^
--ports 20-100 ^
--url https://example.com ^
--output rapports/rapport.md
```

---

## Dépendances

- requests
- beautifulsoup4
- colorama

---

## Structure du projet

scanner/
http_checker/
report/
tls/
utils/
rapports/

---

## Cibles utilisées

Conformément au cahier des charges :

- scanme.nmap.org
- services locaux
- domaines autorisés

Aucun test n'a été réalisé sur un système tiers non autorisé.

---

## Auteur

Projet réalisé dans le cadre du cours :

Python pour la cybersécurité et le pentesting.