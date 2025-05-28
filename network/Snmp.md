# 🌐 Protocole SNMP (Simple Network Management Protocol)

## 📘 Introduction

Le **SNMP** est un protocole standard de l'Internet permettant la **gestion centralisée** des équipements réseau. Il facilite la **surveillance des performances**, la **détection de pannes** et la **configuration à distance** de divers dispositifs (routeurs, commutateurs, imprimantes, etc.).

---

## 📜 Historique

| Version | Année | Caractéristiques principales                        |
| ------- | ----- | --------------------------------------------------- |
| SNMPv1  | 1988  | Version initiale, fonctionnalités de base           |
| SNMPv2  | 1993  | Meilleures performances, nouveaux types de requêtes |
| SNMPv3  | 1998  | Sécurité avancée : authentification et chiffrement  |

---

## 🏗️ Architecture

SNMP repose sur une architecture simple composée de **trois composants** principaux :

* **🎛️ Manager (Gestionnaire)** : Application centrale qui envoie des requêtes SNMP.
* **🔌 Agent** : Logiciel embarqué dans les dispositifs réseau qui répond aux requêtes.
* **📚 MIB (Management Information Base)** : Base de données hiérarchique des objets gérés.

---

## 🔄 Fonctionnement

SNMP fonctionne principalement via **UDP** :

* Port **161** : Communication entre manager et agent
* Port **162** : Réception des traps

### ✳️ Opérations standards

* `GET` : Lire une valeur
* `SET` : Modifier une valeur
* `GET-NEXT` : Lire la valeur suivante
* `GET-BULK` : Lire un ensemble d'objets (v2/v3)
* `TRAP` : Notification asynchrone sans acquittement
* `INFORM` : Notification asynchrone avec acquittement

---

## 📦 MIB (Management Information Base)

La **MIB** structure les objets réseau sous forme d'**OID (Object Identifiers)**.

Exemple :

```bash
1.3.6.1.2.1.1.1  # sysDescr (description système)
```

Chaque OID représente une statistique ou un paramètre spécifique.

---

## 🔐 Sécurité

| Version    | Méthode de sécurité                                |
| ---------- | -------------------------------------------------- |
| SNMPv1/v2c | Community string (ex: "public")                    |
| SNMPv3     | Authentification (MD5/SHA) + Chiffrement (DES/AES) |

SNMPv3 introduit également le **contrôle d'accès basé sur l'utilisateur (VACM)**.

---

## ✅ Avantages

* 🌍 Standard ouvert et largement adopté
* ⚙️ Léger et peu consommateur de ressources
* 🔔 Support des notifications en temps réel (traps)

## ⚠️ Inconvénients

* 🔓 Sécurité faible en v1/v2c
* 🧩 Configuration complexe de SNMPv3
* 📄 Besoin de MIBs propriétaires pour certains matériels

---

## 🛠️ Cas d'utilisation

* 📡 Supervision réseau (Nagios, Zabbix, PRTG...)
* 🌡️ Surveillance matérielle (température, tension, etc.)
* 🔄 Automatisation des configurations à distance

---

## 🧾 Conclusion

Le protocole **SNMP** est essentiel pour la **gestion des réseaux modernes**. Il évolue pour répondre aux besoins en **sécurité** et **performance**, notamment avec SNMPv3 qui apporte une réponse robuste aux enjeux de cybersécurité.

---

## 🔗 Références

* [📄 RFC 1157 - SNMPv1](https://tools.ietf.org/html/rfc1157)
* [📄 RFC 1905 - SNMPv2](https://tools.ietf.org/html/rfc1905)
* [📄 RFC 3411 - SNMPv3 Architecture](https://tools.ietf.org/html/rfc3411)
