# 🔐 Guide Complet – Sécurisation de SSH

## 🎯 Objectif

Protéger l’accès distant aux systèmes Linux via SSH en appliquant des **règles de durcissement**, en limitant les vecteurs d’attaque (brute force, MITM) et en renforçant l’authentification et le chiffrement.

---

## 🧠 1. Fonctionnement de SSH

SSH (Secure Shell) permet une **connexion distante chiffrée** entre deux hôtes, utilisée pour :

- Accès à un shell distant
- Transfert de fichiers sécurisé (SCP, SFTP)
- Tunneling chiffré de services

---

## 📁 2. Fichier de configuration principal

/etc/ssh/sshd_config

yaml


---

## 🔧 3. Configuration sécurisée (`sshd_config`)

```bash
# Désactiver root direct
PermitRootLogin no

# N’autoriser que les clés publiques
PasswordAuthentication no

# Protocole 2 uniquement
Protocol 2

# Limiter les utilisateurs
AllowUsers admin1 admin2

# Réduire les essais
MaxAuthTries 3
LoginGraceTime 30

# Activer le journal SSH
LogLevel VERBOSE

# Port alternatif (optionnel)
Port 2222
➡️ Redémarrer SSH après modification :


systemctl restart sshd
🔑 4. Authentification par clé SSH
🔐 Génération de clé (poste client)

ssh-keygen -t ed25519 -C "admin@exemple"
Utilisez ed25519 ou rsa -b 4096

📥 Déploiement de la clé publique sur le serveur


ssh-copy-id -p 22 admin@serveur
Ou manuellement :

bash

cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
🛡️ 5. Protection contre les attaques
🚫 Désactiver root en SSH
text

PermitRootLogin no
🧱 Fail2Ban (bloquer brute-force)

apt install fail2ban
Configurer :

ini

/etc/fail2ban/jail.local
[sshd]
enabled = true
port = ssh
maxretry = 3
🌐 Limiter par adresse IP (firewall)

ufw allow from 192.168.1.0/24 to any port 22
🔐 6. Chiffrement et algorithmes
Renforcer les algorithmes dans sshd_config :

Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com
KexAlgorithms curve25519-sha256
MACs hmac-sha2-512-etm@openssh.com
📋 7. Journalisation & audit
🔍 Logs SSH

journalctl -u ssh
tail -f /var/log/auth.log
🔎 Tentatives de connexion

grep "Failed password" /var/log/auth.log
🔧 8. Autres mesures de sécurité
Action	Commande / Description
🔁 Changer port SSH	Port 2222 dans sshd_config
🔒 Autoriser uniquement certains utilisateurs	AllowUsers ou AllowGroups
🛑 Interdire forwarding	AllowTcpForwarding no
🧩 Restreindre avec Match	Match User ou Match Address blocs
⏳ Timeout d’inactivité	ClientAliveInterval 300 + ClientAliveCountMax 0

📋 9. Checklist de sécurité SSH
Tâche	Statut
🔒 Authentification par clé uniquement	✅ / ❌
❌ Root login désactivé	✅ / ❌
🔁 Port changé	✅ / ❌
🔐 Chiffrement fort configuré	✅ / ❌
🧱 Fail2Ban actif	✅ / ❌
📊 Logs surveillés	✅ / ❌
🌍 Accès limité aux IP connues	✅ / ❌

🧾 10. Tests utiles
Test	Commande
🔐 Tester une clé	ssh -i ~/.ssh/id_ed25519 user@host
🔎 Analyse du port SSH	nmap -sV -p22 server
🧪 Vérifier les logs	tail -f /var/log/auth.log
⛔ Tester brute-force	(Kali, Hydra – à des fins de test seulement)

📚 11. Références utiles
📖 OpenSSH Man Pages

🔐 Mozilla SSH Guidelines

🧰 Fail2Ban GitHub

🧾 Hardening Linux SSH (CIS)
