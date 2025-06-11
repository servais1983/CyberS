# 🚀 Velociraptor - Installation & Premiers Tests

Velociraptor est un outil open source de **digital forensics** et de **threat hunting**. Il permet d'interroger les systèmes à distance via un langage puissant appelé **VQL** (Velociraptor Query Language).

Ce guide vous accompagne dans l’installation de Velociraptor en mode local (standalone) et l'exécution de premières requêtes pour récupérer des informations basiques sur un système.

---

## 📦 Prérequis

- OS : Linux, Windows ou macOS
- Accès terminal
- Droits d'exécution

---

## 🛠️ Installation

### 1. Télécharger le binaire

Rendez-vous sur la page [Releases GitHub](https://github.com/Velocidex/velociraptor/releases) et téléchargez le binaire adapté à votre OS.

#### Exemple pour Linux :

```bash
wget https://github.com/Velocidex/velociraptor/releases/download/v0.7.1/velociraptor-v0.7.1-linux-amd64
chmod +x velociraptor-v0.7.1-linux-amd64
mv velociraptor-v0.7.1-linux-amd64 velociraptor
```

---

### 2. Générer la configuration

```bash
./velociraptor config generate -i
```

**Réponses à fournir :**
- Type : `Standalone`
- Port HTTP : `8000` (ou autre)
- Interface Web : `127.0.0.1` (pour accès local)

---

### 3. Lancer Velociraptor en mode standalone

```bash
./velociraptor --config velociraptor.config.yaml frontend

ou verbeux .\velociraptor.exe -v --config velociraptor.config.yaml frontend

```

---

## 🔍 Exécuter une première requête VQL

### 🔸 Option 1 : Via le terminal (ligne de commande)

Une fois le service lancé, ouvrez un autre terminal et exécutez :

```bash
./velociraptor --config velociraptor.config.yaml query "SELECT os_info.hostname AS Hostname, os_info.timezone AS Timezone, interfaces.addresses[0] AS IP FROM info()"
```

### 🔸 Option 2 : Via l’interface graphique (GUI)

1. Accédez à l’interface web : `https://localhost:8000`
2. Connectez-vous avec l'identifiant administrateur créé.
3. Allez dans le menu **"Notebooks"** ou **"Hunt Manager"**
4. Créez un nouveau **Notebook**
5. Collez la requête suivante dans l’éditeur VQL :

```vql
SELECT os_info.hostname AS Hostname, os_info.timezone AS Timezone, interfaces.addresses[0] AS IP FROM info()
```

6. Cliquez sur **"Run Query"** pour exécuter la commande et afficher les résultats.

---

### ✅ Ce que cette requête retourne :

| Champ     | Description                      |
|-----------|----------------------------------|
| `Hostname` | Nom de la machine                |
| `Timezone` | Fuseau horaire configuré         |
| `IP`       | Première adresse IP détectée     |

---

### 🔧 Variante : afficher toutes les adresses IP par interface

```vql
SELECT
  os_info.hostname AS Hostname,
  os_info.timezone AS Timezone,
  iface.name AS Interface,
  addr AS IP
FROM info()
  JOIN interfaces AS iface ON true
  JOIN iface.addresses AS addr ON true
```

---

## 📚 Ressources utiles

- Documentation officielle : [https://docs.velociraptor.app](https://docs.velociraptor.app)
- Guide VQL : [https://docs.velociraptor.app/docs/vql](https://docs.velociraptor.app/docs/vql)
- GitHub : [https://github.com/Velocidex/velociraptor](https://github.com/Velocidex/velociraptor)

---

## 🧪 À explorer ensuite

- Créer des **artefacts personnalisés**
- Lancer des **chasses sur les processus** ou fichiers
- Utiliser la **console web Velociraptor**

---

## 🔧 Commandes VQL courantes

Voici quelques exemples de commandes VQL fréquemment utilisées pour explorer un système :

### 📋 Informations système de base
```vql
SELECT * FROM info()
```

### 🧠 Liste des processus en cours
```vql
SELECT * FROM pslist()
```

### 📁 Parcourir un répertoire (ex. : /tmp)
```vql
SELECT * FROM glob(globs='/tmp/*')
```

### 📄 Contenu d’un fichier texte
```vql
SELECT * FROM read_file(filename='/etc/hostname')
```

### 🔍 Recherche dans les fichiers (ex. : fichiers contenant "password")
```vql
SELECT * FROM grep(pattern='password', target=glob(globs='/etc/*'))
```

### 📂 Lister les utilisateurs du système
```vql
SELECT * FROM users()
```

### 📜 Liste des connexions réseau actives
```vql
SELECT * FROM netstat()
```

### 📑 Historique bash (si présent)
```vql
SELECT * FROM read_file(filename='/home/user/.bash_history')
```

### 🕵️‍♂️ Rechercher des fichiers exécutables récents
```vql
SELECT * FROM glob(globs='/usr/bin/*') WHERE AccessTime > now() - 7*24*60*60
```

---

## 📘 Astuce : Créer ses propres artefacts

Vous pouvez créer des artefacts personnalisés avec plusieurs requêtes VQL pour automatiser des tâches d’investigation.
