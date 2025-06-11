# 🛡️ Guide Ultra Complet – Wazuh (SIEM / EDR / HIDS)

## 📖 Introduction

**Wazuh** est une plateforme open source de sécurité permettant de centraliser la **détection d’intrusions**, la **surveillance d’intégrité**, l’**analyse de logs** et la **réponse aux incidents**. Elle combine les fonctionnalités d’un **SIEM**, d’un **HIDS** (Host Intrusion Detection System) et d’un **EDR** basique.

---

## 🧱 1. Architecture

### 🧩 Composants principaux

| Composant      | Rôle                                              |
|----------------|---------------------------------------------------|
| **Manager**    | Collecte, analyse, corrèle les données            |
| **Agent**      | Collecte les logs et les envoie au Manager        |
| **Filebeat**   | Envoie les logs vers OpenSearch/ElasticSearch     |
| **OpenSearch** | Moteur d’indexation et de recherche               |
| **Dashboard**  | Interface de visualisation Kibana (ou OpenSearch Dashboards) |

### 🖥️ Schéma de déploiement

[AGENTS] ---> [WAZUH MANAGER] ---> [FILEBEAT] ---> [OPENSEARCH] ---> [DASHBOARD]

yaml


---

## ⚙️ 2. Installation & Déploiement

### 🔧 Pré-requis système

- OS serveur : Ubuntu 20.04+, CentOS 7+, Debian 11+
- CPU : 4 vCPU minimum
- RAM : 8 Go minimum
- Ports : 1514/UDP (logs), 1515/TCP (agent-auth), 55000/TCP (REST API)

### 🚀 Installation automatique (script officiel)

```bash
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh
sudo bash wazuh-install.sh -a
📡 Déploiement d’un agent
Agent Linux

curl -sO https://packages.wazuh.com/4.7/wazuh-agent.sh
sudo bash wazuh-agent.sh -a --manager_ip <IP_MANAGER>
Agent Windows
powershell
Copier
Modifier
msiexec.exe /i wazuh-agent-4.x.x.msi /quiet
# Configurer ossec.conf
C:\Program Files (x86)\ossec-agent\agent-auth.exe -m <IP_MANAGER>
net start wazuh-agent


🧠 3. Configuration
📁 Fichier de configuration
/var/ossec/etc/ossec.conf (manager)

C:\Program Files (x86)\ossec-agent\ossec.conf (agent)

🔍 Exemples de modules activables
xml

<rootcheck>
  <disabled>no</disabled>
</rootcheck>

<syscheck>
  <frequency>3600</frequency>
  <directories check_all="yes">/etc,/bin,/usr/bin</directories>
</syscheck>

<logcollector>
  <localfile>
    <log_format>syslog</log_format>
    <location>/var/log/auth.log</location>
  </localfile>
</logcollector>
📡 Enregistrement manuel d’un agent

/var/ossec/bin/manage_agents
# Ajouter un agent
# Extraire la clé
# L’importer sur le poste client

🔍 4. Analyse de Logs & Détection
📊 Dashboards
OpenSearch Dashboards via https://<IP>:5601 ou https://<IP>:443

Tableaux : attaques SSH, vulnérabilités, utilisateurs, intégrité...

📚 Règles de détection
Fichiers :

/var/ossec/ruleset/rules/

Fichier principal : ossec.conf

Catégories :

Rootkit

Brute force

File Integrity Monitoring (FIM)

CVE (si vulnérabilité détectée)

🔗 5. Intégrations
Outil externe	Type	Description
VirusTotal	Threat Intel	Analyse de hash et URL suspectes
MISP	Threat Intel	Intégration d’IOC (Indicator of Compromise)
TheHive	Orchestration	Enrichissement et création d’incidents
Suricata	IDS/IPS réseau	Corrélation avec alertes Wazuh
Active Directory	Authentification	Surveillance des logs d’authentification

🧪 6. Test & Simulation
📌 Simulation de brute force SSH

for i in {1..10}; do ssh wronguser@localhost; done

📌 Création d’un fichier critique

touch /etc/shadow.bak
Vérifiez ensuite les alertes dans le dashboard ou /var/ossec/logs/alerts/alerts.json

🔐 7. Sécurité & Durcissement
Activer TLS entre agents et manager

Restreindre les accès au dashboard via NGINX/Apache

Configurer alertes par email / webhook

Activer authentification MFA sur les dashboards

Chiffrement des logs au repos (via OpenSearch config)

🧰 8. Commandes Utiles
🔍 Diagnostic et logs

/var/ossec/bin/agent_control -l           # Liste des agents
/var/ossec/bin/ossec-logtest              # Test de règles
tail -f /var/ossec/logs/ossec.log         # Log général
tail -f /var/ossec/logs/alerts/alerts.json # Alertes en temps réel

🔄 Redémarrage des services

systemctl restart wazuh-manager
systemctl restart wazuh-agent
🧼 9. Maintenance & Supervision
📅 Tâches régulières
Fréquence	Tâche
Journalier	Vérifier les alertes critiques
Hebdo	S’assurer que tous les agents sont en ligne
Mensuel	Vérifier les mises à jour Wazuh / OS
Trimestriel	Faire une sauvegarde complète de la config

🧾 Sauvegarde de la config

tar -czvf wazuh-backup.tar.gz /var/ossec
📘 10. Annexes & Références
🔗 Documentation officielle Wazuh

🔗 Playbooks GitHub Wazuh

📎 Liste des règles : /var/ossec/ruleset/rules/

🔐 Configuration TLS : /var/ossec/etc/internal_options.conf

🔄 Intégration SIEM : Graylog, Splunk, ELK

