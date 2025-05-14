# 📁 Analyse forensic de la MFT (Master File Table) – FTK Imager + mft2csv

La **MFT (Master File Table)** contient des métadonnées sur **tous les fichiers et dossiers** d’un volume NTFS. Elle est essentielle pour reconstituer une chronologie ou identifier des fichiers effacés.

---

## 🧰 Étape 1 – Extraire le fichier `$MFT` avec FTK Imager

1. **Monter l’image disque dans FTK Imager**
   - `File > Add Evidence Item > Image File`
   - Choisir votre image `.E01` ou `.dd`

2. **Accéder à la racine du volume NTFS**
   - Dans la vue “Evidence Tree”, ouvrir :  
     ➜ `Partition X:` → `Root Directory`

3. **Trouver le fichier `$MFT`**
   - Le fichier `$MFT` est un fichier système caché à la racine.
   - Clic droit sur `$MFT` → **Export File**

4. **Choisir un emplacement d’export**
   - Exemple : `D:\forensic_exports\$MFT`

---

## 🛠️ Étape 2 – Convertir la MFT avec mft2csv

**mft2csv** est un outil Python permettant de convertir un fichier `$MFT` brut en un tableau CSV structuré.

### 🔧 Prérequis :
- Python 3.x
- Outil [mft2csv](https://github.com/dkovar/mft2csv) :  
  Télécharger ou cloner :

```bash
git clone https://github.com/dkovar/mft2csv.git
cd mft2csv
pip install -r requirements.txt
🔁 Conversion de la MFT :

python mft2csv.py --output mft.csv --bodyfile mft.body D:\forensic_exports\$MFT
➡️ Cela génère :

mft.csv → lisible dans Excel

mft.body → format corps UNIX (timeline)

🕒 Étape 3 – Créer une chronologie (timeline) avec la MFT
Utilise l'outil log2timeline ou mactime du package SleuthKit pour générer une chronologie à partir du fichier .body.

🔹 Option 1 – Avec mactime (le plus simple)

mactime -b mft.body -d > timeline.csv
Cela crée un tableau avec :

Horodate (Modified, Accessed, Changed, Created)

Chemin du fichier

UID, GID, Permissions, etc.

🔹 Option 2 – Intégrer dans une timeline complète avec log2timeline (Plaso)
Plaso peut ingérer plusieurs sources (MFT, registre, journaux Windows). Exemple :


log2timeline.py plaso.dump mft.body
psort.py -o l2tcsv plaso.dump > timeline.csv
📊 Exploiter la chronologie
Importe timeline.csv dans Excel ou un outil de visualisation (Kibana, Timesketch, Excel PowerPivot) pour :

Reconstituer les activités de l'utilisateur

Voir quand un fichier a été créé, modifié, supprimé

Détecter des fichiers ou dossiers temporaires suspects

Repérer des effacements récents (souvent révélateurs)

✅ Bonnes pratiques
Toujours croiser la MFT avec d'autres artefacts (Prefetch, Registry, Journaux Windows)

Attention aux horodates falsifiables (ex : timestomping)

Conserver le hash du $MFT extrait pour l'intégrité

📘 Références
FTK Imager Download

mft2csv GitHub

The Sleuth Kit & Autopsy

Timesketch Timeline Tool

yaml

