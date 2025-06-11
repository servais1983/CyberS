# 🔌 Protocole TCP (Transmission Control Protocol)

## 📘 Introduction

Le **protocole TCP** (Transmission Control Protocol) est l’un des protocoles fondamentaux de la suite **TCP/IP**. Il assure une **transmission fiable, ordonnée et sans erreur** des données entre applications sur un réseau IP. TCP est utilisé par des protocoles de niveau supérieur comme HTTP, FTP, SSH et SMTP.

---

## 🧱 Caractéristiques clés

* 📦 **Fiabilité** : les paquets perdus sont retransmis.
* 🔄 **Contrôle de flux** : régule la quantité de données envoyées.
* 📶 **Contrôle de congestion** : adapte la transmission à l'état du réseau.
* 📚 **Transmission ordonnée** : les segments arrivent dans l’ordre.
* 💬 **Full-duplex** : communication bidirectionnelle simultanée.

---

## ⚙️ Fonctionnement

TCP établit une **connexion orientée flux** entre deux hôtes à l’aide du **modèle client-serveur**.

### 🔁 Établissement de la connexion : Handshake 3 étapes

1. **SYN** : Le client envoie une requête de synchronisation.
2. **SYN-ACK** : Le serveur répond avec un acquittement + synchronisation.
3. **ACK** : Le client répond pour valider la connexion.

### 🧾 Transmission des données

Les données sont découpées en segments TCP. Chaque segment contient :

* Numéro de séquence
* Accusé de réception (ACK)
* Données utiles (payload)

### 🔚 Fermeture de la connexion : 4 étapes

1. FIN
2. ACK
3. FIN
4. ACK

---

## 🧩 Structure d’un segment TCP

| Champ                 | Description                       |
| --------------------- | --------------------------------- |
| Port source           | Port d’envoi                      |
| Port destination      | Port de réception                 |
| Numéro de séquence    | Suivi de l’ordre des segments     |
| Numéro d’acquittement | Confirme la réception de données  |
| Flags                 | SYN, ACK, FIN, RST, etc.          |
| Fenêtre               | Taille de la fenêtre de réception |
| Checksum              | Vérification d’intégrité          |

---

## 📡 Ports TCP communs

| Service | Port |
| ------- | ---- |
| HTTP    | 80   |
| HTTPS   | 443  |
| FTP     | 21   |
| SSH     | 22   |
| SMTP    | 25   |
| Telnet  | 23   |

---

## ✅ Avantages

* 🔁 Transmission fiable et vérifiée
* 📚 Gestion de l’ordre des paquets
* 🔧 Adaptatif selon la capacité du réseau

## ⚠️ Inconvénients

* 🐢 Moins rapide que UDP (en raison des vérifications)
* 🧠 Complexité de gestion
* 📈 Overhead plus important

---

## 🔍 Cas d’utilisation

* 📥 Téléchargements de fichiers (FTP, HTTP)
* 📡 Communication sécurisée (SSH, HTTPS)
* 🧪 Transferts critiques nécessitant fiabilité

---

## 🧠 Comparaison TCP vs UDP

| Critère             | TCP                  | UDP                  |
| ------------------- | -------------------- | -------------------- |
| Fiabilité           | ✅ Oui                | ❌ Non                |
| Ordre des paquets   | ✅ Oui                | ❌ Non                |
| Connexion           | ✅ Orientée connexion | ❌ Sans connexion     |
| Débit               | 📉 Moins rapide      | 📈 Plus rapide       |
| Utilisation typique | Web, SSH, Mail       | DNS, VoIP, Streaming |

---

## 📚 Références

* [RFC 793 - TCP](https://tools.ietf.org/html/rfc793)
* [TCP Explained - Cloudflare](https://www.cloudflare.com/learning/ddos/glossary/transmission-control-protocol-tcp/)
* [Wikipedia - TCP](https://fr.wikipedia.org/wiki/Transmission_Control_Protocol)

---

> 💡 **Remarque** : TCP est la colonne vertébrale de nombreuses communications sur Internet. Sa compréhension est indispensable pour les développeurs, administrateurs système et analystes réseau.
