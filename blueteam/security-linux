# 🛡️ Guide Complet – Sécurisation des Systèmes Linux

## 🎯 Objectif

Mettre en œuvre des **mesures de sécurité techniques, préventives et correctives** sur les systèmes Linux (serveurs, postes, conteneurs) pour limiter les attaques, réduire les privilèges et assurer une supervision continue.

---

## 🧱 1. Fondamentaux

| Action                         | Objectif                                     |
|-------------------------------|-----------------------------------------------|
| 🔒 Système à jour              | Éviter les failles connues                   |
| 🧑‍💻 Comptes limités            | Principe du moindre privilège               |
| 🛑 Moins de services actifs    | Réduction de la surface d’attaque           |
| 🕵️ Audit des connexions       | Détection d’anomalies                       |

---

## ⚙️ 2. Mise à jour et durcissement de base

### 🔧 Mise à jour régulière

```bash
# Debian/Ubuntu
apt update && apt upgrade -y

# RHEL/CentOS/Fedora
dnf update -y
🔐 Désactiver les services inutiles

systemctl list-unit-files --type=service
systemctl disable bluetooth.service
systemctl stop bluetooth.service
🧼 Nettoyage des packages obsolètes

apt autoremove -y
dnf autoremove -y
🛡️ 3. Sécurisation de SSH
📋 Paramètres à appliquer (/etc/ssh/sshd_config)
text

PermitRootLogin no
PasswordAuthentication no
Protocol 2
AllowUsers monadmin
MaxAuthTries 3
LogLevel VERBOSE
✅ Redémarrer le service SSH

systemctl restart sshd
🔐 Utiliser des clés SSH + Fail2Ban

sudo apt install fail2ban
👤 4. Gestion des utilisateurs & droits
🔒 Compte avec sudo

usermod -aG sudo monuser
🚫 Verrouiller le compte root (si nécessaire)

passwd -l root
🕵️ Suivi des connexions

last -a     # Historique des connexions
who         # Utilisateurs connectés
🔥 5. Sécurisation du réseau
🌐 Firewall – UFW (Debian/Ubuntu)

ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw enable
🧱 Firewall – Firewalld (RHEL/CentOS/Fedora)

systemctl enable firewalld --now
firewall-cmd --permanent --add-service=ssh
firewall-cmd --reload
🧠 6. Surveillance et audit
🪵 Journaux système

journalctl -xe
tail -f /var/log/auth.log
📋 Auditd – audit de fichiers et commandes

apt install auditd
auditctl -w /etc/passwd -p wa
🛡️ Outils IDS/IPS
Outil	Usage
Fail2Ban	Bloque les IP après échecs
AIDE	Vérifie l'intégrité des fichiers
OSSEC/Wazuh	SIEM/EDR
rkhunter / chkrootkit	Détection rootkits

🧪 7. Hardening Kernel & sécurité
🧷 Paramètres sysctl

cat >> /etc/sysctl.conf <<EOF
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.all.accept_source_route = 0
kernel.randomize_va_space = 2
EOF

sysctl -p
🔒 AppArmor (Ubuntu) / SELinux (RHEL)
AppArmor


aa-status
SELinux


getenforce
setenforce 1
🧰 8. Outils recommandés
Outil	Fonction
ClamAV	Antivirus
Lynis	Audit de sécurité
Logwatch	Rapport quotidien des logs système
Tripwire	Intégrité fichiers systèmes
Gufw	Interface graphique pour UFW (Ubuntu)

🧾 9. Checklist de sécurité Linux
Tâche	Statut
🔒 Mots de passe forts	✅ / ❌
🛑 Root désactivé ou restreint	✅ / ❌
🧑‍💻 Comptes utilisateurs à jour	✅ / ❌
📦 Système à jour	✅ / ❌
🔥 Pare-feu actif	✅ / ❌
🛡️ SSH durci	✅ / ❌
🧪 IDS ou auditd actif	✅ / ❌
🧩 AIDE ou Tripwire pour l'intégrité	✅ / ❌
🔐 SELinux/AppArmor actif	✅ / ❌

📚 10. Références & ressources
📖 CIS Linux Benchmark

🔗 Debian Hardening Guide

📘 Lynis – Hardening tool

🔐 NSA Linux Hardening

🔍 MITRE ATT&CK – Linux Techniques

yaml

