# 10. Glossaire, FAQ et Checklist

## 10.1. Glossaire des termes techniques

**Agent** : Composant logiciel installé sur les endpoints qui collecte des données et applique les politiques de sécurité définies dans la console Cortex XDR.

**Alerte** : Notification générée lorsqu'une activité suspecte ou malveillante est détectée par Cortex XDR.

**Analyse comportementale** : Technique de détection qui identifie les menaces en observant les comportements anormaux plutôt que de se fier uniquement aux signatures connues.

**Analyse statique** : Méthode d'analyse des fichiers sans les exécuter, en examinant leur structure, leur code et leurs caractéristiques.

**Analyse dynamique** : Méthode d'analyse qui observe le comportement d'un fichier ou d'un processus pendant son exécution dans un environnement contrôlé.

**APT (Advanced Persistent Threat)** : Attaque ciblée et sophistiquée menée sur une longue période par des acteurs disposant de ressources importantes.

**C2 (Command and Control)** : Serveur ou infrastructure utilisé par les attaquants pour communiquer avec les systèmes compromis et leur envoyer des instructions.

**Chaîne d'attaque** : Séquence d'événements et d'actions constituant une attaque, depuis l'infection initiale jusqu'aux objectifs finaux de l'attaquant.

**Corrélation** : Processus d'identification des relations entre différents événements de sécurité pour détecter des modèles d'attaque complexes.

**EDR (Endpoint Detection and Response)** : Solution de sécurité focalisée sur la détection et la réponse aux menaces au niveau des endpoints.

**Endpoint** : Tout appareil connecté au réseau d'entreprise, comme un ordinateur, un serveur, un appareil mobile ou un objet connecté.

**Exploit** : Code ou technique permettant d'exploiter une vulnérabilité dans un logiciel ou un système.

**Faux positif** : Alerte de sécurité incorrecte identifiant une activité légitime comme malveillante.

**Faux négatif** : Échec de détection d'une menace réelle par un système de sécurité.

**Forensique** : Ensemble de techniques scientifiques utilisées pour collecter, analyser et préserver des preuves numériques.

**Groupe d'endpoints** : Ensemble d'endpoints partageant des caractéristiques communes et auxquels sont appliquées les mêmes politiques de sécurité.

**Incident** : Ensemble d'alertes et d'événements corrélés représentant une menace potentielle nécessitant une investigation.

**IOC (Indicator of Compromise)** : Artefact observé sur un réseau ou un système qui indique avec une forte probabilité une intrusion ou une attaque.

**Isolation d'endpoint** : Fonction de sécurité permettant de déconnecter un endpoint du réseau tout en maintenant la communication avec la console de gestion.

**Malware** : Logiciel malveillant conçu pour s'infiltrer dans un système informatique afin de voler des données, perturber des opérations ou causer d'autres dommages.

**MITRE ATT&CK** : Framework qui documente les tactiques, techniques et procédures (TTP) utilisées par les attaquants.

**MTTD (Mean Time To Detect)** : Temps moyen nécessaire pour détecter une menace après son introduction dans l'environnement.

**MTTR (Mean Time To Respond)** : Temps moyen nécessaire pour répondre à une menace après sa détection.

**NDR (Network Detection and Response)** : Solution de sécurité focalisée sur la détection et la réponse aux menaces au niveau du réseau.

**Politique de sécurité** : Ensemble de règles définissant comment Cortex XDR doit protéger les endpoints et répondre aux menaces détectées.

**Ransomware** : Type de malware qui chiffre les données de la victime et exige une rançon pour leur déchiffrement.

**Remédiation** : Actions entreprises pour éliminer une menace et restaurer les systèmes affectés à un état sécurisé.

**Sandbox** : Environnement isolé et sécurisé utilisé pour exécuter et analyser des fichiers potentiellement malveillants.

**SIEM (Security Information and Event Management)** : Système qui collecte, analyse et corrèle les données de sécurité provenant de diverses sources.

**SOAR (Security Orchestration, Automation and Response)** : Plateforme qui automatise et orchestre les processus de réponse aux incidents de sécurité.

**SOC (Security Operations Center)** : Centre opérationnel chargé de surveiller, détecter, analyser et répondre aux incidents de cybersécurité.

**Threat Hunting** : Processus proactif de recherche de menaces qui n'ont pas été détectées par les systèmes de sécurité automatisés.

**Triage** : Processus d'évaluation et de priorisation des alertes et incidents de sécurité.

**TTP (Tactics, Techniques, and Procedures)** : Modèles de comportement des attaquants, incluant leurs objectifs (tactiques), méthodes (techniques) et actions spécifiques (procédures).

**UEBA (User and Entity Behavior Analytics)** : Analyse du comportement des utilisateurs et des entités pour détecter des anomalies pouvant indiquer une compromission.

**Vulnérabilité** : Faiblesse dans un système informatique pouvant être exploitée par un attaquant.

**WildFire** : Service cloud de Palo Alto Networks qui analyse les fichiers inconnus pour détecter les malwares.

**XDR (Extended Detection and Response)** : Solution de sécurité qui étend les capacités de l'EDR en intégrant et corrélant des données provenant de multiples sources (endpoints, réseau, cloud, etc.).

**XQL (XDR Query Language)** : Langage de requête utilisé dans Cortex XDR pour rechercher et analyser les données de sécurité.

**Zero-day** : Vulnérabilité inconnue du fabricant du logiciel et pour laquelle aucun correctif n'est disponible.

## 10.2. Foire aux questions (FAQ)

### Questions générales

**Q: Quelle est la différence entre un EDR traditionnel et Cortex XDR ?**

R: Contrairement aux solutions EDR traditionnelles qui se concentrent uniquement sur les endpoints, Cortex XDR est une plateforme de détection et de réponse étendue qui intègre et corrèle des données provenant de multiples sources : endpoints, réseau, cloud et applications SaaS. Cette approche unifiée permet une détection plus précise des menaces complexes et une visibilité complète sur l'ensemble de l'environnement.

**Q: Cortex XDR remplace-t-il mon antivirus existant ?**

R: Oui, Cortex XDR inclut des capacités complètes de protection contre les malwares qui remplacent les solutions antivirus traditionnelles. Il combine des techniques de détection avancées (signatures, heuristique, machine learning, analyse comportementale) offrant une protection supérieure à celle des antivirus conventionnels.

**Q: Combien d'agents Cortex XDR puis-je déployer avec ma licence ?**

R: Le nombre d'agents dépend du modèle de licence que vous avez acquis. Les licences Cortex XDR sont généralement basées sur le nombre d'endpoints protégés. Consultez votre contrat ou contactez votre représentant Palo Alto Networks pour connaître les détails spécifiques de votre licence.

**Q: Cortex XDR fonctionne-t-il hors ligne ?**

R: Oui, les agents Cortex XDR continuent de protéger les endpoints même lorsqu'ils sont déconnectés d'Internet. Les politiques de sécurité locales restent actives, et les événements sont mis en cache localement jusqu'à ce que la connexion soit rétablie. Cependant, certaines fonctionnalités comme l'analyse WildFire ou les mises à jour nécessitent une connexion Internet.

### Installation et déploiement

**Q: Quelles sont les configurations minimales requises pour installer l'agent Cortex XDR ?**

R: Les exigences minimales varient selon le système d'exploitation. En général, pour Windows, il faut au moins 2 Go de RAM, 1 Go d'espace disque libre et un processeur 2 GHz. Pour macOS et Linux, les exigences sont similaires. Consultez la section 3.1.1 du manuel pour les détails complets par système d'exploitation.

**Q: Comment déployer Cortex XDR dans un environnement avec des restrictions réseau strictes ?**

R: Dans les environnements avec des restrictions réseau, vous pouvez :
1. Configurer des exceptions précises dans les pare-feux pour les domaines et ports requis par Cortex XDR
2. Utiliser un proxy pour contrôler et filtrer les communications
3. Configurer l'agent pour fonctionner en mode hors ligne avec synchronisation périodique
4. Déployer un broker de communication local dans une zone démilitarisée (DMZ)

**Q: Peut-on personnaliser le package d'installation pour un déploiement silencieux ?**

R: Oui, Cortex XDR permet de créer des packages d'installation personnalisés avec des paramètres préconfigurés pour un déploiement silencieux. Dans la console, naviguez vers "Endpoints" > "Déploiement", sélectionnez le système d'exploitation cible, puis configurez les options de déploiement silencieux, incluant le tenant ID, le token d'installation et d'autres paramètres spécifiques.

**Q: Comment gérer les conflits avec d'autres solutions de sécurité pendant le déploiement ?**

R: Pour éviter les conflits :
1. Identifiez toutes les solutions de sécurité existantes avant le déploiement
2. Désinstallez les solutions antivirus incompatibles avant d'installer Cortex XDR
3. Configurez des exclusions mutuelles entre Cortex XDR et les autres outils de sécurité maintenus
4. Déployez d'abord sur un groupe pilote pour identifier et résoudre les problèmes potentiels
5. Planifiez un déploiement progressif avec des périodes de stabilisation

### Configuration et utilisation

**Q: Comment réduire les faux positifs dans Cortex XDR ?**

R: Pour réduire les faux positifs :
1. Commencez avec des politiques en mode surveillance pour établir une base de référence
2. Créez des exclusions spécifiques pour les applications légitimes générant des faux positifs
3. Ajustez progressivement la sensibilité des règles de détection
4. Utilisez des exclusions basées sur les certificats pour les applications d'entreprise internes
5. Documentez et analysez régulièrement les faux positifs pour identifier des modèles
6. Mettez à jour régulièrement l'agent et les politiques

**Q: Comment configurer Cortex XDR pour respecter les réglementations de confidentialité comme le RGPD ?**

R: Pour assurer la conformité avec le RGPD et autres réglementations :
1. Configurez les paramètres de collecte de données pour limiter les informations personnelles
2. Définissez des politiques de rétention des données appropriées
3. Mettez en place des contrôles d'accès stricts basés sur les rôles
4. Activez la journalisation complète des audits pour toutes les actions administratives
5. Configurez le chiffrement des données sensibles
6. Documentez toutes les mesures de protection des données dans votre registre de traitement

**Q: Comment intégrer Cortex XDR avec notre solution SIEM existante ?**

R: Cortex XDR offre plusieurs méthodes d'intégration avec les SIEM :
1. API REST pour l'extraction programmée des données
2. Webhooks pour les notifications en temps réel
3. Intégration Syslog pour la transmission des événements
4. Connecteurs spécifiques pour les principales solutions SIEM (Splunk, QRadar, etc.)
La section 4.4.1 du manuel détaille les étapes spécifiques pour chaque type d'intégration.

**Q: Quelle est la meilleure façon d'organiser les groupes d'endpoints ?**

R: Une stratégie efficace d'organisation des groupes d'endpoints comprend :
1. Création d'une hiérarchie logique (par région, fonction, département, criticité)
2. Utilisation de groupes dynamiques basés sur des critères comme le système d'exploitation, l'adresse IP ou les tags
3. Séparation des serveurs et des postes de travail
4. Création de groupes spécifiques pour les systèmes critiques ou sensibles
5. Alignement des groupes avec la structure organisationnelle ou les unités d'affaires

### Dépannage et maintenance

**Q: Que faire si un agent Cortex XDR cause des problèmes de performance ?**

R: Si vous constatez des problèmes de performance :
1. Vérifiez la version de l'agent et mettez-le à jour si nécessaire
2. Ajustez les paramètres de scan pour réduire l'impact (planification, priorité CPU)
3. Configurez des exclusions pour les applications ou dossiers sensibles aux performances
4. Collectez les journaux de diagnostic de l'agent pour analyse
5. Vérifiez les conflits potentiels avec d'autres logiciels de sécurité
6. Contactez le support technique de Palo Alto Networks si le problème persiste

**Q: Comment résoudre les problèmes de connectivité des agents ?**

R: Pour résoudre les problèmes de connectivité :
1. Vérifiez que l'endpoint a accès à Internet
2. Confirmez que les pare-feux autorisent les communications sur le port 443
3. Validez que les domaines requis sont accessibles (*.paloaltonetworks.com)
4. Vérifiez la configuration proxy si applicable
5. Redémarrez le service de l'agent
6. Consultez les journaux de l'agent pour identifier les erreurs spécifiques
7. Réinstallez l'agent si nécessaire

**Q: Comment mettre à jour les agents Cortex XDR à grande échelle ?**

R: Pour les mises à jour à grande échelle :
1. Configurez les mises à jour automatiques dans la console
2. Utilisez des groupes de déploiement pour échelonner les mises à jour
3. Planifiez les mises à jour pendant les fenêtres de maintenance
4. Testez d'abord sur un groupe pilote
5. Surveillez le statut des mises à jour dans la console
6. Préparez une procédure de rollback en cas de problème
7. Utilisez des outils de déploiement d'entreprise (SCCM, Jamf, etc.) pour les environnements complexes

**Q: Comment diagnostiquer un incident non détecté par Cortex XDR ?**

R: Si vous suspectez qu'un incident n'a pas été détecté :
1. Utilisez les requêtes XQL pour rechercher des indicateurs spécifiques
2. Vérifiez que l'agent était actif et à jour sur les systèmes concernés
3. Examinez les politiques appliquées pour identifier d'éventuelles lacunes
4. Collectez les journaux de diagnostic des agents concernés
5. Vérifiez si des exclusions auraient pu empêcher la détection
6. Utilisez les outils de threat hunting pour une recherche approfondie
7. Soumettez les échantillons suspects à WildFire pour analyse

### Questions avancées

**Q: Comment Cortex XDR protège-t-il contre les attaques sans fichier (fileless) ?**

R: Cortex XDR utilise plusieurs mécanismes pour détecter les attaques sans fichier :
1. Surveillance de la mémoire pour détecter les injections de code
2. Analyse comportementale pour identifier les séquences d'actions suspectes
3. Détection des scripts malveillants (PowerShell, WMI, etc.)
4. Surveillance des techniques de persistance sans fichier
5. Analyse des chaînes de processus pour identifier les comportements anormaux
6. Protection contre l'exploitation des vulnérabilités en mémoire

**Q: Comment configurer Cortex XDR pour les environnements hautement sécurisés ou isolés ?**

R: Pour les environnements hautement sécurisés :
1. Déployez un broker de communication local pour limiter les connexions directes à Internet
2. Configurez des politiques strictes en mode liste blanche (autorisation)
3. Mettez en place une authentification multifacteur pour tous les accès à la console
4. Utilisez des clés API avec privilèges minimaux pour les intégrations
5. Configurez une journalisation complète et exportez les logs vers un système SIEM sécurisé
6. Mettez en œuvre une ségrégation des rôles administratifs
7. Établissez des procédures de mise à jour contrôlées et validées

**Q: Comment utiliser Cortex XDR pour la chasse aux menaces (threat hunting) avancée ?**

R: Pour la chasse aux menaces avancée :
1. Maîtrisez le langage de requête XQL pour des recherches personnalisées
2. Créez des requêtes basées sur les techniques MITRE ATT&CK
3. Utilisez les visualisations de processus pour identifier des chaînes d'exécution suspectes
4. Développez des hypothèses basées sur les TTPs des attaquants connus
5. Créez et partagez des playbooks de chasse aux menaces
6. Combinez les données Cortex XDR avec des sources de threat intelligence externes
7. Documentez et transformez les découvertes en détections automatisées

**Q: Comment mesurer le ROI de Cortex XDR ?**

R: Pour mesurer le retour sur investissement :
1. Établissez une base de référence avant le déploiement (nombre d'incidents, MTTD, MTTR)
2. Suivez les métriques clés après le déploiement
3. Calculez les économies liées à la réduction du temps d'investigation
4. Évaluez la réduction des incidents réussis et leur impact financier
5. Mesurez la réduction des ressources humaines nécessaires pour la gestion de la sécurité
6. Quantifiez les avantages de la consolidation des outils de sécurité
7. Considérez les bénéfices intangibles comme l'amélioration de la visibilité et la réduction des risques

## 10.3. Checklist de configuration

Cette checklist vous aidera à vérifier que vous avez correctement configuré et optimisé votre déploiement Cortex XDR.

### Préparation et planification

- [ ] Inventaire complet des endpoints à protéger réalisé
- [ ] Architecture de déploiement documentée
- [ ] Exigences réseau validées (ports, domaines autorisés)
- [ ] Stratégie de déploiement par phases définie
- [ ] Groupe pilote identifié
- [ ] Objectifs et métriques de succès établis
- [ ] Plan de communication aux utilisateurs préparé
- [ ] Procédures de rollback documentées

### Installation de la console

- [ ] Compte Cortex activé
- [ ] Administrateurs principaux créés
- [ ] Authentification multifacteur activée
- [ ] Paramètres régionaux configurés
- [ ] Notifications système configurées
- [ ] Rôles personnalisés créés selon les besoins
- [ ] Paramètres de session sécurisés configurés
- [ ] Journalisation d'audit activée

### Déploiement des agents

- [ ] Packages d'installation personnalisés créés
- [ ] Déploiement pilote réalisé et validé
- [ ] Problèmes identifiés lors du pilote résolus
- [ ] Plan de déploiement global ajusté si nécessaire
- [ ] Déploiement par vagues exécuté
- [ ] Vérification post-déploiement effectuée
- [ ] Endpoints problématiques identifiés et résolus
- [ ] Couverture des agents validée (>95% recommandé)

### Configuration des groupes et politiques

- [ ] Structure de groupes d'endpoints définie
- [ ] Endpoints assignés aux groupes appropriés
- [ ] Politiques de base créées pour chaque type d'environnement
- [ ] Politiques testées en mode surveillance
- [ ] Faux positifs identifiés et exclusions créées
- [ ] Transition progressive vers le mode blocage
- [ ] Politiques spécifiques pour systèmes critiques configurées
- [ ] Ordre de priorité des politiques vérifié

### Configuration des notifications et alertes

- [ ] Canaux de notification configurés (email, webhook, etc.)
- [ ] Règles de notification créées par sévérité
- [ ] Destinataires appropriés définis pour chaque type d'alerte
- [ ] Notifications testées pour validation
- [ ] Seuils d'alerte ajustés pour éviter la fatigue d'alerte
- [ ] Formats de notification personnalisés si nécessaire
- [ ] Planification des rapports récurrents configurée

### Intégrations

- [ ] Intégration SIEM configurée si applicable
- [ ] Intégration SOAR configurée si applicable
- [ ] Connecteurs cloud configurés (AWS, Azure, GCP)
- [ ] Intégration avec les solutions de gestion des vulnérabilités
- [ ] Intégration avec les sources de threat intelligence
- [ ] Intégrations testées et validées
- [ ] Documentation des intégrations mise à jour

### Optimisation des performances

- [ ] Scans planifiés pendant les périodes d'inactivité
- [ ] Exclusions de performance configurées si nécessaire
- [ ] Impact sur les endpoints mesuré et optimisé
- [ ] Paramètres de collecte de données ajustés
- [ ] Rétention des données configurée selon les besoins
- [ ] Performances de la console surveillées

### Opérations et maintenance

- [ ] Procédures de surveillance quotidienne documentées
- [ ] Processus de gestion des incidents établi
- [ ] Plan de mise à jour des agents défini
- [ ] Sauvegarde des configurations critiques réalisée
- [ ] Procédures de récupération documentées
- [ ] Formation des équipes opérationnelles complétée
- [ ] Processus d'amélioration continue établi

### Validation de la sécurité

- [ ] Test de détection de malware effectué (fichier EICAR)
- [ ] Test de détection d'exploit réalisé
- [ ] Test d'isolation d'endpoint validé
- [ ] Test de réponse aux incidents effectué
- [ ] Vérification des contrôles d'accès à la console
- [ ] Audit des configurations de sécurité réalisé
- [ ] Documentation de conformité mise à jour

### Reporting et métriques

- [ ] Tableaux de bord personnalisés créés
- [ ] Rapports récurrents configurés
- [ ] KPIs de sécurité définis et suivis
- [ ] Processus de revue des métriques établi
- [ ] Rapports exécutifs préparés
- [ ] Mécanisme de feedback pour amélioration continue mis en place
