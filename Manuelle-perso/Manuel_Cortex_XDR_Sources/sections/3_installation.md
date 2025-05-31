# 3. Guide d'installation étape par étape

## 3.1. Prérequis techniques

Avant de procéder à l'installation de Cortex XDR, il est essentiel de s'assurer que votre environnement répond aux prérequis techniques nécessaires. Cette préparation garantira un déploiement fluide et une utilisation optimale de la solution.

### 3.1.1. Configuration matérielle requise

Les exigences matérielles varient selon le rôle du système dans l'architecture Cortex XDR.

**Pour la console Cortex XDR (hébergée dans le cloud par Palo Alto Networks)**
- Aucune infrastructure locale n'est requise pour la console elle-même
- Navigateur web moderne pour y accéder :
  - Google Chrome 80 ou version ultérieure
  - Mozilla Firefox 72 ou version ultérieure
  - Microsoft Edge 80 ou version ultérieure
  - Safari 13 ou version ultérieure

**Pour les endpoints avec agents Cortex XDR**

*Postes de travail Windows :*
- Processeur : Intel Pentium 4 ou ultérieur (2 GHz minimum recommandé)
- Mémoire : 2 Go RAM minimum (4 Go recommandés)
- Espace disque : 1 Go d'espace libre minimum
- Systèmes d'exploitation supportés :
  - Windows 7 SP1 (32 et 64 bits)
  - Windows 8.1 (32 et 64 bits)
  - Windows 10 (32 et 64 bits)
  - Windows 11 (64 bits)

*Serveurs Windows :*
- Processeur : Intel Xeon ou équivalent (2 GHz minimum)
- Mémoire : 4 Go RAM minimum (8 Go recommandés)
- Espace disque : 1 Go d'espace libre minimum
- Systèmes d'exploitation supportés :
  - Windows Server 2012 R2
  - Windows Server 2016
  - Windows Server 2019
  - Windows Server 2022

*macOS :*
- Processeur : Intel ou Apple Silicon (M1/M2)
- Mémoire : 2 Go RAM minimum (4 Go recommandés)
- Espace disque : 1 Go d'espace libre minimum
- Systèmes d'exploitation supportés :
  - macOS 10.15 (Catalina)
  - macOS 11 (Big Sur)
  - macOS 12 (Monterey)
  - macOS 13 (Ventura)
  - macOS 14 (Sonoma)

*Linux :*
- Processeur : x86_64 compatible
- Mémoire : 2 Go RAM minimum (4 Go recommandés)
- Espace disque : 1 Go d'espace libre minimum
- Distributions supportées :
  - Red Hat Enterprise Linux (RHEL) 7.x, 8.x, 9.x
  - CentOS 7.x, 8.x
  - Ubuntu 18.04 LTS, 20.04 LTS, 22.04 LTS
  - Debian 10, 11, 12
  - Amazon Linux 2, 2023
  - SUSE Linux Enterprise Server (SLES) 12 SP4+, 15

### 3.1.2. Configuration réseau nécessaire

Pour garantir le bon fonctionnement de Cortex XDR, votre réseau doit répondre aux exigences suivantes :

**Connectivité Internet**
- Les agents Cortex XDR doivent pouvoir communiquer avec le cloud Palo Alto Networks
- Connexion Internet fiable avec une bande passante suffisante (minimum recommandé : 1 Mbps par tranche de 100 agents)

**Ports et protocoles**
- Communication sortante sur le port TCP 443 (HTTPS) pour les agents vers le cloud Cortex XDR
- Communication sortante sur le port TCP 443 pour l'accès à la console de gestion
- Pour la fonctionnalité d'isolation réseau : ports TCP 8443, 443 et 80

**Proxy et pare-feu**
- Si votre organisation utilise un proxy pour le trafic Internet sortant, Cortex XDR prend en charge :
  - Proxys HTTP/HTTPS
  - Authentification de base et NTLM
- Les domaines suivants doivent être autorisés dans les pare-feux et proxys :
  - *.paloaltonetworks.com
  - *.cortex.paloaltonetworks.com
  - *.wildfire.paloaltonetworks.com

**Latence réseau**
- Latence maximale recommandée entre les agents et le cloud Cortex XDR : < 300 ms
- Latence optimale pour les performances en temps réel : < 100 ms

### 3.1.3. Comptes et permissions

La mise en place de Cortex XDR nécessite différents niveaux d'accès et de permissions :

**Compte Cortex**
- Un compte Cortex actif auprès de Palo Alto Networks
- Licences appropriées pour les fonctionnalités souhaitées (Prevent, Pro, Enterprise)

**Permissions administratives**
- Pour l'installation des agents :
  - Droits d'administrateur local sur les endpoints Windows
  - Droits root sur les systèmes macOS et Linux
  - Pour les déploiements à grande échelle : accès aux outils de déploiement de logiciels (SCCM, Jamf, etc.)

**Comptes utilisateurs pour la console**
- Administrateur Cortex XDR : gestion complète de la plateforme
- Analystes de sécurité : accès aux incidents et aux outils d'investigation
- Opérateurs : gestion quotidienne et déploiement des agents
- Auditeurs : accès en lecture seule pour la conformité

**Intégrations avec Active Directory/LDAP (optionnel)**
- Compte de service avec permissions de lecture pour l'intégration avec l'annuaire d'entreprise
- Permissions pour la synchronisation des groupes et utilisateurs

**Tableau des permissions recommandées**

| Rôle | Accès à la console | Gestion des politiques | Investigation | Réponse | Rapports |
|------|-------------------|------------------------|--------------|---------|----------|
| Administrateur | Complet | Complet | Complet | Complet | Complet |
| Analyste SOC | Limité | Lecture seule | Complet | Limité | Complet |
| Opérateur | Limité | Limité | Limité | Limité | Limité |
| Auditeur | Lecture seule | Lecture seule | Lecture seule | Aucun | Complet |

## 3.2. Installation de la console Cortex XDR

La console Cortex XDR est hébergée dans le cloud par Palo Alto Networks, ce qui simplifie considérablement le processus d'installation. Voici les étapes pour activer et configurer votre console :

### Étape 1 : Activation de votre compte Cortex

1. **Réception de l'email d'activation**
   - Après l'achat de licences Cortex XDR, un email d'activation est envoyé à l'adresse fournie lors de l'achat
   - Cet email contient un lien d'activation et des instructions initiales

2. **Création du compte administrateur**
   - Cliquez sur le lien d'activation dans l'email
   - Remplissez le formulaire d'inscription avec les informations demandées
   - Créez un mot de passe fort respectant les critères de complexité
   - Configurez l'authentification à deux facteurs (fortement recommandée)

3. **Connexion initiale à la console**
   - Accédez à https://cortex.paloaltonetworks.com
   - Connectez-vous avec les identifiants créés
   - Complétez la configuration initiale guidée

### Étape 2 : Configuration initiale de la console

1. **Définition des paramètres régionaux**
   - Sélectionnez la région de données principale pour votre organisation
   - Configurez le fuseau horaire et les formats de date/heure

2. **Configuration des notifications**
   - Configurez les adresses email pour les notifications système
   - Définissez les seuils d'alerte et les canaux de notification

3. **Création des comptes utilisateurs**
   - Naviguez vers "Administration" > "Utilisateurs"
   - Cliquez sur "Ajouter un utilisateur"
   - Remplissez les informations requises et attribuez les rôles appropriés
   - Répétez pour tous les utilisateurs nécessaires

4. **Configuration des rôles personnalisés (optionnel)**
   - Naviguez vers "Administration" > "Rôles"
   - Cliquez sur "Ajouter un rôle"
   - Définissez les permissions spécifiques pour ce rôle
   - Attribuez le rôle aux utilisateurs concernés

### Étape 3 : Configuration des paramètres de tenant

1. **Accès aux paramètres du tenant**
   - Dans la console, naviguez vers "Administration" > "Paramètres du tenant"

2. **Configuration des paramètres généraux**
   - Définissez le nom du tenant
   - Configurez les options de rétention des données
   - Paramétrez les options de journalisation

3. **Configuration de l'authentification**
   - Configurez l'intégration avec votre fournisseur d'identité (IdP) si vous utilisez SSO
   - Définissez les politiques de mot de passe
   - Activez et configurez l'authentification multifacteur

4. **Configuration des paramètres de sécurité**
   - Définissez les politiques de verrouillage de compte
   - Configurez les paramètres de session (délai d'expiration, etc.)
   - Paramétrez les options de journalisation des audits

### Étape 4 : Vérification de l'installation de la console

1. **Vérification de l'accès**
   - Assurez-vous que tous les utilisateurs peuvent se connecter à la console
   - Vérifiez que les rôles et permissions sont correctement appliqués

2. **Vérification des fonctionnalités**
   - Naviguez à travers les différentes sections de la console
   - Confirmez que toutes les fonctionnalités achetées sont disponibles

3. **Test des notifications**
   - Générez une notification de test
   - Vérifiez que les notifications sont reçues par les canaux configurés

## 3.3. Déploiement des agents

Le déploiement des agents Cortex XDR sur les endpoints est une étape cruciale pour assurer la protection et la visibilité sur l'ensemble de votre environnement.

### 3.3.1. Agents Windows

**Préparation au déploiement**

1. **Téléchargement du package d'installation**
   - Dans la console Cortex XDR, naviguez vers "Endpoints" > "Déploiement"
   - Sélectionnez "Windows" comme système d'exploitation
   - Choisissez la version de l'agent (32 ou 64 bits)
   - Configurez les options de déploiement (profil de protection, groupes, etc.)
   - Téléchargez le package d'installation (.msi)

2. **Préparation des endpoints**
   - Vérifiez que les endpoints répondent aux prérequis système
   - Désinstallez tout logiciel antivirus tiers conflictuel
   - Assurez-vous que les endpoints ont accès à Internet

**Méthodes de déploiement**

1. **Installation manuelle**
   - Copiez le fichier MSI sur l'endpoint
   - Exécutez le fichier MSI avec des droits d'administrateur
   - Suivez les instructions de l'assistant d'installation
   - Redémarrez l'endpoint si demandé

2. **Déploiement via ligne de commande**
   ```
   msiexec /i CortexXDRSetup.msi /quiet TENANT_ID=<votre_tenant_id> INSTALLATION_TOKEN=<votre_token> UNINSTALL_PASSWORD=<mot_de_passe>
   ```

3. **Déploiement via Microsoft SCCM**
   - Créez un package de déploiement dans SCCM
   - Ajoutez le fichier MSI et les paramètres de ligne de commande
   - Définissez la collection cible
   - Planifiez le déploiement

4. **Déploiement via GPO (Stratégie de groupe)**
   - Créez un partage réseau contenant le fichier MSI
   - Créez une nouvelle GPO ou modifiez une existante
   - Naviguez vers "Configuration ordinateur" > "Politiques" > "Paramètres du logiciel" > "Installation de logiciels"
   - Ajoutez un nouveau package en pointant vers le MSI sur le partage réseau
   - Configurez les options de déploiement
   - Liez la GPO à l'unité d'organisation appropriée

**Vérification post-déploiement**

1. **Vérification locale**
   - Vérifiez que le service Cortex XDR est en cours d'exécution
   - Confirmez la présence de l'icône dans la barre des tâches
   - Vérifiez les journaux d'installation dans l'Observateur d'événements

2. **Vérification dans la console**
   - Dans la console Cortex XDR, naviguez vers "Endpoints" > "Gestion"
   - Confirmez que les nouveaux endpoints apparaissent dans la liste
   - Vérifiez leur statut et leur version d'agent

### 3.3.2. Agents macOS

**Préparation au déploiement**

1. **Téléchargement du package d'installation**
   - Dans la console Cortex XDR, naviguez vers "Endpoints" > "Déploiement"
   - Sélectionnez "macOS" comme système d'exploitation
   - Configurez les options de déploiement
   - Téléchargez le package d'installation (.pkg)

2. **Préparation des endpoints**
   - Vérifiez que les Mac répondent aux prérequis système
   - Assurez-vous que les utilisateurs disposent des droits d'administrateur
   - Vérifiez la compatibilité avec la version de macOS

**Méthodes de déploiement**

1. **Installation manuelle**
   - Copiez le fichier PKG sur le Mac
   - Double-cliquez sur le package pour lancer l'installation
   - Suivez les instructions de l'assistant d'installation
   - Accordez les permissions système requises lorsque demandé

2. **Déploiement via ligne de commande**
   ```
   sudo installer -pkg /path/to/CortexXDRInstaller.pkg -target /
   ```

3. **Déploiement via Jamf Pro**
   - Importez le package PKG dans Jamf Pro
   - Créez une nouvelle politique d'installation
   - Configurez les options de déploiement
   - Définissez la portée (ordinateurs ou groupes cibles)
   - Planifiez le déploiement

4. **Déploiement via Apple Remote Desktop**
   - Ajoutez les Mac cibles à Apple Remote Desktop
   - Utilisez la fonction "Installer des packages" pour déployer le PKG
   - Surveillez l'état du déploiement

**Configuration des permissions système**

Sur macOS, l'agent Cortex XDR nécessite plusieurs permissions système qui doivent être accordées :

1. **Extensions système**
   - Accédez à "Préférences Système" > "Sécurité et confidentialité" > "Général"
   - Autorisez les extensions système de Cortex XDR

2. **Accès complet au disque**
   - Accédez à "Préférences Système" > "Sécurité et confidentialité" > "Confidentialité"
   - Accordez l'accès complet au disque à l'agent Cortex XDR

3. **Surveillance de l'activité système**
   - Accordez les permissions pour la surveillance de l'activité système
   - Cette étape peut nécessiter un profil de configuration MDM

**Vérification post-déploiement**

1. **Vérification locale**
   - Vérifiez la présence de l'agent dans les préférences système
   - Confirmez que les services sont en cours d'exécution

2. **Vérification dans la console**
   - Confirmez que les Mac apparaissent dans la console Cortex XDR
   - Vérifiez leur statut et leur version d'agent

### 3.3.3. Agents Linux

**Préparation au déploiement**

1. **Téléchargement du package d'installation**
   - Dans la console Cortex XDR, naviguez vers "Endpoints" > "Déploiement"
   - Sélectionnez "Linux" comme système d'exploitation
   - Choisissez la distribution Linux appropriée
   - Téléchargez le package d'installation (.rpm ou .deb)

2. **Préparation des endpoints**
   - Vérifiez que les serveurs Linux répondent aux prérequis système
   - Assurez-vous que les dépendances requises sont installées
   - Vérifiez l'accès Internet pour la communication avec le cloud

**Méthodes de déploiement**

1. **Installation manuelle sur systèmes basés sur RPM (RHEL, CentOS)**
   ```
   sudo rpm -ivh cortex_xdr_agent.rpm
   ```

2. **Installation manuelle sur systèmes basés sur DEB (Ubuntu, Debian)**
   ```
   sudo dpkg -i cortex_xdr_agent.deb
   sudo apt-get -f install
   ```

3. **Déploiement via script d'installation**
   - Créez un script shell incluant les commandes d'installation
   - Ajoutez la configuration du tenant et du token
   - Déployez et exécutez le script sur les serveurs cibles

4. **Déploiement via outils de gestion de configuration**
   - Ansible : Créez un playbook pour le déploiement
   - Puppet : Développez un module pour l'installation
   - Chef : Créez une recette pour le déploiement automatisé

**Configuration post-installation**

1. **Vérification du service**
   ```
   systemctl status cortex_xdr_agent
   ```

2. **Configuration du pare-feu**
   - Assurez-vous que les règles de pare-feu permettent la communication sortante vers le cloud Cortex XDR
   ```
   firewall-cmd --permanent --add-port=443/tcp
   firewall-cmd --reload
   ```

3. **Configuration des journaux**
   - Les journaux de l'agent sont généralement stockés dans `/var/log/cortex`
   - Configurez la rotation des journaux si nécessaire

**Vérification post-déploiement**

1. **Vérification locale**
   ```
   ps aux | grep cortex
   netstat -tulpn | grep cortex
   ```

2. **Vérification dans la console**
   - Confirmez que les serveurs Linux apparaissent dans la console
   - Vérifiez leur statut et leur version d'agent

### 3.3.4. Agents pour appareils mobiles

Cortex XDR propose également des solutions pour les appareils mobiles, bien que les fonctionnalités soient différentes de celles des endpoints traditionnels.

**Agents Android**

1. **Préparation au déploiement**
   - Dans la console Cortex XDR, naviguez vers "Endpoints" > "Déploiement"
   - Sélectionnez "Android" comme système d'exploitation
   - Configurez les options de déploiement
   - Générez un lien de téléchargement ou un QR code

2. **Méthodes de déploiement**
   - Déploiement via solution MDM (Mobile Device Management)
   - Installation manuelle via Google Play Store
   - Distribution du lien de téléchargement aux utilisateurs

3. **Configuration requise**
   - Android 8.0 ou version ultérieure
   - Accès Internet
   - Permissions d'application appropriées

**Agents iOS**

1. **Préparation au déploiement**
   - Dans la console Cortex XDR, naviguez vers "Endpoints" > "Déploiement"
   - Sélectionnez "iOS" comme système d'exploitation
   - Configurez les options de déploiement
   - Générez un lien de téléchargement ou un QR code

2. **Méthodes de déploiement**
   - Déploiement via Apple Business Manager et MDM
   - Installation manuelle via App Store
   - Distribution du lien de téléchargement aux utilisateurs

3. **Configuration requise**
   - iOS 13.0 ou version ultérieure
   - Accès Internet
   - Permissions d'application appropriées

**Fonctionnalités disponibles sur mobile**

| Fonctionnalité | Android | iOS |
|----------------|---------|-----|
| Analyse des applications | ✓ | ✓ |
| Détection de malware | ✓ | Limitée |
| Analyse des URL | ✓ | ✓ |
| Protection réseau | ✓ | Limitée |
| Détection de jailbreak/root | ✓ | ✓ |
| Réponse aux incidents | Limitée | Limitée |

## 3.4. Vérification post-installation

Après avoir déployé les agents Cortex XDR, il est essentiel de vérifier que l'installation s'est déroulée correctement et que le système fonctionne comme prévu.

### Vérification de la connectivité des agents

1. **Vérification dans la console**
   - Naviguez vers "Endpoints" > "Gestion"
   - Confirmez que tous les endpoints déployés apparaissent dans la liste
   - Vérifiez que leur statut est "En ligne" (colonne "État")
   - Confirmez que la version de l'agent est correcte

2. **Vérification des groupes d'endpoints**
   - Assurez-vous que les endpoints sont assignés aux bons groupes
   - Vérifiez que les politiques appropriées sont appliquées à chaque groupe

3. **Test de communication**
   - Sélectionnez un endpoint et cliquez sur "Actions" > "Collecter les journaux"
   - Si l'opération réussit, cela confirme que la communication bidirectionnelle fonctionne

### Vérification des politiques de sécurité

1. **Application des politiques**
   - Naviguez vers "Politiques" > "État du déploiement"
   - Vérifiez que toutes les politiques sont correctement déployées
   - Confirmez qu'il n'y a pas d'erreurs de déploiement

2. **Test des politiques**
   - Effectuez des tests de base pour vérifier que les politiques fonctionnent
   - Par exemple, tentez d'exécuter un fichier de test EICAR pour confirmer la détection de malware

### Vérification des fonctionnalités de détection

1. **Test de détection de base**
   - Utilisez des fichiers de test comme EICAR (https://www.eicar.org/download-anti-malware-testfile/)
   - Vérifiez que l'agent détecte et bloque correctement le fichier

2. **Vérification des alertes**
   - Naviguez vers "Alertes" dans la console
   - Confirmez que les alertes de test sont correctement générées et affichées

3. **Test de réponse**
   - Sélectionnez un endpoint de test
   - Essayez d'exécuter une action de réponse simple comme "Collecter les informations système"
   - Vérifiez que l'action est exécutée correctement

### Vérification de la journalisation

1. **Journaux des agents**
   - Sur un endpoint Windows, vérifiez les journaux dans l'Observateur d'événements
   - Sur macOS et Linux, vérifiez les fichiers journaux dans les répertoires appropriés

2. **Journaux de la console**
   - Naviguez vers "Administration" > "Journaux d'audit"
   - Vérifiez que les activités d'installation et de configuration sont correctement enregistrées

3. **Journaux d'activité**
   - Naviguez vers "Recherche" > "Activité des endpoints"
   - Confirmez que les données d'activité sont collectées et disponibles pour la recherche

## 3.5. Résolution des problèmes courants d'installation

Malgré une préparation minutieuse, des problèmes peuvent survenir lors de l'installation de Cortex XDR. Voici comment résoudre les problèmes les plus courants.

### Problèmes de connectivité des agents

1. **Agent hors ligne**
   - **Symptôme** : L'agent apparaît comme "Hors ligne" dans la console
   - **Solutions** :
     - Vérifiez la connectivité Internet de l'endpoint
     - Confirmez que les ports et domaines requis sont autorisés dans les pare-feux
     - Redémarrez le service de l'agent
     - Vérifiez les journaux de l'agent pour identifier les erreurs de connexion

2. **Échec de l'enregistrement de l'agent**
   - **Symptôme** : L'agent est installé mais n'apparaît pas dans la console
   - **Solutions** :
     - Vérifiez que l'ID du tenant et le token d'installation sont corrects
     - Assurez-vous que le token d'installation n'a pas expiré
     - Réinstallez l'agent avec les paramètres corrects

### Problèmes d'installation

1. **Échec de l'installation sur Windows**
   - **Symptôme** : Le processus d'installation se termine avec une erreur
   - **Solutions** :
     - Vérifiez les journaux d'installation dans %TEMP%
     - Assurez-vous que l'utilisateur a des droits d'administrateur
     - Désinstallez tout logiciel antivirus conflictuel
     - Exécutez l'installation en mode de compatibilité si nécessaire

2. **Échec de l'installation sur macOS**
   - **Symptôme** : L'installation échoue ou l'agent ne fonctionne pas correctement
   - **Solutions** :
     - Vérifiez que les extensions système sont autorisées
     - Accordez l'accès complet au disque à l'agent
     - Vérifiez les journaux système dans Console.app
     - Utilisez la commande `sudo installer -dumplog -pkg /path/to/package.pkg -target /` pour obtenir des journaux détaillés

3. **Échec de l'installation sur Linux**
   - **Symptôme** : Erreurs lors de l'installation du package
   - **Solutions** :
     - Vérifiez les dépendances manquantes
     - Assurez-vous que le noyau Linux est compatible
     - Consultez les journaux système avec `journalctl`
     - Vérifiez l'espace disque disponible

### Problèmes de performance

1. **Impact sur les performances système**
   - **Symptôme** : Ralentissement notable du système après l'installation
   - **Solutions** :
     - Vérifiez la configuration de l'agent pour réduire l'impact
     - Ajustez les paramètres de scan pour éviter les périodes d'activité intense
     - Mettez à jour l'agent vers la dernière version
     - Excluez certains processus ou dossiers si nécessaire

2. **Conflits avec d'autres logiciels**
   - **Symptôme** : Instabilité du système ou problèmes avec d'autres applications
   - **Solutions** :
     - Identifiez les applications en conflit
     - Configurez des exclusions pour ces applications
     - Contactez le support technique pour des recommandations spécifiques

### Problèmes de politique

1. **Politiques non appliquées**
   - **Symptôme** : Les politiques configurées ne semblent pas être en vigueur
   - **Solutions** :
     - Vérifiez que l'endpoint est dans le bon groupe
     - Forcez la synchronisation des politiques
     - Redémarrez l'agent
     - Vérifiez les conflits de politique potentiels

2. **Faux positifs excessifs**
   - **Symptôme** : Trop d'alertes pour des activités légitimes
   - **Solutions** :
     - Ajustez les paramètres de sensibilité des politiques
     - Créez des exclusions pour les applications légitimes
     - Mettez à jour la base de données de réputation

### Ressources de dépannage

1. **Outils de diagnostic intégrés**
   - Utilisez l'outil de collecte de journaux dans la console
   - Exécutez l'outil de diagnostic sur l'endpoint

2. **Documentation officielle**
   - Consultez le guide de dépannage de Cortex XDR
   - Référez-vous aux notes de version pour les problèmes connus

3. **Support technique**
   - Ouvrez un ticket auprès du support Palo Alto Networks
   - Fournissez les journaux et les informations de diagnostic collectés
