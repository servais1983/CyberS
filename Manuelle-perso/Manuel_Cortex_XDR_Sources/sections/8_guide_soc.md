# 8. Guide pratique pour les analystes SOC

## 8.1. Méthodologie de triage

Le triage efficace des alertes et incidents est essentiel pour optimiser le temps et les ressources des analystes SOC. Cortex XDR facilite ce processus grâce à ses fonctionnalités avancées de priorisation et d'analyse.

### Processus de triage structuré

Un processus de triage structuré permet d'aborder méthodiquement le flux constant d'alertes :

**Étape 1 : Évaluation initiale**

1. **Vérification de la sévérité**
   - Examinez la sévérité attribuée automatiquement
   - Vérifiez si elle correspond à l'impact potentiel réel
   - Ajustez si nécessaire en fonction du contexte

2. **Analyse du contexte**
   - Identifiez les systèmes et utilisateurs affectés
   - Évaluez la criticité des actifs concernés
   - Vérifiez s'il existe des incidents similaires récents

3. **Validation de l'alerte**
   - Déterminez s'il s'agit d'un vrai positif ou d'un faux positif
   - Vérifiez les indicateurs de compromission
   - Consultez les informations de réputation disponibles

**Étape 2 : Priorisation**

1. **Matrice de priorisation**

| Sévérité | Criticité de l'actif | Priorité résultante |
|----------|----------------------|---------------------|
| Critique | Critique             | P0 (immédiate)      |
| Critique | Standard             | P1 (haute)          |
| Élevée   | Critique             | P1 (haute)          |
| Élevée   | Standard             | P2 (moyenne)        |
| Moyenne  | Critique             | P2 (moyenne)        |
| Moyenne  | Standard             | P3 (basse)          |
| Faible   | Critique             | P3 (basse)          |
| Faible   | Standard             | P4 (planifiée)      |

2. **Facteurs d'ajustement**
   - Présence d'activité malveillante confirmée (+1 niveau)
   - Détection dans un environnement sensible (+1 niveau)
   - Alerte faisant partie d'une campagne connue (+1 niveau)
   - Alerte isolée sans contexte supplémentaire (-1 niveau)
   - Modèle connu de faux positifs (-1 niveau)

**Étape 3 : Assignation**

1. **Critères d'assignation**
   - Expertise requise pour l'investigation
   - Charge de travail actuelle des analystes
   - Continuité des incidents liés
   - Escalade vers des équipes spécialisées si nécessaire

2. **Niveaux d'escalade**
   - Niveau 1 : Triage initial et résolution des incidents simples
   - Niveau 2 : Investigation approfondie et réponse
   - Niveau 3 : Expertise avancée et gestion des incidents complexes
   - CERT/CSIRT : Incidents majeurs nécessitant une coordination étendue

### Utilisation des outils de triage dans Cortex XDR

Cortex XDR offre plusieurs fonctionnalités pour faciliter le triage :

**Vue de triage des alertes**

1. Naviguez vers "Alertes" > "Triage"
2. Utilisez les filtres prédéfinis pour afficher les alertes par sévérité, type ou statut
3. Exploitez la vue groupée pour identifier les modèles récurrents
4. Utilisez les actions en lot pour traiter efficacement les alertes similaires

**Indicateurs visuels**

- Codes couleur par sévérité (rouge pour critique, orange pour élevé, etc.)
- Badges indiquant le statut de l'investigation
- Icônes représentant le type de menace
- Indicateurs de tendance (augmentation/diminution par rapport à la normale)

**Automatisation du triage**

1. **Règles de triage automatique**
   - Créez des règles pour catégoriser automatiquement certaines alertes
   - Définissez des critères basés sur les caractéristiques des alertes
   - Configurez des actions automatiques pour les cas récurrents

2. **Exemple de règle de triage automatique**
   ```
   SI type_alerte = "Connexion depuis un pays inhabituel"
   ET utilisateur IN liste_VIP
   ET pays NOT IN pays_approuvés
   ALORS
      sévérité = "Élevée"
      assigner_à = "Équipe_Identité"
      ajouter_tag = "Accès_Suspect_VIP"
   ```

### Bonnes pratiques de triage

Pour optimiser le processus de triage dans votre SOC :

1. **Documentation standardisée**
   - Utilisez des modèles de notes de triage
   - Documentez systématiquement les décisions prises
   - Maintenez un historique des actions de triage

2. **Amélioration continue**
   - Analysez régulièrement les métriques de triage
   - Identifiez les sources fréquentes de faux positifs
   - Affinez les règles de détection en fonction des résultats

3. **Rotation des rôles**
   - Alternez les responsabilités de triage entre analystes
   - Évitez la fatigue d'alerte par des rotations régulières
   - Partagez les connaissances sur les différents types d'alertes

4. **Métriques de performance**
   - Temps moyen de triage par alerte
   - Taux de faux positifs identifiés
   - Précision des décisions de triage
   - Délai entre détection et assignation

## 8.2. Chasse aux menaces (Threat Hunting)

La chasse aux menaces est une approche proactive qui consiste à rechercher activement des signes de compromission non détectés par les mécanismes automatisés. Cortex XDR fournit des outils puissants pour cette activité essentielle.

### 8.2.1. Techniques de threat hunting avec Cortex XDR

**Approches fondamentales de la chasse aux menaces**

1. **Chasse basée sur les hypothèses**
   - Formulation d'hypothèses basées sur les TTPs (Tactiques, Techniques et Procédures) connues
   - Recherche ciblée de preuves confirmant ou infirmant ces hypothèses
   - Itération et affinage des hypothèses en fonction des résultats

2. **Chasse basée sur les IOCs**
   - Utilisation d'indicateurs de compromission externes (rapports de threat intelligence)
   - Recherche rétrospective de ces indicateurs dans les données historiques
   - Validation de la présence ou absence des IOCs dans l'environnement

3. **Chasse basée sur les anomalies**
   - Identification de comportements s'écartant des profils normaux
   - Analyse des outliers statistiques dans les données
   - Investigation des activités inhabituelles même sans correspondance avec des menaces connues

**Outils de chasse dans Cortex XDR**

1. **Requêtes XQL avancées**
   - Création de requêtes personnalisées pour rechercher des comportements spécifiques
   - Utilisation de jointures et d'agrégations pour des analyses complexes
   - Sauvegarde et partage des requêtes efficaces

2. **Visualisations de données**
   - Utilisation des graphiques de processus pour identifier des chaînes d'exécution suspectes
   - Analyse des connexions réseau pour détecter des modèles anormaux
   - Visualisation temporelle pour identifier des corrélations d'événements

3. **Playbooks de chasse**
   - Création de workflows structurés pour des scénarios de chasse spécifiques
   - Automatisation partielle des étapes répétitives
   - Documentation systématique des résultats

### 8.2.2. Exemples de scénarios de chasse

Voici quelques scénarios de chasse aux menaces que vous pouvez mettre en œuvre avec Cortex XDR :

**Scénario 1 : Détection de persistance via WMI**

1. **Hypothèse** : Un attaquant utilise WMI pour établir la persistance
2. **Requête XQL** :
   ```
   dataset=xdr_data
   | filter action_type = "PROCESS_START"
   | filter process_name = "wmic.exe" or process_name = "powershell.exe"
   | filter command_line contains "subscription" or command_line contains "event" or command_line contains "consumer"
   | fields hostname, user_name, process_name, command_line, process_start_time
   | sort process_start_time desc
   ```
3. **Indicateurs de suspicion** :
   - Création d'abonnements WMI permanents
   - Utilisation de consommateurs d'événements inhabituels
   - Exécution depuis des emplacements non standard

**Scénario 2 : Recherche de mouvement latéral via Pass-the-Hash**

1. **Hypothèse** : Un attaquant utilise des techniques de Pass-the-Hash pour se déplacer latéralement
2. **Requête XQL** :
   ```
   dataset=xdr_data
   | filter action_type = "AUTHENTICATION"
   | filter auth_method = "NTLM"
   | stats count=count() by src_host, dst_host, user_name
   | sort count desc
   | filter count > 3
   ```
3. **Indicateurs de suspicion** :
   - Authentifications NTLM multiples depuis un même hôte vers plusieurs destinations
   - Authentifications en dehors des heures habituelles
   - Utilisation de comptes privilégiés pour des connexions inhabituelles

**Scénario 3 : Détection d'exfiltration de données**

1. **Hypothèse** : Un attaquant exfiltre des données via des canaux de communication inhabituels
2. **Requête XQL** :
   ```
   dataset=xdr_data
   | filter action_type = "NETWORK_CONNECTION"
   | filter (dst_port not in (80, 443, 53, 25, 587, 993, 995) or dst_ip_country != "FR")
   | stats sum(bytes_out) as total_bytes_out by hostname, process_name, dst_ip, dst_port
   | filter total_bytes_out > 10000000
   | sort total_bytes_out desc
   ```
3. **Indicateurs de suspicion** :
   - Volumes de données importants vers des destinations inhabituelles
   - Utilisation de ports non standard
   - Transferts vers des pays où l'organisation n'a pas d'activité

### Méthodologie de chasse structurée

Pour mener des activités de chasse aux menaces efficaces :

1. **Préparation**
   - Définissez clairement l'objectif de la chasse
   - Rassemblez les informations de threat intelligence pertinentes
   - Identifiez les données nécessaires et vérifiez leur disponibilité

2. **Exécution**
   - Suivez une approche méthodique et documentée
   - Commencez par des requêtes larges puis affinez progressivement
   - Utilisez des techniques de pivotement pour explorer les connexions

3. **Analyse**
   - Examinez les résultats avec un œil critique
   - Distinguez les activités légitimes des comportements suspects
   - Corrélation avec d'autres sources de données pour confirmation

4. **Documentation et partage**
   - Documentez toutes les étapes et résultats
   - Partagez les techniques efficaces avec l'équipe
   - Créez une base de connaissances des chasses précédentes

5. **Amélioration**
   - Transformez les découvertes en détections automatisées
   - Affinez les hypothèses pour les futures sessions de chasse
   - Mesurez l'efficacité des activités de chasse

## 8.3. Tableaux de bord personnalisés

Les tableaux de bord personnalisés permettent aux analystes SOC d'avoir une vue adaptée à leurs besoins spécifiques, améliorant ainsi leur efficacité quotidienne.

### 8.3.1. Création de tableaux de bord

**Processus de création d'un tableau de bord**

1. **Accès à l'outil de création**
   - Naviguez vers "Tableaux de bord" > "Créer un tableau de bord"
   - Donnez un nom descriptif au tableau de bord
   - Sélectionnez une disposition initiale (1, 2 ou 3 colonnes)

2. **Ajout de widgets**
   - Cliquez sur "Ajouter un widget"
   - Sélectionnez le type de widget souhaité :
     - Graphiques (barres, lignes, camembert)
     - Tableaux de données
     - Compteurs et indicateurs
     - Cartes géographiques
     - Listes d'alertes ou d'incidents

3. **Configuration des widgets**
   - Définissez la source de données (requête XQL, données d'alerte, etc.)
   - Configurez les paramètres de visualisation
   - Définissez les filtres et conditions
   - Ajustez la période temporelle (dernières 24h, 7 jours, etc.)

4. **Organisation du tableau de bord**
   - Disposez les widgets par glisser-déposer
   - Redimensionnez les widgets selon leur importance
   - Regroupez logiquement les widgets liés

5. **Paramètres avancés**
   - Configurez l'actualisation automatique
   - Définissez les options de partage
   - Ajoutez des filtres globaux applicables à tous les widgets

**Types de widgets et leur utilisation**

| Type de widget | Description | Cas d'usage |
|---------------|-------------|------------|
| Compteur | Affiche une valeur numérique avec indicateur de tendance | Nombre d'incidents actifs, alertes critiques |
| Graphique en barres | Représente des données catégorielles | Répartition des alertes par type, par sévérité |
| Graphique en lignes | Montre l'évolution temporelle | Tendances des alertes sur une période |
| Camembert | Visualise des proportions | Répartition des incidents par statut |
| Tableau | Affiche des données détaillées en lignes et colonnes | Liste des derniers incidents, top des endpoints affectés |
| Carte thermique | Représente des données sur une carte géographique | Origine géographique des attaques |
| Liste | Affiche des éléments avec détails et actions rapides | Alertes récentes nécessitant une attention |

### 8.3.2. Exemples de tableaux de bord pour différents rôles

**Tableau de bord pour analyste de niveau 1**

Objectif : Triage efficace et gestion des incidents quotidiens

Widgets recommandés :
1. **Compteur d'alertes non traitées** (par sévérité)
2. **Liste des incidents assignés** (avec statut et temps écoulé)
3. **Graphique des alertes par heure** (dernières 24h)
4. **Top 10 des endpoints générant le plus d'alertes**
5. **Répartition des alertes par type** (camembert)
6. **Liste des dernières alertes critiques**
7. **Indicateur de charge de travail** (comparaison avec la moyenne)

**Tableau de bord pour analyste de niveau 2**

Objectif : Investigation approfondie et analyse des tendances

Widgets recommandés :
1. **Incidents en cours d'investigation** (avec chronologie)
2. **Graphique des techniques MITRE ATT&CK détectées** (7 derniers jours)
3. **Carte des connexions externes suspectes**
4. **Tableau des IOCs détectés récemment**
5. **Graphique de corrélation des alertes**
6. **Liste des endpoints isolés**
7. **Tendances des types d'attaques** (comparaison mensuelle)

**Tableau de bord pour responsable SOC**

Objectif : Supervision globale et reporting

Widgets recommandés :
1. **KPIs principaux** (MTTD, MTTR, taux de faux positifs)
2. **Statut global des incidents** (ouverts, en cours, résolus)
3. **Charge de travail par analyste**
4. **Tendances mensuelles des incidents**
5. **Répartition des incidents par criticité d'actif**
6. **Temps moyen de résolution par type d'incident**
7. **Calendrier des incidents majeurs**

**Tableau de bord de threat hunting**

Objectif : Support aux activités proactives de recherche de menaces

Widgets recommandés :
1. **Activités réseau inhabituelles** (connexions vers des destinations rares)
2. **Exécutions de processus suspects** (basé sur des requêtes XQL personnalisées)
3. **Anomalies d'authentification**
4. **Activités administratives inhabituelles**
5. **Transferts de données volumineux**
6. **Timeline des événements sur endpoints critiques**
7. **Indicateurs de compromission récents** (intégration threat intelligence)

### Bonnes pratiques pour les tableaux de bord

1. **Conception efficace**
   - Limitez le nombre de widgets (7-9 maximum par tableau de bord)
   - Placez les informations les plus importantes en haut à gauche
   - Utilisez un code couleur cohérent (rouge pour critique, etc.)
   - Privilégiez la lisibilité à la densité d'information

2. **Organisation logique**
   - Regroupez les widgets liés thématiquement
   - Suivez un flux de travail naturel de gauche à droite et de haut en bas
   - Créez plusieurs tableaux de bord spécialisés plutôt qu'un seul surchargé

3. **Optimisation des performances**
   - Limitez les requêtes complexes qui ralentissent le chargement
   - Ajustez les périodes temporelles selon la pertinence des données
   - Configurez des actualisations appropriées (pas trop fréquentes)

4. **Maintenance et évolution**
   - Révisez régulièrement l'utilité des widgets
   - Adaptez les tableaux de bord en fonction des menaces émergentes
   - Recueillez les retours des utilisateurs pour amélioration continue

## 8.4. Rapports et métriques

Les rapports et métriques sont essentiels pour évaluer l'efficacité du SOC, identifier les tendances et communiquer avec les parties prenantes.

### Types de rapports dans Cortex XDR

Cortex XDR permet de générer différents types de rapports pour répondre à divers besoins :

1. **Rapports opérationnels**
   - Activité quotidienne/hebdomadaire du SOC
   - Statut des incidents en cours
   - Résumé des alertes par catégorie
   - Activité des endpoints

2. **Rapports de conformité**
   - État de la couverture des agents
   - Conformité des politiques de sécurité
   - Historique des modifications de configuration
   - Journaux d'audit des actions administratives

3. **Rapports d'analyse**
   - Tendances des menaces détectées
   - Analyse des incidents majeurs
   - Efficacité des contrôles de sécurité
   - Benchmarks et comparaisons

4. **Rapports exécutifs**
   - Résumé de haut niveau pour la direction
   - Métriques clés et KPIs
   - Évaluation des risques
   - Recommandations stratégiques

### Métriques clés pour les analystes SOC

Pour évaluer l'efficacité des opérations de sécurité, suivez ces métriques essentielles :

**Métriques de détection**

| Métrique | Description | Objectif cible |
|----------|-------------|---------------|
| MTTD (Mean Time To Detect) | Temps moyen entre le début d'une attaque et sa détection | < 24 heures |
| Taux de détection | Pourcentage de menaces connues détectées lors de tests | > 95% |
| Taux de faux positifs | Pourcentage d'alertes identifiées comme fausses | < 15% |
| Couverture de détection | Pourcentage de techniques MITRE ATT&CK couvertes | > 80% |

**Métriques de réponse**

| Métrique | Description | Objectif cible |
|----------|-------------|---------------|
| MTTR (Mean Time To Respond) | Temps moyen entre la détection et la résolution | < 4 heures (critique) |
| Taux de résolution | Pourcentage d'incidents résolus vs. ouverts | > 90% |
| Temps d'escalade | Délai moyen pour escalader les incidents complexes | < 30 minutes |
| Efficacité de remédiation | Pourcentage d'incidents sans récurrence | > 95% |

**Métriques opérationnelles**

| Métrique | Description | Objectif cible |
|----------|-------------|---------------|
| Charge par analyste | Nombre moyen d'incidents traités par analyste | 5-10 par jour |
| Couverture des agents | Pourcentage d'endpoints protégés par Cortex XDR | > 98% |
| Disponibilité du système | Pourcentage de temps de fonctionnement de Cortex XDR | > 99.9% |
| Temps d'investigation | Temps moyen consacré à l'analyse d'un incident | Variable selon sévérité |

### Création de rapports personnalisés

Pour créer des rapports personnalisés dans Cortex XDR :

1. **Accès au module de rapports**
   - Naviguez vers "Rapports" > "Créer un rapport"
   - Sélectionnez un modèle ou créez un rapport personnalisé

2. **Sélection des données**
   - Choisissez les sources de données (incidents, alertes, endpoints)
   - Définissez la période couverte par le rapport
   - Sélectionnez les filtres appropriés (sévérité, type, statut)

3. **Configuration du format**
   - Choisissez les sections à inclure
   - Sélectionnez les visualisations (tableaux, graphiques)
   - Définissez l'ordre et la hiérarchie des informations

4. **Options de planification**
   - Configurez la génération automatique (quotidienne, hebdomadaire, mensuelle)
   - Définissez les destinataires pour la distribution automatique
   - Spécifiez le format de livraison (PDF, HTML, CSV)

5. **Personnalisation avancée**
   - Ajoutez un résumé exécutif
   - Incluez des notes d'analyse et recommandations
   - Personnalisez l'apparence avec le logo de l'entreprise

### Communication efficace des résultats

Pour communiquer efficacement les résultats de sécurité aux différentes parties prenantes :

1. **Adaptation au public**
   - Direction : Focus sur les risques métier et les métriques de haut niveau
   - Équipes techniques : Détails techniques et recommandations spécifiques
   - Auditeurs : Preuves de conformité et documentation des contrôles

2. **Visualisation des données**
   - Utilisez des graphiques clairs et pertinents
   - Évitez la surcharge d'informations
   - Mettez en évidence les tendances et anomalies
   - Utilisez des codes couleur cohérents

3. **Contextualisation**
   - Comparez avec les périodes précédentes
   - Fournissez des benchmarks de l'industrie quand disponibles
   - Expliquez l'impact métier des incidents
   - Liez les métriques aux objectifs de sécurité

4. **Recommandations actionnables**
   - Incluez des recommandations claires et spécifiques
   - Priorisez les actions en fonction de l'impact
   - Proposez des mesures préventives
   - Suivez les recommandations précédentes
