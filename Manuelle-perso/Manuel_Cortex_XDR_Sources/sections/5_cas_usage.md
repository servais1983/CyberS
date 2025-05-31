# 5. Cas d'usage concrets

## 5.1. Détection de malware

La détection de malware est l'une des fonctionnalités fondamentales de Cortex XDR. Grâce à ses capacités avancées, la plateforme peut identifier et neutraliser une grande variété de logiciels malveillants avant qu'ils ne causent des dommages.

### 5.1.1. Mécanismes de détection

Cortex XDR utilise une approche multicouche pour la détection des malwares, combinant plusieurs technologies complémentaires :

**Analyse statique**

L'analyse statique examine les fichiers sans les exécuter, en recherchant des caractéristiques suspectes :

1. **Signatures et hachages** : Comparaison avec une base de données de signatures de malwares connus
2. **Analyse heuristique** : Identification de modèles et structures suspects dans le code
3. **Machine learning statique** : Utilisation d'algorithmes entraînés pour identifier les caractéristiques malveillantes
4. **Analyse de réputation** : Vérification de la réputation du fichier dans les bases de données globales

**Analyse dynamique**

L'analyse dynamique observe le comportement des fichiers lors de leur exécution dans un environnement sécurisé :

1. **Sandboxing local** : Exécution du fichier dans un environnement isolé sur l'endpoint
2. **Intégration WildFire** : Soumission automatique des fichiers suspects au service cloud d'analyse WildFire
3. **Surveillance comportementale** : Observation des actions effectuées par le programme lors de son exécution
4. **Détection d'exploitation** : Identification des tentatives d'exploitation de vulnérabilités

**Analyse en temps réel**

La surveillance continue des activités système permet de détecter les menaces en temps réel :

1. **Surveillance des processus** : Suivi des processus en cours d'exécution et de leurs actions
2. **Surveillance des modifications de fichiers** : Détection des modifications suspectes du système de fichiers
3. **Surveillance du registre** : Identification des modifications suspectes du registre Windows
4. **Surveillance réseau** : Détection des communications suspectes avec des serveurs de commande et contrôle

### 5.1.2. Exemple de détection de ransomware

Les ransomwares représentent une menace particulièrement grave pour les organisations. Voici comment Cortex XDR détecte et neutralise une attaque de ransomware typique :

**Scénario : Attaque de ransomware via un document Office malveillant**

1. **Point d'entrée**
   - Un employé reçoit un email de phishing contenant une pièce jointe Excel
   - Le document contient une macro malveillante

2. **Détection initiale**
   - Cortex XDR analyse le document à l'ouverture
   - L'analyse statique identifie des macros suspectes
   - Le document est soumis à WildFire pour analyse approfondie

3. **Exécution de la macro**
   - Si l'utilisateur active les macros, Cortex XDR surveille l'activité
   - Détection de l'exécution de PowerShell avec des paramètres de contournement
   - Identification du téléchargement de contenu depuis une URL malveillante

4. **Blocage de l'infection**
   - Cortex XDR bloque l'exécution du script PowerShell malveillant
   - La connexion au serveur de commande et contrôle est interrompue
   - Une alerte de haute priorité est générée dans la console

5. **Réponse automatisée**
   - Isolation réseau automatique de l'endpoint affecté
   - Collecte des artefacts pour analyse forensique
   - Analyse des autres systèmes pour détecter des signes de compromission similaires

**Capture d'écran : Alerte de détection de ransomware dans la console Cortex XDR**

```
[ALERTE CRITIQUE] Tentative de ransomware détectée
Endpoint: WORKSTATION-FINANCE3
Utilisateur: jdupont
Processus: excel.exe (PID 4256)
Processus enfant: powershell.exe (PID 5823)
Action: Exécution de commande PowerShell encodée en Base64
Indicateurs: 
- Téléchargement de fichier exécutable
- Tentative de modification massive de fichiers
- Communication avec IOC connu (185.212.x.x)
Action prise: Processus terminé, endpoint isolé
```

### 5.1.3. Détection de malware sans fichier (fileless)

Les malwares sans fichier (fileless) représentent un défi particulier car ils n'écrivent pas de fichiers sur le disque, rendant inefficaces les méthodes traditionnelles de détection basées sur les signatures.

**Techniques de détection des malwares sans fichier**

Cortex XDR utilise plusieurs approches pour détecter ces menaces avancées :

1. **Surveillance de la mémoire**
   - Analyse des injections de code dans les processus légitimes
   - Détection des techniques d'allocation mémoire suspectes
   - Identification des shellcodes et autres charges utiles malveillantes en mémoire

2. **Surveillance des scripts**
   - Analyse du contenu des scripts PowerShell, VBScript, etc.
   - Détection des techniques d'obfuscation courantes
   - Identification des comportements suspects dans les scripts

3. **Détection des techniques de persistance**
   - Surveillance des modifications du registre pour la persistance
   - Détection des tâches planifiées suspectes
   - Identification des DLL hijacking et autres techniques de persistance avancées

**Exemple de scénario : Attaque sans fichier via PowerShell**

1. **Infection initiale**
   - L'utilisateur clique sur un lien malveillant dans un email
   - Le navigateur télécharge et exécute un script JavaScript malveillant

2. **Exécution de la charge utile**
   - Le script JavaScript lance PowerShell avec des paramètres encodés
   - PowerShell charge un shellcode directement en mémoire
   - Aucun fichier malveillant n'est écrit sur le disque

3. **Détection par Cortex XDR**
   - Identification de la ligne de commande PowerShell suspecte
   - Détection de l'injection de code en mémoire
   - Reconnaissance des modèles de communication avec le serveur C2

4. **Réponse**
   - Terminaison des processus malveillants
   - Capture de la mémoire pour analyse forensique
   - Génération d'une alerte détaillée avec la chaîne d'attaque complète

**Tableau des indicateurs de compromission pour les malwares sans fichier**

| Indicateur | Description | Niveau de risque |
|------------|-------------|-----------------|
| PowerShell avec encodage Base64 | Commande PowerShell contenant des paramètres encodés en Base64 | Élevé |
| Injection de code dans des processus légitimes | Processus légitimes effectuant des actions inhabituelles | Critique |
| Appels API suspects | Séquences d'appels API associées à des techniques d'attaque | Élevé |
| Connexions réseau anormales | Communications avec des domaines générés algorithmiquement ou des IP suspectes | Moyen à élevé |
| Exécution à partir de répertoires temporaires | Lancement de processus depuis des emplacements temporaires | Moyen |

## 5.2. Investigation post-infection

Lorsqu'une infection est détectée, Cortex XDR fournit des outils puissants pour mener une investigation approfondie, comprendre l'étendue de la compromission et identifier les actions nécessaires pour y remédier.

### 5.2.1. Méthodologie d'investigation

Cortex XDR facilite une approche structurée pour l'investigation des incidents :

**Phase 1 : Triage initial**

1. **Évaluation de l'alerte**
   - Examen des détails de l'alerte dans la console Cortex XDR
   - Vérification de la sévérité et du type de menace
   - Identification de l'endpoint et de l'utilisateur affectés

2. **Collecte d'informations préliminaires**
   - Consultation du résumé de l'incident
   - Examen des indicateurs de compromission (IOC)
   - Vérification des actions automatiques déjà prises

**Phase 2 : Investigation approfondie**

1. **Analyse de la chronologie**
   - Examen de la séquence des événements
   - Identification du patient zéro et du vecteur d'infection
   - Cartographie de la propagation de l'attaque

2. **Analyse des artefacts**
   - Examen des fichiers et processus impliqués
   - Analyse des modifications du système
   - Étude des connexions réseau établies

3. **Recherche d'activités connexes**
   - Utilisation de requêtes XQL pour identifier des activités similaires
   - Recherche d'autres systèmes potentiellement compromis
   - Identification d'autres indicateurs de compromission

**Phase 3 : Détermination de l'impact**

1. **Évaluation de l'étendue**
   - Identification de tous les systèmes affectés
   - Détermination des données potentiellement compromises
   - Évaluation de l'impact sur les opérations

2. **Analyse des risques**
   - Évaluation des risques résiduels
   - Identification des vulnérabilités exploitées
   - Détermination des mesures correctives nécessaires

### 5.2.2. Analyse de la chaîne d'attaque

Cortex XDR excelle dans la visualisation et l'analyse de la chaîne d'attaque complète, permettant aux analystes de comprendre précisément comment une attaque s'est déroulée.

**Composants de la visualisation de la chaîne d'attaque**

1. **Chronologie des événements**
   - Représentation visuelle de la séquence temporelle des événements
   - Mise en évidence des actions clés de l'attaquant
   - Identification des techniques MITRE ATT&CK utilisées

2. **Graphe de processus**
   - Visualisation des relations parent-enfant entre les processus
   - Identification des processus légitimes détournés
   - Mise en évidence des comportements anormaux

3. **Cartographie des connexions réseau**
   - Visualisation des communications internes et externes
   - Identification des connexions vers des serveurs de commande et contrôle
   - Détection des mouvements latéraux dans le réseau

**Exemple d'analyse de chaîne d'attaque**

```
1. [10:15:23] Email reçu avec pièce jointe "Facture_123.xlsx"
2. [10:17:45] Utilisateur ouvre le document Excel
3. [10:17:52] Macros activées dans le document
4. [10:17:55] Excel lance cmd.exe avec paramètres cachés
5. [10:17:58] cmd.exe exécute PowerShell avec commande encodée
6. [10:18:03] PowerShell télécharge payload.dll depuis 185.212.x.x
7. [10:18:10] PowerShell injecte code dans explorer.exe
8. [10:18:15] explorer.exe établit connexion persistante avec 185.212.x.x
9. [10:25:37] explorer.exe commence scan du réseau interne (ports 445, 139)
10. [10:32:14] Tentative d'accès à des partages réseau détectée
```

### 5.2.3. Exemple d'investigation complète

Voici un exemple détaillé d'investigation d'incident avec Cortex XDR :

**Scénario : Détection d'une attaque de type Advanced Persistent Threat (APT)**

1. **Alerte initiale**
   - Cortex XDR génère une alerte de sévérité élevée pour un comportement suspect
   - L'alerte indique une possible exécution de code à distance sur un serveur
   - L'analyste ouvre l'incident dans la console Cortex XDR

2. **Triage et évaluation initiale**
   - L'analyste examine les détails de l'alerte :
     - Serveur affecté : SRV-WEB-03 (serveur web de production)
     - Processus impliqué : w3wp.exe (processus IIS)
     - Comportement suspect : chargement de DLL inhabituelle et connexions sortantes non standard
   - Sévérité évaluée comme élevée en raison de la criticité du serveur

3. **Investigation approfondie**
   - L'analyste utilise la visualisation de la chaîne de processus pour examiner l'activité :
     - Identification d'une exploitation de vulnérabilité dans l'application web
     - Détection de l'exécution d'un webshell via le processus IIS
     - Découverte de tentatives d'élévation de privilèges
   - Analyse des connexions réseau :
     - Identification de communications avec une adresse IP connue comme malveillante
     - Détection de transferts de données inhabituels
   - Recherche d'activités similaires sur d'autres systèmes :
     - Utilisation de requêtes XQL pour identifier des modèles similaires
     - Découverte de deux autres serveurs présentant des signes de compromission

4. **Collecte de preuves**
   - Capture de la mémoire des systèmes affectés
   - Extraction des fichiers malveillants pour analyse
   - Collecte des journaux système et réseau pertinents
   - Préservation des artefacts pour analyse forensique

5. **Analyse de l'impact**
   - Détermination de l'étendue de la compromission :
     - Trois serveurs web compromis
     - Accès potentiel à la base de données clients
   - Évaluation des données potentiellement exfiltrées
   - Identification des systèmes critiques potentiellement affectés

6. **Actions de remédiation**
   - Isolation réseau des systèmes compromis
   - Suppression des fichiers malveillants et webshells
   - Application des correctifs de sécurité pour la vulnérabilité exploitée
   - Réinitialisation des identifiants compromis
   - Renforcement des règles de pare-feu

7. **Documentation et rapport**
   - Création d'un rapport détaillé de l'incident
   - Documentation des IOC pour surveillance future
   - Mise à jour des règles de détection pour prévenir des incidents similaires
   - Partage des informations avec les équipes concernées

**Outils Cortex XDR utilisés pendant l'investigation**

| Outil | Utilisation dans l'investigation |
|-------|----------------------------------|
| Visualisation de la chaîne d'attaque | Cartographie de la progression de l'attaquant à travers les systèmes |
| Explorateur de processus | Analyse détaillée des processus malveillants et de leurs actions |
| Requêtes XQL | Recherche d'activités similaires sur d'autres systèmes |
| Collecte de preuves | Extraction des artefacts pour analyse approfondie |
| Timeline d'événements | Reconstruction chronologique de l'incident |
| Intégration MITRE ATT&CK | Identification des tactiques et techniques utilisées par l'attaquant |

## 5.3. Réponse automatique aux incidents

La capacité de Cortex XDR à répondre automatiquement aux incidents de sécurité permet de contenir rapidement les menaces, réduisant ainsi leur impact potentiel sur l'organisation.

### 5.3.1. Configuration des réponses automatiques

Cortex XDR permet de configurer des réponses automatiques basées sur des déclencheurs spécifiques :

**Création d'une règle de réponse automatique**

1. Dans la console Cortex XDR, naviguez vers "Réponse" > "Règles de réponse automatique"
2. Cliquez sur "Ajouter une règle"
3. Configurez les paramètres suivants :
   - Nom et description de la règle
   - Conditions de déclenchement (type d'alerte, sévérité, etc.)
   - Actions à exécuter automatiquement
   - Portée d'application (groupes d'endpoints concernés)
4. Activez la règle et définissez sa priorité

**Types de déclencheurs disponibles**

| Déclencheur | Description | Exemple |
|-------------|-------------|---------|
| Type d'alerte | Basé sur la catégorie d'alerte | Détection de malware, comportement suspect |
| Sévérité | Basé sur le niveau de gravité | Critique, élevé, moyen, faible |
| Indicateurs | Basé sur des IOC spécifiques | Hachage de fichier, domaine, adresse IP |
| Source | Basé sur l'origine de la détection | Endpoint, réseau, cloud |
| Utilisateur | Basé sur l'utilisateur affecté | Comptes privilégiés, départements spécifiques |
| Groupe d'endpoints | Basé sur le groupe d'endpoints | Serveurs critiques, postes de direction |

**Actions automatiques configurables**

| Action | Description | Cas d'usage |
|--------|-------------|------------|
| Isoler l'endpoint | Déconnecte l'endpoint du réseau | Contenir une infection active |
| Terminer le processus | Arrête un processus malveillant | Stopper l'exécution d'un malware |
| Bloquer le hachage | Empêche l'exécution d'un fichier spécifique | Prévenir la propagation d'un malware |
| Bloquer l'adresse IP/domaine | Bloque les communications avec une destination | Couper la communication avec un C2 |
| Collecter des preuves | Extrait des artefacts pour analyse | Préserver les preuves pour investigation |
| Exécuter un script | Lance un script personnalisé | Actions de remédiation spécifiques |
| Créer un ticket | Génère un ticket dans un système externe | Intégration avec les workflows IT |

### 5.3.2. Isolation d'endpoint

L'isolation d'endpoint est une action de réponse puissante qui permet de contenir rapidement une menace en déconnectant un système compromis du réseau tout en maintenant la connexion avec la console Cortex XDR.

**Fonctionnement de l'isolation d'endpoint**

1. **Activation de l'isolation**
   - Déclenchée manuellement par un analyste
   - Exécutée automatiquement par une règle de réponse
   - Initiée via une intégration SOAR

2. **Effets de l'isolation**
   - Blocage de toutes les communications réseau entrantes et sortantes
   - Maintien de la connexion avec la console Cortex XDR
   - Préservation de la capacité à gérer et investiguer l'endpoint

3. **Types d'isolation disponibles**
   - **Isolation complète** : Bloque toutes les communications sauf avec la console Cortex XDR
   - **Isolation sélective** : Permet des communications avec des destinations spécifiques (ex: outils de remédiation)

**Exemple de scénario d'isolation**

```
1. Cortex XDR détecte une activité de ransomware sur un poste de travail
2. Une règle de réponse automatique déclenche l'isolation de l'endpoint
3. L'endpoint est immédiatement isolé du réseau
4. L'analyste SOC reçoit une notification de l'incident
5. L'analyste peut se connecter à l'endpoint isolé pour investigation
6. Une fois la menace neutralisée, l'isolation est levée manuellement
```

**Bonnes pratiques pour l'isolation d'endpoint**

- Définir clairement les scénarios justifiant une isolation automatique
- Tester régulièrement la fonctionnalité d'isolation dans un environnement contrôlé
- Établir des procédures pour la levée de l'isolation
- Communiquer avec les utilisateurs affectés pour éviter des tentatives de contournement
- Documenter chaque cas d'isolation pour analyse post-incident

### 5.3.3. Blocage de processus malveillants

Le blocage de processus permet d'arrêter immédiatement l'exécution de logiciels malveillants, limitant ainsi les dommages potentiels.

**Méthodes de blocage de processus**

1. **Terminaison de processus**
   - Arrêt immédiat d'un processus en cours d'exécution
   - Peut être déclenché automatiquement ou manuellement
   - Efficace pour stopper une menace active

2. **Blocage par hachage**
   - Empêche l'exécution future d'un fichier basé sur son hachage
   - Appliqué à l'échelle de l'organisation
   - Persistant jusqu'à sa révocation

3. **Blocage comportemental**
   - Bloque les processus présentant certains comportements
   - Basé sur des modèles d'activité plutôt que sur des signatures
   - Efficace contre les menaces inconnues ou modifiées

**Exemple de workflow de blocage de processus**

1. **Détection**
   - Cortex XDR identifie un processus présentant un comportement malveillant
   - L'alerte est générée avec les détails du processus

2. **Analyse automatique**
   - Le système évalue le risque associé au processus
   - Les dépendances et l'impact potentiel sont analysés

3. **Action de blocage**
   - Si le risque est élevé, le processus est automatiquement terminé
   - Le hachage du fichier exécutable est ajouté à la liste de blocage
   - Une alerte de remédiation est générée

4. **Vérification**
   - Le système confirme que le processus a été terminé
   - Des vérifications sont effectuées pour détecter des processus enfants potentiellement malveillants
   - L'efficacité du blocage est évaluée

**Considérations pour le blocage de processus**

| Considération | Description | Recommandation |
|---------------|-------------|----------------|
| Processus système | Blocage de processus système légitimes | Exclure les processus système critiques des règles de blocage automatique |
| Faux positifs | Blocage de processus légitimes | Commencer avec des règles conservatrices et affiner progressivement |
| Processus persistants | Malware qui se relance automatiquement | Combiner le blocage de processus avec d'autres actions (isolation, blocage de hachage) |
| Applications critiques | Impact sur les opérations métier | Tester les règles de blocage dans un environnement non-production |

## 5.4. Gestion des faux positifs

La gestion efficace des faux positifs est essentielle pour maintenir l'efficacité de Cortex XDR tout en minimisant les interruptions des activités légitimes.

### 5.4.1. Identification des faux positifs

Un faux positif se produit lorsque Cortex XDR identifie incorrectement une activité légitime comme malveillante. Voici comment les identifier correctement :

**Caractéristiques des faux positifs courants**

1. **Modèles récurrents**
   - Alertes similaires générées régulièrement
   - Déclenchées par les mêmes applications ou processus
   - Surviennent à des moments prévisibles (ex: après des mises à jour)

2. **Contexte d'entreprise**
   - Alertes liées à des outils internes légitimes
   - Activités associées à des processus métier spécifiques
   - Comportements normaux dans votre environnement particulier

3. **Validation technique**
   - Analyse approfondie ne révélant aucun comportement réellement malveillant
   - Confirmation que le processus ou fichier provient d'une source légitime
   - Vérification que l'activité fait partie du fonctionnement normal du système

**Processus d'investigation des faux positifs**

1. **Examen initial**
   - Analyser les détails de l'alerte dans la console
   - Vérifier le contexte de l'activité détectée
   - Consulter l'historique des alertes similaires

2. **Analyse approfondie**
   - Examiner le processus et ses actions en détail
   - Vérifier la source et la signature du fichier
   - Analyser les connexions réseau associées

3. **Validation**
   - Confirmer avec les propriétaires d'applications si l'activité est attendue
   - Vérifier si l'activité coïncide avec des changements ou mises à jour
   - Comparer avec des comportements connus dans l'environnement

4. **Documentation**
   - Documenter le faux positif identifié
   - Noter les caractéristiques distinctives pour référence future
   - Enregistrer la justification de la classification comme faux positif

### 5.4.2. Ajustement des règles pour réduire les faux positifs

Une fois les faux positifs identifiés, Cortex XDR offre plusieurs mécanismes pour affiner les règles de détection et réduire leur occurrence.

**Création d'exclusions**

1. **Exclusions basées sur les fichiers**
   - Naviguez vers "Politiques" > "Exclusions"
   - Cliquez sur "Ajouter une exclusion"
   - Spécifiez le hachage du fichier ou le chemin d'accès
   - Définissez la portée de l'exclusion (groupes d'endpoints)

2. **Exclusions basées sur les processus**
   - Créez des exclusions pour des processus légitimes spécifiques
   - Définissez des conditions précises (chemin, arguments, processus parent)
   - Limitez l'exclusion au minimum nécessaire pour la sécurité

3. **Exclusions basées sur les certificats**
   - Créez des exclusions pour les fichiers signés par des certificats approuvés
   - Particulièrement utile pour les applications d'entreprise internes

**Ajustement des politiques de détection**

1. **Modification de la sensibilité**
   - Ajustez le niveau de sensibilité des règles générant des faux positifs
   - Trouvez un équilibre entre détection des menaces et réduction des faux positifs

2. **Personnalisation des règles**
   - Modifiez les règles existantes pour tenir compte des spécificités de votre environnement
   - Ajoutez des conditions supplémentaires pour affiner la détection

3. **Création de règles personnalisées**
   - Développez des règles adaptées à votre environnement
   - Intégrez la connaissance de vos applications et processus légitimes

**Bonnes pratiques pour la gestion des exclusions**

| Pratique | Description | Exemple |
|----------|-------------|---------|
| Spécificité | Créer des exclusions aussi spécifiques que possible | Exclure un chemin précis plutôt qu'un répertoire entier |
| Documentation | Documenter chaque exclusion avec sa justification | "Exclusion pour l'outil de déploiement interne validé par l'équipe sécurité" |
| Révision périodique | Revoir régulièrement les exclusions pour confirmer leur pertinence | Audit trimestriel des exclusions |
| Approche progressive | Commencer par des exclusions limitées et élargir si nécessaire | Exclure d'abord un comportement spécifique avant d'exclure l'application entière |
| Test | Tester les exclusions avant déploiement en production | Valider dans un environnement de test que l'exclusion fonctionne comme prévu |

**Processus de gestion des faux positifs**

```
1. Alerte identifiée comme potentiel faux positif
2. Investigation pour confirmer qu'il s'agit bien d'un faux positif
3. Documentation du faux positif avec justification
4. Création d'une exclusion appropriée
5. Test de l'exclusion dans un environnement contrôlé
6. Déploiement de l'exclusion en production
7. Surveillance pour confirmer l'efficacité
8. Révision périodique de l'exclusion
```

**Métriques de suivi des faux positifs**

Pour évaluer l'efficacité de votre gestion des faux positifs, suivez ces métriques clés :

- Taux de faux positifs (pourcentage d'alertes qui sont des faux positifs)
- Temps consacré à l'investigation des faux positifs
- Nombre d'exclusions créées et leur spécificité
- Réduction du taux de faux positifs après ajustements
- Impact des exclusions sur la capacité de détection globale
