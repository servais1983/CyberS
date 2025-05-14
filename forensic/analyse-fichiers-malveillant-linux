# 🧪 Analyse rapide de fichier malveillant avec `file` et `strings`

Lorsqu’on récupère un fichier suspect (exécutable, document, script), une première **analyse statique rapide** peut être faite avec les outils en ligne de commande `file` et `strings`.

---

## 📂 Objectif

- Identifier le **type réel du fichier**
- Extraire les **chaînes de texte visibles** (commandes, URLs, mots de passe, etc.)
- Détecter des indices de **compilation, d'obfuscation ou d'injection**

---

## 🛠️ 1. `file` – Déterminer le type de fichier

La commande `file` examine les **en-têtes binaires** pour déterminer le type réel du fichier, **indépendamment de son extension**.

### 📌 Syntaxe

```bash
file nom_du_fichier
🧾 Exemples de sortie utiles
Sortie file	Signification
PE32 executable (GUI)	Fichier exécutable Windows 32 bits
MS-DOS executable	Possiblement un dropper/loader
PDF document	PDF, souvent utilisé pour exploits
Zip archive	Archive ou fichier Office (DOCX, etc.)
HTML document	Fichier web, possible phishing
Bourne-Again shell script	Script Bash

🧠 2. strings – Extraire les chaînes ASCII visibles
strings cherche des séquences de texte lisible dans un binaire. Cela peut révéler :

Des URLs (C2, download)

Des commandes système

Des chemins de fichiers

Des noms de fonctions/API Windows

Des mots de passe ou clés en dur

📌 Syntaxe

strings nom_du_fichier
🔎 Avec filtrage (grep)

strings fichier_suspect | grep -i "http"
strings fichier_suspect | grep -Ei "cmd|powershell|wget|curl"
💡 Option utile
-n 6 → Ne garde que les chaînes de plus de 6 caractères (réduction du bruit)


strings -n 6 fichier_suspect
🛡️ Signes de danger fréquents à repérer
Indice trouvé via strings	Interprétation
powershell -enc, cmd /c	Script d’exécution
http://, https://, IP en clair	Téléchargement distant
kernel32.dll, LoadLibrary	Appels API système Windows
Chemins étranges : %TEMP%, C:\	Emplacement d’exécution ou drop
MZ ou This program cannot be run	Signature binaire Windows (PE)

🎓 Astuce : combiner avec less ou grep

strings fichier_suspect | less
strings fichier_suspect | grep -Ei "exe|dll|http|cmd"
🧩 Étapes suivantes recommandées
Hash du fichier (sha256sum) et analyse sur VirusTotal

Analyse dynamique (sandbox : Any.Run, Cuckoo, etc.)

Déobfuscation avec radare2, Ghidra, ou IDA

Extraction avec binwalk si c’est un fichier packé

📘 Références
man file / man strings

Virustotal

AnyRun

radare2
