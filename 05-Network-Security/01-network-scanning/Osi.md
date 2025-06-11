# 🌐 Guide Complet – Modèle OSI (Open Systems Interconnection)

## 🎯 Objectif

Comprendre et exploiter le **modèle OSI** pour :

- Diagnostiquer les problèmes réseau  
- Concevoir une architecture sécurisée  
- Documenter les flux et responsabilités  
- Former les équipes IT (réseau, sécurité, dev)

---

## 🧱 1. Présentation du Modèle OSI

Le **modèle OSI** est une normalisation théorique définissant **7 couches** qui structurent la communication entre deux systèmes informatiques. Il permet d'analyser les flux réseau de manière modulaire.

---

## 🔢 2. Les 7 Couches OSI (du bas vers le haut)

| N° | Couche           | Rôle principal                        | Protocoles / Exemples                     |
|----|------------------|----------------------------------------|-------------------------------------------|
| 7  | **Application**  | Interface utilisateur / services       | HTTP, FTP, DNS, SMTP, SSH, SNMP           |
| 6  | **Présentation** | Encodage, chiffrement, compression     | TLS, SSL, JPEG, ASCII, MPEG               |
| 5  | **Session**      | Connexion, synchronisation             | NetBIOS, RPC, PPTP, SMB (sessions)        |
| 4  | **Transport**    | Fiabilité, segmentation                | TCP, UDP, SCTP                            |
| 3  | **Réseau**       | Routage et adressage                   | IP, ICMP, ARP, OSPF, BGP                  |
| 2  | **Liaison**      | Transmission locale, MAC, erreurs      | Ethernet, PPP, VLAN, STP                 |
| 1  | **Physique**     | Signal électrique ou optique brut      | RJ45, Wi-Fi, câble fibre/cuivre          |

---

## 🛠️ 3. Outils & Tests par couche

| Couche     | Outils / Commandes                              |
|------------|--------------------------------------------------|
| 1 – Physique  | Testeur câble, LED switch, `ethtool`, Wi-Fi analyzer |
| 2 – Liaison   | `arp`, `ip link`, `ifconfig`, `tcpdump -e`          |
| 3 – Réseau    | `ping`, `traceroute`, `ip addr`, `netstat -r`       |
| 4 – Transport | `nmap`, `netcat`, `ss -tulpn`, `telnet`             |
| 5 – Session   | Wireshark (sessions TCP), `rpcinfo`, SMB test tools |
| 6 – Présentation | SSL/TLS checkers, `openssl`, `testssl.sh`     |
| 7 – Application | `curl`, `wget`, navigateur, `dig`, `ftp`, `ssh`   |

---

## 🔐 4. Vulnérabilités typiques par couche

| Couche | Exemples de menaces                         |
|--------|---------------------------------------------|
| 1      | Coupure physique, brouillage (Wi-Fi)        |
| 2      | MAC spoofing, ARP spoofing, VLAN hopping    |
| 3      | IP spoofing, ICMP flood, route hijacking    |
| 4      | TCP SYN flood, UDP flood, port scanning     |
| 5      | Hijacking de session, MITM SMB              |
| 6      | TLS downgrade, certificats invalides        |
| 7      | XSS, SQLi, CSRF, injections LDAP/XML        |

---

## 🧩 5. Cas d’usage du modèle OSI en entreprise

- 📶 **Dépannage réseau** : Localiser où une panne se produit (physique ? IP ? DNS ?).
- 🔐 **Architecture de sécurité** : Appliquer les protections à chaque couche.
- 📃 **Documentation** : Structurer les flux réseau dans les dossiers projet.
- 🛑 **Détection d’intrusion** : Identifier le vecteur d’attaque par couche.
- 📡 **Surveillance réseau** : S’assurer de la bonne communication sur chaque couche.

---

## 🔄 6. Comparaison OSI vs TCP/IP

| Couche OSI       | Couche TCP/IP           |
|------------------|-------------------------|
| 7 – Application  | 4 – Application         |
| 6 – Présentation | 4 – Application         |
| 5 – Session      | 4 – Application         |
| 4 – Transport    | 3 – Transport           |
| 3 – Réseau       | 2 – Internet            |
| 2 – Liaison      | 1 – Accès réseau        |
| 1 – Physique     | 1 – Accès réseau        |

> Le modèle TCP/IP est plus pratique, mais le modèle OSI est plus pédagogique et précis.

---

## 📑 7. Mémo OSI mnémotechnique

### 🧠 Du bas vers le haut :
**P**as **L**es **R**outes **T**raversent **S**ouvent **P**aris **A**vec **Hâte**

**P**hysique → **L**iaison → **R**éseau → **T**ransport → **S**ession → **P**résentation → **A**pplication

### 🧠 Du haut vers le bas :
**A**ll **P**eople **Seem** **To** **Need** **Data** **Processing**

---

## 📦 8. Annexes & Références

- 🔗 [RFC 1122 – Requirements for Internet Hosts](https://datatracker.ietf.org/doc/html/rfc1122)
- 📘 [Cisco – OSI Model Explained](https://www.cisco.com/c/en/us/support/docs/osi-model.html)
- 🧾 [ANSSI – Sécurité réseau](https://www.ssi.gouv.fr/)
- 🛠️ [Wireshark Protocol Hierarchy](https://www.wireshark.org)

