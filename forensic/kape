🛠️ KAPE (Kroll Artifact Parser and Extractor)
🧩 Introduction
KAPE est un outil de collecte et d’analyse forensique développé par Eric Zimmerman. Il est utilisé pour :

Collecter rapidement des artefacts numériques sur un système.

Exécuter des outils d’analyse sur les artefacts collectés.

Gagner du temps et automatiser les tâches courantes d’investigation.

⚠️ KAPE est conçu exclusivement pour une utilisation légale et autorisée dans des contextes forensiques.

📦 Fonctionnalités clés
🧲 Collecte rapide des artefacts forensiques (RAM, journaux, historiques, etc.).

🔧 Exécution de modules personnalisables pour analyser les données.

🗃️ Génération de rapports (CSV, JSON, HTML).

🔌 Extensible via Targets et Modules définis en JSON.

🧑‍💻 Utilisation possible via CLI ou GUI.

🧠 Architecture de KAPE
KAPE fonctionne en deux phases principales :

Phase	Description
🎯 Targets	Collecte des artefacts depuis une source (live ou image disque)
🧪 Modules	Exécution de scripts/outils sur les fichiers collectés

📁 Structure des répertoires
python

KAPE/
├── KAPE.exe
├── Get-KAPEUpdate.ps1
├── Modules/
│   ├── .\bin\
│   └── .\Modules\
├── Targets/
│   └── .\Targets\
├── Logs/
└── Output/
⚙️ Installation
Télécharger depuis le GitHub d'Eric Zimmerman.

Extraire l’archive dans un répertoire.

Mettre à jour les Targets et Modules :

powershell

.\Get-KAPEUpdate.ps1
💡 Concepts clés : Targets & Modules
🎯 Targets
Définit quoi collecter (ex : historique de navigateur, fichiers système).

Fichier .tkape (JSON) :

json

{
  "TargetName": "BrowserHistory",
  "Author": "Eric Zimmerman",
  "Paths": [
    "%AppData%\\Local\\Google\\Chrome\\User Data\\Default\\History"
  ]
}
🧪 Modules
Définit quel outil exécuter sur les artefacts collectés.

Fichier .mkape (JSON) :

json

{
  "ModuleName": "AnalyzeChromeHistory",
  "Tool": "ChromehistoryParser.exe",
  "CommandLine": "-f %InputFile% -o %OutputDirectory%",
  "InputExtensions": [".db"],
  "OutputExtension": ".csv"
}
🧪 Utilisation : Ligne de commande (CLI)
📥 Collecte des artefacts
bash

kape.exe --tsource C: --tdest D:\Output --target BrowserHistory
--tsource : Source (ex: disque C:)

--tdest : Destination des artefacts collectés

--target : Nom du Target à utiliser

🔎 Exécution des modules
bash

kape.exe --msource D:\Output --mdest D:\Report --module AnalyzeChromeHistory
--msource : Dossier contenant les fichiers à analyser

--mdest : Où stocker les résultats

--module : Nom du module à exécuter

⚡ Tout en un
bash

kape.exe --tsource C: --tdest D:\Artifacts --target BrowserHistory ^
         --msource D:\Artifacts --mdest D:\Report --module AnalyzeChromeHistory
🖥️ Interface Graphique (Gkape)
KAPE est aussi livré avec une interface graphique :

Sélection de Targets via checkboxes

Configuration des chemins source/destination

Exécution et logs temps réel

✅ Bonnes pratiques
🧪 Tester les modules sur des machines non critiques.

🔐 Travailler uniquement dans des environnements autorisés.

💾 Toujours utiliser un support d’export externe (clé USB, disque dur).

🧼 Éviter de modifier la source en lecture.

🔄 Garder les Targets/Modules à jour avec Get-KAPEUpdate.ps1.

🛠️ Outils tiers souvent utilisés avec KAPE
Outil	Description
MFTECmd	Analyse des MFT
RECmd	Exploration du Registre
EvtxECmd	Analyse des journaux d’événements
JLECmd	Analyse des Jump Lists
LECmd	Analyse des LNK

📚 Ressources
GitHub (KAPE Files) : https://github.com/EricZimmerman/KapeFiles

Wiki officiel : https://github.com/EricZimmerman/KapeFiles/wiki

Documentation outils : https://ericzimmerman.github.io/#!index.md

Discord DFIR : Serveurs communautaires d’entraide

🧑‍🔬 Cas d’usage typique
🎯 Incident Response
En cas de compromission, KAPE peut collecter des logs système, fichiers suspects et exécuter automatiquement des outils pour aider à l’investigation initiale en quelques minutes.

🧾 Exemple complet de commande
bash

kape.exe --tsource C: --tdest D:\KapeOut ^
         --target RegistryHives,BrowserHistory,SystemLogs ^
         --msource D:\KapeOut --mdest D:\KapeResults ^
         --module EvtxECmd,LECmd,RECmd ^
         --vhdx C:\disk.vhdx
