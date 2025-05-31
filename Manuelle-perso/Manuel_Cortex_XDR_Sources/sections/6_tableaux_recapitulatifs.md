# 6. Tableaux récapitulatifs

## 6.1. Types d'alertes et leur signification

Cortex XDR génère différents types d'alertes pour signaler les menaces potentielles. Comprendre ces alertes est essentiel pour une réponse efficace aux incidents de sécurité.

### Classification des alertes par catégorie

| Catégorie d'alerte | Description | Niveau de risque typique | Réponse recommandée |
|-------------------|-------------|-------------------------|---------------------|
| **Malware** | Détection de logiciels malveillants connus ou suspects | Élevé à Critique | Isolation immédiate, analyse des artefacts, suppression du malware |
| **Exploit** | Tentative d'exploitation de vulnérabilités | Élevé à Critique | Isolation, analyse de la vulnérabilité, application de correctifs |
| **Comportement suspect** | Activités anormales pouvant indiquer une compromission | Moyen à Élevé | Investigation approfondie, surveillance accrue |
| **Mouvement latéral** | Tentatives de propagation au sein du réseau | Élevé à Critique | Isolation, blocage des communications, analyse de l'étendue |
| **Élévation de privilèges** | Tentatives d'obtention de droits supérieurs | Élevé | Vérification des comptes, révocation des accès compromis |
| **Exfiltration de données** | Transferts de données suspects vers l'extérieur | Élevé à Critique | Blocage des communications, analyse des données concernées |
| **Reconnaissance** | Activités de découverte et cartographie du réseau | Moyen | Surveillance accrue, vérification des contrôles d'accès |
| **Persistance** | Mécanismes mis en place pour maintenir l'accès | Élevé | Suppression des mécanismes de persistance, analyse complète du système |
| **Command & Control** | Communications avec des serveurs de contrôle | Élevé à Critique | Blocage des communications, isolation, analyse forensique |
| **Défense Evasion** | Tentatives de contournement des mécanismes de sécurité | Élevé | Renforcement des contrôles, analyse approfondie |

### Niveaux de sévérité des alertes

| Niveau de sévérité | Description | Temps de réponse recommandé | Exemple |
|-------------------|-------------|----------------------------|---------|
| **Critique** | Menace active avec impact potentiel immédiat et sévère | Immédiat (< 30 minutes) | Ransomware en cours d'exécution, exfiltration active de données sensibles |
| **Élevé** | Menace significative nécessitant une attention rapide | < 2 heures | Malware détecté mais contenu, tentative d'exploitation bloquée |
| **Moyen** | Menace potentielle nécessitant une investigation | < 8 heures | Comportement inhabituel, connexions à des domaines suspects |
| **Faible** | Anomalie mineure ou information contextuelle | < 24 heures | Tentative d'accès échouée, modification de configuration mineure |
| **Informatif** | Information de contexte sans menace immédiate | Aucune action immédiate requise | Mise à jour système, changement de politique |

### Indicateurs associés aux alertes

| Type d'indicateur | Description | Exemple |
|------------------|-------------|---------|
| **Hachage de fichier** | Empreinte numérique unique d'un fichier | MD5: d41d8cd98f00b204e9800998ecf8427e |
| **URL/Domaine** | Adresses web malveillantes ou suspectes | malware-distribution.example.com |
| **Adresse IP** | Adresses IP associées à des activités malveillantes | 192.0.2.1 |
| **Artefact système** | Modifications système associées à l'alerte | Clé de registre: HKLM\SOFTWARE\Malware |
| **Signature comportementale** | Modèle d'activité identifié comme malveillant | Séquence d'appels API caractéristique d'une injection de processus |
| **Technique MITRE ATT&CK** | Technique d'attaque identifiée selon le framework MITRE | T1055: Process Injection |

## 6.2. Sources de données supportées

Cortex XDR intègre et analyse des données provenant de multiples sources pour offrir une visibilité complète sur l'environnement informatique.

### Sources de données par catégorie

| Catégorie | Source de données | Type d'information collectée | Valeur pour la détection |
|-----------|-------------------|------------------------------|-------------------------|
| **Endpoint** | Agents Cortex XDR | Processus, fichiers, registre, connexions réseau, logs système | Élevée - Visibilité détaillée sur les activités des endpoints |
| **Réseau** | Pare-feux Palo Alto Networks | Trafic réseau, applications, URL, menaces | Élevée - Détection des menaces au niveau réseau |
| **Réseau** | Logs VPC Cloud | Flux réseau dans les environnements cloud | Moyenne - Visibilité sur les communications cloud |
| **Réseau** | Logs DNS | Requêtes et réponses DNS | Moyenne - Détection de communications C2 et exfiltration |
| **Cloud** | AWS CloudTrail | Activités API et actions utilisateurs | Élevée - Détection des compromissions de comptes cloud |
| **Cloud** | Azure Activity Logs | Actions administratives et alertes | Élevée - Visibilité sur les activités Azure |
| **Cloud** | Google Cloud Audit Logs | Activités administratives et accès aux données | Élevée - Traçabilité des actions dans GCP |
| **SaaS** | Microsoft 365 | Activités utilisateurs, emails, partages de fichiers | Élevée - Détection des compromissions de comptes |
| **SaaS** | Google Workspace | Connexions, accès aux documents, paramètres | Moyenne - Visibilité sur les activités collaboratives |
| **Identité** | Active Directory | Authentifications, modifications de groupes | Élevée - Détection des mouvements latéraux |
| **Identité** | LDAP | Requêtes d'authentification et de recherche | Moyenne - Visibilité sur les accès aux ressources |
| **Applications** | Logs d'applications web | Requêtes HTTP, authentifications, erreurs | Moyenne - Détection des attaques web |
| **Sécurité** | Logs d'autres solutions de sécurité | Alertes, événements de sécurité | Moyenne - Corrélation avec d'autres détections |

### Formats de données supportés

| Format | Description | Sources typiques | Méthode d'ingestion |
|--------|-------------|-----------------|---------------------|
| **Syslog** | Format standard pour les logs système | Appareils réseau, serveurs Linux | Collecteur Syslog, intégration directe |
| **CEF** | Common Event Format | Solutions de sécurité diverses | Intégration directe, API |
| **JSON** | Format de données structuré | APIs cloud, applications modernes | API REST, intégration directe |
| **CSV** | Valeurs séparées par des virgules | Exports de données, rapports | Import manuel, scripts personnalisés |
| **Windows Event Logs** | Logs d'événements Windows | Serveurs et postes Windows | Agent Cortex XDR |
| **Logs bruts** | Texte non structuré | Applications legacy, scripts | Parsers personnalisés |

### Méthodes de collecte des données

| Méthode | Description | Avantages | Limitations |
|---------|-------------|-----------|------------|
| **Agent Cortex XDR** | Logiciel installé sur les endpoints | Données détaillées, fonctionnalités de réponse | Nécessite installation sur chaque endpoint |
| **Intégration cloud native** | Connexion directe aux APIs cloud | Déploiement simple, couverture complète | Limité aux services cloud supportés |
| **Forwarding depuis SIEM** | Transfert de logs depuis un SIEM existant | Réutilise l'infrastructure existante | Latence potentielle, dépendance au SIEM |
| **API REST** | Collecte via l'API Cortex XDR | Flexibilité, intégration personnalisée | Nécessite développement ou scripts |
| **Syslog direct** | Envoi de logs au format syslog | Simple, standard ouvert | Format potentiellement limité |
| **Collecteurs dédiés** | Appliances ou logiciels de collecte | Agrégation et filtrage préliminaire | Coût et complexité supplémentaires |

## 6.3. Intégrations disponibles

Cortex XDR s'intègre avec un large éventail de solutions pour étendre ses capacités et s'adapter à l'écosystème de sécurité existant.

### Intégrations par catégorie

| Catégorie | Produit/Service | Type d'intégration | Fonctionnalités |
|-----------|----------------|-------------------|----------------|
| **SIEM/SOAR** | Splunk | Bidirectionnelle | Envoi d'alertes, requêtes de données, actions de réponse |
| **SIEM/SOAR** | IBM QRadar | Bidirectionnelle | Envoi d'alertes, enrichissement d'incidents |
| **SIEM/SOAR** | Microsoft Sentinel | Bidirectionnelle | Synchronisation d'incidents, playbooks automatisés |
| **SIEM/SOAR** | Cortex XSOAR | Native | Orchestration complète, playbooks prédéfinis |
| **SIEM/SOAR** | ServiceNow SecOps | Bidirectionnelle | Création de tickets, suivi des incidents |
| **Threat Intelligence** | Palo Alto Networks AutoFocus | Native | Enrichissement des IOCs, contexte des menaces |
| **Threat Intelligence** | VirusTotal | Unidirectionnelle | Vérification des hachages de fichiers |
| **Threat Intelligence** | MISP | Bidirectionnelle | Partage d'IOCs, import/export d'indicateurs |
| **Cloud Security** | Prisma Cloud | Native | Visibilité unifiée cloud/endpoint, corrélation des menaces |
| **Cloud Security** | AWS Security Hub | Bidirectionnelle | Centralisation des alertes, actions de remédiation |
| **Cloud Security** | Microsoft Defender for Cloud | Bidirectionnelle | Échange d'alertes, enrichissement contextuel |
| **Identity** | Okta | Bidirectionnelle | Corrélation des événements d'authentification, actions sur les comptes |
| **Identity** | Azure AD | Bidirectionnelle | Surveillance des identités, actions sur les comptes |
| **Identity** | Ping Identity | Unidirectionnelle | Import des événements d'authentification |
| **Endpoint Management** | Microsoft Intune | Bidirectionnelle | Déploiement d'agents, actions de remédiation |
| **Endpoint Management** | Jamf | Bidirectionnelle | Gestion des endpoints macOS, déploiement d'agents |
| **Endpoint Management** | VMware Workspace ONE | Bidirectionnelle | Déploiement et gestion des agents mobiles |
| **Network Security** | Palo Alto Networks Firewalls | Native | Corrélation des menaces réseau et endpoint |
| **Network Security** | Cisco ISE | Bidirectionnelle | Actions de contrôle d'accès réseau |
| **Vulnerability Management** | Tenable | Unidirectionnelle | Corrélation des vulnérabilités et menaces |
| **Vulnerability Management** | Qualys | Unidirectionnelle | Import des données de vulnérabilité |
| **Email Security** | Proofpoint | Bidirectionnelle | Corrélation des menaces email et endpoint |
| **Email Security** | Microsoft Defender for Office 365 | Bidirectionnelle | Visibilité sur les menaces email |

### Intégrations Office 365

| Composant Office 365 | Données collectées | Cas d'usage |
|---------------------|-------------------|------------|
| **Exchange Online** | Logs de messagerie, pièces jointes | Détection de phishing, malware par email |
| **SharePoint Online** | Accès aux documents, partages | Détection d'exfiltration de données |
| **OneDrive for Business** | Activités de fichiers, partages externes | Surveillance des fuites de données |
| **Teams** | Messages, fichiers partagés | Détection de partage de contenu malveillant |
| **Azure AD** | Connexions, modifications de comptes | Détection de compromission de comptes |
| **Office Apps** | Activités dans les applications | Détection de macros malveillantes |

### Intégrations AWS

| Service AWS | Données collectées | Cas d'usage |
|------------|-------------------|------------|
| **CloudTrail** | API calls, actions administratives | Détection d'activités suspectes, erreurs de configuration |
| **VPC Flow Logs** | Flux réseau entre instances | Détection de communications suspectes |
| **GuardDuty** | Alertes de sécurité AWS | Corrélation avec les menaces endpoint |
| **S3** | Accès aux buckets, modifications | Détection d'exfiltration de données |
| **Lambda** | Exécutions de fonctions | Détection d'activités anormales |
| **EC2** | Activités des instances | Protection des workloads cloud |
| **IAM** | Modifications de permissions | Détection d'élévation de privilèges |

## 6.4. Comparaison des fonctionnalités par licence

Cortex XDR propose différents niveaux de licence pour s'adapter aux besoins variés des organisations.

### Niveaux de licence

| Fonctionnalité | Cortex XDR Prevent | Cortex XDR Pro | Cortex XDR Enterprise |
|---------------|-------------------|---------------|---------------------|
| **Protection contre les malwares** | ✓ | ✓ | ✓ |
| **Protection contre les exploits** | ✓ | ✓ | ✓ |
| **Contrôle des périphériques** | ✓ | ✓ | ✓ |
| **Contrôle des applications** | ✓ | ✓ | ✓ |
| **Pare-feu local** | ✓ | ✓ | ✓ |
| **Analyse comportementale locale** | ✓ | ✓ | ✓ |
| **Détection basée sur les IOCs** | ✓ | ✓ | ✓ |
| **Analyse comportementale avancée** | - | ✓ | ✓ |
| **Corrélation multi-source** | - | ✓ | ✓ |
| **Détection d'anomalies par ML** | - | ✓ | ✓ |
| **Analyse de la chaîne d'attaque** | - | ✓ | ✓ |
| **Requêtes XQL** | Limitées | ✓ | ✓ |
| **Intégration des logs réseau** | - | ✓ | ✓ |
| **Intégration des logs cloud** | - | ✓ | ✓ |
| **Intégration des logs SaaS** | - | - | ✓ |
| **Analytics UEBA** | - | - | ✓ |
| **Détection d'identité (ITDR)** | - | - | ✓ |
| **Réponse automatisée** | Basique | Avancée | Complète |
| **Isolation d'endpoint** | ✓ | ✓ | ✓ |
| **Remédiation à distance** | Limitée | ✓ | ✓ |
| **Playbooks automatisés** | - | Limités | ✓ |
| **Intégration SOAR native** | - | - | ✓ |
| **Période de rétention des données** | 30 jours | 90 jours | 365 jours |
| **Support des API** | Limité | Standard | Complet |

### Fonctionnalités de protection par système d'exploitation

| Fonctionnalité | Windows | macOS | Linux | Android | iOS |
|---------------|---------|-------|-------|---------|-----|
| **Protection contre les malwares** | ✓ | ✓ | ✓ | ✓ | Limitée |
| **Protection contre les exploits** | ✓ | ✓ | ✓ | - | - |
| **Contrôle des périphériques** | ✓ | ✓ | Limitée | - | - |
| **Contrôle des applications** | ✓ | ✓ | ✓ | ✓ | - |
| **Pare-feu local** | ✓ | ✓ | Limitée | - | - |
| **Analyse comportementale** | ✓ | ✓ | ✓ | Limitée | - |
| **Isolation réseau** | ✓ | ✓ | ✓ | - | - |
| **Remédiation à distance** | ✓ | ✓ | ✓ | Limitée | - |
| **Collecte de preuves** | ✓ | ✓ | ✓ | Limitée | Limitée |
| **Protection des données** | ✓ | ✓ | Limitée | - | - |
| **Détection de jailbreak/root** | - | - | - | ✓ | ✓ |

### Capacités d'intégration par licence

| Intégration | Cortex XDR Prevent | Cortex XDR Pro | Cortex XDR Enterprise |
|------------|-------------------|---------------|---------------------|
| **Palo Alto Networks Firewalls** | Limitée | ✓ | ✓ |
| **Prisma Cloud** | - | ✓ | ✓ |
| **AWS/Azure/GCP** | - | ✓ | ✓ |
| **Microsoft 365** | - | - | ✓ |
| **SIEM (Splunk, QRadar, etc.)** | Exportation uniquement | Bidirectionnelle | Bidirectionnelle avancée |
| **SOAR** | - | Limitée | Complète |
| **Threat Intelligence** | Basique | Avancée | Premium |
| **Active Directory/LDAP** | - | Limitée | Complète |
| **Systèmes de tickets** | - | ✓ | ✓ |
| **Solutions MDM** | Limitée | ✓ | ✓ |
