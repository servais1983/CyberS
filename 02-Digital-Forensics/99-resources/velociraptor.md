# Guide d'installation et d'utilisation de **Velociraptor**

*Dernière mise à jour : 19 juin 2025*

---

## Table des matières

1. [Introduction](#introduction)
2. [Téléchargement](#téléchargement)
3. [Configuration rapide](#configuration-rapide)
4. [Démarrage du serveur](#démarrage-du-serveur)
5. [Connexion à l'interface Web](#connexion-à-linterface-web)
6. [Déploiement d'un agent](#déploiement-dun-agent)
7. [Collecte de la « carte d'identité »](#collecte-de-la-carte-didentité)
8. [Commandes utiles](#commandes-utiles)
9. [Mise à jour](#mise-à-jour)
10. [Ressources](#ressources)

---

## Introduction

<a name="introduction"></a>
Velociraptor est un outil **DFIR & EDR open‑source** permettant la collecte forensique à grande échelle et la chasse aux menaces en temps réel.

Ce guide pas‐à‐pas couvre :

* l'installation sous **Windows** (binaire autonome),
* la génération d'une configuration serveur,
* le démarrage et la connexion à l'interface Web,
* les premières collectes d'informations (« carte d'identité » d'un hôte).

> **Pré‑requis :** PowerShell 5+, droits administrateur, connexion Internet (pour le téléchargement initial).

---

## Téléchargement

<a name="téléchargement"></a>

1. Rendez‑vous sur la page **Releases** officielle : [https://github.com/Velocidex/velociraptor/releases](https://github.com/Velocidex/velociraptor/releases)
2. Notez la version la plus récente (au **19/06/2025 : v0.74.2**).
3. Téléchargez le binaire Windows 64 bits :

```powershell
Invoke-WebRequest -Uri "https://github.com/Velocidex/velociraptor/releases/download/v0.74.2/velociraptor-v0.74.2-windows-amd64.exe" -OutFile "C:\Velociraptor\velociraptor.exe"
```

4. (Facultatif) : décochez *« Bloquer »* dans les **Propriétés** du fichier si SmartScreen l'a marqué.

---

## Configuration rapide

<a name="configuration-rapide"></a>
Créez un répertoire de travail puis générez la configuration :

```powershell
cd C:\Velociraptor
.\velociraptor.exe config generate -i
```

Répondez :

| Question              | Réponse conseillée                  |
| --------------------- | ----------------------------------- |
| TLS / SSL             | **Self‑signed certificates** (test) |
| Hostname              | `localhost`                         |
| Frontend port         | `8086` (défaut)                     |
| GUI port              | `8889` (défaut)                     |
| Admin user / password | Choisissez un mot de passe fort     |

Le fichier **`server.config.yaml`** est créé dans le dossier courant.

---

## Démarrage du serveur

<a name="démarrage-du-serveur"></a>

```powershell
cd C:\Velociraptor
.\velociraptor.exe --config .\server.config.yaml frontend -v
```

Si tout va bien, la console affiche :

```
[INFO] Listening on https://localhost:8889 (Admin UI)
[INFO] Frontend running on 127.0.0.1:8086 (for clients)
```

> **Astuce :** ajoutez `--logtostderr --v 10` pour un débogage détaillé.

Laissez la fenêtre PowerShell **ouverte** : elle héberge le serveur.

---

## Connexion à l'interface Web

<a name="connexion-à-linterface-web"></a>

1. Ouvrez votre navigateur et allez à : `https://localhost:8889`
2. Ignorez l'avertissement SSL (*Certificat auto‑signé*).
3. Connectez‑vous avec l'utilisateur/mot de passe défini à l'étape précédente.

Vous arrivez sur le tableau de bord **Velociraptor**.

---

## Déploiement d'un agent

<a name="déploiement-dun-agent"></a>

### Via l'interface

1. Menu **Server Artifacts** → `Server.Utils.CreateMSI` → *Launch*.
2. Renseignez (ou laissez) les valeurs par défaut et validez.
3. Téléchargez le **MSI** généré ; il contient la configuration embarquée.
4. Exécutez le MSI sur la machine cible (administrateur requis).

### En ligne de commande (portable)

```powershell
# Sur le poste client
.\velociraptor.exe --config client.config.yaml service install -v
```

Le client apparaît dans l'onglet **Clients** du serveur sous quelques secondes.

---

## Collecte de la « carte d'identité »

<a name="collecte-de-la-carte-didentité"></a>

1. **Clients** → cliquez sur l'hôte cible.
2. Onglet **Artifacts** → **Collect**.
3. Recherchez `Windows.System.Interrogation` ; sélectionnez‑le.
4. *Launch* sans modifier les paramètres.
5. Suivez la progression, puis ouvrez les résultats dans **Collected**.

> Ce méta‑artefact inclut : infos système, réseau, utilisateurs, processus, services, tâches planifiées, disques, etc.

---

## Commandes utiles

<a name="commandes-utiles"></a>

| Action                          | Commande PowerShell                                                            |
| ------------------------------- | ------------------------------------------------------------------------------ |
| Vérifier la version             | `.\velociraptor.exe version`                                                   |
| Liste des utilisateurs          | `SELECT * FROM users()` (Notebook)                                             |
| Processus live                  | `SELECT * FROM pslist()`                                                       |
| Redémarrer le serveur (service) | `Restart-Service Velociraptor`                                                 |
| Logs en temps réel              | `.\velociraptor.exe --config server.config.yaml --logtostderr --v 10 frontend` |

---

## Mise à jour

<a name="mise-à-jour"></a>

1. Téléchargez le nouveau binaire et remplacez l'ancien :

```powershell
Invoke-WebRequest -Uri "https://github.com/Velocidex/velociraptor/releases/download/v0.74.3/velociraptor-v0.74.3-windows-amd64.exe" -OutFile "C:\Velociraptor\velociraptor.exe"
```

2. Redémarrez le service ou la console : `Ctrl+C` puis relancez la commande `frontend -v`.

La configuration et le datastore restent valides.

---

## Ressources

<a name="ressources"></a>

* Documentation officielle : [https://docs.velociraptor.app](https://docs.velociraptor.app)
* Artefacts communautaires : [https://github.com/Velocidex/velociraptor-docs](https://github.com/Velocidex/velociraptor-docs)
* Forum & Slack : [https://velociraptor.app/community](https://velociraptor.app/community)

---

> 🐾 *Dig deep & hunt smart !*
