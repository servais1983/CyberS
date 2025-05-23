

markdown

# 🚨 Guide Complet – IDR (Incident Detection & Response) en Entreprise

## 🎯 Objectif

Ce document a pour but de définir les étapes, outils, bonnes pratiques et commandes pour détecter, analyser et répondre efficacement aux incidents de sécurité dans un réseau d'entreprise.

---

## 🧠 1. Principes de base

- **Visibilité complète** sur les postes clients, serveurs et équipements réseau.
- **Collecte centralisée** des logs, alertes, anomalies comportementales.
- **Réponse rapide** automatisée ou semi-automatisée.
- **Plan de reprise et documentation claire.**

---

## 🛠️ 2. Déploiement d'une Solution IDR

### 🗺️ Architecture typique

- Serveur IDR central (on-prem ou cloud)
- Agents légers déployés sur tous les endpoints
- Intégration SIEM pour corrélation avancée
- Backup des logs et alertes

### 🧩 Exemples de solutions IDR

| Solution         | Type       | Commentaire                                  |
|------------------|------------|----------------------------------------------|
| Wazuh            | Open Source| Puissant et personnalisable                  |
| CrowdStrike      | SaaS       | Détection comportementale et EDR complet     |
| SentinelOne      | SaaS       | Réponse automatique intégrée                 |
| Microsoft Defender| Intégré   | Très adapté aux environnements Windows       |

---

### ⚙️ Étapes de déploiement

1. **Choisir la solution adaptée (selon budget, environnement)**
2. **Installer le serveur IDR** (ou souscrire au service cloud)
3. **Déployer les agents sur tous les postes**
4. **Ouvrir les ports nécessaires** (ex: TCP 1514, HTTPS)
5. **Configurer les alertes, règles, détections**
6. **Connecter à un SIEM ou SOC**
7. **Documenter le plan de réponse**

---

### 📦 Exemple – Déploiement de Wazuh

#### Serveur Wazuh (Linux)

```bash
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh
bash wazuh-install.sh -a
Accès : https://[IP]:5601 (via Kibana)

Agent Wazuh – Windows
powershell

msiexec.exe /i wazuh-agent-4.x.x.msi /quiet
# Configurer ossec.conf, puis
agent-auth.exe -m [IP_SERVEUR]
net start wazuh-agent
Agent Wazuh – Linux

curl -sO https://packages.wazuh.com/4.7/wazuh-agent.sh
sudo bash wazuh-agent.sh -a --manager_ip [IP_SERVEUR]
🔍 3. Surveillance et Détection
🔒 Composants essentiels à surveiller
Fichiers système (intégrité, changements non autorisés)

Activité réseau (exfiltration, scan, beaconing)

Processus suspects (scripts, LOLBins)

Comportement utilisateur (login inhabituels, escalade)

🧠 Outils de détection
Catégorie	Outils recommandés
Analyse mémoire	Volatility, Rekall
Réseau	Zeek, Wireshark, Suricata
Disque/Forensic	Autopsy, FTK Imager, Sleuth Kit
EDR	SentinelOne, Wazuh, CrowdStrike
SIEM	Graylog, ELK, Splunk, LogPoint

💻 4. Commandes Utiles – Détection & Analyse
🪟 Windows
powershell

netstat -ano                    # Connexions réseau
tasklist /v                    # Processus détaillés
query user                     # Utilisateurs connectés
schtasks /query /fo LIST /v    # Tâches planifiées
Get-EventLog -LogName Security -Newest 100
🐧 Linux
bash

ss -tunap                      # Connexions réseau
ps aux --sort=-%cpu           # Processus actifs
who / w                       # Utilisateurs connectés
last -a                       # Historique de login
journalctl -xe                # Logs système
⚔️ 5. Réponse à l’incident
📑 Étapes
Isoler le poste du réseau immédiatement

Capturer l’état système (disque, RAM)

Changer les identifiants compromis

Analyser les logs et comportements suspects

Bloquer les IOC (IP, fichiers, hash, domaine)

Noter les horodatages précis

Documenter et alerter le RSSI / DSI

🧰 Commandes de réponse rapide
Windows
powershell

taskkill /PID 1234 /F
net user utilisateur /active:no
wevtutil epl Security C:\incident\logs.evtx
Linux

kill -9 [PID]
usermod -L utilisateur
tar -czvf logs.tar.gz /var/log
📝 6. Post-Incident & Amélioration
Rapport détaillé (chronologie, vecteurs, impact)

Amélioration des règles SIEM / EDR

Patching des failles utilisées

Retour d’expérience avec les équipes IT

Mise à jour du plan de réponse à incident (PRI)

📅 7. Check-lists IDR
✅ Hebdomadaire
 Vérifier que les agents IDR sont actifs

 Analyser les alertes critiques

 Vérifier les mises à jour des règles

✅ Mensuel
 Audit des connexions RDP/SSH

 Analyse des logs centralisés

 Simulation de tentative d’intrusion (Red Team/Blue Team)

✅ Annuel
 Simulation complète de crise (tabletop)

 Test de restauration et reconfiguration

 Revue complète du plan de réponse à incident

📎 Annexes
🔗 MITRE ATT&CK Framework

🔗 Volatility – Analyse mémoire

🔗 ANSSI – Guide Réponse à Incident
