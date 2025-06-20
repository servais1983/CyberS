# 🧠 Volatility - Analyse Forensique de la Mémoire

## 📌 Qu'est-ce que Volatility ?

**Volatility** est un framework open-source destiné à l’analyse de la mémoire volatile (RAM) d’un système informatique. Il permet aux enquêteurs forensiques de :
- Extraire des informations sensibles (processus, connexions réseau, DLL, etc.)
- Analyser les traces d’un logiciel malveillant
- Déterminer l’état d’un système à un moment donné

Volatility est indépendant du système d’exploitation de l’hôte et peut analyser des images mémoire de **Windows, Linux, macOS**, etc.

Il existe deux principales versions :
- **Volatility 2.x** (Python 2, plus utilisée mais moins maintenue)
- **Volatility 3** (Python 3, réécriture complète avec une meilleure structure modulaire)

---

## ⚙️ Installation

### Volatility 2.x (Linux)

git clone https://github.com/volatilityfoundation/volatility.git
cd volatility
python2 vol.py -h
Volatility 3 (Linux ou Windows)

git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
python3 vol.py -h
🧠 Formats de fichiers supportés
.raw (dump brut)

.mem, .lime (Linux)

.vmem (VMware)

.dmp / .hiberfil.sys (Windows)

.elf, .core, .crash (Linux)

🔍 Commandes générales (Volatility 3)

python3 vol.py -f <fichier_memoire> windows.info
python3 vol.py -f <fichier_memoire> -p <profile> <plugin>
🪟 Modules Volatility pour Windows
🔧 Informations système
windows.info — Infos sur l’OS, version, build, etc.

windows.pslist — Liste des processus actifs

windows.pstree — Arborescence des processus

windows.psscan — Recherche de processus (inclus processus cachés)

windows.modules — Liste des modules chargés

📂 Fichiers et registres
windows.filescan — Recherche de fichiers en mémoire

windows.registry.printkey — Affiche une clé de registre

windows.registry.hivescan — Recherche de hives en mémoire

windows.registry.hivelist — Liste des hives

🌐 Réseau
windows.netscan — Connexions réseau et sockets (TCP/UDP)

🔐 Mots de passe et utilisateurs
windows.hashdump — Dump des mots de passe NTLM

windows.lsadump — Extraction des secrets du LSA

🧟 Détection de malwares
windows.malfind — Recherche d’injections de code

windows.ssdt — Analyse de la SSDT (rootkits)

windows.callbacks — Vérifie les callbacks suspects

🐧 Modules Volatility pour Linux
🔧 Informations système
linux_banner — Version du kernel

linux_pslist — Liste des processus

linux_pstree — Arborescence des processus

linux_psaux — Processus avec arguments

linux_proc_maps — Cartographie mémoire d’un processus

linux_cpuinfo — Infos CPU

📂 Fichiers et modules
linux_lsmod — Liste des modules noyau

linux_check_afinfo — Vérifie les fonctions socket

linux_find_file — Recherche de fichiers en mémoire

🔒 Sécurité et utilisateurs
linux_bash — Affiche les historiques Bash

linux_passwd — Montre les utilisateurs et leurs mots de passe

linux_shadow_hashes — Dump des hashes depuis /etc/shadow

🌐 Réseau
linux_netstat — Ports et connexions

linux_ifconfig — Interfaces réseau

📘 Exemples de commandes

# Windows - Liste des processus
python3 vol.py -f win10.raw windows.pslist

# Windows - Recherche de rootkits via malfind
python3 vol.py -f win10.raw windows.malfind

# Linux - Affiche l’historique bash
python3 vol.py -f linux.lime linux_bash

# Linux - Liste les processus
python3 vol.py -f linux.lime linux_pslist
🛠 Astuces
Toujours utiliser windows.psscan en plus de pslist pour détecter les processus cachés.

Utiliser malfind pour détecter les injections en mémoire.

Combinez hivelist + printkey pour explorer les clés de registre.

📚 Liens utiles
Site officiel : https://www.volatilityfoundation.org/

Repo GitHub Volatility 3 : https://github.com/volatilityfoundation/volatility3

Profils Linux avec LiME : https://github.com/504ensicsLabs/LiME


## 🧾 Analyse du Registre Windows avec Volatility

Le **registre Windows** contient une énorme quantité d'informations sur le système, les logiciels, les utilisateurs, les configurations, etc. Volatility permet d'extraire et d'examiner ces données **directement depuis l'image mémoire**, sans avoir besoin d’un accès au disque.

---

### 📜 Modules liés au registre

#### `windows.registry.hivescan`
- **But** : Scanne la mémoire à la recherche de structures de registre (`CMHIVE`).
- **Utilité** : Identifier les emplacements des hives (bases de registre) dans la mémoire, y compris celles non répertoriées.

#### `windows.registry.hivelist`
- **But** : Affiche une liste des hives (bases du registre) trouvées dans la mémoire.
- **Affiche** :
  - L'adresse mémoire
  - Le chemin du fichier hive (par ex. `\SystemRoot\System32\Config\SAM`)
  - Le nom associé (SAM, SYSTEM, SOFTWARE, NTUSER.DAT…)

#### `windows.registry.printkey`
- **But** : Affiche le contenu d'une **clé spécifique** dans le registre.
- **Usage** :

  python3 vol.py -f win10.raw windows.registry.printkey --key "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
Utilité :

Voir les programmes lancés au démarrage (Run, RunOnce)

Explorer des valeurs précises dans les branches NTUSER, SYSTEM, etc.

windows.registry.userassist
But : Affiche les programmes utilisés récemment via les clés UserAssist

Utilité : Révéler les habitudes d’utilisation d’un utilisateur

🧪 Exemple de Workflow : Analyse du registre
Lister les hives disponibles


python3 vol.py -f win10.raw windows.registry.hivelist
Résultat attendu :

pgsql

Virtual            Physical           Name
0xfffff8a000022000 0x122000           \SystemRoot\System32\Config\SYSTEM
0xfffff8a000070000 0x170000           \??\C:\Users\User\ntuser.dat
Explorer une clé du registre SYSTEM


python3 vol.py -f win10.raw windows.registry.printkey --key "Select" --hive-offset 0xfffff8a000022000
Explorer les programmes lancés au démarrage d’un utilisateur


python3 vol.py -f win10.raw windows.registry.printkey --key "Software\\Microsoft\\Windows\\CurrentVersion\\Run" --hive-offset 0xfffff8a000070000
📂 Types de hives utiles
Hive	Contenu principal
SYSTEM	Infos sur les pilotes, services, contrôle du démarrage
SOFTWARE	Infos sur les programmes installés
SAM	Comptes utilisateurs locaux, SID, groupes
SECURITY	Infos sur les politiques de sécurité
NTUSER.DAT	Paramètres spécifiques à l'utilisateur

🔍 Astuce pratique
Combinez hivelist avec printkey pour naviguer et extraire n'importe quelle valeur de registre.

Les valeurs comme Run, LastVisitedMRU, TypedURLs ou MountPoints2 révèlent souvent des indices d’activités malveillantes ou d’utilisation suspecte.

📘 Exemple avancé : Extraction du SID utilisateur
Identifier le hive SAM :


python3 vol.py -f win10.raw windows.registry.hivelist
Extraire les utilisateurs :


python3 vol.py -f win10.raw windows.registry.printkey --key "SAM\\Domains\\Account\\Users\\Names" --hive-offset 0xfffff8a000034000
Cela donne les noms d'utilisateurs et permet d'aller plus loin pour récupérer les SID ou analyser les droits associés.

🔐 Sécurité et malveillance
Les artefacts du registre sont précieux pour :

Détecter les persistances (Run, Services, etc.)

Révéler les utilisateurs actifs

Identifier les logiciels malveillants configurés pour se relancer

go



## 🔐 Extraction des mots de passe avec `hashdump` (Volatility)

### ❓ Qu’est-ce que `hashdump` ?

La commande `hashdump` permet d’extraire les **hashs NTLM** des mots de passe des comptes utilisateurs Windows à partir d’une image mémoire.

Ces hashs peuvent ensuite être :
- Comparés à des dictionnaires (attaque par dictionnaire)
- Bruts (attaque par force brute)
- Crackés via des outils comme `john`, `hashcat`, etc.

---

### 📦 Fichiers nécessaires en mémoire

Pour que `hashdump` fonctionne, Volatility doit **trouver et charger deux hives** dans la mémoire :
- `SAM` — Contient les comptes utilisateurs
- `SYSTEM` — Contient la clé d’obfuscation nécessaire pour déchiffrer les hashs

---

### 🔧 Syntaxe générale (Volatility 3)

python3 vol.py -f <image_memoire> windows.hashdump
Volatility 3 détecte automatiquement les profils et les hives requis. Pas besoin de spécifier le profil contrairement à Volatility 2.

⚠️ Avec Volatility 2
Syntaxe :

python2 vol.py -f <image_memoire> --profile=<profil_windows> hashdump
Exemples de profils :
Win7SP1x64

Win10x64_19041

Exemple complet :

python2 vol.py -f memdump.raw --profile=Win7SP1x64 hashdump
📋 Exemple de sortie hashdump
text

Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
User1:1001:aad3b435b51404eeaad3b435b51404ee:f1b7f8d2566c8e3ef2ddc99a9f7a17b3:::
Structure :
ruby

nom_utilisateur:RID:LM_hash:NTLM_hash:::
LM_hash : Ancienne méthode de hash (souvent désactivée aujourd'hui)

NTLM_hash : Hash réel du mot de passe Windows

🛠 Que faire avec ces hashs ?
Utiliser hashcat

hashcat -m 1000 hash.txt rockyou.txt
Utiliser john

john --format=nt hash.txt --wordlist=rockyou.txt
🔍 Étapes de vérification (optionnel)
Si hashdump échoue, il est conseillé de :

Lister les hives avec hivelist :


python3 vol.py -f memdump.raw windows.registry.hivelist
Vérifier que SAM et SYSTEM sont présents.

🧠 Autres modules liés aux mots de passe
windows.lsadump — Extrait les secrets du LSA (tokens, clés DPAPI, etc.)

windows.cachedump — Hashed mots de passe en cache (utiles en cas de déconnexion)

✅ Résumé des commandes
Volatility 3 (recommandé)

python3 vol.py -f memdump.raw windows.hashdump
Volatility 2 (avec profil)

python2 vol.py -f memdump.raw --profile=Win7SP1x64 hashdump
🔐 Recommandation
Toujours coupler hashdump avec lsadump et hivelist pour faire une analyse complète de la sécurité des identifiants.

yaml


---
# 🧠 Analyse mémoire avec Volatility sous Linux

Ce guide présente pas à pas comment utiliser **Volatility 2** pour analyser un dump mémoire (`memdump.mem`) à l’aide de commandes de base : vérification, identification de profil, processus actifs, et connexions réseau.

---

## ✅ Étape 1 – Voir les commandes disponibles

Commencez par afficher l’aide pour explorer les plugins disponibles :


volatility -h
Cela liste tous les plugins disponibles (pslist, netscan, dlllist, etc.) ainsi que les options générales.

🔍 Étape 2 – Identifier le profil mémoire
Avant toute analyse, il faut identifier le profil (profil kernel) à utiliser pour votre image mémoire :


volatility -f memdump.mem imageinfo
🔎 Cette commande affiche :

Les profils suggérés (ex: Win7SP1x64, Win10x64_18362, etc.)

L’horodatage du système au moment de la capture

Le type de système détecté (Windows/Linux)

➡️ Choisis le profil le plus probable dans la liste retournée.

🧠 Étape 3 – Lister les processus en cours
Utilise le profil identifié pour extraire la liste des processus actifs avec leurs métadonnées :


volatility -f memdump.mem --profile=NomDuProfil pslist
Exemple :


volatility -f memdump.mem --profile=Win7SP1x64 pslist
🔹 Cette commande fournit :

PID / PPID

Nom du processus

Date/Heure de lancement

Nombre de threads/handles

🎯 Rechercher les anomalies :

Noms de processus suspects ou déguisés (svchost.exe, explorer.exe hors contexte)

Processus sans parent (PPID incohérent)

Horodatages anormaux ou postérieurs à l'heure système

🌐 Étape 4 – Analyser les connexions réseau
Utilisez le plugin netscan pour extraire les connexions réseau actives (TCP/UDP) au moment du dump :


volatility -f memdump.mem --profile=NomDuProfil netscan
Cette commande retourne :

PID associé à chaque connexion

Adresse locale / distante

Port

État de la connexion (LISTENING, ESTABLISHED, etc.)

🔎 À surveiller :

Connexions vers des IP externes non connues

Processus inconnus établissant des connexions réseau

Ports non standard

🧩 Astuces supplémentaires
Ajouter > resultat.txt à vos commandes pour exporter les résultats dans un fichier texte.

Croiser pslist avec netscan pour identifier quels processus communiquent avec l’extérieur.

Utiliser ensuite dlllist, cmdline, ou malfind pour explorer un processus suspect.


# 🔍 Analyse avancée mémoire avec Volatility

Cette section complète l’analyse de base avec des **plugins plus poussés** pour détecter du code malveillant et extraire les exécutables suspects.

---

## 🌲 Étape 5 – Arbre des processus (`pstree`)

Affiche l’**arborescence des processus** (parent/enfant), utile pour repérer des processus qui ne devraient pas exister ou sont lancés par des processus légitimes.

```bash
volatility -f memdump.mem --profile=Win7SP1x64 pstree
🔎 À surveiller :

Processus enfants anormaux (ex: cmd.exe lancé par explorer.exe)

Hiérarchie incohérente ou vide

Double instance de services critiques

🧬 Étape 6 – Détection de code malveillant en mémoire (malfind)
Détecte les zones de mémoire exécutables non légitimes (ex: injection, reflective DLL, shellcode) utilisées souvent par les malwares.


volatility -f memdump.mem --profile=Win7SP1x64 malfind
🔍 Cette commande affiche :

PID du processus concerné

Adresse mémoire suspecte

Dump hexadécimal et aperçu du code ASM

Signature de l’injection

🎯 Cibler un processus spécifique
Pour analyser un processus précis avec malfind, ajoute l’option -p suivie du PID :


volatility -f memdump.mem --profile=Win7SP1x64 malfind -p 1234
Cela limite l’analyse et accélère les résultats.

💣 Étape 7 – Extraire un exécutable en mémoire (procdump)
Ce plugin permet de dumpez un processus entier depuis la mémoire, utile pour l’analyser avec un antivirus ou dans un sandbox.


volatility -f memdump.mem --profile=Win7SP1x64 procdump -p 1234 --dump-dir=procdump/
📁 Cela crée un fichier .exe du processus dans le dossier procdump/.

✅ Bonnes pratiques :

Toujours analyser les fichiers extraits avec VirusTotal, Hybrid Analysis ou IDA/Ghidra

Croiser avec les résultats de malfind, pstree, cmdline, etc.

🛠️ Étapes suivantes recommandées
dlllist -p <PID> : pour lister les DLL chargées par un processus

cmdline -p <PID> : pour voir comment le processus a été lancé

handles -p <PID> : objets (fichiers, clés de registre, etc.) utilisés

getsids -p <PID> : SID associés pour vérifier les permissions

📘 Références
Volatility Plugin Reference

Analyse de malware en mémoire

yaml





📘 Références
Volatility GitHub (v2)

Cheat Sheet officielle Volatility




