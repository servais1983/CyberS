# 9. Bonnes pratiques de déploiement et de durcissement

## 9.1. Stratégie de déploiement optimale

Le déploiement de Cortex XDR dans un environnement d'entreprise nécessite une approche méthodique et progressive pour garantir son efficacité tout en minimisant les perturbations.

### 9.1.1. Approche par phases

Une stratégie de déploiement par phases permet de maîtriser le processus et d'ajuster la configuration en fonction des retours d'expérience :

**Phase 1 : Planification et préparation**

1. **Évaluation de l'environnement**
   - Inventaire des systèmes et applications
   - Identification des systèmes critiques
   - Cartographie du réseau et des flux de données
   - Analyse des solutions de sécurité existantes

2. **Définition des objectifs**
   - Établissement des cas d'usage prioritaires
   - Définition des métriques de succès
   - Alignement avec la stratégie de sécurité globale
   - Identification des exigences de conformité

3. **Conception de l'architecture**
   - Dimensionnement de la solution
   - Planification de la couverture des endpoints
   - Conception des intégrations avec l'écosystème existant
   - Définition des flux de données et de la rétention

4. **Préparation organisationnelle**
   - Formation de l'équipe projet
   - Communication aux parties prenantes
   - Établissement des processus opérationnels
   - Définition des rôles et responsabilités

**Phase 2 : Déploiement pilote**

1. **Sélection du groupe pilote**
   - Choix d'un échantillon représentatif (5-10% des endpoints)
   - Inclusion de différents types de systèmes
   - Participation d'utilisateurs techniques et non techniques
   - Représentation de différentes unités d'affaires

2. **Configuration initiale**
   - Mise en place de la console Cortex XDR
   - Configuration des politiques en mode surveillance
   - Établissement des groupes d'endpoints
   - Configuration des notifications et alertes

3. **Déploiement contrôlé**
   - Installation des agents sur le groupe pilote
   - Surveillance étroite des performances
   - Documentation des problèmes rencontrés
   - Ajustement des configurations si nécessaire

4. **Évaluation du pilote**
   - Analyse des données collectées
   - Évaluation de l'impact sur les performances
   - Recueil des retours utilisateurs
   - Identification des ajustements nécessaires

**Phase 3 : Déploiement progressif**

1. **Planification du déploiement global**
   - Segmentation en vagues de déploiement
   - Priorisation basée sur la criticité et les risques
   - Établissement d'un calendrier réaliste
   - Allocation des ressources nécessaires

2. **Automatisation du déploiement**
   - Intégration avec les outils de gestion de parc
   - Création de packages de déploiement silencieux
   - Mise en place de scripts de vérification
   - Configuration des rapports de déploiement

3. **Exécution par vagues**
   - Déploiement sur des groupes successifs
   - Période de stabilisation entre les vagues
   - Surveillance des indicateurs de performance
   - Résolution des problèmes avant la vague suivante

4. **Transition vers les opérations**
   - Formation des équipes opérationnelles
   - Documentation des procédures
   - Transfert progressif des responsabilités
   - Établissement des processus de support

**Phase 4 : Optimisation continue**

1. **Affinage des politiques**
   - Passage progressif du mode surveillance au mode protection
   - Ajustement des règles pour réduire les faux positifs
   - Personnalisation des politiques par groupe d'endpoints
   - Mise en place de règles avancées

2. **Intégration approfondie**
   - Connexion avec les systèmes SIEM/SOAR
   - Intégration des flux de threat intelligence
   - Automatisation des workflows de réponse
   - Synchronisation avec les autres outils de sécurité

3. **Mesure et amélioration**
   - Suivi régulier des KPIs définis
   - Analyse des tendances et patterns
   - Benchmarking avec les meilleures pratiques
   - Mise en œuvre d'améliorations continues

### 9.1.2. Considérations spécifiques par environnement

Les stratégies de déploiement doivent être adaptées aux spécificités de chaque type d'environnement :

**Environnements de bureau**

| Considération | Recommandation |
|---------------|----------------|
| Déploiement | Utiliser les outils de gestion de parc existants (SCCM, Intune, Jamf) |
| Performance | Planifier les analyses complètes en dehors des heures de travail |
| Formation | Sensibiliser les utilisateurs aux notifications potentielles |
| Exclusions | Identifier les applications métier sensibles aux performances |

**Environnements serveurs**

| Considération | Recommandation |
|---------------|----------------|
| Fenêtres de maintenance | Coordonner l'installation avec les calendriers de maintenance |
| Tests préalables | Valider dans un environnement de pré-production |
| Haute disponibilité | Déployer progressivement sur les clusters pour éviter les interruptions |
| Charge système | Configurer des politiques spécifiques pour minimiser l'impact CPU/mémoire |

**Environnements industriels (OT/ICS)**

| Considération | Recommandation |
|---------------|----------------|
| Validation | Tester extensivement dans un environnement de simulation |
| Mode | Commencer en mode surveillance uniquement |
| Coordination | Impliquer les équipes d'ingénierie industrielle |
| Certification | Vérifier la compatibilité avec les systèmes certifiés |

**Environnements cloud**

| Considération | Recommandation |
|---------------|----------------|
| Automatisation | Intégrer le déploiement dans les templates d'infrastructure |
| Élasticité | Configurer pour s'adapter aux environnements dynamiques |
| Intégrations natives | Utiliser les connecteurs cloud natifs pour AWS, Azure, GCP |
| Conteneurs | Adapter la stratégie pour les environnements conteneurisés |

## 9.2. Durcissement de la configuration

Le durcissement de la configuration de Cortex XDR est essentiel pour maximiser la protection tout en maintenant la stabilité opérationnelle.

### 9.2.1. Sécurisation de la console

La console d'administration étant le point central de contrôle, sa sécurisation est primordiale :

**Contrôle d'accès**

1. **Authentification renforcée**
   - Activer l'authentification multifacteur pour tous les utilisateurs
   - Imposer des mots de passe complexes (16+ caractères)
   - Configurer la rotation périodique des mots de passe
   - Mettre en place le verrouillage de compte après échecs multiples

2. **Gestion des utilisateurs**
   - Appliquer le principe du moindre privilège
   - Créer des rôles personnalisés pour chaque fonction
   - Réviser régulièrement les droits d'accès
   - Mettre en place un processus de révocation immédiate

3. **Intégration avec IAM**
   - Configurer l'authentification unique (SSO)
   - Synchroniser avec l'annuaire d'entreprise
   - Automatiser la gestion du cycle de vie des comptes
   - Implémenter des politiques d'accès conditionnel

**Sécurité des sessions**

1. **Paramètres de session**
   - Configurer un délai d'expiration de session approprié (15-30 minutes)
   - Limiter le nombre de sessions simultanées par utilisateur
   - Mettre en place le verrouillage géographique si applicable
   - Activer les notifications de connexion

2. **Journalisation et audit**
   - Activer la journalisation complète des actions administratives
   - Configurer l'exportation des logs vers un système externe
   - Mettre en place des alertes pour les actions sensibles
   - Conserver les journaux d'audit pour la période requise

**Sécurisation des API**

1. **Gestion des clés API**
   - Générer des clés API avec le minimum de privilèges nécessaires
   - Mettre en place une rotation régulière des clés
   - Documenter l'utilisation de chaque clé API
   - Révoquer immédiatement les clés compromises

2. **Contrôle d'accès API**
   - Limiter l'accès API à des adresses IP spécifiques
   - Mettre en place des quotas et limites de taux
   - Surveiller l'utilisation anormale des API
   - Implémenter OAuth 2.0 pour les intégrations complexes

### 9.2.2. Durcissement des agents

Les agents Cortex XDR déployés sur les endpoints doivent être configurés pour résister aux tentatives de contournement :

**Protection de l'agent**

1. **Auto-protection**
   - Activer toutes les fonctionnalités d'auto-défense
   - Configurer un mot de passe de désinstallation complexe
   - Protéger les processus et services de l'agent
   - Activer la protection contre la modification des fichiers de l'agent

2. **Mise à jour**
   - Configurer les mises à jour automatiques des agents
   - Définir une fenêtre de maintenance appropriée
   - Tester les mises à jour sur un groupe pilote
   - Surveiller le statut des mises à jour

3. **Surveillance de l'intégrité**
   - Configurer des alertes en cas de désactivation de l'agent
   - Mettre en place une vérification périodique de l'intégrité
   - Automatiser la réinstallation des agents défectueux
   - Surveiller les endpoints sans communication récente

**Configuration des politiques de sécurité**

1. **Approche progressive**
   - Commencer en mode surveillance pour établir une base de référence
   - Passer progressivement en mode blocage par catégorie de menace
   - Documenter et analyser chaque faux positif
   - Ajuster les politiques en fonction des retours

2. **Segmentation des politiques**
   - Créer des politiques distinctes par type d'environnement
   - Adapter les règles selon la criticité des systèmes
   - Personnaliser les politiques pour les systèmes spécialisés
   - Maintenir une cohérence globale tout en permettant des variations

3. **Paramètres recommandés par fonction**

| Fonction | Protection malware | Protection exploit | Analyse comportementale | Contrôle applications |
|----------|-------------------|-------------------|------------------------|----------------------|
| Postes standard | Blocage | Élevée | Moyenne | Surveillance |
| Postes VIP | Blocage | Élevée | Moyenne-basse | Surveillance |
| Serveurs web | Blocage | Élevée | Élevée | Liste blanche |
| Serveurs BDD | Blocage | Élevée | Moyenne | Liste blanche |
| Développement | Détection | Moyenne | Basse | Désactivé |
| Systèmes critiques | Blocage | Élevée | Élevée | Liste blanche stricte |

### 9.2.3. Sécurisation des communications

La sécurisation des flux de communication est essentielle pour préserver l'intégrité du système :

**Communications agent-console**

1. **Chiffrement et authentification**
   - Vérifier l'utilisation de TLS 1.2+ pour toutes les communications
   - Mettre en place l'authentification mutuelle TLS si possible
   - Configurer la validation des certificats
   - Mettre à jour régulièrement les suites cryptographiques

2. **Configuration réseau**
   - Documenter précisément les flux réseau nécessaires
   - Configurer les pare-feux pour autoriser uniquement ces flux
   - Mettre en place des règles de QoS pour garantir la communication
   - Configurer des routes de secours si nécessaire

**Intégrations externes**

1. **Sécurisation des intégrations**
   - Utiliser des canaux chiffrés pour toutes les intégrations
   - Mettre en place des authentifications dédiées par intégration
   - Limiter les permissions au strict nécessaire
   - Surveiller l'activité des intégrations

2. **Validation des données**
   - Mettre en place des mécanismes de validation des données entrantes
   - Filtrer les données potentiellement malveillantes
   - Limiter le volume de données par intégration
   - Surveiller les anomalies dans les flux de données

## 9.3. Maintenance et mises à jour

Une stratégie de maintenance proactive est essentielle pour garantir l'efficacité continue de Cortex XDR.

### 9.3.1. Gestion des mises à jour

**Stratégie de mise à jour**

1. **Veille sur les nouvelles versions**
   - S'abonner aux notifications de Palo Alto Networks
   - Consulter régulièrement le portail de support
   - Examiner les notes de version pour les nouvelles fonctionnalités
   - Identifier les correctifs de sécurité critiques

2. **Processus de mise à jour**
   - Tester les mises à jour dans un environnement de pré-production
   - Planifier les mises à jour pendant les fenêtres de maintenance
   - Déployer progressivement sur des groupes d'endpoints
   - Prévoir une procédure de rollback en cas de problème

3. **Priorisation des mises à jour**

| Type de mise à jour | Délai recommandé | Approche |
|---------------------|------------------|----------|
| Correctifs critiques | < 7 jours | Déploiement accéléré après test minimal |
| Correctifs de sécurité | < 30 jours | Déploiement après tests sur environnement pilote |
| Mises à jour fonctionnelles | 30-90 jours | Déploiement progressif après tests complets |
| Mises à jour majeures | Planification spécifique | Projet dédié avec tests approfondis |

**Gestion des versions d'agents**

1. **Standardisation**
   - Viser l'homogénéité des versions d'agents dans l'environnement
   - Limiter le nombre de versions différentes en production
   - Documenter les exceptions et leurs justifications
   - Planifier la mise à niveau des agents obsolètes

2. **Compatibilité**
   - Vérifier la compatibilité avec les systèmes d'exploitation
   - Tester l'impact sur les applications critiques
   - Valider les performances après mise à jour
   - Maintenir une matrice de compatibilité à jour

### 9.3.2. Surveillance de la santé du système

**Indicateurs de santé à surveiller**

1. **Santé des agents**
   - Taux de connexion des agents
   - Versions des agents déployés
   - Erreurs récurrentes signalées
   - Performance des agents (utilisation CPU/mémoire)

2. **Santé de la console**
   - Temps de réponse de l'interface
   - Utilisation des ressources serveur
   - Taux de succès des requêtes API
   - Temps de traitement des alertes

3. **Efficacité opérationnelle**
   - Volume d'alertes par catégorie
   - Taux de faux positifs
   - Temps de traitement des incidents
   - Couverture des endpoints

**Tableau de bord de santé système**

Créez un tableau de bord dédié pour surveiller ces indicateurs clés :

| Indicateur | Seuil d'alerte | Action recommandée |
|------------|----------------|---------------------|
| Agents déconnectés | > 5% | Investiguer les causes de déconnexion |
| Agents obsolètes | > 10% | Planifier une campagne de mise à jour |
| Utilisation CPU agent | > 10% en moyenne | Ajuster les paramètres de scan |
| Temps de réponse console | > 3 secondes | Vérifier les ressources serveur |
| Échecs de mise à jour | > 2% | Investiguer les causes d'échec |

**Maintenance préventive**

1. **Vérifications régulières**
   - Audit mensuel de la couverture des agents
   - Vérification hebdomadaire des agents déconnectés
   - Analyse trimestrielle des performances
   - Revue semestrielle des politiques et configurations

2. **Nettoyage de la base de données**
   - Archivage des anciennes alertes et incidents
   - Optimisation des requêtes fréquentes
   - Purge des données obsolètes
   - Défragmentation périodique si nécessaire

3. **Documentation**
   - Maintenir un journal des interventions de maintenance
   - Documenter les problèmes récurrents et leurs solutions
   - Mettre à jour la documentation après chaque changement majeur
   - Conserver l'historique des configurations

## 9.4. Optimisation des performances

L'optimisation des performances de Cortex XDR est essentielle pour garantir une protection efficace tout en minimisant l'impact sur les systèmes protégés.

### 9.4.1. Réduction de l'impact sur les endpoints

**Configuration des scans**

1. **Planification intelligente**
   - Programmer les scans complets pendant les périodes d'inactivité
   - Échelonner les scans pour éviter les pics de charge
   - Adapter la fréquence selon le profil de risque
   - Configurer des scans différenciés par type de système

2. **Paramètres d'optimisation**
   - Ajuster la priorité des processus de scan
   - Configurer des limites d'utilisation CPU
   - Définir des exclusions pour les dossiers à forte activité
   - Optimiser les paramètres de mise en cache

**Recommandations par type de système**

| Type de système | Fréquence de scan | Période recommandée | Limite CPU | Exclusions recommandées |
|-----------------|-------------------|---------------------|------------|------------------------|
| Postes de travail | Hebdomadaire | Nuit / Pause déjeuner | 30% | Dossiers temporaires, fichiers volumineux |
| Serveurs critiques | Bi-hebdomadaire | Heures creuses | 15% | Bases de données actives, fichiers de journalisation |
| Serveurs de production | Hebdomadaire | Fenêtre de maintenance | 20% | Répertoires de données transactionnelles |
| Systèmes de développement | Bi-mensuelle | Weekend | 40% | Répertoires de compilation, dépôts de code |

**Exclusions stratégiques**

Les exclusions doivent être soigneusement évaluées pour trouver l'équilibre entre performance et sécurité :

1. **Types d'exclusions**
   - Exclusions de chemins (répertoires spécifiques)
   - Exclusions de processus (applications légitimes)
   - Exclusions de fichiers (par extension ou nom)
   - Exclusions de signatures (règles spécifiques)

2. **Critères d'évaluation**
   - Impact sur les performances
   - Niveau de confiance dans le contenu exclu
   - Risque potentiel de l'exclusion
   - Alternatives possibles

3. **Documentation des exclusions**
   - Justification détaillée de chaque exclusion
   - Approbation formelle par la sécurité
   - Période de validité et date de révision
   - Mesures compensatoires mises en place

### 9.4.2. Optimisation de la console

**Performance de la base de données**

1. **Gestion des données**
   - Configurer des politiques de rétention appropriées
   - Archiver les données historiques rarement consultées
   - Mettre en place une purge automatique des données obsolètes
   - Optimiser les index pour les requêtes fréquentes

2. **Requêtes XQL**
   - Optimiser les requêtes fréquemment utilisées
   - Limiter les plages temporelles des recherches
   - Utiliser des filtres efficaces en début de requête
   - Créer des vues matérialisées pour les rapports complexes

**Gestion des ressources**

1. **Surveillance des ressources**
   - Suivre l'utilisation CPU, mémoire et disque
   - Identifier les tendances de croissance
   - Anticiper les besoins d'extension
   - Surveiller les temps de réponse

2. **Dimensionnement approprié**
   - Ajuster les ressources en fonction du nombre d'endpoints
   - Prévoir une marge pour les pics d'activité
   - Adapter les ressources après des changements significatifs
   - Considérer la séparation des environnements pour les déploiements importants

### 9.4.3. Équilibrage sécurité-performance

L'équilibre entre sécurité et performance est un ajustement continu :

1. **Approche par niveaux**
   - Appliquer des contrôles plus stricts aux systèmes critiques
   - Adapter les politiques selon la sensibilité des données
   - Différencier les environnements de production et de test
   - Considérer le profil de risque de chaque groupe d'endpoints

2. **Mesure et ajustement**
   - Établir des métriques de référence avant les changements
   - Mesurer l'impact de chaque modification
   - Recueillir les retours des utilisateurs
   - Ajuster progressivement pour trouver le point d'équilibre optimal

3. **Compromis acceptables**

| Fonctionnalité | Impact performance | Valeur sécurité | Recommandation |
|----------------|-------------------|-----------------|----------------|
| Analyse comportementale | Moyen | Élevée | Activer avec paramètres optimisés |
| Scan temps réel | Élevé | Élevée | Configurer avec exclusions ciblées |
| Scan complet | Très élevé | Moyenne | Planifier pendant les périodes d'inactivité |
| Collecte de données | Variable | Moyenne | Ajuster la granularité selon les besoins |
| Protection mémoire | Moyen | Très élevée | Maintenir active sur tous les systèmes |

## 9.5. Intégration dans l'écosystème de sécurité

L'intégration efficace de Cortex XDR dans l'écosystème de sécurité existant maximise sa valeur et renforce la posture de sécurité globale.

### 9.5.1. Architecture d'intégration

**Principes d'intégration**

1. **Centralisation de la visibilité**
   - Agréger les données de sécurité dans une plateforme centrale
   - Établir une source unique de vérité pour les incidents
   - Corréler les événements de différentes sources
   - Maintenir une vue holistique de la posture de sécurité

2. **Automatisation des workflows**
   - Réduire les tâches manuelles répétitives
   - Standardiser les processus de réponse
   - Accélérer le temps de réaction
   - Minimiser les erreurs humaines

3. **Enrichissement contextuel**
   - Enrichir les alertes avec des informations contextuelles
   - Faciliter la priorisation basée sur le risque
   - Améliorer la précision des détections
   - Réduire le temps d'investigation

**Architecture de référence**

Une architecture d'intégration bien conçue connecte Cortex XDR avec les autres composants de l'écosystème de sécurité :

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  Sources de     │────▶│  Cortex XDR     │────▶│  SIEM / SOAR    │
│  données        │     │                 │     │                 │
│                 │     │                 │     │                 │
└─────────────────┘     └────────┬────────┘     └────────┬────────┘
                               │                        │
                               │                        │
                               ▼                        ▼
                        ┌─────────────────┐     ┌─────────────────┐
                        │                 │     │                 │
                        │  Threat         │     │  Systèmes de    │
                        │  Intelligence   │     │  ticketing      │
                        │                 │     │                 │
                        └─────────────────┘     └─────────────────┘
```

### 9.5.2. Intégrations clés et cas d'usage

**Intégration SIEM**

1. **Objectifs**
   - Centraliser la collecte et l'analyse des logs
   - Corréler les alertes Cortex XDR avec d'autres sources
   - Fournir des capacités avancées de reporting
   - Conserver les données historiques pour conformité

2. **Configuration recommandée**
   - Transmettre toutes les alertes de sévérité moyenne à critique
   - Envoyer les métadonnées des incidents
   - Configurer des tableaux de bord spécifiques dans le SIEM
   - Établir des règles de corrélation cross-plateformes

3. **Cas d'usage**
   - Corrélation d'une alerte endpoint avec des logs de pare-feu
   - Détection de mouvements latéraux via multiple sources
   - Reporting consolidé pour la conformité
   - Analyse historique des tendances de sécurité

**Intégration SOAR**

1. **Objectifs**
   - Automatiser les actions de réponse
   - Standardiser les processus d'investigation
   - Orchestrer les actions multi-plateformes
   - Accélérer le temps de réponse aux incidents

2. **Configuration recommandée**
   - Développer des playbooks pour les scénarios courants
   - Configurer des déclencheurs basés sur la sévérité et le type
   - Mettre en place des points de décision humaine pour les actions critiques
   - Documenter automatiquement les actions entreprises

3. **Cas d'usage**
   - Isolation automatique d'un endpoint compromis
   - Enrichissement d'incidents avec des données contextuelles
   - Orchestration de la réponse multi-plateformes
   - Création et suivi automatisés des tickets d'incident

**Intégration Threat Intelligence**

1. **Objectifs**
   - Enrichir les détections avec du contexte externe
   - Identifier les campagnes et acteurs de menace
   - Améliorer la précision des alertes
   - Anticiper les menaces émergentes

2. **Configuration recommandée**
   - Sélectionner des sources de TI pertinentes pour votre secteur
   - Filtrer les feeds pour réduire le bruit
   - Configurer des mises à jour automatiques
   - Définir des niveaux de confiance pour chaque source

3. **Cas d'usage**
   - Enrichissement automatique des IOCs détectés
   - Recherche proactive de menaces connues
   - Contextualisation des alertes avec des informations sur les attaquants
   - Adaptation des défenses basée sur les tendances de menaces

### 9.5.3. Développement d'intégrations personnalisées

Pour les besoins spécifiques non couverts par les intégrations standard :

1. **Utilisation de l'API Cortex XDR**
   - Explorer la documentation complète de l'API
   - Générer des clés API avec les permissions minimales requises
   - Développer des scripts pour les cas d'usage spécifiques
   - Mettre en place une gestion sécurisée des clés API

2. **Développement d'intégrations**
   - Identifier clairement les besoins d'intégration
   - Concevoir une architecture d'intégration robuste
   - Développer avec des pratiques de code sécurisé
   - Mettre en place des tests automatisés

3. **Exemples de scripts d'intégration**

```python
# Exemple simplifié d'intégration Python avec l'API Cortex XDR
import requests
import json
import hashlib
import time

# Configuration
API_KEY_ID = "your_api_key_id"
API_KEY = "your_api_key"
FQDN = "cortex.paloaltonetworks.com"

# Calculer l'authentification
def generate_auth(api_key_id, api_key):
    nonce = str(int(time.time() * 1000))
    auth_key = "%s%s%s" % (api_key_id, nonce, api_key)
    auth_key = auth_key.encode("utf-8")
    auth_key = hashlib.sha256(auth_key).hexdigest()
    return {
        "x-xdr-auth-id": api_key_id,
        "x-xdr-nonce": nonce,
        "x-xdr-signature": auth_key
    }

# Récupérer les incidents récents
def get_recent_incidents():
    headers = generate_auth(API_KEY_ID, API_KEY)
    headers["Content-Type"] = "application/json"
    
    data = {
        "request_data": {
            "time_frame": {
                "start_time": int(time.time()) - 86400,  # Dernières 24h
                "end_time": int(time.time())
            },
            "sort": {
                "field": "creation_time",
                "keyword": "desc"
            },
            "limit": 10
        }
    }
    
    response = requests.post(
        f"https://{FQDN}/public_api/v1/incidents/get_incidents/",
        headers=headers,
        data=json.dumps(data)
    )
    
    return response.json()

# Utilisation
incidents = get_recent_incidents()
print(json.dumps(incidents, indent=4))
```

4. **Bonnes pratiques pour les intégrations personnalisées**
   - Documenter exhaustivement le code et les configurations
   - Mettre en place une gestion des erreurs robuste
   - Prévoir des mécanismes de reprise après échec
   - Surveiller les performances et l'utilisation des API
   - Maintenir à jour les intégrations avec les évolutions de l'API
