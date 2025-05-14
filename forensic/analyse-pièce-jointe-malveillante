# 🛡️ Outils Linux pour analyser les pièces jointes malveillantes d'un email

Ce guide fournit une liste d’outils et de commandes sous Linux permettant d’analyser des pièces jointes suspectes, telles que des documents Office, PDF, archives ou exécutables.

---

## 📥 1. Extraction des pièces jointes

- **ripmime**  
  Extrait les pièces jointes d’un email au format MIME.
  ```bash
  ripmime -i email.eml -d ./output
munpack
Décode les messages MIME au format texte.


munpack email.eml
eml-parser (Python)
Analyse complète d’un fichier .eml.


pip install eml-parser
eml-parser file.eml
🧪 2. Analyse statique
🧾 Identification du type de fichier
file


file suspicious_attachment
strings


strings suspicious_attachment | less
hexdump / xxd


xxd suspicious_attachment | less
hashing


sha256sum suspicious_attachment
📄 Documents Office & PDF
oletools (oleid, olevba, etc.)


olevba suspicious.doc
Détection de macros VBA, URLs, et obfuscation.

mraptor


mraptor suspicious.doc
pdfid / pdf-parser


pdfid suspicious.pdf
pdf-parser suspicious.pdf
📦 Archives (ZIP, RAR, etc.)
binwalk


binwalk suspicious.zip
7z


7z x suspicious.zip
unrar / unzip


unrar x suspicious.rar
unzip suspicious.zip
⚙️ Fichiers exécutables
pefile (Python)

python

import pefile
pe = pefile.PE("malware.exe")
pe.print_info()
exiftool


exiftool suspicious_file
radare2


r2 -AA suspicious.exe
strings + grep


strings suspicious.exe | grep -Ei 'http|cmd|powershell'
🧬 3. Analyse dynamique (sandboxing)
Cuckoo Sandbox
Environnement complet pour exécuter et analyser les comportements.

https://cuckoosandbox.org

Firejail
Sandboxing simple d’un binaire.

firejail ./suspicious.bin
☁️ 4. Vérification en ligne
VirusTotal (en ligne ou via API)


curl --request POST --url https://www.virustotal.com/api/v3/files \
--header 'x-apikey: <API_KEY>' \
--form file=@suspicious_file
Hybrid Analysis

https://www.hybrid-analysis.com

🧰 5. Bonus : outils utiles
YARA
Règles de détection de malwares :


yara -r rules.yar suspicious_file
clamav
Antivirus open-source :


clamscan suspicious_file
hashlookup / MISP
Recherche de hash dans des bases de données de menaces.

✅ Conclusion
Utiliser une combinaison d’analyse statique, d’analyse dynamique, et de renseignement sur les menaces permet une détection plus fiable des fichiers malveillants.

⚠️ Toujours effectuer l’analyse dans un environnement isolé (VM, conteneur) pour éviter tout risque d’exécution accidentelle.

css

