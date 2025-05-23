# 📌 Guide de Configuration du Pare-feu pour une Entreprise

## 🛡️ Objectif
Ce document vise à définir les règles et bonnes pratiques de configuration d’un pare-feu afin de sécuriser le réseau d’une entreprise contre les menaces internes et externes.

---

## 🔧 Principes Généraux

- **Principe du moindre privilège** : Bloquer tout le trafic par défaut, puis ouvrir uniquement ce qui est nécessaire.
- **Segmentation réseau** : Créer des VLANs et appliquer des règles spécifiques à chaque zone (DMZ, utilisateurs, serveurs, invités).
- **Journalisation** : Activer les logs sur toutes les règles critiques pour permettre un audit.
- **Mises à jour** : Garder le pare-feu à jour avec les derniers correctifs de sécurité.

---

## 🌐 Règles de Base

| Priorité | Source        | Destination    | Port/Service         | Action | Commentaire |
|----------|---------------|----------------|-----------------------|--------|-------------|
| 1        | LAN           | LAN            | Tous                  | Allow  | Communication interne |
| 2        | LAN           | Internet       | 80 (HTTP), 443 (HTTPS)| Allow  | Accès web sortant |
| 3        | LAN           | Internet       | Autres ports          | Deny   | Bloquer tout autre trafic sortant |
| 4        | Internet      | LAN            | Tous                  | Deny   | Bloquer tout accès entrant |
| 5        | Internet      | DMZ (ex: Web)  | 80, 443               | Allow  | Accès aux services publics |
| 6        | DMZ           | LAN            | Tous                  | Deny   | Empêcher communication inverse |

---

## 🧱 Recommandations Avancées

### 🔐 Accès Administratif

- Autoriser uniquement les IPs internes spécifiques.
- Chiffrer les connexions (ex: SSH avec clé, HTTPS avec certificat).
- Utiliser un VPN pour les connexions distantes.

### 📁 Accès aux Fichiers (ex: NAS, serveurs Windows)

- Restreindre par utilisateur/groupe.
- Filtrer les ports SMB (445, 139) aux seuls VLANs internes.

### 📡 VPN et Accès Distant

- Utiliser IPsec ou OpenVPN avec MFA.
- Bloquer tout autre trafic VPN non autorisé.
- Surveiller les connexions par logs.

---

## 🔍 Monitoring & Audit

- Activer les alertes en cas de connexion suspecte ou de port scan.
- Configurer une solution SIEM pour corréler les logs.
- Réaliser des audits réguliers (tests de pénétration inclus).

---

## 🚨 Règles Spécifiques à Bloquer

- **Blocage des applications P2P (BitTorrent, etc.)**
- **Blocage de Tor et proxies anonymes**
- **Filtrage par catégories (sites adultes, jeux, etc.) via DNS ou proxy**

---

## 🧪 Test & Validation

- Vérifier chaque règle avec des outils comme `nmap`, `telnet`, ou `curl`.
- Simuler des scénarios d’attaque pour tester la robustesse (ex: faille SSH, brute-force RDP).

---

## 📎 Annexes

- 🔗 Liste des ports standards : [IANA Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
- 🔐 Bonnes pratiques de l’ANSSI : https://www.ssi.gouv.fr/

---

## 📅 Maintenance

- **Revue mensuelle** des règles obsolètes ou inutilisées.
- **Revue trimestrielle** de la journalisation.
- **Simulation annuelle** de récupération en cas d’incident.



# 📌 Guide de Configuration du Pare-feu pour une Entreprise

(... contenu précédent inchangé ...)

---

## 🖥️ Commandes de Configuration – Rappels

### 🔷 Sous **Windows** (via PowerShell ou CMD)

> Utilise `netsh advfirewall` ou `Set-NetFirewallRule` via PowerShell

#### 📋 Exemples de commandes :

```powershell
# Activer le pare-feu
netsh advfirewall set allprofiles state on

# Créer une règle pour autoriser le port 443 en entrée
netsh advfirewall firewall add rule name="Allow HTTPS" dir=in action=allow protocol=TCP localport=443

# Bloquer un programme
netsh advfirewall firewall add rule name="Block App" dir=out action=block program="C:\Path\to\App.exe"

# Supprimer une règle
netsh advfirewall firewall delete rule name="Allow HTTPS"

# Voir les règles existantes
netsh advfirewall firewall show rule name=all
🧠 PowerShell (Windows 10+ recommandé) :
powershell

# Lister les règles
Get-NetFirewallRule

# Ajouter une règle personnalisée
New-NetFirewallRule -DisplayName "Allow SSH" -Direction Inbound -LocalPort 22 -Protocol TCP -Action Allow
🐧 Sous Linux (UFW / iptables / firewalld)
🧩 UFW (Uncomplicated Firewall) – Ubuntu/Debian

# Activer UFW
sudo ufw enable

# Autoriser un port (ex: SSH)
sudo ufw allow 22

# Bloquer un port sortant
sudo ufw deny out 25

# Afficher les règles
sudo ufw status numbered

# Supprimer une règle
sudo ufw delete [numéro de la règle]
🔧 iptables – Bas niveau, très flexible

# Voir les règles actuelles
sudo iptables -L -v -n

# Bloquer tout le trafic entrant par défaut
sudo iptables -P INPUT DROP

# Autoriser le trafic sur le port 80
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Sauvegarder les règles (Debian/Ubuntu)
sudo iptables-save > /etc/iptables/rules.v4
🔥 firewalld – Red Hat / CentOS / Fedora

# Démarrer et activer firewalld
sudo systemctl start firewalld
sudo systemctl enable firewalld

# Ajouter une règle permanente pour le port 443
sudo firewall-cmd --permanent --add-port=443/tcp

# Recharger les règles
sudo firewall-cmd --reload

# Liste des services et ports autorisés
sudo firewall-cmd --list-all
🗃️ Bonnes pratiques pour la configuration CLI
Toujours tester les règles avec une session secondaire avant d’appliquer un blocage total.

Sauvegarder la configuration avant modification.

Script de restauration en cas de blocage complet.

Intégrer la configuration dans un outil d’automatisation (Ansible, Puppet, etc.).
