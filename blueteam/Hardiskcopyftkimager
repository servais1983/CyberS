# 💽 Faire une copie du disque dur avec FTK Imager

FTK Imager permet de créer une **image forensique** (copie fidèle bit à bit) d’un disque dur, d'une partition ou d’un support amovible. Cette opération est cruciale en investigation numérique pour préserver l'intégrité des preuves.

---

## 🛠️ Prérequis

- Télécharger et installer **FTK Imager** (ou le lancer en version portable).
- Avoir les **droits administrateur** sur la machine cible.
- Prévoir un **support de stockage externe** avec assez d’espace pour accueillir l’image (généralement en `.E01` ou `.dd`).

---

## 🧭 Étapes pour créer une image du disque

1. **Lancer FTK Imager en tant qu'administrateur**
   - Clic droit > *"Exécuter en tant qu'administrateur"*.

2. Aller dans le menu **`File` > `Create Disk Image`**

3. Sélectionner le **type de source** :
   - 🖴 **Physical Drive** → pour capturer un disque entier (secteur par secteur).
   - 💽 **Logical Drive** → pour une partition (C:, D:, etc.).
   - 🗂️ **Image File**, **Folder**, etc. → autres sources.

4. Sélectionner le **disque à copier** (⚠️ attention à ne pas se tromper de disque !)

5. Choisir le **type de format de sortie** :
   - `.E01` (**EnCase image format**) – recommandé pour forensic (avec compression, hash, métadonnées).
   - `.dd` – image brute, sans métadonnées.
   - `.AFF` – Advanced Forensics Format (moins courant).

6. Configurer les **informations du cas** *(facultatif mais recommandé)* :
   - Nom du cas
   - Référence
   - Description
   - Nom de l'examinateur

7. Choisir le **dossier de destination** pour enregistrer l’image :
   - Ex: `E:\images\cas001.E01`
   - Vous pouvez définir une taille de segment (ex: 2 Go) si nécessaire.

8. ✅ Cocher les options :
   - **Verify images after they are created** (fortement recommandé)
   - **Add AD1/MD5/SHA1 hash** pour garantir l'intégrité

9. **Lancer la création de l’image**
   - Cliquez sur **Start**.
   - La durée dépend de la taille du disque et de la vitesse du support.

---

## 📂 Résultat

Vous obtiendrez :
- Un ou plusieurs fichiers `.E01` (ou `.dd`)
- Un fichier de log de l’opération
- Un fichier de hash (`.txt` ou `.csv`) pour vérification

---

## ✅ Vérification

Après la copie :
- Vérifiez que le **hash MD5/SHA1** de l’image correspond à celui du disque source.
- Documentez :
  - Le nom du disque, sa taille
  - La date/heure de l’image
  - Le support de destination

---

## 📘 Références

- [Guide FTK Imager - AccessData](https://accessdata.com/product-download)
- [Analyse des images disque avec Autopsy, X-Ways, etc.]

