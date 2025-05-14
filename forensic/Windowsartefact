# 🕵️‍♂️ Artefacts Windows en Forensic

Les artefacts Windows sont des **traces résiduelles** laissées par les utilisateurs, les logiciels ou le système d’exploitation. Ils permettent de **reconstituer l’activité d’un système**, détecter une compromission ou analyser un comportement utilisateur.

---

## 📁 1. Fichiers de registre (Registry)

| Clé / Fichier              | Description                                    | Emplacement                         |
|---------------------------|------------------------------------------------|-------------------------------------|
| `NTUSER.DAT`              | Paramètres utilisateur (programmes, MRU, etc.) | `C:\Users\<user>\NTUSER.DAT`        |
| `SAM`, `SYSTEM`, `SECURITY`, `SOFTWARE` | Configuration système et utilisateurs       | `C:\Windows\System32\config\`       |

🔧 **Outils** :
- RECmd (Eric Zimmerman)
- Registry Explorer
- regipy (Python)
- Autopsy

---

## 📝 2. Journaux d’événements (Event Logs)

| Nom        | Utilité principale                         | Fichier         |
|------------|---------------------------------------------|-----------------|
| `System.evtx` | Démarrages, périphériques, services         | `C:\Windows\System32\winevt\Logs\` |
| `Security.evtx` | Connexions, UID, logs audit               | idem            |
| `Application.evtx` | Logs des logiciels Windows               | idem            |

🔧 **Outils** :
- `EvtxECmd` (Zimmerman)
- Event Log Explorer
- Plaso (log2timeline)

---

## ⏳ 3. MFT et journaux NTFS

| Fichier       | Rôle                                           |
|---------------|------------------------------------------------|
| `$MFT`        | Master File Table (index de tous les fichiers) |
| `$LogFile`    | Journal NTFS des changements                   |
| `$UsnJrnl`    | Journal d’accès, modification, suppression     |

🔧 **Outils** :
- `MFTECmd` (Zimmerman)
- `AnalyzeMFT`, `mft2csv`
- TSK (`fsstat`, `fls`)

---

## 🧭 4. Raccourcis et fichiers temporaires

| Fichier / Artefact | Description                                |
|--------------------|--------------------------------------------|
| `.lnk` files       | Fichiers de raccourci                      |
| `Recent`           | Derniers fichiers ouverts                  |
| `Thumbs.db`        | Cache des miniatures d’images              |
| `Prefetch`         | Infos de lancement des programmes (XP/10)  |

🔧 **Outils** :
- `LECmd`, `JLECmd` (Zimmerman)
- NirSoft ShellBagsView
- PECmd (préfetch parser)

---

## 🌐 5. Activité Internet

| Type             | Emplacement / Fichier                      |
|------------------|--------------------------------------------|
| Historique Edge  | `WebCacheV01.dat`                          |
| Historique Chrome | `History` (base SQLite)                  |
| Cookies, Cache   | `AppData\Local\Microsoft\Windows\WebCache`|

🔧 **Outils** :
- `BrowsingHistoryView` (NirSoft)
- `SQLECmd` (Zimmerman)
- `WebCacheView`, `IECacheView`

---

## 🗂️ 6. Shellbags (activité des dossiers ouverts)

| Artefact     | Emplacement                                   |
|--------------|-----------------------------------------------|
| Shellbags    | `NTUSER.DAT` (clé BagMRU/BagMRU Size, etc.)   |

🔧 **Outils** :
- `SBECmd` (Zimmerman)
- ShellBagExplorer
- RECmd + modèle `.revs`

---

## 🧠 7. Amcache & Shimcache

| Artefact        | Description                           |
|------------------|----------------------------------------|
| Amcache.hve      | Liste des exécutables lancés           |
| AppCompatCache   | Cache de compatibilité Windows         |

🔧 **Outils** :
- `AmcacheParser`
- `AppCompatCacheParser`
- RECmd avec modèles intégrés

---

## 🧱 8. Jump Lists

| Artefact    | Description                                  |
|-------------|----------------------------------------------|
| *.automaticDestinations-ms | Historique de fichiers ouverts par application |
| *.customDestinations-ms | Historique personnalisé             |

🔧 **Outils** :
- `JLECmd` (Zimmerman)
- JumpList Explorer

---

## 🧩 9. Activité utilisateur

| Comportement       | Artefacts impliqués                                   |
|--------------------|--------------------------------------------------------|
| Connexions         | `Security.evtx`, `TerminalServices`, `SRUM`, `LogonEvents` |
| Fichiers lancés    | Prefetch, Amcache, MFT, LNK                            |
| Répertoires explorés | Shellbags, Recent, JumpLists                          |
| Navigation web     | WebCache, SQLite History                               |

---

## 🔧 10. Outils recommandés

- 🧠 **Eric Zimmerman Tools** → https://ericzimmerman.github.io/
- 🔎 **Autopsy** (SleuthKit GUI)
- 🧬 **Plaso (log2timeline)** → timeline automatique
- 🛠️ **Timesketch** → analyse visuelle de timeline
- 📦 **Velociraptor** → collecte à distance d'artefacts forensic

---

## 📘 Références

- [DFIR Artifact Museum](https://dfir.art)
- [Zimmerman Tools](https://ericzimmerman.github.io/)
- [SANS DFIR Poster](https://www.sans.org/posters/windows-forensic-analysis/)
- [ForensicWiki](https://forensics.wiki/windows/)

