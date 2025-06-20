# 🔐 Guide Complet – Chiffrement des Connexions Réseau en Entreprise

## 🎯 Objectif

Assurer la **confidentialité**, l'**intégrité** et l'**authenticité** des communications réseau internes et externes, via le **chiffrement** à tous les niveaux du SI (services, accès, tunnels, administration).

---

## 🧠 1. Principes de base

- 🔒 **Chiffrement** : rendre les données illisibles sans clé
- 🧾 **Authentification** : certifier l’identité des participants
- 🔄 **Intégrité** : vérifier que les données n'ont pas été altérées
- ✅ **Conformité** : répondre aux exigences RGPD, ISO 27001, NIS2...

---

## 📡 2. Protocoles à utiliser (et à proscrire)

| Usage                    | Recommandé                       | À proscrire                      |
|--------------------------|----------------------------------|----------------------------------|
| Site Web                 | **HTTPS (TLS 1.2/1.3)**          | HTTP, TLS 1.0/1.1                |
| Accès distant            | **SSH, OpenVPN, WireGuard**      | Telnet, PPTP                     |
| Fichiers/Partages        | **SMB v3 (avec encryption)**     | FTP, SMB v1                      |
| Administration système   | **SSH, RDP via VPN ou TLS**      | Rlogin, VNC en clair             |
| Mails                    | **SMTP/TLS, IMAPS, POP3S**       | SMTP/25, POP3/110                |
| Réplication DB / API     | **TLS 1.2/1.3**                  | Connexions TCP non chiffrées     |

---

## 🛠️ 3. Mise en œuvre TLS/SSL

### 🔐 Génération de certificats auto-signés


# Autorité racine (Root CA)
openssl genrsa -out rootCA.key 4096
openssl req -x509 -new -key rootCA.key -sha256 -days 3650 -out rootCA.crt

# Certificat serveur
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr
openssl x509 -req -in server.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out server.crt -days 365 -sha256
💡 Utiliser Let's Encrypt en production pour les services web publics (via certbot)

🕸️ Serveur Web (Nginx – HTTPS)
nginx

server {
  listen 443 ssl;
  server_name secure.example.com;

  ssl_certificate /etc/ssl/certs/server.crt;
  ssl_certificate_key /etc/ssl/private/server.key;

  ssl_protocols TLSv1.2 TLSv1.3;
  ssl_ciphers 'HIGH:!aNULL:!MD5';

  location / {
    proxy_pass http://localhost:8080;
  }
}
🌐 4. VPN Chiffrés
🔐 IPsec (Strongswan)
Chiffrement natif au niveau IP

Compatible avec pare-feux, routeurs

Authentification par certificats ou PSK


apt install strongswan
# Configuration dans /etc/ipsec.conf et /etc/ipsec.secrets
⚡ WireGuard (recommandé, moderne)

# Installation
apt install wireguard
wg genkey | tee privatekey | wg pubkey > publickey
Ports : UDP/51820

Ultra rapide, simple à configurer

Chiffrement via ChaCha20-Poly1305

🌍 OpenVPN

apt install openvpn easy-rsa
make-cadir /etc/openvpn/easy-rsa
# Génération des clés + fichiers .ovpn
🧑‍💻 5. Accès et services sécurisés
🔐 SSH
Clés RSA/ECDSA/ED25519 obligatoires

Interdire root, password :


PermitRootLogin no
PasswordAuthentication no
🖥️ RDP
Utiliser via VPN ou TLS interne

Activer NLA (Network Level Authentication)

🗂️ SMB
Utiliser SMB v3 avec chiffrement :

powershell

Set-SmbServerConfiguration -EncryptData $true
🔍 6. Tests et vérifications
🔧 Tester un port sécurisé (OpenSSL)

openssl s_client -connect example.com:443
🧪 Scanner la sécurité SSL/TLS
SSL Labs

Outils CLI :


nmap --script ssl-enum-ciphers -p 443 example.com
🔐 Vérifier la validité d’un certificat

openssl x509 -in server.crt -text -noout
📦 7. Bonnes pratiques
🔄 Renouveler les certificats tous les 6–12 mois

🔁 Automatiser les renouvellements (Certbot + cron)

🛡️ Utiliser des algorithmes modernes (TLS 1.3, SHA256+)

📋 Gérer une PKI interne si besoins internes massifs

🔍 Auditer les ports ouverts et services régulièrement

🔧 8. Commandes utiles
Action	Commande
Générer un certificat auto-signé	openssl req -x509 ...
Inspecter une connexion SSL	openssl s_client -connect host:port
Lister les protocoles/ports	nmap -sV -p- host
Scanner SSL	sslyze, testssl.sh, nmap --script ssl-*
Tester le VPN	ping, traceroute, wg show, ipsec status

🧾 9. Annexes & Références
🔐 Mozilla SSL Configuration Generator

🌍 SSL Labs - Test public

📖 OpenSSL Cookbook

📦 WireGuard Docs

📘 ANSSI – Guide VPN sécurisé
