# 🕵️‍♂️ EmploLeaks — Un outil redoutable d’OSINT pour identifier les failles humaines via les fuites de données

**EmploLeaks** est un outil d’**OSINT (Open Source Intelligence)** spécialisé dans la **détection de fuites de données personnelles et professionnelles**. Il cible les **failles humaines** au sein des entreprises, souvent exploitées dans le cadre d’ingénierie sociale ou de recon reconnaissances offensives.

---

## 🎯 Objectif principal

**Identifier les employés exposés publiquement** (emails, comptes, mots de passe, documents, CV, etc.) afin de **cartographier les risques humains** liés à la sécurité d’un système d’information.

---

## 🔎 Fonctionnalités clés

- 📥 **Recherche dans les bases de données compromises** (HaveIBeenPwned, DeHashed, etc.)
- 🧑‍💼 **Extraction de profils professionnels** (LinkedIn, GitHub, etc.)
- 📄 **Collecte automatique de CV publiquement accessibles**
- 🔐 **Détection de mots de passe exposés**
- 🧠 **Analyse de vecteurs d’ingénierie sociale potentiels**
- 🌐 **Scraping de domaines spécifiques (entreprises, organisations)**

---

## 🛠️ Cas d’usage

- **Red Team / Pentesting humain** : identification des employés les plus exposés
- **Prévention** : sensibilisation à la sécurité des données personnelles
- **Veille** : suivi régulier de l’exposition humaine d’une entreprise
- **Audit RH / Sécurité** : évaluer les vulnérabilités internes via OSINT

---

## ⚙️ Exemple de fonctionnement

```bash
python3 emploleaks.py --domain exemple.com --breaches --linkedin --cv
🧰 Technologies utilisées
Python

API OSINT publiques et privées

Scraping et parsing HTML

Intégration possible avec Maltego, TheHarvester, etc.

🧱 Pré-requis
Python 3.x

Clés API pour certains services (facultatif mais recommandé)

Proxy ou VPN recommandé pour les recherches intensives

📚 Ressources
GitHub du projet (exemple)

Guide d’utilisation pas-à-pas

Liste des fuites publiques analysées

⚠️ Avertissement éthique et légal
EmploLeaks est un outil d’audit et de sensibilisation. Son usage doit strictement respecter le cadre légal, notamment le RGPD et les lois relatives à la vie privée. L’utilisation non autorisée peut entraîner des sanctions juridiques sévères.

🧠 En résumé
EmploLeaks permet de détecter les points faibles humains d'une organisation à travers les fuites de données accessibles publiquement. Un outil puissant d’OSINT défensif et offensif, au service de la cybersécurité proactive.

🔐 Parce qu’avant de pirater une machine, on exploite une personne.
