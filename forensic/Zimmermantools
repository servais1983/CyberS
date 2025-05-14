# 🕵️‍♂️ Outils Forensic – Eric Zimmerman Tools

Le site officiel d’Eric Zimmerman (ancien analyste du FBI) héberge une **collection d’outils en ligne de commande** spécialement conçus pour les enquêteurs numériques, les DFIR, et les analystes de malwares.

🔗 **URL principale :** https://ericzimmerman.github.io/#!index.md

---

## 📚 Structure du site

- **Homepage** : brève description des outils
- **Lien vers les dépôts GitHub**
- **Documentation (index.md)** : synthèse des outils avec liens, options, et usage
- **Téléchargement** via le GitHub ou la **page de téléchargement automatisée**

---

## 📦 Liste des outils principaux disponibles

| Outil         | Description courte |
|---------------|--------------------|
| **MFTECmd**   | Analyse de la **Master File Table** (MFT) d’un volume NTFS |
| **RECmd**     | Analyse et parsing des **fichiers de registre Windows** |
| **EvtxECmd**  | Extraction des **journaux d’événements Windows** (EVTX) |
| **JLECmd**    | Analyse des fichiers **Jump Lists** |
| **LECmd**     | Analyse des **LNK (fichiers raccourcis)** |
| **RBCmd**     | Analyse des **RecentBag** (shellbags) |
| **SBECmd**    | ShellBag Explorer – données d’exploration de fichiers |
| **WFA**       | Windows Forensic Artifacts parser (Framework général) |
| **AmcacheParser** | Extraction et analyse des fichiers `Amcache.hve` |
| **AppCompatCacheParser** | Analyse des artefacts AppCompatCache (ShimCache) |
| **SQLECmd**   | Parsing des bases **SQLite (Chrome, journaux, etc.)** |
| **bstrings**  | Recherche de chaînes intelligentes dans les fichiers binaires |
| **pecmd**     | Analyse de fichiers PE (executables Windows) |
| **TimelineExplorer** | GUI pour visualiser chronologies CSV de logs |

---

## 💾 Téléchargement

### ✅ Télécharger tous les outils

1. Télécharger le **script de téléchargement automatique** :

```powershell
iwr -useb https://f001.backblazeb2.com/file/EricZimmermanTools/Get-ZimmermanTools.ps1 | iex
Ce script télécharge tous les outils dans un dossier .\Tools.

⚠️ Exécution possible uniquement avec PowerShell (Windows)

🧠 Focus : Outils phares en détail
🔍 MFTECmd
Analyse le fichier $MFT

Export CSV et Bodyfile pour timeline

Permet de voir les fichiers supprimés, timestamps, attributs NTFS, etc.

Exemple :


MFTECmd.exe -f "$MFT" --csv outdir --bodyfile mft.body
📝 EvtxECmd
Lit les fichiers .evtx (logs Windows)

Génère des exports lisibles (CSV, JSON)

Exemple :


EvtxECmd.exe -f System.evtx --csv out
🔐 RECmd
Lit les fichiers de registre Windows (NTUSER.DAT, SYSTEM, etc.)

Fournit des modèles (.revs) pour requêtes automatisées

Génère des rapports formatés

💣 AmcacheParser
Analyse le fichier Amcache.hve (présence d’exécutables, programmes installés)

Permet d’identifier des programmes exécutés même supprimés

🗂️ Utilitaires annexes
TimelineExplorer (GUI) : permet d’ouvrir les fichiers .csv générés par les outils pour une visualisation filtrée, triée, plus accessible qu’Excel.

bstrings : bien plus qu’un "strings", il détecte et classe les chaînes significatives (URL, chemins, scripts, etc.)

🔗 Liens utiles
🔧 GitHub principal : https://github.com/EricZimmerman

📄 Documentation centralisée : https://ericzimmerman.github.io/#!index.md

💬 Discord / DFIR Community (officiel) : souvent indiqué sur GitHub

📥 Outils : https://f001.backblazeb2.com/file/EricZimmermanTools/Get-ZimmermanTools.ps1

✅ Conseils pratiques
Exécute toujours les outils en tant qu’administrateur pour éviter les erreurs d’accès.

Combine les résultats avec des outils comme Plaso, Timesketch, Autopsy, ou Kibana.

Utilise un environnement de travail dédié (VM ou machine d’analyse).

yaml

