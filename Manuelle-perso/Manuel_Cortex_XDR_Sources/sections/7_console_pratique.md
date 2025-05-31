# 7. Console Cortex XDR en pratique

## 7.1. Interface utilisateur

L'interface utilisateur de Cortex XDR est conçue pour offrir une expérience intuitive et efficace aux analystes de sécurité. Sa conception permet d'accéder rapidement aux informations critiques tout en facilitant les investigations approfondies.

### Structure générale de l'interface

L'interface de Cortex XDR est organisée en plusieurs zones fonctionnelles :

**Barre de navigation principale**

Située en haut de l'écran, elle permet d'accéder aux principales sections de la console :
- Tableau de bord
- Incidents
- Alertes
- Endpoints
- Recherche
- Politiques
- Réponse
- Administration

**Panneau latéral**

Situé à gauche, il affiche des sous-menus contextuels en fonction de la section principale sélectionnée.

**Zone de travail principale**

Occupe la majeure partie de l'écran et affiche le contenu de la section sélectionnée.

**Barre d'état**

Située en bas de l'écran, elle affiche des informations système comme l'état de la connexion, les notifications et l'utilisateur connecté.

### Personnalisation de l'interface

Cortex XDR offre plusieurs options de personnalisation pour adapter l'interface aux préférences de chaque utilisateur :

1. **Thèmes visuels**
   - Mode clair
   - Mode sombre (recommandé pour réduire la fatigue oculaire)
   - Mode automatique (suit les préférences système)

2. **Disposition des tableaux**
   - Colonnes visibles/masquées
   - Ordre des colonnes
   - Taille des colonnes
   - Filtres par défaut

3. **Préférences utilisateur**
   - Format de date et heure
   - Fuseau horaire
   - Langue de l'interface
   - Nombre d'éléments par page

4. **Raccourcis personnalisés**
   - Création de favoris pour les recherches fréquentes
   - Enregistrement des filtres personnalisés
   - Tableaux de bord personnalisés

### Navigation efficace

Pour naviguer efficacement dans l'interface Cortex XDR :

1. **Utilisation des filtres rapides**
   - Filtres prédéfinis pour les vues courantes
   - Filtres personnalisés enregistrés
   - Filtres contextuels selon la section

2. **Recherche globale**
   - Accessible depuis n'importe quelle page
   - Recherche par nom d'hôte, adresse IP, hachage de fichier, etc.
   - Suggestions automatiques pendant la saisie

3. **Navigation par contexte**
   - Liens contextuels entre les éléments liés
   - Pivotement d'un incident vers les alertes associées
   - Passage d'un endpoint à son historique d'alertes

4. **Raccourcis clavier**
   - `Ctrl+F` : Recherche dans la page
   - `Ctrl+G` : Recherche globale
   - `Ctrl+I` : Vue des incidents
   - `Ctrl+A` : Vue des alertes
   - `Ctrl+E` : Vue des endpoints
   - `Esc` : Fermer les fenêtres modales

## 7.2. Tableau de bord principal

Le tableau de bord principal de Cortex XDR offre une vue d'ensemble de l'état de sécurité de votre environnement, permettant d'identifier rapidement les problèmes nécessitant une attention immédiate.

### Composants du tableau de bord par défaut

Le tableau de bord principal comprend plusieurs widgets configurables :

**Résumé des incidents**
- Nombre total d'incidents actifs
- Répartition par sévérité (critique, élevée, moyenne, faible)
- Tendance sur les dernières 24 heures/7 jours/30 jours
- Incidents nécessitant une attention immédiate

**État des endpoints**
- Nombre total d'endpoints gérés
- Répartition par statut (en ligne, hors ligne, problématique)
- Endpoints nécessitant une attention (mises à jour, problèmes de configuration)
- Couverture des agents par groupe

**Alertes récentes**
- Liste des dernières alertes générées
- Filtrage rapide par type et sévérité
- Indicateurs visuels pour les alertes critiques
- Options de triage rapide

**Carte thermique des menaces**
- Visualisation géographique des menaces détectées
- Concentration des attaques par région
- Origines des connexions malveillantes
- Cibles principales dans votre environnement

**Tendances des menaces**
- Graphiques d'évolution des détections
- Comparaison avec les périodes précédentes
- Identification des pics d'activité anormale
- Répartition par type de menace

### Personnalisation du tableau de bord

Pour adapter le tableau de bord à vos besoins spécifiques :

1. **Ajout/suppression de widgets**
   - Cliquez sur "Modifier le tableau de bord"
   - Sélectionnez "Ajouter un widget" pour choisir parmi les widgets disponibles
   - Utilisez l'icône de suppression pour retirer un widget

2. **Redimensionnement et réorganisation**
   - Faites glisser les widgets pour les repositionner
   - Utilisez les poignées de redimensionnement pour ajuster la taille
   - Organisez les widgets par ordre de priorité

3. **Configuration des widgets**
   - Cliquez sur l'icône de configuration de chaque widget
   - Ajustez les paramètres spécifiques (période, filtres, visualisation)
   - Définissez les seuils d'alerte visuelle

4. **Création de tableaux de bord multiples**
   - Naviguez vers "Tableaux de bord" > "Nouveau tableau de bord"
   - Donnez un nom descriptif au tableau de bord
   - Configurez les widgets selon le focus souhaité
   - Partagez le tableau de bord avec d'autres utilisateurs si nécessaire

### Tableaux de bord spécialisés

En plus du tableau de bord principal, vous pouvez créer des tableaux de bord spécialisés pour différents cas d'usage :

**Tableau de bord de surveillance des endpoints**
- État des agents par version
- Problèmes de configuration
- Endpoints nécessitant des mises à jour
- Historique des problèmes de connectivité

**Tableau de bord de chasse aux menaces**
- Activités réseau inhabituelles
- Exécutions de processus suspects
- Connexions externes anormales
- Modifications système sensibles

**Tableau de bord de conformité**
- État des politiques de sécurité
- Exceptions et déviations
- Tendances des violations de politique
- Statut des correctifs de sécurité

**Tableau de bord exécutif**
- Métriques de haut niveau
- Tendances des incidents sur le long terme
- Comparaisons avec les benchmarks de l'industrie
- ROI des investissements en sécurité

## 7.3. Gestion des incidents

La gestion efficace des incidents est au cœur de Cortex XDR, permettant aux analystes de sécurité de traiter méthodiquement les menaces détectées.

### Cycle de vie des incidents

Cortex XDR structure le traitement des incidents selon un cycle de vie bien défini :

1. **Détection**
   - Génération automatique d'un incident basé sur des alertes corrélées
   - Assignation d'une sévérité initiale basée sur l'impact potentiel
   - Enrichissement automatique avec des informations contextuelles

2. **Triage**
   - Évaluation initiale de la légitimité et de la gravité
   - Assignation à un analyste ou une équipe
   - Définition de la priorité de traitement

3. **Investigation**
   - Analyse approfondie des alertes constituant l'incident
   - Collecte de preuves supplémentaires
   - Détermination de l'étendue de la compromission

4. **Réponse**
   - Exécution d'actions de remédiation
   - Confinement des systèmes compromis
   - Élimination des menaces détectées

5. **Clôture**
   - Documentation des actions entreprises
   - Catégorisation finale de l'incident
   - Extraction des enseignements pour amélioration future

### Interface de gestion des incidents

L'interface de gestion des incidents de Cortex XDR est conçue pour faciliter le travail des analystes :

**Vue principale des incidents**
- Liste de tous les incidents avec filtres configurables
- Indicateurs visuels de sévérité et de statut
- Options de tri par différents critères (date, sévérité, statut)
- Fonctionnalités de recherche et de filtrage avancées

**Vue détaillée d'un incident**
- Résumé de l'incident avec informations clés
- Chronologie des événements associés
- Liste des alertes constituant l'incident
- Visualisation de la chaîne d'attaque
- Endpoints et utilisateurs impliqués
- Actions de réponse disponibles

**Panneau d'investigation**
- Outils d'analyse approfondie
- Visualisation des relations entre entités
- Accès aux données brutes pour investigation
- Fonctionnalités de pivotement entre éléments liés

### Workflow de traitement des incidents

Pour traiter efficacement un incident dans Cortex XDR :

1. **Accès à l'incident**
   - Naviguez vers la section "Incidents"
   - Sélectionnez l'incident à traiter dans la liste
   - Examinez le résumé et la sévérité assignée

2. **Prise en charge**
   - Changez le statut de l'incident à "En cours"
   - Assignez l'incident à vous-même ou à l'équipe appropriée
   - Ajoutez des notes initiales si nécessaire

3. **Investigation**
   - Examinez les alertes constituant l'incident
   - Utilisez la visualisation de la chaîne d'attaque pour comprendre la progression
   - Analysez les artefacts et indicateurs associés
   - Utilisez les outils de recherche pour identifier d'autres systèmes potentiellement affectés

4. **Actions de réponse**
   - Sélectionnez les endpoints concernés
   - Choisissez les actions appropriées (isolation, collecte de preuves, etc.)
   - Exécutez les actions et surveillez leur progression
   - Documentez les actions entreprises

5. **Clôture et documentation**
   - Mettez à jour le statut de l'incident
   - Ajoutez des notes détaillées sur l'investigation et les actions
   - Catégorisez l'incident (vrai positif, faux positif, etc.)
   - Documentez les enseignements tirés

### Collaboration et escalade

Cortex XDR facilite la collaboration entre analystes et l'escalade des incidents complexes :

1. **Partage d'incidents**
   - Assignation à d'autres analystes ou équipes
   - Ajout de commentaires et de notes
   - Notification des changements de statut

2. **Processus d'escalade**
   - Modification de la sévérité si nécessaire
   - Assignation à des équipes spécialisées
   - Ajout de parties prenantes supplémentaires
   - Intégration avec les systèmes de gestion d'incidents

3. **Documentation collaborative**
   - Historique complet des actions et commentaires
   - Pièces jointes et preuves partagées
   - Journal d'audit des modifications

## 7.4. Alertes corrélées

Les alertes corrélées constituent la base des incidents dans Cortex XDR, regroupant des événements liés pour présenter une vue complète d'une menace potentielle.

### Principe de corrélation des alertes

Cortex XDR utilise des algorithmes avancés pour corréler automatiquement les alertes liées :

1. **Critères de corrélation**
   - Proximité temporelle des événements
   - Relation entre les endpoints concernés
   - Similarité des techniques d'attaque
   - Indicateurs de compromission communs
   - Utilisateurs impliqués

2. **Avantages de la corrélation**
   - Réduction du nombre d'alertes à traiter individuellement
   - Présentation d'une vue complète de l'attaque
   - Mise en évidence des relations non évidentes
   - Priorisation basée sur l'impact cumulatif

3. **Types de corrélation**
   - Corrélation basée sur les techniques MITRE ATT&CK
   - Corrélation basée sur les entités (endpoints, utilisateurs)
   - Corrélation basée sur les indicateurs de compromission
   - Corrélation temporelle et causale

### Navigation dans les alertes corrélées

Pour explorer efficacement les alertes corrélées dans un incident :

1. **Accès aux alertes**
   - Ouvrez un incident dans la console
   - Naviguez vers l'onglet "Alertes"
   - Visualisez la liste des alertes constituant l'incident

2. **Filtrage et tri**
   - Filtrez par type d'alerte, sévérité ou source
   - Triez par ordre chronologique ou par sévérité
   - Recherchez des mots-clés spécifiques

3. **Analyse des relations**
   - Utilisez la visualisation graphique pour comprendre les liens
   - Identifiez les alertes pivots (points de départ de l'attaque)
   - Suivez la progression chronologique des événements

4. **Exploration des détails**
   - Cliquez sur une alerte spécifique pour voir ses détails
   - Examinez les artefacts associés (fichiers, processus, connexions)
   - Pivotez vers d'autres éléments liés pour approfondir l'investigation

### Exemples de scénarios de corrélation

**Scénario 1 : Attaque de phishing menant à une exécution de malware**

Alertes corrélées :
1. Email contenant une pièce jointe malveillante (source : intégration email)
2. Exécution d'un document Office avec macros (source : agent endpoint)
3. Lancement de PowerShell avec commande encodée (source : agent endpoint)
4. Téléchargement de fichier depuis un domaine suspect (source : agent endpoint)
5. Exécution d'un binaire non signé (source : agent endpoint)
6. Communication avec un serveur C2 connu (source : pare-feu)

**Scénario 2 : Mouvement latéral après compromission initiale**

Alertes corrélées :
1. Multiples tentatives d'authentification échouées (source : logs Windows)
2. Authentification réussie avec un compte administrateur (source : logs Windows)
3. Exécution de l'outil Mimikatz (source : agent endpoint)
4. Création d'un service distant sur un autre endpoint (source : agent endpoint)
5. Exécution de commandes PowerShell sur plusieurs systèmes (source : agent endpoint)
6. Accès à des partages réseau sensibles (source : logs Windows)

**Scénario 3 : Attaque de ransomware**

Alertes corrélées :
1. Exécution d'un processus suspect (source : agent endpoint)
2. Modification massive de fichiers (source : agent endpoint)
3. Accès à de nombreux partages réseau (source : logs Windows)
4. Suppression des shadow copies (source : agent endpoint)
5. Création de fichiers de rançon (source : agent endpoint)
6. Tentative de communication avec des domaines de paiement de rançon (source : pare-feu)

## 7.5. Requêtes XQL

Le langage de requête XQL (XDR Query Language) est un outil puissant de Cortex XDR permettant aux analystes de rechercher et d'analyser les données collectées de manière flexible et précise.

### 7.5.1. Syntaxe de base

XQL est un langage de requête conçu spécifiquement pour l'analyse de données de sécurité. Sa syntaxe s'inspire du SQL tout en étant adaptée aux besoins spécifiques de la cybersécurité.

**Structure d'une requête XQL basique**

```
dataset=<nom_dataset> 
| filter <champ> <opérateur> <valeur> 
| fields <liste_champs> 
| limit <nombre>
```

**Éléments principaux**

1. **Dataset** : Source de données à interroger
   - `dataset=xdr_data` : Données des endpoints
   - `dataset=firewall` : Données des pare-feux
   - `dataset=cloud` : Données des environnements cloud

2. **Opérateurs de filtrage**
   - `=` : Égalité exacte
   - `!=` : Différence
   - `>`, `<`, `>=`, `<=` : Comparaisons numériques
   - `contains` : Recherche de sous-chaîne
   - `in` : Appartenance à une liste
   - `matches` : Correspondance avec une expression régulière

3. **Opérateurs logiques**
   - `and` : Condition ET logique
   - `or` : Condition OU logique
   - `not` : Négation

4. **Fonctions de manipulation**
   - `fields` : Sélection des champs à afficher
   - `rename` : Renommage de champs
   - `sort` : Tri des résultats
   - `limit` : Limitation du nombre de résultats
   - `count` : Comptage d'occurrences

### 7.5.2. Exemples de requêtes courantes

Voici quelques exemples de requêtes XQL pour des cas d'usage courants :

**Recherche de processus suspects**

```
dataset=xdr_data
| filter action_type = "PROCESS_START" 
| filter process_name = "powershell.exe" 
| filter command_line contains "-enc" or command_line contains "-encodedcommand"
| fields hostname, user_name, command_line, process_start_time
| sort process_start_time desc
```

**Détection de connexions réseau suspectes**

```
dataset=xdr_data
| filter action_type = "NETWORK_CONNECTION" 
| filter dst_port in (4444, 4445, 8080, 8443)
| filter dst_ip_country != "FR"
| fields hostname, user_name, process_name, dst_ip, dst_port, dst_ip_country
| sort hostname
```

**Recherche de fichiers récemment modifiés**

```
dataset=xdr_data
| filter action_type = "FILE_MODIFICATION" 
| filter file_path contains ".docx" or file_path contains ".xlsx" or file_path contains ".pdf"
| filter timestamp > timestamp(now() - 24h)
| fields hostname, user_name, file_path, file_md5, timestamp
| sort timestamp desc
```

**Analyse des tentatives d'authentification échouées**

```
dataset=xdr_data
| filter action_type = "AUTHENTICATION" 
| filter success = false
| stats count=count() by user_name, hostname
| filter count > 5
| sort count desc
```

**Détection de comportements de ransomware**

```
dataset=xdr_data
| filter action_type = "FILE_MODIFICATION"
| filter file_path matches ".*\.(doc|xls|pdf|jpg)$"
| stats count=count() by hostname, process_name
| filter count > 100
| sort count desc
```

### 7.5.3. Création de requêtes personnalisées

Pour créer des requêtes XQL efficaces et personnalisées :

**Interface de création de requêtes**

1. Naviguez vers "Recherche" > "Créer une requête"
2. Sélectionnez le dataset approprié dans le menu déroulant
3. Utilisez l'éditeur de requête pour saisir votre code XQL
4. Utilisez les suggestions automatiques pour les noms de champs et fonctions
5. Cliquez sur "Exécuter" pour lancer la requête

**Bonnes pratiques pour les requêtes XQL**

1. **Optimisation des performances**
   - Filtrez d'abord, puis sélectionnez les champs
   - Limitez la période de recherche autant que possible
   - Utilisez des index lorsqu'ils sont disponibles
   - Limitez le nombre de résultats si vous n'avez besoin que d'un échantillon

2. **Organisation des requêtes**
   - Utilisez des commentaires (`//`) pour documenter vos requêtes
   - Structurez vos requêtes avec des sauts de ligne pour la lisibilité
   - Nommez clairement vos requêtes enregistrées
   - Utilisez des alias explicites pour les champs renommés

3. **Requêtes avancées**
   - Utilisez des sous-requêtes pour des analyses complexes
   - Exploitez les fonctions d'agrégation pour l'analyse statistique
   - Combinez plusieurs datasets pour des corrélations avancées
   - Utilisez des expressions régulières pour des correspondances complexes

**Enregistrement et partage de requêtes**

1. **Enregistrement**
   - Après avoir créé une requête utile, cliquez sur "Enregistrer"
   - Donnez un nom descriptif à la requête
   - Ajoutez une description détaillant son objectif
   - Choisissez de la rendre privée ou partagée

2. **Organisation**
   - Créez des dossiers thématiques pour organiser vos requêtes
   - Utilisez des tags pour faciliter la recherche
   - Regroupez les requêtes liées à des cas d'usage similaires

3. **Partage**
   - Partagez les requêtes utiles avec votre équipe
   - Exportez les requêtes pour les sauvegarder
   - Importez des requêtes partagées par d'autres analystes

**Automatisation avec les requêtes planifiées**

1. Créez une requête qui détecte un comportement spécifique
2. Cliquez sur "Planifier"
3. Définissez la fréquence d'exécution
4. Configurez les notifications en cas de résultats
5. Définissez les actions automatiques à déclencher si nécessaire
