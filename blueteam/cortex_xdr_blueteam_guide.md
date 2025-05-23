# 🛡️ CORTEX XDR - COMMANDES, DETECTIONS ET PLAYBOOKS POUR BLUE TEAM & FIDR

## 🧭 Sommaire
1. [📌 Vue d'ensemble de Cortex XDR](#📌-vue-densemble-de-cortex-xdr)
2. [🔍 Recherches XQL essentielles](#🔍-recherches-xql-essentielles)
3. [🚨 Alertes personnalisées](#🚨-alertes-personnalisées)
4. [🔎 Cas d’usage investigation](#🔎-cas-dusage-investigation)
5. [🧱 Mapping MITRE ATT&CK](#🧱-mapping-mitre-attck)
6. [🤖 Playbooks XSOAR](#🤖-playbooks-xsoar)
7. [📊 Dashboards recommandés](#📊-dashboards-recommandés)
8. [🛠️ Bonnes pratiques XDR](#🛠️-bonnes-pratiques-xdr)

---

## 📌 Vue d'ensemble de Cortex XDR

**Cortex XDR** est une solution de détection et réponse étendue (**XDR**) développée par **Palo Alto Networks**. Elle centralise la collecte, la corrélation, et l’analyse de données issues de :

- 🖥️ Endpoints (agents Traps / XDR)
- 🌐 Réseau (via Cortex Data Broker, Firewall PAN-OS)
- ☁️ Cloud (AWS, Azure, GCP via Prisma)
- 📩 Email (via API ou intégration EOP/Proofpoint)

Fonctionnalités clés :
- 💡 **XQL (XDR Query Language)** : langage SQL-like pour interroger toutes les sources
- 🧠 Analytique comportementale et corrélation multi-couche
- 🔁 Réponse automatisée via **XSOAR** (SOAR intégré ou externe)
- 🛰️ Enrichissement automatique (VT, WHOIS, AbuseIPDB, AutoFocus, etc.)
- 📦 Rétention personnalisable (30j → jusqu’à 1 an avec add-on)

---

## 🔍 Recherches XQL essentielles

### 🖧 Connexions RDP
```xql
...
```

### 💣 Tentatives de brute force
```xql
...
```

### ⚙️ PowerShell suspect
```xql
...
```

### 🗃️ Transferts de fichiers compressés
```xql
...
```

---

## 🚨 Alertes personnalisées

### 🔐 Brute force user AD
- 📈 Condition : >10 logon failures / 5 minutes
- ⚙️ Action : Créer alerte + push XSOAR

### ⚠️ PowerShell encodé
- 📌 Condition : EncodedCommand
- 🚫 Action : Isoler machine + alerte SOC

---

## 🔎 Cas d’usage investigation

### 📡 Exfiltration DNS
```xql
...
```

### 🕓 Scheduled Tasks suspects
```xql
...
```

---

## 🧱 Mapping MITRE ATT&CK

| 🆔 ID | 🔍 Technique                   | 📄 XQL associé                                      |
|------|--------------------------------|----------------------------------------------------|
| T1059 | Command-Line Interface        | PowerShell Encoded, cmd.exe                       |
| T1078 | Valid Accounts                | Logon multi-IP                                     |
| T1021.001 | RDP                       | Port 3389, NETWORK_CONNECTION                     |
| T1566.001 | Phishing (attachment)     | Analyse email logs .doc/.exe                      |

---

## 🤖 Playbooks XSOAR

### 🛡️ Brute Force AD
1. Détection via XQL
2. VT enrichment
3. 🧲 Isolement via agent XDR
4. 📥 Ticket SOAR

### 🛰️ DNS Exfiltration
1. Longueur DNS > 50
2. Blocage IP via firewall
3. 🗃️ Log dans incident manager

---

## 📊 Dashboards recommandés
- 🔑 Authentification : succès/échecs
- 🌍 Réseau : top IP/ports/process
- 🧾 Scripts exécutés : PowerShell, cmd
- 📦 DLP : transferts fichiers/externes

---

## 🛠️ Bonnes pratiques XDR
- 📘 Structurer les requêtes avec `actor`, `action`, `agent`
- 📂 Préfixer les noms de playbook (ex: `CONTAIN_`, `INV_`)
- 🌐 Enrichir automatiquement via WHOIS, VT, GeoIP
- 🧪 Vérifier via XQL Live avant activation alerte
- 🧩 Mapper avec MITRE ATT&CK pour priorité SOC
- 🔄 Versionner vos XQL et rules dans Git privé

---

Besoin de templates JSON, exports XQL, ou d'intégration XDR + XSOAR ? 🎯 Demande !
