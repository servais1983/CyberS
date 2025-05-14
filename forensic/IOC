# 🧩 IOC (Indicators of Compromise)

Les **IOC** sont des éléments techniques permettant d’identifier des compromissions ou des activités malveillantes sur un système ou un réseau.

---

## 📌 Définition

Un **IOC** (Indicator of Compromise) est une donnée observable utilisée pour détecter une intrusion, une attaque ou une infection. Il sert de **signal d'alerte** pour les équipes de sécurité.

---

## 🧪 Types d’IOC courants

- **Hashs de fichiers**
  - MD5, SHA1, SHA256
  - Utilisés pour identifier des fichiers malveillants
- **Adresses IP**
  - IPs connues pour héberger des serveurs C2 (Command & Control)
- **Noms de domaines / URLs**
  - Liens utilisés pour le phishing, le téléchargement de malwares, ou l'exfiltration
- **Signatures YARA**
  - Règles personnalisées pour détecter des patterns de malware
- **Emplacements système**
  - Chemins inhabituels d'exécution, fichiers placés dans des répertoires système
- **Clés de registre (Windows)**
  - Modifications suspectes souvent utilisées pour la persistance
- **Horodatages anormaux**
  - Création ou modification de fichiers à des heures inhabituelles
- **Comportements réseau**
  - Communication vers des pays à risque, ports exotiques, etc.

---

## 📈 Usage des IOC

- **Détection** : via IDS/IPS, antivirus, SIEM
- **Réponse à incident** : analyse forensique, containment
- **Chasse aux menaces (Threat Hunting)** : recherche proactive d'activités suspectes
- **Partage de renseignements** : plateformes comme MISP, VirusTotal, AbuseIPDB

---

## 🔄 Format de partage

- STIX / TAXII
- CSV, JSON, OpenIOC, etc.

---

## 🧠 Exemple simple d'IOC

| Type        | Valeur                            |
|-------------|------------------------------------|
| SHA256      | `9e107d9d372bb6826bd81d3542a419d6` |
| IP          | `185.234.219.12`                   |
| Domaine     | `malicious-update.com`             |
| URL         | `http://malicious-update.com/payload.exe` |
| YARA Rule   | `rule Suspicious_Payload {...}`    |

---

## ⚠️ Bonnes pratiques

- Corréler les IOC avec le contexte
- Éviter les faux positifs
- Mettre à jour les bases de données IOC régulièrement
- Compléter avec des IOA (Indicators of Attack) pour des analyses comportementales

