# 4. Configuration de Cortex XDR

## 4.1. Configuration initiale

Après l'installation réussie de la console Cortex XDR et le déploiement des agents, la configuration initiale est une étape cruciale pour optimiser la protection et adapter la solution à votre environnement spécifique.

### Accès à la configuration

Pour accéder aux paramètres de configuration :

1. Connectez-vous à la console Cortex XDR à l'adresse https://cortex.paloaltonetworks.com
2. Utilisez les identifiants administrateur créés lors de l'activation
3. Naviguez vers la section "Administration" dans le menu principal
4. Sélectionnez "Paramètres" pour accéder aux options de configuration globale

### Configuration des paramètres généraux

La configuration des paramètres généraux permet de personnaliser l'environnement Cortex XDR selon vos besoins organisationnels :

1. **Informations du tenant**
   - Définissez le nom de votre organisation
   - Configurez les coordonnées de l'administrateur principal
   - Spécifiez le fuseau horaire et les formats de date/heure

2. **Paramètres de notification**
   - Configurez les adresses email pour les notifications système
   - Définissez les seuils d'alerte pour les notifications
   - Configurez les canaux de notification alternatifs (webhooks, intégrations SIEM)

3. **Paramètres de rétention des données**
   - Définissez la durée de conservation des données d'événements
   - Configurez la rétention des données d'alerte et d'incident
   - Paramétrez les politiques d'archivage automatique

4. **Paramètres d'audit**
   - Activez la journalisation complète des actions administratives
   - Configurez la durée de conservation des journaux d'audit
   - Définissez les événements d'audit à capturer

### Configuration des groupes d'endpoints

L'organisation des endpoints en groupes logiques facilite la gestion et l'application des politiques de sécurité :

1. **Création de groupes d'endpoints**
   - Naviguez vers "Endpoints" > "Groupes"
   - Cliquez sur "Ajouter un groupe"
   - Donnez un nom descriptif au groupe
   - Définissez les critères d'appartenance au groupe

2. **Types de groupes disponibles**
   - **Groupes statiques** : Endpoints assignés manuellement
   - **Groupes dynamiques** : Endpoints assignés automatiquement selon des critères
   - **Groupes hiérarchiques** : Structure de groupes parent-enfant

3. **Critères pour les groupes dynamiques**
   - Système d'exploitation et version
   - Nom d'hôte ou modèle de nom
   - Adresse IP ou plage d'adresses
   - Unité organisationnelle Active Directory
   - Tags personnalisés

4. **Hiérarchie de groupes recommandée**

| Niveau | Exemple de groupe | Critère de regroupement |
|--------|-------------------|-------------------------|
| 1 | Par région | Amérique du Nord, Europe, Asie |
| 2 | Par fonction | Serveurs, Postes de travail, Appareils mobiles |
| 3 | Par département | Finance, RH, IT, R&D |
| 4 | Par criticité | Critique, Standard, Test |

### Configuration des utilisateurs et des rôles

La gestion des accès utilisateurs est essentielle pour maintenir la sécurité de votre environnement Cortex XDR :

1. **Création de rôles personnalisés**
   - Naviguez vers "Administration" > "Rôles"
   - Cliquez sur "Ajouter un rôle"
   - Définissez un nom et une description pour le rôle
   - Configurez les permissions spécifiques

2. **Permissions configurables**
   - Accès en lecture/écriture aux différentes sections
   - Capacité à exécuter des actions de réponse
   - Droits de configuration des politiques
   - Accès aux données sensibles

3. **Création d'utilisateurs**
   - Naviguez vers "Administration" > "Utilisateurs"
   - Cliquez sur "Ajouter un utilisateur"
   - Remplissez les informations requises
   - Assignez le(s) rôle(s) approprié(s)

4. **Intégration avec les fournisseurs d'identité**
   - Configuration de l'authentification unique (SSO)
   - Intégration avec Active Directory/LDAP
   - Support des protocoles SAML et OAuth

## 4.2. Politiques de sécurité

Les politiques de sécurité définissent comment Cortex XDR protège votre environnement contre les menaces. Une configuration appropriée des politiques est essentielle pour équilibrer sécurité et productivité.

### 4.2.1. Création et gestion des politiques

**Accès aux politiques**

1. Dans la console Cortex XDR, naviguez vers "Politiques"
2. Sélectionnez le type de politique à configurer :
   - Politiques de prévention des malwares
   - Politiques de protection contre les exploits
   - Politiques de contrôle des périphériques
   - Politiques de restriction des applications
   - Politiques de détection comportementale

**Création d'une nouvelle politique**

1. Cliquez sur "Ajouter une politique"
2. Donnez un nom descriptif à la politique
3. Définissez la portée de la politique (groupes d'endpoints concernés)
4. Configurez les règles spécifiques
5. Définissez les actions à prendre en cas de détection
6. Configurez les exceptions si nécessaire
7. Activez la politique et définissez sa priorité

**Gestion des politiques existantes**

1. **Modification** : Sélectionnez une politique et cliquez sur "Modifier"
2. **Duplication** : Utilisez "Dupliquer" pour créer une variante d'une politique existante
3. **Désactivation** : Désactivez temporairement une politique sans la supprimer
4. **Suppression** : Supprimez les politiques obsolètes ou inutilisées

**Ordre de priorité des politiques**

Les politiques sont appliquées selon un ordre de priorité défini. En cas de conflit entre plusieurs politiques applicables à un même endpoint, la politique avec la priorité la plus élevée prévaut.

1. Naviguez vers "Politiques" > "Ordre de priorité"
2. Réorganisez les politiques par glisser-déposer
3. Enregistrez la nouvelle configuration de priorité

### 4.2.2. Paramètres recommandés par type d'environnement

Les paramètres de politique optimaux varient selon le type d'environnement. Voici des recommandations pour différents contextes :

**Environnement de production critique**

| Type de politique | Paramètre | Valeur recommandée | Justification |
|------------------|-----------|-------------------|---------------|
| Malware | Mode de protection | Blocage | Environnement critique nécessitant une protection maximale |
| Malware | Analyse à l'accès | Activée | Détection immédiate des menaces |
| Exploits | Protection mémoire | Élevée | Protection contre les attaques sans fichier |
| Comportementale | Sensibilité | Moyenne-élevée | Équilibre entre détection et faux positifs |
| Applications | Mode | Liste d'autorisation | Seules les applications approuvées sont autorisées |

**Environnement de bureau standard**

| Type de politique | Paramètre | Valeur recommandée | Justification |
|------------------|-----------|-------------------|---------------|
| Malware | Mode de protection | Blocage | Protection complète contre les malwares |
| Malware | Analyse à l'accès | Activée | Détection immédiate des menaces |
| Exploits | Protection mémoire | Moyenne | Bon équilibre sécurité/performance |
| Comportementale | Sensibilité | Moyenne | Équilibre entre détection et faux positifs |
| Applications | Mode | Surveillance | Surveillance des applications non approuvées |

**Environnement de développement**

| Type de politique | Paramètre | Valeur recommandée | Justification |
|------------------|-----------|-------------------|---------------|
| Malware | Mode de protection | Détection | Permet de tester sans bloquer |
| Malware | Analyse à l'accès | Activée | Détection des menaces sans interruption |
| Exploits | Protection mémoire | Basse | Minimise l'impact sur les outils de développement |
| Comportementale | Sensibilité | Basse | Réduit les interruptions pour les développeurs |
| Applications | Mode | Surveillance | Permet l'utilisation d'outils de développement |

**Serveurs critiques**

| Type de politique | Paramètre | Valeur recommandée | Justification |
|------------------|-----------|-------------------|---------------|
| Malware | Mode de protection | Blocage | Protection maximale pour les serveurs critiques |
| Malware | Analyse planifiée | Heures creuses | Minimise l'impact sur les performances |
| Exploits | Protection mémoire | Élevée | Protection contre les attaques sophistiquées |
| Comportementale | Sensibilité | Élevée | Détection maximale pour les serveurs critiques |
| Applications | Mode | Liste d'autorisation stricte | Seules les applications serveur approuvées sont autorisées |

## 4.3. Configuration de l'analyse comportementale

L'analyse comportementale est l'une des fonctionnalités les plus puissantes de Cortex XDR, permettant de détecter les menaces inconnues et les attaques sophistiquées qui échappent aux méthodes de détection traditionnelles.

### Principes de l'analyse comportementale

L'analyse comportementale dans Cortex XDR repose sur plusieurs principes clés :

1. **Établissement d'une ligne de base** : Le système observe le comportement normal des utilisateurs, systèmes et applications pour établir une référence.
2. **Détection des anomalies** : Les écarts par rapport à cette ligne de base sont identifiés comme des anomalies potentielles.
3. **Analyse contextuelle** : Les anomalies sont évaluées dans leur contexte pour déterminer si elles représentent une menace réelle.
4. **Machine learning** : Des algorithmes d'apprentissage automatique affinent continuellement la détection.

### Configuration des politiques d'analyse comportementale

Pour configurer l'analyse comportementale :

1. Naviguez vers "Politiques" > "Analyse comportementale"
2. Cliquez sur "Ajouter une politique" ou sélectionnez une politique existante
3. Configurez les paramètres suivants :

**Paramètres généraux**
- Nom et description de la politique
- Groupes d'endpoints ciblés
- Niveau de sensibilité global (Bas, Moyen, Élevé)

**Détection des comportements suspects**
- Exécution de processus inhabituels
- Modifications de registre suspectes
- Connexions réseau anormales
- Accès aux fichiers sensibles
- Élévation de privilèges
- Persistance système

**Actions automatiques**
- Alerter uniquement
- Bloquer le processus
- Isoler l'endpoint
- Exécuter un script personnalisé

### Optimisation de l'analyse comportementale

Pour maximiser l'efficacité de l'analyse comportementale tout en minimisant les faux positifs :

1. **Phase d'apprentissage**
   - Commencez avec un niveau de sensibilité bas
   - Passez en revue les alertes générées pendant 2-4 semaines
   - Ajustez progressivement la sensibilité

2. **Exclusions ciblées**
   - Identifiez les processus légitimes générant des faux positifs
   - Créez des exclusions spécifiques pour ces processus
   - Documentez toutes les exclusions avec leur justification

3. **Personnalisation par groupe**
   - Adaptez la sensibilité selon le profil de risque de chaque groupe
   - Appliquez des règles plus strictes aux systèmes critiques
   - Réduisez la sensibilité pour les environnements de développement

4. **Révision périodique**
   - Analysez régulièrement les alertes générées
   - Affinez les paramètres en fonction des résultats
   - Mettez à jour les exclusions selon l'évolution de l'environnement

## 4.4. Intégration avec d'autres solutions

L'intégration de Cortex XDR avec d'autres solutions de sécurité et d'infrastructure permet de créer un écosystème de cybersécurité cohérent et efficace.

### 4.4.1. Intégration SIEM

L'intégration avec les systèmes SIEM (Security Information and Event Management) permet de centraliser la gestion des événements de sécurité et d'enrichir l'analyse.

**Méthodes d'intégration SIEM**

1. **API REST** : Utilisation de l'API Cortex XDR pour extraire les données
   - Naviguez vers "Administration" > "API"
   - Générez une clé API avec les permissions appropriées
   - Configurez le connecteur SIEM pour utiliser cette clé

2. **Webhooks** : Configuration de notifications en temps réel
   - Naviguez vers "Administration" > "Webhooks"
   - Créez un nouveau webhook pointant vers votre SIEM
   - Configurez les types d'événements à transmettre

3. **Syslog** : Transmission des événements via syslog
   - Naviguez vers "Administration" > "Intégrations"
   - Configurez les paramètres syslog (serveur, port, protocole)
   - Sélectionnez les événements à transmettre

**Intégrations SIEM spécifiques**

| SIEM | Méthode recommandée | Fonctionnalités supportées |
|------|---------------------|----------------------------|
| Splunk | App Cortex XDR pour Splunk | Alertes, incidents, données brutes, tableaux de bord |
| IBM QRadar | Extension QRadar | Alertes, corrélation d'événements |
| Microsoft Sentinel | Connecteur Azure | Alertes, incidents, analyse automatisée |
| Elastic | Logstash/API | Données brutes, visualisations personnalisées |

**Configuration de l'intégration Splunk (exemple)**

1. Installez l'application Cortex XDR depuis Splunkbase
2. Configurez les paramètres de connexion :
   - URL de l'API Cortex XDR
   - Clé API et ID API
   - Intervalle de collecte
3. Sélectionnez les types de données à collecter
4. Validez la connexion et vérifiez la réception des données
5. Personnalisez les tableaux de bord selon vos besoins

### 4.4.2. Intégration SOAR

L'intégration avec les plateformes SOAR (Security Orchestration, Automation and Response) permet d'automatiser les workflows de réponse aux incidents.

**Configuration de l'intégration SOAR**

1. **Préparation dans Cortex XDR**
   - Naviguez vers "Administration" > "API"
   - Créez une clé API avec les permissions de lecture et d'action
   - Notez l'ID API et la clé générée

2. **Configuration dans la plateforme SOAR**
   - Installez le pack d'intégration Cortex XDR
   - Configurez la connexion avec l'URL, l'ID API et la clé API
   - Testez la connexion pour valider les paramètres

3. **Création de playbooks automatisés**
   - Développez des workflows pour les scénarios courants
   - Configurez les déclencheurs basés sur les alertes Cortex XDR
   - Définissez les actions automatiques et les points de décision humaine

**Cas d'usage d'automatisation SOAR**

| Scénario | Déclencheur | Actions automatisées | Intervention humaine |
|----------|-------------|----------------------|---------------------|
| Détection de malware | Alerte malware | Isoler l'endpoint, collecter les artefacts | Analyse des artefacts, décision de remédiation |
| Comportement suspect | Alerte comportementale | Enrichir avec contexte, vérifier réputation | Évaluation de la menace |
| Mouvement latéral | Détection de connexions anormales | Bloquer les communications, collecter les logs | Investigation approfondie |
| Exfiltration de données | Alerte de transfert suspect | Bloquer la communication, capturer le trafic | Analyse des données potentiellement exfiltrées |

**Intégration avec Cortex XSOAR**

L'intégration native avec Cortex XSOAR (la solution SOAR de Palo Alto Networks) offre des fonctionnalités avancées :

1. Synchronisation bidirectionnelle des incidents
2. Playbooks préconfigurés pour les scénarios courants
3. Visualisation unifiée des alertes et des actions de réponse
4. Enrichissement automatique des incidents avec des données contextuelles

### 4.4.3. Intégration avec les solutions cloud (Office365, AWS, Azure, GCP)

L'intégration de Cortex XDR avec les environnements cloud étend la visibilité et la protection au-delà des endpoints traditionnels.

**Intégration Microsoft Office 365**

1. **Configuration dans Cortex XDR**
   - Naviguez vers "Administration" > "Intégrations" > "Cloud"
   - Sélectionnez "Microsoft Office 365"
   - Suivez l'assistant de configuration

2. **Autorisations requises**
   - Consentement administrateur pour les API Microsoft Graph
   - Permissions de lecture pour les journaux d'audit
   - Permissions pour les données Exchange, SharePoint et OneDrive

3. **Fonctionnalités supportées**
   - Détection des emails malveillants
   - Surveillance des accès aux documents sensibles
   - Identification des comptes compromis
   - Détection des partages externes suspects

**Intégration AWS**

1. **Configuration dans AWS**
   - Créez un rôle IAM avec les permissions appropriées
   - Configurez CloudTrail pour capturer les événements pertinents
   - Activez les journaux VPC Flow si nécessaire

2. **Configuration dans Cortex XDR**
   - Naviguez vers "Administration" > "Intégrations" > "Cloud"
   - Sélectionnez "Amazon Web Services"
   - Fournissez l'ARN du rôle IAM et l'ID de compte AWS

3. **Fonctionnalités supportées**
   - Surveillance des activités dans les services AWS
   - Détection des configurations à risque
   - Identification des accès non autorisés
   - Analyse du trafic réseau anormal

**Intégration Azure**

1. **Configuration dans Azure**
   - Créez une application dans Azure AD
   - Attribuez les permissions nécessaires
   - Générez une clé secrète client

2. **Configuration dans Cortex XDR**
   - Naviguez vers "Administration" > "Intégrations" > "Cloud"
   - Sélectionnez "Microsoft Azure"
   - Fournissez l'ID d'application, la clé secrète et l'ID de tenant

3. **Fonctionnalités supportées**
   - Surveillance des journaux Azure Activity
   - Analyse des événements Azure Security Center
   - Détection des comportements anormaux dans les services Azure
   - Identification des configurations à risque

**Intégration Google Cloud Platform**

1. **Configuration dans GCP**
   - Créez un compte de service avec les permissions appropriées
   - Activez les API nécessaires
   - Générez une clé de compte de service

2. **Configuration dans Cortex XDR**
   - Naviguez vers "Administration" > "Intégrations" > "Cloud"
   - Sélectionnez "Google Cloud Platform"
   - Téléchargez le fichier de clé JSON du compte de service

3. **Fonctionnalités supportées**
   - Analyse des journaux Cloud Audit
   - Surveillance des journaux VPC Flow
   - Détection des configurations à risque
   - Identification des accès non autorisés

## 4.5. Configuration des notifications et alertes

Une configuration efficace des notifications et alertes est essentielle pour garantir que les équipes de sécurité soient informées rapidement des menaces potentielles, tout en évitant la fatigue d'alerte.

### Types de notifications

Cortex XDR propose plusieurs types de notifications :

1. **Alertes de sécurité** : Notifications générées lors de la détection d'une menace
2. **Notifications d'incident** : Informations sur les nouveaux incidents ou les mises à jour
3. **Notifications système** : Informations sur l'état du système, les mises à jour, etc.
4. **Rapports planifiés** : Résumés périodiques des activités et des menaces

### Configuration des canaux de notification

Pour configurer les canaux de notification :

1. Naviguez vers "Administration" > "Notifications"
2. Cliquez sur "Ajouter un canal de notification"
3. Sélectionnez le type de canal :
   - Email
   - Webhook
   - Syslog
   - Intégration SIEM/SOAR
4. Configurez les paramètres spécifiques au canal
5. Testez la notification pour valider la configuration

### Personnalisation des règles de notification

Pour personnaliser quand et comment les notifications sont envoyées :

1. Naviguez vers "Administration" > "Règles de notification"
2. Cliquez sur "Ajouter une règle"
3. Définissez les critères de déclenchement :
   - Type d'événement (alerte, incident, système)
   - Sévérité minimale
   - Catégories spécifiques
   - Endpoints ou groupes concernés
4. Sélectionnez les canaux de notification à utiliser
5. Définissez la fréquence des notifications
6. Activez ou planifiez la règle

### Bonnes pratiques pour les notifications

Pour optimiser l'efficacité des notifications et éviter la fatigue d'alerte :

1. **Hiérarchisation des alertes**
   - Réservez les notifications en temps réel pour les alertes critiques
   - Utilisez des résumés périodiques pour les alertes de moindre importance
   - Définissez clairement les critères de sévérité

2. **Personnalisation par équipe**
   - Adaptez les notifications selon les responsabilités de chaque équipe
   - Créez des canaux dédiés pour différents types de menaces
   - Utilisez des formats de notification adaptés à chaque équipe

3. **Réduction du bruit**
   - Consolidez les alertes similaires
   - Implémentez des seuils pour éviter les notifications répétitives
   - Utilisez des périodes de silence pour les systèmes en maintenance

4. **Enrichissement des notifications**
   - Incluez des informations contextuelles dans les notifications
   - Ajoutez des liens directs vers les incidents dans la console
   - Fournissez des recommandations d'action initiales

**Exemple de stratégie de notification**

| Sévérité | Canal | Fréquence | Destinataires | Contenu |
|----------|-------|-----------|--------------|---------|
| Critique | Email + SMS | Immédiate | Équipe SOC 24/7 | Détails complets + actions recommandées |
| Élevée | Email | Immédiate | Équipe SOC | Résumé + lien vers la console |
| Moyenne | Email | Résumé toutes les 4h | Analystes | Liste consolidée |
| Faible | Dashboard | Rapport quotidien | Gestionnaires | Statistiques et tendances |
