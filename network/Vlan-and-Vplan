
# 🌐 Guide Complet – VLAN & PVLAN en Entreprise

## 🎯 Objectif

Segmenter logiquement un réseau physique en plusieurs sous-réseaux pour :

- 🔒 Améliorer la **sécurité**
- 🚦 Réduire le **bruit de broadcast**
- 🧩 Faciliter l’**organisation logique** (DMZ, prod, dev...)
- 🔧 Permettre une **meilleure gestion du trafic**

---

## 📚 1. Définitions

### 🔸 VLAN (Virtual LAN)

Un **VLAN** est un réseau logique indépendant, créé au-dessus d’une infrastructure physique unique, permettant d’isoler des groupes de machines au niveau de la couche 2 (Data Link Layer).

### 🔹 PVLAN (Private VLAN)

Un **PVLAN** est une extension du VLAN standard qui permet une **isolation plus fine** entre les ports au sein d’un même VLAN. Principalement utilisé dans les environnements multi-locataires (ex : datacenters).

---

## 🧱 2. Types de PVLAN

| Type         | Description                                               |
|--------------|-----------------------------------------------------------|
| **Primary VLAN**   | VLAN parent contenant les PVLAN associés               |
| **Isolated**       | Aucun port ne peut parler à un autre, sauf au promiscuous |
| **Community**      | Ports peuvent communiquer entre eux + promiscuous     |
| **Promiscuous**    | Peut parler à tous (routeur, firewall, gateway)       |

---

## 🧩 3. Cas d’usage

- 🧑‍💻 Séparer les utilisateurs (comptabilité, RH, IT)
- 🔐 Isoler des serveurs sensibles dans un VLAN dédié
- 🌐 DMZ (zone démilitarisée) dans un PVLAN Isolated
- 🛑 Bloquer la communication inter-VM dans un même VLAN
- 📦 Contenir un incident réseau (limiter les L2 lateral moves)

---

## ⚙️ 4. Configuration – VLAN

### 🖧 Cisco IOS (exemple)

```cisco
# Créer un VLAN
vlan 10
 name PROD

# Assigner un port
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 10

🌐 Juniper (JunOS)
juniper

set vlans PROD vlan-id 10
set interfaces ge-0/0/1 unit 0 family ethernet-switching vlan members PROD
🐧 Linux (avec iproute2)

# Créer un VLAN 10 sur eth0
ip link add link eth0 name eth0.10 type vlan id 10
ip addr add 192.168.10.1/24 dev eth0.10
ip link set up eth0.10
⚙️ 5. Configuration – PVLAN (Cisco)
cisco

vlan 100
 private-vlan primary

vlan 101
 private-vlan isolated

vlan 102
 private-vlan community

# Lier les PVLAN au VLAN primaire
vlan 100
 private-vlan association 101,102

# Configuration des ports
interface FastEthernet0/1
 switchport mode private-vlan host
 switchport private-vlan host-association 100 101

interface FastEthernet0/24
 switchport mode private-vlan promiscuous
 switchport private-vlan mapping 100 101,102
🔐 6. Bonnes pratiques de sécurité
🧱 Segmenter tout ce qui est critique (AD, bases de données, sauvegardes)

🔄 Interdire la communication inter-VLAN sans firewall (ACL)

🔍 Superviser le trafic inter-VLAN

🧑‍🔧 Bloquer les VLAN inutilisés sur les trunks

⛔ Désactiver DTP (Dynamic Trunking Protocol)

cisco

interface FastEthernet0/1
 switchport mode access
 switchport nonegotiate

🛠️ 7. Outils de supervision
Outil	Usage
Wireshark	Analyse du trafic VLAN
Nmap	Détection d’isolement L2
NetBox	Documentation des VLAN
LibreNMS	Supervision de ports VLAN
Grafana/Prometheus	Dashboard réseau

🧪 8. Tests & vérifications
📌 Vérifier le VLAN sur un port Cisco
cisco

show vlan brief
show interfaces switchport
🧪 Linux – ping entre VLANs
Tester la séparation en pingant des machines sur d’autres VLANs.

Utiliser tcpdump pour observer si des paquets passent sur des VLANs inattendus.

🧾 9. Commandes utiles
Action	Cisco	Linux
Voir les VLAN configurés	show vlan brief	ip -d link show
Voir les PVLANs	show vlan private-vlan	—
Configurer une interface VLAN	switchport access vlan 10	ip link add link eth0 name eth0.10...
Capturer les paquets VLAN	—	tcpdump -i eth0 vlan

🧩 10. VLAN vs PVLAN – Comparatif
Critère	VLAN classique	PVLAN
Isolement entre ports	Non (au sein du VLAN)	Oui (selon type PVLAN)
Routage inter-réseau	Via L3 uniquement	PVLAN = L2 avec contrôle
Complexité	Faible	Moyenne à élevée
Cas d'usage typique	LAN de service	DMZ, datacenter multi-tenant

📘 11. Annexes & Références
🔗 Cisco PVLAN Documentation

🔗 Juniper VLAN Guide

🧾 Linux VLAN HOWTO

🔒 ANSSI – Sécurité des réseaux locaux

yaml


