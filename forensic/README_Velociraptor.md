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
```

---

## 🔍 Exécuter une première requête VQL

Une fois le service lancé, ouvrez un autre terminal et exécutez :

```bash
./velociraptor --config velociraptor.config.yaml query "SELECT Hostname, Timezone, Interfaces FROM info()"
```

### ✅ Ce que cette requête retourne :
| Champ | Description |
|-------|-------------|
| `Hostname` | Nom de la machine |
| `Timezone` | Fuseau horaire configuré |
| `Interfaces` | Interfaces réseau avec adresses IP |

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
