# 🛡️ Sn1per - Outil de Pentest Automatisé par 1N3

Sn1per est un outil de reconnaissance et de pentesting automatisé, développé par l'équipe 1N3. Il est conçu pour effectuer des audits de sécurité complets sur des cibles individuelles ou des plages d'adresses IP. Il s'agit d'un outil puissant pour les professionnels de la cybersécurité, les red teams et les chasseurs de bugs bounty.

---

## 📌 Caractéristiques principales

- **Reconnaissance passive et active**
- **Scan de vulnérabilités automatique**
- **Intégration de nombreux outils (Nmap, Nikto, Metasploit, etc.)**
- **Modes personnalisés selon le type d’audit**
- **Support des scans de sous-domaines, CMS, vulnérabilités web**
- **Génération automatique de rapports HTML**

---

## 🛠️ Installation

### Prérequis

- Système Linux (Debian-based recommandé)
- Git
- Bash
- Accès root

### Installation via Git :

```bash
git clone https://github.com/1N3/Sn1per.git
cd Sn1per
./install.sh
🚀 Utilisation de base
Lancer un scan standard :
bash
Copier
Modifier
sniper -t <IP ou domaine>
Modes disponibles :
Mode	Description
normal	Scan standard (recon + vulnérabilités)
stealth	Recon passif
recon	Reconnaissance active uniquement
full	Recon + scans + vulnérabilités + bruteforce
web	Scan des vulnérabilités web (XSS, SQLi, etc.)
custom	Scan avec configuration personnalisée
nuke	Scan agressif (brute-force inclus, usage à vos risques)

Exemple :
bash
Copier
Modifier
sniper -t example.com -m stealth
🔍 Outils intégrés
Sn1per s’appuie sur plusieurs outils bien connus dans le domaine du pentest :

Nmap – Scan réseau et détection de services

Nikto – Scan de vulnérabilités Web

TheHarvester – Récolte d'emails et informations

Metasploit Framework

WhatWeb – Détection de technologies Web

WafW00f – Détection de WAF

CMSmap – Détection de vulnérabilités CMS

DNSenum, DNSrecon – Reconnaissance DNS

Hydra / Medusa – Bruteforce

📄 Génération de rapports
Après un scan, Sn1per génère automatiquement :

Un rapport HTML complet

Des logs bruts dans des répertoires organisés

Un historique consultable via interface web (Sn1per Professional)

🧱 Sn1per Professional (Version commerciale)
La version professionnelle de Sn1per ajoute :

Une interface web graphique

Des tableaux de bord pour le suivi de la sécurité

Des options de collaboration en équipe

Une gestion de projets avec export PDF, etc.

👉 Plus d'infos sur Sn1per Professional

⚠️ Avertissements
N'utilisez Sn1per que sur des systèmes que vous possédez ou êtes autorisé à tester.

Certains modules peuvent être bruyants et détectés par les IDS/IPS.

En mode nuke, il peut y avoir des conséquences légales ou techniques graves si mal utilisé.

📚 Ressources
GitHub : https://github.com/1N3/Sn1per

Documentation : https://sn1persecurity.com/documentation

Forum de support : https://community.sn1persecurity.com

🧑‍💻 Exemple de cas d’usage
bash

sniper -t vulnsite.com -m full
Ce scan inclura :

Détection de sous-domaines

Détection de ports et services

Analyse des technologies web

Scan de vulnérabilités web

Bruteforce (si activé)

📦 Alternatives à Sn1per
Recon-ng

SpiderFoot

AutoRecon

LazyRecon

Sn1per se distingue par son intégration tout-en-un et son automatisation poussée.

✅ Conclusion
Sn1per est un framework d’audit de sécurité automatisé extrêmement complet, idéal pour les phases de reconnaissance, scan et énumération. Il s’intègre facilement dans un workflow de pentest professionnel et permet de gagner un temps précieux tout en générant des rapports clairs.

yaml

