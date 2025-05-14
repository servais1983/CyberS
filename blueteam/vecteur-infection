# ☣️ Vecteurs d'infection en cybersécurité

Un **vecteur d’infection** (ou vecteur d’attaque) est le **moyen utilisé par une menace (malware, ransomware, APT)** pour **pénétrer un système ou un réseau**. Identifier ces vecteurs est **essentiel en forensic** pour reconstituer l'intrusion, fermer les brèches et prévenir la récidive.

---

## 🧾 Catégories principales de vecteurs d’infection

### 📨 1. Phishing / Spear Phishing

- **Emails malveillants** contenant des pièces jointes piégées (DOC, XLS, PDF) ou des liens vers des scripts/exploit kits.
- **Spear phishing** = ciblage spécifique (employé, direction, service).

🛠️ Exemples :
- `invoice.doc` avec macro VBA
- Lien vers un faux site Office 365 (credential harvesting)

### 📦 2. Téléchargements piégés (Drive-by / Fake software)

- Visite d’un site compromis → chargement automatique d’un malware via exploit.
- Téléchargement de logiciels cracks, keygens, plugins infectés.

🛠️ Exemples :
- Fichiers `.exe`, `.js`, `.scr`, `.zip` téléchargés via navigateur
- Site pirate ou publicitaire infecté

### 👤 3. Ingénierie sociale

- Manipulation psychologique pour pousser un utilisateur à exécuter un code malveillant.
- Peut inclure faux supports techniques, "mises à jour urgentes", ou interactions directes (chat, téléphone).

🛠️ Exemple :
- Faux technicien demandant d'installer TeamViewer ou AnyDesk

### 💾 4. Supports amovibles (USB / CD / SD)

- Clé USB contenant un **autorun.inf**, un exécutable déguisé ou un payload automatique (BadUSB, Rubber Ducky).
- Très utilisés dans les attaques physiques ciblées.

🛠️ Exemple :
- Script PowerShell sur clé USB lancé automatiquement
- Drop de fichiers dans un dossier `C:\Users\Public`

### 🌐 5. Exploits réseau

- Failles non corrigées dans des services accessibles (RDP, SMB, HTTP, VPN).
- Utilisés par les ransomwares (ex : EternalBlue pour WannaCry).

🛠️ Exemples :
- RDP exposé sans MFA → brute force
- Vulnérabilité Log4Shell, ProxyShell, etc.

### 🧰 6. Applications vulnérables / macros / scripts

- Exploitation de logiciels tiers installés : navigateurs, Acrobat, Office, plugins.
- Utilisation de scripts (`.vbs`, `.js`, `.bat`, `.ps1`) injectés via e-mail ou site.

🛠️ Exemple :
- Macro Word : `Document protected, enable content`
- Fichier `.hta` déguisé

---

## 📦 Techniques d'infection typiques

| Technique             | Description rapide                               |
|-----------------------|--------------------------------------------------|
| Droppers              | Fichiers "transporteurs" qui déposent la charge |
| Loaders               | Téléchargent la charge depuis internet           |
| Fileless Malware      | Code injecté directement en mémoire              |
| Persistence Mechanisms| Ajout au registre, tâches planifiées, etc.      |

---

## 🔍 Outils forensic pour détecter les vecteurs

| Outil                 | Fonction                          |
|-----------------------|-----------------------------------|
| **Volatility**        | Recherche de process / injection  |
| **MFTECmd**           | Fichiers récents, exécutés        |
| **EvtxECmd**          | Logs d’événement (email, script)  |
| **LECmd / JLECmd**    | Analyse LNK, JumpLists            |
| **Prefetch viewer**   | Lancement d’exécutables           |
| **Wireshark / Zeek**  | Analyse réseau / transfert payload|

---

## 🛡️ Bonnes pratiques de prévention

- Mise à jour régulière des systèmes
- Désactivation des macros Office par défaut
- Limitation des supports amovibles
- Formation à la détection des emails suspects
- Filtrage DNS et pare-feu applicatif

---

## 📘 Références

- MITRE ATT&CK Initial Access: https://attack.mitre.org/tactics/TA0001/
- ANSSI Guide Prévention: https://www.ssi.gouv.fr
- DFIR Report (cas réels) : https://thedfirreport.com/

