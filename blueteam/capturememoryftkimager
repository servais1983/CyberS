# 📥 Capture de la mémoire vive avec FTK Imager

FTK Imager est un outil de forensic gratuit développé par **AccessData**. Il permet, entre autres, de réaliser une **capture de la mémoire RAM** d’un système en cours d’exécution, ce qui est essentiel en analyse forensic pour récupérer des données volatiles comme les processus, connexions réseau ou mots de passe en clair.

---

## 🛠️ Prérequis

- Avoir **FTK Imager** installé (ou sur une clé USB).
- Être **administrateur** de la machine ciblée. (non possible à distance)
- Désactiver, si possible, les applications qui pourraient interférer avec la capture.
- Préparer un **espace de stockage suffisant** pour le dump mémoire.

---

## 🔍 Étapes pour capturer la mémoire

1. **Lancer FTK Imager en tant qu'administrateur**
   - Clic droit sur `FTK Imager.exe` > "Exécuter en tant qu’administrateur".

2. **Aller dans le menu** `File` > `Capture Memory...`

3. **Configurer les options de capture** :
   - ✅ Cochez **"Include pagefile"** pour inclure le fichier d’échange (`pagefile.sys`).
   - 📁 Choisissez un **dossier de destination** pour le fichier `.mem` (ex : `D:\captures\dump1.mem`).

4. **Démarrer la capture**
   - Cliquez sur **Start**.
   - Attendez la fin du processus (cela peut prendre quelques minutes).

5. **Vérification**
   - Une fois la capture terminée, vérifiez la présence du fichier `.mem` dans le dossier sélectionné.

---

## 📂 Résultat

Le fichier généré est un **dump brut de la mémoire vive**, que vous pouvez analyser avec des outils comme :

- **Volatility** (Linux / Windows)
- **Rekall**
- **Redline** (Mandiant)

---

## ⚠️ Recommandations

- Toujours effectuer la capture **le plus tôt possible** lors d'une investigation.
- Ne jamais stocker le dump sur le disque système de la machine analysée.
- Documenter soigneusement : date, heure, nom de la machine, utilisateur connecté.

---

## 📘 Références

- [FTK Imager - AccessData](https://accessdata.com/product-download)
- [Volatility Framework](https://www.volatilityfoundation.org/)

