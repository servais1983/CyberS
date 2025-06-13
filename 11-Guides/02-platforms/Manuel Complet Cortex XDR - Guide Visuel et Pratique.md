# Manuel Complet Cortex XDR - Guide Visuel et Pratique

## Table des matières

1. [Introduction à Cortex XDR](#1-introduction-à-cortex-xdr)
2. [Accès et Navigation dans la Console](#2-accès-et-navigation-dans-la-console)
3. [Le Dashboard Principal - Guide Détaillé](#3-le-dashboard-principal---guide-détaillé)
4. [Dashboards Prédéfinis - Guide Pratique](#4-dashboards-prédéfinis---guide-pratique)
5. [Création et Personnalisation de Dashboards](#5-création-et-personnalisation-de-dashboards)
6. [Gestion des Incidents - Guide Visuel](#6-gestion-des-incidents---guide-visuel)
7. [Investigation des Alertes - Tutoriel Pratique](#7-investigation-des-alertes---tutoriel-pratique)
8. [Analyse des Endpoints - Guide Pas à Pas](#8-analyse-des-endpoints---guide-pas-à-pas)
9. [Requêtes XQL - Guide Pratique](#9-requêtes-xql---guide-pratique)
10. [Configuration et Administration](#10-configuration-et-administration)
11. [Intégrations et Connecteurs](#11-intégrations-et-connecteurs)
12. [Bonnes Pratiques et Optimisation](#12-bonnes-pratiques-et-optimisation)
13. [Cas d'Usage Concrets - Tutoriels Visuels](#13-cas-dusage-concrets---tutoriels-visuels)
14. [Glossaire, FAQ et Ressources](#14-glossaire-faq-et-ressources)

# 1. Introduction à Cortex XDR

## 1.1 Présentation générale de Cortex XDR

Cortex XDR est une plateforme de détection et de réponse étendue (Extended Detection and Response) développée par Palo Alto Networks. Cette solution de sécurité avancée unifie la prévention, la détection, l'investigation et la réponse aux menaces à travers les endpoints, le réseau et le cloud.

La plateforme Cortex XDR offre une visibilité complète sur l'ensemble de l'infrastructure informatique, permettant aux équipes de sécurité de détecter les menaces sophistiquées qui pourraient passer inaperçues avec des outils traditionnels.

![Dashboard Cortex XDR](https://private-us-east-1.manuscdn.com/sessionFile/IneiHlKkFeKoZw52ZHVaBe/sandbox/N8Zg3ynBYJoUPj4tVTqKHa-images_1749752210082_na1fn_L2hvbWUvdWJ1bnR1L2NvcnRleF94ZHJfbWFudWVsL2ltYWdlc19yZWVsbGVzL2Rhc2hib2FyZF9hc3NldF9pbnZlbnRvcnk.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvSW5laUhsS2tGZUtvWnc1MlpIVmFCZS9zYW5kYm94L044WmczeW5CWUpvVVBqNHRWVHFLSGEtaW1hZ2VzXzE3NDk3NTIyMTAwODJfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnZjblJsZUY5NFpISmZiV0Z1ZFdWc0wybHRZV2RsYzE5eVpXVnNiR1Z6TDJSaGMyaGliMkZ5WkY5aGMzTmxkRjlwYm5abGJuUnZjbmsucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=Mjc4kanLL9upDMDBLn0sdiXwcWPSCDxfogbJU0nFgo7dyUfsWCvBmXlCCY3yt~MttrnT3qqHYxoEHeB1-6uXnNzieDh7jaFaddSCSJOrhyeF1pgaAd5tepE3zOLvoNKpQkNjszeL~dIv0W8YK30oVrZ0GPO0Hd1PZLr5cMdc0jdBAV~kE9JzAwGGmkxs4c-elzdWORyqhz4OfjSVLBvxFKRyjETuofW0KTdjivntn5-iRjZk8qOHsJpwMkhwfMqCG8oSyr4ve7VrTQcSuh68dTf9nG9EZccvrAy1pKb65VjXT6hH2pHtlGqDKNqg7kQYPjdH1D0XS-0Tbv~SaLv2FQ__)
*Figure 1.1: Vue du dashboard d'inventaire des actifs dans Cortex XDR (Source: Documentation officielle Palo Alto Networks)*

## 1.2 Positionnement dans l'écosystème de cybersécurité

Dans l'écosystème actuel de la cybersécurité, Cortex XDR se positionne comme une solution unifiée qui va au-delà des capacités traditionnelles des outils EDR (Endpoint Detection and Response), SIEM (Security Information and Event Management) et SOAR (Security Orchestration, Automation and Response).

Cortex XDR se distingue par:
- L'intégration native des données provenant de multiples sources
- L'analyse comportementale basée sur l'intelligence artificielle
- La corrélation automatique des alertes en incidents significatifs
- La capacité de réponse automatisée aux menaces

## 1.3 Avantages par rapport aux solutions EDR traditionnelles

Contrairement aux solutions EDR traditionnelles qui se concentrent uniquement sur les endpoints, Cortex XDR offre plusieurs avantages significatifs:

| Fonctionnalité | EDR Traditionnel | Cortex XDR |
|----------------|------------------|------------|
| Sources de données | Endpoints uniquement | Endpoints, réseau, cloud, identités |
| Corrélation | Limitée aux endpoints | Corrélation multi-source |
| Analyse | Basée sur les signatures et règles | Analyse comportementale avancée |
| Investigation | Manuelle et complexe | Assistée et simplifiée |
| Réponse | Principalement manuelle | Automatisée et orchestrée |
| Visibilité | Partielle | Complète sur l'infrastructure |

Cette approche unifiée permet une détection plus précise des menaces complexes et une vision plus complète des incidents de sécurité.

## 1.4 Architecture globale

L'architecture de Cortex XDR repose sur plusieurs composants clés qui travaillent ensemble pour offrir une protection complète:

1. **Agents Cortex XDR**: Déployés sur les endpoints (postes de travail, serveurs) pour collecter des données et appliquer des politiques de sécurité.

2. **Console de gestion centralisée**: Interface web permettant de configurer, surveiller et gérer l'ensemble de la solution.

3. **Moteur d'analyse**: Utilise l'intelligence artificielle et le machine learning pour détecter les comportements anormaux.

4. **Data Lake**: Stockage centralisé des données de sécurité provenant de toutes les sources.

5. **Connecteurs d'intégration**: Permettent d'intégrer des sources de données tierces et d'autres solutions de sécurité.

![Architecture Cortex XDR](https://private-us-east-1.manuscdn.com/sessionFile/IneiHlKkFeKoZw52ZHVaBe/sandbox/N8Zg3ynBYJoUPj4tVTqKHa-images_1749752210082_na1fn_L2hvbWUvdWJ1bnR1L2NvcnRleF94ZHJfbWFudWVsL2ltYWdlc19yZWVsbGVzL2luY2lkZW50X2hhbmRsaW5nX3BhZ2U.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvSW5laUhsS2tGZUtvWnc1MlpIVmFCZS9zYW5kYm94L044WmczeW5CWUpvVVBqNHRWVHFLSGEtaW1hZ2VzXzE3NDk3NTIyMTAwODJfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnZjblJsZUY5NFpISmZiV0Z1ZFdWc0wybHRZV2RsYzE5eVpXVnNiR1Z6TDJsdVkybGtaVzUwWDJoaGJtUnNhVzVuWDNCaFoyVS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=M2zvrqeZkbuNi4vsNr4cQuSGeenr1tyV36TCxjj8eOEehwQKXWXC9Ruuq6fmkAC2agbeABSXOp4ldmydJgT-n0fHsIP8eZd-Pom0YR0H0IvG3sLYiPZRgZaufncLdBE6HzLV3Mf-B7AtrklRNLFjLJ125wzArxXojodgDkbJENbujEmoMJH6HFRWGQaN5NEr09joDQIHRlWiMCBtXpWEfBDh3nc2EgX7mV~mSFh3iQ3e~npJrZLyr~mglexMoEP0wPjADpMDdvTSWC6FXQrlPVJR7beK35dt7M0g~BCaWyiujUg2R3~t4ZyumnuMOZgDEauRwjnR48yDg1megOw5cw__)
*Figure 1.2: Vue de la page de gestion des incidents dans Cortex XDR (Source: Documentation officielle Palo Alto Networks)*

## 1.5 Prérequis techniques et licences

Pour déployer et utiliser efficacement Cortex XDR, plusieurs prérequis techniques et options de licence sont à considérer:

### Prérequis techniques:

- **Pour la console Cortex XDR**: Accessible via navigateur web (Chrome, Firefox, Edge récents)
- **Pour les agents Endpoints**:
  - Windows 7 SP1 ou supérieur / Windows Server 2008 R2 SP1 ou supérieur
  - macOS 10.13 (High Sierra) ou supérieur
  - Linux: distributions majeures (RHEL, CentOS, Ubuntu, SUSE)
  - Minimum 2 GB RAM et 1 GB d'espace disque disponible

### Options de licence:

Cortex XDR propose plusieurs niveaux de licence adaptés aux besoins spécifiques des organisations:

1. **Cortex XDR Prevent**: Fonctionnalités de protection de base incluant NGAV (Next-Generation Antivirus)
2. **Cortex XDR Pro**: Ensemble complet de fonctionnalités de détection et réponse
3. **Cortex XDR Enterprise**: Toutes les fonctionnalités Pro plus des capacités avancées d'analyse et d'automatisation

Chaque niveau de licence détermine les fonctionnalités et dashboards disponibles dans la console, comme indiqué dans la documentation officielle:

![Tableau des licences](https://private-us-east-1.manuscdn.com/sessionFile/IneiHlKkFeKoZw52ZHVaBe/sandbox/N8Zg3ynBYJoUPj4tVTqKHa-images_1749752210083_na1fn_L2hvbWUvdWJ1bnR1L2NvcnRleF94ZHJfbWFudWVsL2ltYWdlc19yZWVsbGVzL3ByZWRlZmluZWRfZGFzaGJvYXJkc190YWJsZQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvSW5laUhsS2tGZUtvWnc1MlpIVmFCZS9zYW5kYm94L044WmczeW5CWUpvVVBqNHRWVHFLSGEtaW1hZ2VzXzE3NDk3NTIyMTAwODNfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnZjblJsZUY5NFpISmZiV0Z1ZFdWc0wybHRZV2RsYzE5eVpXVnNiR1Z6TDNCeVpXUmxabWx1WldSZlpHRnphR0p2WVhKa2MxOTBZV0pzWlEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=aVWu87lm-R87a8j-OVdCZXeBHBT7dyanI22LPLMxRNAr-ZzISBcrRjK-E2uEuW-MuNIHP29nCKMflG4H6~pgL-pCEI2xltrVp62rV8WrJjGq4bvUKEwqEdU~U8uRNmrLfncScpEK0UVQ~z33ukTvR9USntTzOb5UEiGR4uGDnTeAFfAG1mivIbypnc2mg5CRCp0T7Ct778ZlKU-~suyGwmy-2oU6c2nWKOETudlZ7dMBik1DGWanWP6Ayp68Wm42YNOJm5oQ5aOeNjzwqAH-Me04FvsVyy525TsqJgL7BLjpux9kanPhAoJEAidZKPnaC~ygrqbRAGQ9hZwbqI3Jow__)
*Figure 1.3: Tableau des dashboards prédéfinis disponibles selon le type de licence (Source: Documentation officielle Palo Alto Networks)*

Dans les sections suivantes, nous explorerons en détail l'interface utilisateur de Cortex XDR et vous guiderons pas à pas dans l'utilisation de ses principales fonctionnalités.
# 2. Accès et Navigation dans la Console

## 2.1 Connexion à la console Cortex XDR

Pour accéder à la console Cortex XDR, suivez ces étapes simples:

1. Ouvrez votre navigateur web (Chrome, Firefox ou Edge recommandés)
2. Accédez à l'URL de votre instance Cortex XDR (généralement sous la forme `https://[votre-tenant].xdr.paloaltonetworks.com`)
3. Sur la page de connexion, saisissez vos identifiants (nom d'utilisateur et mot de passe)
4. Si l'authentification à deux facteurs est activée, complétez cette étape selon la méthode configurée

![Page de connexion Cortex XDR](https://private-us-east-1.manuscdn.com/sessionFile/IneiHlKkFeKoZw52ZHVaBe/sandbox/N8Zg3ynBYJoUPj4tVTqKHa-images_1749752210083_na1fn_L2hvbWUvdWJ1bnR1L2NvcnRleF94ZHJfbWFudWVsL2ltYWdlc19yZWVsbGVzL21hbmFnZV9pbmNpZGVudHNfcGFnZQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvSW5laUhsS2tGZUtvWnc1MlpIVmFCZS9zYW5kYm94L044WmczeW5CWUpvVVBqNHRWVHFLSGEtaW1hZ2VzXzE3NDk3NTIyMTAwODNfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnZjblJsZUY5NFpISmZiV0Z1ZFdWc0wybHRZV2RsYzE5eVpXVnNiR1Z6TDIxaGJtRm5aVjlwYm1OcFpHVnVkSE5mY0dGblpRLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NzIyNTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=C~DXDEMzryiUmxvZdXQlFN-GFE6ATtfaWiM~j4D8e4UuD6IGeaGrIwnpFkre2xEnjFI8kv9fNvuBUEKbwy1IEgHklB9caA4yxPTqV4aCk5~fnW1QA4JuQdnALFtR~593qDpOvNfhEsVYxGaey5-CiK8x~N~CNfvxLGtlLN5pBnClDQoTqCfCNSpYfJ4j37vncPZVwaUPIFghW4wZHMaEdnbg7g7HlhXmnmeib87KZqIZ63vtSiwcl5uluRHQzruKTsWR0gBe5dBy1P~V2Lf~9ZQCqcqFadLRehv180bsJcD1twQlD5mNxEllaEony-CYhUfLThCiErumNrP3EoQmUQ__)
*Figure 2.1: Interface de gestion des incidents après connexion (Source: Documentation officielle Palo Alto Networks)*

## 2.2 Présentation de l'interface utilisateur

Une fois connecté, vous accédez à l'interface principale de Cortex XDR. L'interface est organisée de manière intuitive pour faciliter la navigation et l'accès aux différentes fonctionnalités:

1. **Barre de navigation principale**: Située en haut de l'écran, elle permet d'accéder aux sections principales.
2. **Menu latéral**: Situé à gauche, il affiche les sous-sections de la catégorie sélectionnée.
3. **Zone de contenu principale**: Occupe la majeure partie de l'écran et affiche les informations et contrôles de la section active.
4. **Barre d'outils supérieure**: Contient les options de recherche, notifications et paramètres utilisateur.

![Interface principale](https://private-us-east-1.manuscdn.com/sessionFile/IneiHlKkFeKoZw52ZHVaBe/sandbox/N8Zg3ynBYJoUPj4tVTqKHa-images_1749752210083_na1fn_L2hvbWUvdWJ1bnR1L2NvcnRleF94ZHJfbWFudWVsL2ltYWdlc19yZWVsbGVzL2ludmVzdGlnYXRlX2FsZXJ0c19wYWdl.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvSW5laUhsS2tGZUtvWnc1MlpIVmFCZS9zYW5kYm94L044WmczeW5CWUpvVVBqNHRWVHFLSGEtaW1hZ2VzXzE3NDk3NTIyMTAwODNfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnZjblJsZUY5NFpISmZiV0Z1ZFdWc0wybHRZV2RsYzE5eVpXVnNiR1Z6TDJsdWRtVnpkR2xuWVhSbFgyRnNaWEowYzE5d1lXZGwucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=TQzWtMeAVcAWNFcqULhRQq4ppwuDYeuylvTizJehAQ1J~NjOHV0fEIg45CnYOqIynSLFqzCSxlXGgIAKPE9PjAPLNw1rgx9sW~oMT8TxtFE12XCK0LIyDxoQwdLu14GrHmTvFVHz8hT-rAcvobXkfLM4uQTVVjMT7Vd0QP72WUE6HI5g~NEw8rcjM6SfFDaTnFLr4HlJiiFQ0uGscv8WqTMdz7VaNpl1SwaZ1qiCnfTQS3s8LMm8LitE0WvOS3GH0nU9mCcUF18Caji2h98JZoBAWhh1rhSLc7a6N7El8Jsm-ql2aBxIqBbzAHm9yKH1WgIwilM0MFEcrq9L28kZqg__)
*Figure 2.2: Interface d'investigation des alertes dans Cortex XDR (Source: Documentation officielle Palo Alto Networks)*

## 2.3 Navigation entre les différentes sections

La console Cortex XDR est organisée en plusieurs sections principales, accessibles depuis la barre de navigation:

1. **Dashboard**: Affiche une vue d'ensemble de la sécurité avec des widgets personnalisables.
2. **Incidents**: Permet de visualiser et gérer les incidents de sécurité détectés.
3. **Alerts**: Affiche les alertes individuelles avant leur corrélation en incidents.
4. **Investigate**: Fournit des outils pour l'investigation approfondie des menaces.
5. **Endpoints**: Permet de gérer les agents déployés sur les postes de travail et serveurs.
6. **Assets**: Inventaire complet des actifs surveillés par la plateforme.
7. **Query**: Interface pour exécuter des requêtes XQL personnalisées.
8. **Settings**: Configuration générale de la plateforme.

Pour naviguer entre ces sections:
- Cliquez sur l'icône ou le nom de la section dans la barre de navigation principale
- Utilisez les sous-menus qui apparaissent dans le panneau latéral gauche
- Suivez les liens contextuels qui peuvent apparaître dans la zone de contenu principale

## 2.4 Personnalisation de l'interface

Cortex XDR offre plusieurs options pour personnaliser l'interface selon vos préférences et besoins:

### Personnalisation des dashboards:
1. Accédez à la section "Dashboard"
2. Cliquez sur "Dashboard Manager" pour créer ou modifier des dashboards
3. Ajoutez, supprimez ou réorganisez les widgets selon vos besoins

### Personnalisation des vues de liste:
1. Dans les sections Incidents, Alerts ou Assets, utilisez les filtres disponibles
2. Cliquez sur l'icône de colonnes pour sélectionner les informations à afficher
3. Enregistrez vos vues personnalisées pour un accès rapide ultérieur

### Personnalisation des paramètres d'affichage:
1. Accédez à votre profil utilisateur (icône en haut à droite)
2. Sélectionnez "User Preferences"
3. Ajustez les paramètres comme le fuseau horaire, le format de date et les options d'affichage

## 2.5 Gestion des préférences utilisateur

Chaque utilisateur peut configurer ses préférences personnelles pour optimiser son expérience avec Cortex XDR:

### Paramètres de notification:
1. Accédez à votre profil utilisateur
2. Sélectionnez "Notification Settings"
3. Configurez les types d'alertes que vous souhaitez recevoir et leur mode de livraison (email, console, etc.)

### Paramètres d'affichage:
1. Définissez votre dashboard par défaut
2. Configurez le nombre d'éléments à afficher par page dans les listes
3. Choisissez votre thème d'interface (si disponible)

### Raccourcis clavier:
Cortex XDR propose plusieurs raccourcis clavier pour accélérer la navigation et les actions courantes:
- `Ctrl+/` ou `Cmd+/`: Afficher l'aide des raccourcis clavier
- `Ctrl+F` ou `Cmd+F`: Recherche rapide
- `Esc`: Fermer les fenêtres modales ou annuler les actions en cours

La maîtrise de l'interface utilisateur et de la navigation est essentielle pour utiliser efficacement Cortex XDR. Dans les sections suivantes, nous explorerons en détail chaque fonctionnalité principale de la plateforme, en commençant par le dashboard principal.



# 3. Le Dashboard Principal - Guide Visuel

## 3.1 Vue d'ensemble du dashboard

Le dashboard principal de Cortex XDR offre une vue synthétique et personnalisable de l'état de sécurité de votre environnement. Cette interface centralisée permet de visualiser rapidement les informations critiques et d'accéder aux fonctionnalités essentielles de la plateforme.

![Dashboard Principal](https://private-us-east-1.manuscdn.com/sessionFile/IneiHlKkFeKoZw52ZHVaBe/sandbox/N8Zg3ynBYJoUPj4tVTqKHa-images_1749752210084_na1fn_L2hvbWUvdWJ1bnR1L2NvcnRleF94ZHJfbWFudWVsL2ltYWdlc19yZWVsbGVzL2Rhc2hib2FyZF9hc3NldF9pbnZlbnRvcnk.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvSW5laUhsS2tGZUtvWnc1MlpIVmFCZS9zYW5kYm94L044WmczeW5CWUpvVVBqNHRWVHFLSGEtaW1hZ2VzXzE3NDk3NTIyMTAwODRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnZjblJsZUY5NFpISmZiV0Z1ZFdWc0wybHRZV2RsYzE5eVpXVnNiR1Z6TDJSaGMyaGliMkZ5WkY5aGMzTmxkRjlwYm5abGJuUnZjbmsucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=GRN8XZMshJom10Ged~PH1aISz0fITxUNGX8MU~wqkmZugeAaTmzD6qvPIGppz4lgMLgdRihvZHTJne0IVZ3Q7m78-d-0Ly1Nmh1Hpqkrcdqyn1p~SLfPEhy0uKGfYP7CETIA1M5Huab4Mk40tK3fT0oTq5jK7lZFZYQtzgUcxX1b7YSpFUrVTqO4rrFeNx6-SjsDI7y6dtNgAbE7R-tmfLZYGr-PvevQih08YGvFekXWc5kzIQUrOY6E3rteM3fJXhuBlKZA3Sp0rP-NEJkrVH3Tktscx6Oi2cmUPyYu5WebwrhWbQ3v~5cCY1VtmJlitx7Dl-vJcIX0DShwh~5qkw__)
*Figure 3.1: Dashboard d'inventaire des actifs dans Cortex XDR (Source: Documentation officielle Palo Alto Networks)*

Le dashboard principal est organisé en widgets configurables qui affichent différentes métriques et informations:

1. **En-tête**: Contient le titre du dashboard, les options de période temporelle et les contrôles de gestion
2. **Zone principale**: Affiche les widgets organisés selon une mise en page personnalisable
3. **Filtres**: Permettent d'affiner les données affichées selon différents critères

## 3.2 Comprendre les widgets et indicateurs clés

Chaque widget du dashboard représente un aspect spécifique de votre environnement de sécurité. Les widgets standard incluent:

### Widget d'incidents
Affiche le nombre total d'incidents actifs, leur répartition par sévérité et leur évolution dans le temps. Les incidents sont généralement représentés par un code couleur:
- Rouge: Critique
- Orange: Élevé
- Jaune: Moyen
- Bleu: Faible

### Widget d'alertes
Présente les alertes récentes, leur distribution par type et source. Ce widget permet d'identifier rapidement les tendances anormales dans les alertes générées.

### Widget d'état des agents
Montre l'état de déploiement et de santé des agents Cortex XDR sur les endpoints. Il indique:
- Le nombre total d'agents déployés
- La répartition par système d'exploitation
- Les agents nécessitant une attention (déconnectés, obsolètes, etc.)

### Widget d'inventaire des actifs
Comme illustré dans la Figure 3.1, ce widget présente une vue d'ensemble des actifs surveillés, organisés par catégories:
- Par classe (AI, Organisation, Network, etc.)
- Par catégorie (Model, Account, Security Group, etc.)
- Par fournisseur (AWS, GCP, On-Prem, etc.)
- Par région

### Widget de tendances
Affiche l'évolution des métriques clés sur une période définie, permettant d'identifier les anomalies ou les tendances préoccupantes.

## 3.3 Interprétation des données en temps réel

Les données affichées sur le dashboard sont actualisées régulièrement pour refléter l'état actuel de votre environnement. Pour interpréter efficacement ces données:

1. **Observez les tendances**: Comparez les données actuelles avec les périodes précédentes pour identifier les anomalies
2. **Identifiez les priorités**: Concentrez-vous d'abord sur les incidents critiques et à haute sévérité
3. **Corrélation**: Recherchez des relations entre différents widgets (par exemple, une augmentation des alertes coïncidant avec des agents déconnectés)
4. **Contexte**: Tenez compte des activités planifiées qui pourraient expliquer certaines variations (déploiements, mises à jour, etc.)

La dernière mise à jour des données est généralement indiquée en bas de chaque widget ou dans l'en-tête du dashboard.

## 3.4 Filtres et options de visualisation

Cortex XDR offre plusieurs options pour filtrer et personnaliser l'affichage des données sur le dashboard:

### Filtres globaux
Situés généralement en haut du dashboard, ils permettent de filtrer l'ensemble des widgets selon:
- La période temporelle (dernières 24h, 7 jours, 30 jours, etc.)
- L'environnement (production, test, développement)
- Les groupes d'endpoints
- Les types d'actifs

### Filtres par widget
Chaque widget dispose également de ses propres options de filtrage, accessibles via l'icône de paramètres (⚙️) dans le coin supérieur droit du widget.

### Options de visualisation
Pour modifier l'affichage des données dans un widget:
1. Cliquez sur l'icône de paramètres du widget
2. Sélectionnez "Edit Widget" ou "Visualization Options"
3. Choisissez le type de graphique approprié (camembert, histogramme, tableau, etc.)
4. Ajustez les paramètres spécifiques au type de visualisation

## 3.5 Navigation entre les différentes périodes temporelles

La dimension temporelle est essentielle pour l'analyse de sécurité. Cortex XDR permet de naviguer facilement entre différentes périodes:

### Sélecteur de période prédéfinie
Utilisez le menu déroulant de période (généralement en haut à droite) pour sélectionner:
- Dernières 24 heures
- Derniers 7 jours
- Derniers 30 jours
- Trimestre en cours
- Année en cours

### Sélecteur de période personnalisée
Pour une analyse plus précise:
1. Cliquez sur le sélecteur de période
2. Choisissez "Custom Range"
3. Définissez les dates de début et de fin
4. Cliquez sur "Apply"

### Navigation temporelle contextuelle
Certains widgets permettent une navigation directe:
- Cliquez sur un point spécifique d'un graphique temporel pour voir les détails de ce moment
- Utilisez les contrôles de zoom pour élargir ou réduire la période affichée
- Utilisez les flèches de navigation pour avancer ou reculer par intervalles de temps égaux

Le dashboard principal est votre point de départ pour la surveillance et l'analyse de sécurité. Dans la section suivante, nous explorerons les dashboards prédéfinis spécialisés qui offrent des vues plus détaillées sur des aspects spécifiques de votre environnement.



# 4. Dashboards Prédéfinis - Guide Pratique

## 4.1 Liste des dashboards disponibles

Cortex XDR propose plusieurs dashboards prédéfinis, chacun conçu pour répondre à des besoins spécifiques de surveillance et d'analyse. Ces dashboards sont accessibles directement depuis le menu principal ou via le sélecteur de dashboard.

![Tableau des dashboards prédéfinis](https://private-us-east-1.manuscdn.com/sessionFile/IneiHlKkFeKoZw52ZHVaBe/sandbox/N8Zg3ynBYJoUPj4tVTqKHa-images_1749752210085_na1fn_L2hvbWUvdWJ1bnR1L2NvcnRleF94ZHJfbWFudWVsL2ltYWdlc19yZWVsbGVzL3ByZWRlZmluZWRfZGFzaGJvYXJkc190YWJsZQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvSW5laUhsS2tGZUtvWnc1MlpIVmFCZS9zYW5kYm94L044WmczeW5CWUpvVVBqNHRWVHFLSGEtaW1hZ2VzXzE3NDk3NTIyMTAwODVfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnZjblJsZUY5NFpISmZiV0Z1ZFdWc0wybHRZV2RsYzE5eVpXVnNiR1Z6TDNCeVpXUmxabWx1WldSZlpHRnphR0p2WVhKa2MxOTBZV0pzWlEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=f2zJTb5gshXUKVyr07fysv-2cpiqbV~AL1gEzvzRdZPxn1ISuAWrRSPsnqaFhfW1ZslVyl4Z69u~n2XtwLI9CVMFR~BkwZVqiBZgKNGdXHz8MR2bbts3HIXjhDnnR178hi~9~cDLrcgkDai8zdrIiTYPZtIkoQNBC0NnSGnmMLc0WAsb4lVTRtrUhH0-PUoC1SxZMDR1JUzKb67t~1KP~mp~4FwvubXInBAjYQKE~i7BBLnHdo8uKWMJbMP7SNRG1rOlA8ZUsM2fY10pFvl5VrM-bgaeJNFgBEUQvKcW2Ssep5d~2XQ5hWC4N2wB9ujbre79~0CbCM8TCGBu7E~etg__)
*Figure 4.1: Tableau des dashboards prédéfinis disponibles dans Cortex XDR (Source: Documentation officielle Palo Alto Networks)*

Comme le montre la Figure 4.1, la disponibilité de certains dashboards dépend du type de licence dont vous disposez. Voici les principaux dashboards prédéfinis:

| Nom du Dashboard | Description | Type de licence requis |
|-----------------|-------------|------------------------|
| Agent management | Vue d'ensemble des agents déployés | Cortex XDR Prevent ou Pro |
| Cloud inventory | Inventaire des actifs cloud | Cortex XDR Pro par licence GB |
| Data ingestion | Aperçu de l'ingestion des données | Cortex XDR Pro |
| Incidents | Résumé des incidents actifs | Toutes licences |
| Network | Analyse du trafic réseau | Cortex XDR Pro avec Network Analytics |
| Threat Hunter | Outils de chasse aux menaces | Cortex XDR Pro |

## 4.2 Dashboard de gestion des agents

Le dashboard "Agent management" offre une vue complète sur l'état et la santé des agents Cortex XDR déployés dans votre environnement.

### Principales sections:

1. **Vue d'ensemble des agents**:
   - Nombre total d'agents déployés
   - Répartition par statut (connecté, déconnecté, en attente)
   - Distribution par système d'exploitation

2. **État de santé des agents**:
   - Agents nécessitant une mise à jour
   - Problèmes de configuration détectés
   - Historique des connexions/déconnexions

3. **Déploiement et couverture**:
   - Progression du déploiement par groupe
   - Taux de couverture par département/région
   - Endpoints non protégés

### Utilisation pratique:

1. Accédez au dashboard via le menu "Dashboards" > "Agent management"
2. Utilisez les filtres en haut pour affiner l'affichage (par groupe, OS, version)
3. Identifiez les agents problématiques nécessitant une attention
4. Cliquez sur un agent spécifique pour accéder à ses détails complets

## 4.3 Dashboard d'inventaire cloud

Le dashboard "Cloud inventory" présente une vue consolidée de vos actifs cloud surveillés par Cortex XDR.

### Principales sections:

1. **Vue d'ensemble des actifs cloud**:
   - Nombre total d'actifs par fournisseur (AWS, Azure, GCP)
   - Distribution par type de ressource (VM, conteneurs, fonctions)
   - Répartition par région

2. **État de sécurité**:
   - Actifs avec vulnérabilités détectées
   - Conformité aux politiques de sécurité
   - Tendances des alertes cloud

3. **Activité et performance**:
   - Métriques d'utilisation
   - Événements de sécurité par service
   - Tendances d'activité anormale

### Utilisation pratique:

1. Accédez au dashboard via le menu "Dashboards" > "Cloud inventory"
2. Filtrez par fournisseur cloud ou type de ressource
3. Identifiez les ressources présentant des risques de sécurité
4. Explorez les détails d'un actif spécifique en cliquant dessus

## 4.4 Dashboard d'ingestion de données

Le dashboard "Data ingestion" permet de surveiller et d'analyser les flux de données entrant dans Cortex XDR.

### Principales sections:

1. **Vue d'ensemble de l'ingestion**:
   - Volume total de données ingérées
   - Répartition par source (endpoint, réseau, cloud)
   - Tendances d'ingestion sur la période sélectionnée

2. **Quotas et utilisation**:
   - Consommation quotidienne par rapport aux quotas
   - Prévisions d'utilisation
   - Alertes de dépassement potentiel

3. **Qualité des données**:
   - Taux d'erreurs d'ingestion
   - Latence des données
   - Couverture des sources configurées

### Utilisation pratique:

1. Accédez au dashboard via le menu "Dashboards" > "Data ingestion"
2. Sélectionnez la période d'analyse souhaitée
3. Identifiez les tendances anormales ou les pics d'ingestion
4. Vérifiez la conformité avec les quotas alloués

## 4.5 Autres dashboards spécialisés

En fonction de votre licence et de votre configuration, d'autres dashboards spécialisés peuvent être disponibles:

### Dashboard Incidents

Ce dashboard offre une vue d'ensemble des incidents de sécurité détectés:
- Répartition des incidents par sévérité
- Tendances temporelles des incidents
- Incidents par type de menace
- Statut de résolution des incidents

### Dashboard Network

Dédié à l'analyse du trafic réseau, ce dashboard présente:
- Visualisation des flux de trafic
- Détection d'anomalies réseau
- Communications suspectes
- Analyse des protocoles

### Dashboard Threat Hunter

Conçu pour les analystes de sécurité avancés, ce dashboard facilite la chasse aux menaces:
- Indicateurs de compromission (IoC) détectés
- Activités suspectes par MITRE ATT&CK
- Outils de recherche avancée
- Modèles de comportement anormal

## Bonnes pratiques pour l'utilisation des dashboards prédéfinis

1. **Personnalisation limitée**: Contrairement au dashboard principal, les dashboards prédéfinis offrent moins d'options de personnalisation, mais vous pouvez toujours:
   - Ajuster les périodes temporelles
   - Appliquer des filtres spécifiques
   - Modifier l'ordre de tri des données

2. **Exportation des données**: Pour partager ou analyser plus en détail:
   - Utilisez l'option "Export" disponible sur la plupart des widgets
   - Formats disponibles: CSV, PDF, PNG (pour les graphiques)
   - Programmez des rapports automatiques basés sur ces dashboards

3. **Navigation efficace**:
   - Utilisez le sélecteur de dashboard en haut de l'interface pour basculer rapidement entre les différentes vues
   - Créez des favoris pour vos dashboards les plus utilisés
   - Définissez votre dashboard préféré comme page d'accueil

Les dashboards prédéfinis constituent un excellent point de départ pour l'analyse de sécurité. Dans la section suivante, nous verrons comment créer et personnaliser vos propres dashboards pour répondre à des besoins spécifiques.



# 5. Création et Personnalisation de Dashboards

## 5.1 Accès au Dashboard Manager

Le Dashboard Manager est l'outil central qui vous permet de créer, modifier et gérer vos dashboards personnalisés dans Cortex XDR. Pour y accéder:

1. Connectez-vous à votre console Cortex XDR
2. Dans la barre de navigation principale, cliquez sur "Dashboards"
3. Dans le menu déroulant qui apparaît, sélectionnez "Dashboard Manager"
4. Vous accédez alors à l'interface de gestion des dashboards

![Interface de gestion des dashboards](https://private-us-east-1.manuscdn.com/sessionFile/IneiHlKkFeKoZw52ZHVaBe/sandbox/N8Zg3ynBYJoUPj4tVTqKHa-images_1749752210085_na1fn_L2hvbWUvdWJ1bnR1L2NvcnRleF94ZHJfbWFudWVsL2ltYWdlc19yZWVsbGVzL21hbmFnZV9pbmNpZGVudHNfcGFnZQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvSW5laUhsS2tGZUtvWnc1MlpIVmFCZS9zYW5kYm94L044WmczeW5CWUpvVVBqNHRWVHFLSGEtaW1hZ2VzXzE3NDk3NTIyMTAwODVfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnZjblJsZUY5NFpISmZiV0Z1ZFdWc0wybHRZV2RsYzE5eVpXVnNiR1Z6TDIxaGJtRm5aVjlwYm1OcFpHVnVkSE5mY0dGblpRLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NzIyNTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=f-zNKRaY6uuSCsfeA69YczWqM35qB7XWYoQUsxjuXG3NtEE9oD2ZkYwN5GhYluDnK6juxqCdGA0DA8NzQ0l-GTFBD0QtiIoYP4msG5Cp-Y1AediL-BKk1pRtTVK4gasT-Xfm7SsAeDxBHtEIYiViQ8ioejSFqy9pu9vmKJRJz0QVxpgx0GBSBqoCpqOUMgi7F5WvLaeUA5sRq3VHsXusdblpPJ6URk0D~v6xUsYxyZRL-rEXP6V37e~9QG0myJBaMSUQsUadzK1wUKjJL0ktdPk43uOFrO2vRp-ZenMX5w4vNZ0NP5sNOop21xdj17xDofAXYFFZZClhSgq13L3b4A__)
*Figure 5.1: Interface de gestion dans Cortex XDR (Source: Documentation officielle Palo Alto Networks)*

Le Dashboard Manager affiche la liste de tous les dashboards disponibles, y compris les dashboards prédéfinis et ceux que vous avez créés. Vous pouvez effectuer plusieurs actions:
- Voir les dashboards existants
- Créer un nouveau dashboard
- Modifier un dashboard existant
- Dupliquer un dashboard
- Supprimer un dashboard personnalisé
- Définir un dashboard comme page d'accueil

## 5.2 Création d'un nouveau dashboard (pas à pas)

Pour créer un nouveau dashboard personnalisé, suivez ces étapes:

### Étape 1: Initialiser le nouveau dashboard
1. Dans le Dashboard Manager, cliquez sur le bouton "New Dashboard" ou "+" (généralement situé en haut à droite)
2. Dans la boîte de dialogue qui s'ouvre, saisissez:
   - Un nom pour votre dashboard (obligatoire)
   - Une description (facultatif)
   - Choisissez les options de partage (privé, partagé avec des groupes spécifiques, ou global)
3. Cliquez sur "Create" ou "Next" pour continuer

### Étape 2: Sélectionner une mise en page
1. Choisissez un modèle de mise en page parmi les options proposées:
   - Grille standard (disposition la plus flexible)
   - Colonnes égales (2, 3 ou 4 colonnes)
   - Disposition asymétrique (combinaison de zones larges et étroites)
2. Cliquez sur "Apply" ou "Next" pour continuer

### Étape 3: Ajouter des widgets
1. Cliquez sur le bouton "Add Widget" ou sur l'icône "+" dans une zone vide
2. Dans le sélecteur de widgets, parcourez les catégories disponibles:
   - Widgets d'incidents
   - Widgets d'alertes
   - Widgets d'endpoints
   - Widgets de réseau
   - Widgets de cloud
   - Widgets personnalisés basés sur XQL
3. Sélectionnez le widget souhaité et cliquez sur "Add" ou faites-le glisser vers l'emplacement désiré

### Étape 4: Enregistrer votre dashboard
1. Une fois tous les widgets ajoutés et configurés, cliquez sur "Save" en haut à droite
2. Votre nouveau dashboard est maintenant disponible dans la liste des dashboards

## 5.3 Ajout et configuration de widgets

Chaque widget peut être personnalisé pour afficher exactement les informations dont vous avez besoin:

### Types de widgets disponibles:
- **Widgets de métriques**: Affichent une valeur numérique simple (nombre d'incidents, d'alertes, etc.)
- **Widgets de graphiques**: Présentent des données sous forme de graphiques (camembert, histogramme, courbe, etc.)
- **Widgets de tableaux**: Affichent des données sous forme de tableau
- **Widgets de texte**: Permettent d'ajouter des notes, instructions ou explications
- **Widgets basés sur XQL**: Affichent les résultats d'une requête XQL personnalisée

### Configuration d'un widget:
1. Cliquez sur l'icône d'engrenage (⚙️) dans le coin supérieur droit du widget
2. Sélectionnez "Edit Widget" dans le menu contextuel
3. Dans le panneau de configuration qui s'ouvre, ajustez les paramètres:
   - Titre du widget
   - Source de données
   - Filtres spécifiques
   - Type de visualisation
   - Période temporelle (par défaut ou personnalisée)
   - Options d'affichage (légendes, axes, couleurs)
4. Cliquez sur "Apply" pour enregistrer les modifications

### Exemple: Configuration d'un widget d'incidents
1. Ajoutez un widget "Incidents by Severity"
2. Dans les options de configuration:
   - Définissez le titre: "Incidents critiques par type"
   - Filtrez pour n'afficher que les incidents de sévérité "Critical"
   - Groupez par "Incident Type"
   - Choisissez une visualisation en camembert
   - Limitez l'affichage aux 5 types les plus fréquents
3. Appliquez les changements pour voir le résultat

## 5.4 Organisation et mise en page

Une fois vos widgets ajoutés, vous pouvez organiser votre dashboard pour optimiser la lisibilité et l'efficacité:

### Redimensionnement des widgets:
1. Survolez le bord d'un widget jusqu'à ce que le curseur se transforme en flèche double
2. Cliquez et faites glisser pour redimensionner le widget
3. Relâchez lorsque le widget a la taille souhaitée

### Déplacement des widgets:
1. Survolez l'en-tête du widget jusqu'à ce que le curseur se transforme en main
2. Cliquez et maintenez pour faire glisser le widget
3. Déplacez-le vers son nouvel emplacement
4. Relâchez pour le positionner

### Organisation logique:
Pour une efficacité maximale, organisez vos widgets selon ces principes:
- Placez les informations les plus critiques en haut à gauche (zone de vision primaire)
- Regroupez les widgets liés thématiquement
- Créez un flux visuel logique (du général au spécifique)
- Équilibrez la densité d'information pour éviter la surcharge visuelle

### Utilisation des sections:
Pour les dashboards complexes, utilisez des widgets de texte comme séparateurs de section:
1. Ajoutez un widget de texte
2. Utilisez un formatage distinctif (texte en gras, plus grand)
3. Ajoutez une ligne horizontale en dessous (---) pour créer une séparation visuelle
4. Placez les widgets relatifs à cette section en dessous

## 5.5 Partage et exportation des dashboards

Une fois votre dashboard personnalisé créé, vous pouvez le partager avec d'autres utilisateurs ou l'exporter:

### Partage d'un dashboard:
1. Dans le Dashboard Manager, localisez votre dashboard
2. Cliquez sur l'icône de partage (généralement représentée par trois points verticaux)
3. Sélectionnez "Share" dans le menu contextuel
4. Choisissez les options de partage:
   - Utilisateurs spécifiques
   - Groupes d'utilisateurs
   - Tous les utilisateurs (global)
5. Définissez les permissions (lecture seule ou modification)
6. Cliquez sur "Apply" pour confirmer

### Exportation d'un dashboard:
1. Ouvrez le dashboard que vous souhaitez exporter
2. Cliquez sur l'icône d'options (⋮) en haut à droite
3. Sélectionnez "Export" dans le menu déroulant
4. Choisissez le format d'exportation:
   - PDF: pour le partage et l'archivage
   - PNG: pour l'inclusion dans des présentations
   - JSON: pour la sauvegarde ou le transfert vers une autre instance
5. Configurez les options d'exportation (taille, orientation, etc.)
6. Cliquez sur "Export" pour générer et télécharger le fichier

### Programmation de rapports:
Vous pouvez également configurer l'envoi automatique de vos dashboards par email:
1. Ouvrez le dashboard souhaité
2. Cliquez sur l'icône d'options (⋮)
3. Sélectionnez "Schedule Report"
4. Configurez:
   - Fréquence (quotidienne, hebdomadaire, mensuelle)
   - Heure d'envoi
   - Destinataires
   - Format (PDF, PNG)
5. Cliquez sur "Save" pour activer le rapport programmé

La création de dashboards personnalisés vous permet d'adapter Cortex XDR à vos besoins spécifiques et d'optimiser votre workflow de sécurité. Dans la section suivante, nous explorerons la gestion des incidents, une fonctionnalité centrale de la plateforme.



# 6. Gestion des Incidents - Guide Visuel

## 6.1 Vue d'ensemble de la page Incidents

La gestion des incidents est l'une des fonctionnalités centrales de Cortex XDR. La page Incidents offre une vue consolidée de tous les incidents de sécurité détectés dans votre environnement.

![Page de gestion des incidents](https://private-us-east-1.manuscdn.com/sessionFile/IneiHlKkFeKoZw52ZHVaBe/sandbox/N8Zg3ynBYJoUPj4tVTqKHa-images_1749752210086_na1fn_L2hvbWUvdWJ1bnR1L2NvcnRleF94ZHJfbWFudWVsL2ltYWdlc19yZWVsbGVzL2luY2lkZW50X2hhbmRsaW5nX3BhZ2U.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvSW5laUhsS2tGZUtvWnc1MlpIVmFCZS9zYW5kYm94L044WmczeW5CWUpvVVBqNHRWVHFLSGEtaW1hZ2VzXzE3NDk3NTIyMTAwODZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnZjblJsZUY5NFpISmZiV0Z1ZFdWc0wybHRZV2RsYzE5eVpXVnNiR1Z6TDJsdVkybGtaVzUwWDJoaGJtUnNhVzVuWDNCaFoyVS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjcyMjU2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=qNGsy-iKJeSLe5OA9A32Og7KYGX2fktk-QcQkKKEDAQTjdzKtf0EERcWtiTGFUtz-ppI7GrzuBp8cNtygAI~Xl7mvQEe2eCNkRHQUHmZXiDVxIELlDtxonXqFfygX9aJh4QV8oKBrT6muO0fozxmyOrgv2GItC3DHRrLt-9BWJUjnL14wLdzQojS6-5U1gNIyrOMDfs2da~fmeJjmz7oDwAPcbpp40vveFxE3iwUyCCA~x9RPCi5jwWnt7Fd9UVdr~q94Kik1dFSbXzbQ2M2kX7QwIsSzfHGq32GYmFLLtseXWg1URoDbZRRYLAtpYFAzDcg5laj-cwHaRV9j08VCw__)
*Figure 6.1: Vue de la page de gestion des incidents dans Cortex XDR (Source: Documentation officielle Palo Alto Networks)*

La page Incidents est organisée en plusieurs sections:

1. **Barre de filtres**: Située en haut, elle permet de filtrer les incidents selon divers critères (sévérité, statut, période, etc.)
2. **Liste des incidents**: Affiche tous les incidents correspondant aux filtres appliqués
3. **Panneau de détails**: S'ouvre lorsqu'un incident est sélectionné, montrant ses informations détaillées
4. **Barre d'actions**: Propose des actions à effectuer sur les incidents sélectionnés

## 6.2 Anatomie d'un incident dans Cortex XDR

Comme illustré dans la Figure 6.1, un incident dans Cortex XDR représente un ensemble cohérent d'alertes et d'événements liés à une même menace potentielle. Chaque incident comprend:

### Informations générales:
- **ID de l'incident**: Identifiant unique
- **Nom**: Description concise de l'incident
- **Sévérité**: Niveau de gravité (Critique, Élevé, Moyen, Faible)
- **Statut**: État actuel (Nouveau, En cours, Résolu, Fermé)
- **Score**: Valeur numérique reflétant la gravité calculée
- **Étoile**: Marqueur visuel pour les incidents prioritaires

### Détails techniques:
- **Heure de détection**: Date et heure de la première alerte
- **Dernière mise à jour**: Date et heure de la dernière activité
- **Actifs concernés**: Endpoints, utilisateurs ou ressources impliqués
- **Type de menace**: Catégorisation de la menace détectée
- **Alertes associées**: Liste des alertes corrélées dans cet incident
- **Artefacts**: Éléments techniques liés (fichiers, processus, adresses IP, etc.)

### Informations de traitement:
- **Assigné à**: Utilisateur responsable de l'incident
- **Notes**: Commentaires ajoutés par les analystes
- **Actions effectuées**: Historique des actions de remédiation
- **Raison de résolution**: Justification de la clôture (si résolu)

## 6.3 Filtrage et recherche d'incidents

Pour gérer efficacement les incidents, Cortex XDR propose plusieurs options de filtrage et de recherche:

### Filtres prédéfinis:
1. **Par sévérité**: Filtrez par niveau de gravité (Critique, Élevé, Moyen, Faible)
2. **Par statut**: Affichez les incidents selon leur état (Nouveau, En cours, Résolu, Fermé)
3. **Par période**: Limitez l'affichage à une période spécifique (Aujourd'hui, 7 derniers jours, 30 derniers jours, etc.)
4. **Par type**: Filtrez par catégorie de menace (Malware, Exploitation, Reconnaissance, etc.)

### Recherche avancée:
1. Cliquez sur "Advanced Search" ou l'icône de recherche avancée
2. Construisez votre requête en utilisant les opérateurs disponibles:
   - Utilisez `AND`, `OR`, `NOT` pour combiner des critères
   - Spécifiez des champs précis: `severity:critical`, `status:new`
   - Recherchez des textes: `description:"ransomware"`
   - Utilisez des plages: `detection_time:[2023-01-01 TO 2023-01-31]`
3. Enregistrez vos recherches fréquentes pour un accès rapide ultérieur

### Vues personnalisées:
1. Configurez vos filtres selon vos besoins
2. Cliquez sur "Save View" ou l'icône équivalente
3. Donnez un nom à votre vue personnalisée
4. Choisissez si elle doit être privée ou partagée
5. Accédez rapidement à cette vue depuis le menu déroulant des vues

## 6.4 Priorisation avec le système de scoring et starring

Cortex XDR propose deux mécanismes complémentaires pour prioriser les incidents:

### Système de scoring automatique:
Le score d'un incident est calculé automatiquement en fonction de plusieurs facteurs:
- Sévérité des alertes associées
- Nombre d'alertes corrélées
- Criticité des actifs touchés
- Techniques d'attaque identifiées (MITRE ATT&CK)
- Indicateurs de compromission détectés

Plus le score est élevé, plus l'incident est considéré comme grave et prioritaire. Ce score est visible dans la liste des incidents et dans les détails de chaque incident.

### Système de starring manuel:
Le starring permet aux analystes de marquer manuellement les incidents prioritaires:
1. Localisez l'icône d'étoile à côté de l'incident
2. Cliquez sur l'étoile pour marquer l'incident comme prioritaire
3. Cliquez à nouveau pour retirer le marquage

Les incidents marqués d'une étoile apparaissent en haut de la liste et peuvent être filtrés spécifiquement via l'option "Starred Incidents".

### Utilisation combinée:
Pour une priorisation efficace:
1. Utilisez le score automatique comme première indication de gravité
2. Appliquez votre expertise pour évaluer le contexte spécifique
3. Utilisez le starring pour marquer les incidents nécessitant une attention immédiate
4. Créez des vues personnalisées combinant score élevé et starring

## 6.5 Workflow de traitement des incidents

Cortex XDR propose un workflow structuré pour le traitement des incidents:

### Étape 1: Triage initial
1. Examinez les nouveaux incidents en les filtrant par statut "New"
2. Évaluez rapidement la sévérité et le contexte de chaque incident
3. Décidez des actions immédiates:
   - Prioriser pour investigation approfondie
   - Assigner à un analyste spécifique
   - Marquer comme faux positif

### Étape 2: Investigation
1. Ouvrez l'incident pour accéder à ses détails complets
2. Analysez les alertes associées et leur chronologie
3. Examinez les actifs concernés et les artefacts
4. Utilisez les outils d'investigation intégrés:
   - Timeline de l'incident
   - Graphe de causalité
   - Détails des processus et connexions

### Étape 3: Réponse
1. Sélectionnez les actions de réponse appropriées:
   - Isoler un endpoint
   - Bloquer un fichier ou un processus
   - Terminer un processus malveillant
   - Mettre en quarantaine un fichier
2. Documentez les actions entreprises dans les notes de l'incident
3. Mettez à jour le statut de l'incident en "In Progress"

### Étape 4: Résolution
1. Une fois la menace neutralisée, vérifiez qu'aucune trace ne persiste
2. Documentez les conclusions finales et les leçons apprises
3. Sélectionnez "Resolve Incident" et choisissez une raison de résolution:
   - True Positive - Remediated
   - True Positive - Benign
   - False Positive
   - Duplicate
4. Ajoutez des notes détaillées expliquant la résolution

### Étape 5: Suivi et amélioration
1. Analysez régulièrement les incidents résolus pour identifier des tendances
2. Mettez à jour les politiques de sécurité en fonction des leçons apprises
3. Affinez les règles de détection pour réduire les faux positifs similaires
4. Partagez les connaissances acquises avec l'équipe de sécurité

La gestion efficace des incidents est essentielle pour maintenir la sécurité de votre environnement. Dans la section suivante, nous explorerons l'investigation des alertes, qui constituent les éléments de base des incidents.



# 7. Investigation des Alertes - Tutoriel Pratique

## 7.1 Accès à la page Alerts

La page Alerts est le point central pour visualiser, trier et investiguer toutes les alertes générées par Cortex XDR. Pour y accéder:

1. Connectez-vous à la console Cortex XDR
2. Dans la barre de navigation principale, cliquez sur "Alerts"
3. Vous accédez alors à la vue principale des alertes

![Page d'investigation des alertes](https://private-us-east-1.manuscdn.com/sessionFile/IneiHlKkFeKoZw52ZHVaBe/sandbox/N8Zg3ynBYJoUPj4tVTqKHa-images_1749752210086_na1fn_L2hvbWUvdWJ1bnR1L2NvcnRleF94ZHJfbWFudWVsL2ltYWdlc19yZWVsbGVzL2ludmVzdGlnYXRlX2FsZXJ0c19wYWdl.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvSW5laUhsS2tGZUtvWnc1MlpIVmFCZS9zYW5kYm94L044WmczeW5CWUpvVVBqNHRWVHFLSGEtaW1hZ2VzXzE3NDk3NTIyMTAwODZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyTnZjblJsZUY5NFpISmZiV0Z1ZFdWc0wybHRZV2RsYzE5eVpXVnNiR1Z6TDJsdWRtVnpkR2xuWVhSbFgyRnNaWEowYzE5d1lXZGwucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=p6rO1ryqKfvxRvLSRqqJrhtUFQgEoYDwCVJ9hjAZxi~F48Jaw4hbIXDyiVPlWfCcWYZHQSp00mhD5cn4vXAaNGfiQtsyHqFdgL4Gr~NPelIzME~PYpn5cEcL~iNWxBRfBmtH7g12qb7hb0L8VMfy65zdKHY4uqtlg5Pnn3DlREw4wNe08lBR17XnhnqcjIbaAVmq3dDaSalltXtXSbRXYrVmhFMWtWFPcaN23Eu~YPPXNlj96VSeBQ8zKHVW3o4L2w8rSTlBkf~z3xi4PU63YZ45zZTQz29EwfFjsxK9xxV7EuUlu7VlbHSlGbrHNVNVrk3kBC-NkVEuNN3EuDTvzg__)
*Figure 7.1: Vue de la page d'investigation des alertes dans Cortex XDR (Source: Documentation officielle Palo Alto Networks)*

Comme le montre la Figure 7.1, la page Alerts est organisée en plusieurs sections:

1. **Barre de filtres**: Située en haut, elle permet de filtrer les alertes selon divers critères
2. **Liste des alertes**: Affiche toutes les alertes correspondant aux filtres appliqués
3. **Panneau de détails**: S'ouvre lorsqu'une alerte est sélectionnée
4. **Barre d'actions**: Propose des actions à effectuer sur les alertes sélectionnées

## 7.2 Comprendre les différents types d'alertes

Cortex XDR génère plusieurs types d'alertes, chacun correspondant à une source ou un mécanisme de détection spécifique:

### Alertes basées sur les règles
Ces alertes sont déclenchées lorsqu'une activité correspond à une règle de détection prédéfinie:
- **BIOC (Behavioral Indicators of Compromise)**: Détection de comportements suspects
- **IOC (Indicators of Compromise)**: Correspondance avec des indicateurs connus de compromission
- **Règles de corrélation**: Détection de séquences d'événements suspects

### Alertes basées sur l'analyse comportementale
Ces alertes sont générées par les moteurs d'analyse comportementale de Cortex XDR:
- **Analytics**: Détections basées sur le machine learning et l'analyse statistique
- **Anomalies**: Comportements qui dévient significativement des modèles normaux
- **Détections heuristiques**: Basées sur des algorithmes spécialisés

### Alertes provenant des intégrations
Ces alertes sont importées depuis d'autres systèmes de sécurité:
- **Firewalls**: Alertes provenant des pare-feu Palo Alto Networks ou autres
- **SIEM**: Alertes transmises depuis des systèmes SIEM intégrés
- **Threat Intelligence**: Alertes basées sur des flux de renseignements sur les menaces

Chaque type d'alerte est identifié par une icône distinctive et un code couleur reflétant sa sévérité.

## 7.3 Triage et investigation des alertes

Le processus de triage et d'investigation des alertes suit généralement ces étapes:

### Étape 1: Filtrage initial
1. Utilisez les filtres en haut de la page pour affiner votre vue:
   - Par sévérité (Critique, Élevée, Moyenne, Faible)
   - Par statut (Nouvelle, En cours, Résolue)
   - Par source (Endpoint, Réseau, Cloud, etc.)
   - Par période temporelle
2. Créez et enregistrez des vues personnalisées pour vos filtres fréquemment utilisés

### Étape 2: Évaluation rapide
Pour chaque alerte dans la liste filtrée:
1. Observez la sévérité et le type d'alerte
2. Lisez la description concise pour comprendre la nature de la détection
3. Notez les actifs concernés (endpoints, utilisateurs, etc.)
4. Vérifiez si l'alerte fait partie d'un incident plus large

### Étape 3: Investigation détaillée
Pour investiguer une alerte spécifique:
1. Cliquez sur l'alerte pour ouvrir le panneau de détails
2. Examinez les informations complètes:
   - Description détaillée de l'alerte
   - Actifs impliqués
   - Processus et fichiers concernés
   - Connexions réseau associées
   - Utilisateurs impliqués
3. Utilisez les onglets disponibles pour approfondir:
   - "Details": Informations générales sur l'alerte
   - "Timeline": Chronologie des événements liés
   - "Artifacts": Fichiers, processus et autres artefacts techniques
   - "Network": Connexions réseau associées
   - "Similar Alerts": Alertes similaires détectées précédemment

### Étape 4: Actions et documentation
Après investigation:
1. Déterminez si l'alerte est un vrai positif ou un faux positif
2. Pour les vrais positifs:
   - Prenez les mesures de remédiation appropriées
   - Documentez vos observations et actions
   - Créez un incident si nécessaire (si non automatiquement créé)
3. Pour les faux positifs:
   - Documentez pourquoi l'alerte est considérée comme un faux positif
   - Marquez-la comme résolue avec le statut approprié
   - Envisagez d'ajuster les règles de détection si nécessaire

## 7.4 Corrélation entre alertes et incidents

Cortex XDR utilise un moteur de corrélation sophistiqué pour regrouper les alertes liées en incidents cohérents:

### Mécanismes de corrélation automatique
Le système regroupe automatiquement les alertes en incidents selon plusieurs critères:
- Proximité temporelle
- Actifs communs impliqués
- Techniques d'attaque similaires
- Artefacts partagés (fichiers, adresses IP, etc.)
- Utilisateurs concernés

### Visualisation des relations
Pour comprendre la relation entre une alerte et son incident parent:
1. Dans les détails de l'alerte, recherchez la section "Related Incident"
2. Cliquez sur l'ID de l'incident pour accéder à sa vue complète
3. Dans la vue de l'incident, examinez toutes les alertes corrélées dans l'onglet "Alerts"

### Corrélation manuelle
Vous pouvez également associer manuellement des alertes à des incidents:
1. Sélectionnez une ou plusieurs alertes dans la liste
2. Cliquez sur "Actions" puis "Add to Incident"
3. Choisissez un incident existant ou créez-en un nouveau
4. Ajoutez un commentaire expliquant la raison de cette association

## 7.5 Actions possibles sur les alertes

Cortex XDR propose plusieurs actions que vous pouvez effectuer sur les alertes:

### Actions individuelles
Accessibles depuis le panneau de détails d'une alerte:
- **Investigate**: Lancer des outils d'investigation supplémentaires
- **Resolve**: Marquer l'alerte comme résolue
- **Suppress**: Supprimer temporairement les alertes similaires
- **Add Note**: Ajouter un commentaire ou une observation
- **Assign**: Assigner l'alerte à un analyste spécifique

### Actions en lot
Disponibles après sélection de plusieurs alertes:
1. Cochez les cases à côté des alertes concernées
2. Utilisez le menu "Actions" en haut de la liste pour:
   - Résoudre toutes les alertes sélectionnées
   - Les assigner à un analyste
   - Les ajouter à un incident existant ou nouveau
   - Exporter les détails pour analyse externe

### Actions de remédiation
Pour les alertes liées aux endpoints:
1. Dans le panneau de détails, identifiez l'endpoint concerné
2. Cliquez sur l'icône d'actions à côté du nom de l'endpoint
3. Sélectionnez l'action appropriée:
   - Isoler l'endpoint
   - Collecter des fichiers forensiques
   - Terminer un processus malveillant
   - Supprimer ou mettre en quarantaine un fichier

L'investigation efficace des alertes est fondamentale pour maintenir un niveau de sécurité optimal. Dans la section suivante, nous explorerons l'analyse des endpoints, qui constitue une source majeure d'alertes et un point focal pour les actions de remédiation.



# 8. Analyse des Endpoints - Guide Pas à Pas

## 8.1 Vue d'ensemble des endpoints

La section Endpoints de Cortex XDR permet de surveiller, gérer et sécuriser tous les postes de travail, serveurs et appareils mobiles protégés par les agents Cortex XDR. Cette vue centralisée offre une visibilité complète sur l'état de sécurité de votre parc informatique.

Pour accéder à la vue d'ensemble des endpoints:
1. Connectez-vous à la console Cortex XDR
2. Dans la barre de navigation principale, cliquez sur "Endpoints"
3. La page principale affiche un tableau de bord résumant l'état de vos endpoints

La vue d'ensemble des endpoints présente généralement:
- Le nombre total d'endpoints protégés
- La répartition par système d'exploitation
- L'état de connexion des agents (connectés, déconnectés)
- Les endpoints nécessitant une attention (vulnérables, avec alertes actives)
- Les versions d'agents déployées

## 8.2 Déploiement et gestion des agents

Le déploiement et la gestion des agents Cortex XDR sont des étapes essentielles pour assurer une protection optimale de votre environnement.

### Déploiement de nouveaux agents:

1. Dans la section Endpoints, cliquez sur "Deployment" ou "Add Endpoint"
2. Sélectionnez le type d'agent à déployer:
   - Windows
   - macOS
   - Linux
   - Android (si pris en charge)
3. Choisissez la méthode de déploiement:
   - Installation manuelle (téléchargement direct)
   - Déploiement via GPO (pour environnements Windows)
   - Déploiement via MDM (pour appareils mobiles)
   - Installation silencieuse via script
4. Configurez les options de l'agent:
   - Groupe d'endpoints (pour appliquer des politiques spécifiques)
   - Modules à activer (antivirus, EDR, etc.)
   - Paramètres de proxy si nécessaire
5. Générez le package d'installation ou les commandes de déploiement
6. Déployez l'agent selon la méthode choisie

### Gestion des agents existants:

Pour gérer les agents déjà déployés:
1. Accédez à la liste des endpoints dans la section "Endpoints"
2. Utilisez les filtres pour affiner votre vue (OS, groupe, statut, etc.)
3. Sélectionnez un ou plusieurs endpoints
4. Utilisez le menu "Actions" pour:
   - Mettre à jour les agents
   - Modifier les groupes d'appartenance
   - Activer/désactiver des fonctionnalités
   - Désinstaller des agents

## 8.3 Analyse de l'état de santé des endpoints

Cortex XDR fournit des informations détaillées sur l'état de santé de chaque endpoint, vous permettant d'identifier rapidement les problèmes potentiels.

### Indicateurs de santé globaux:

Dans la vue d'ensemble des endpoints, observez:
- Le pourcentage d'endpoints en bonne santé vs problématiques
- Les endpoints avec des alertes actives
- Les endpoints déconnectés ou inactifs
- Les endpoints nécessitant des mises à jour

### Analyse détaillée par endpoint:

Pour analyser l'état de santé d'un endpoint spécifique:
1. Localisez l'endpoint dans la liste
2. Cliquez sur son nom pour ouvrir la vue détaillée
3. Examinez les différentes sections:
   - Informations système (OS, version, spécifications matérielles)
   - État de l'agent (version, modules actifs, dernière connexion)
   - Historique des alertes
   - Vulnérabilités détectées
   - Applications installées
   - Correctifs de sécurité manquants

### Rapports de santé:

Pour générer des rapports sur l'état de santé des endpoints:
1. Dans la section Endpoints, cliquez sur "Reports" ou l'icône équivalente
2. Sélectionnez le type de rapport souhaité:
   - État général des endpoints
   - Rapport de vulnérabilités
   - Conformité des correctifs
   - Inventaire logiciel
3. Configurez les paramètres du rapport (période, groupes d'endpoints, etc.)
4. Générez le rapport au format souhaité (PDF, CSV, etc.)

## 8.4 Investigation d'un endpoint spécifique

Lorsqu'un endpoint est suspect ou impliqué dans un incident, Cortex XDR offre des outils puissants pour l'investiguer en profondeur.

### Accès à la vue détaillée:

1. Localisez l'endpoint concerné dans la liste des endpoints
2. Cliquez sur son nom pour ouvrir la vue détaillée
3. Alternativement, depuis une alerte ou un incident, cliquez sur le nom de l'endpoint impliqué

### Analyse des processus:

Dans la vue détaillée de l'endpoint:
1. Accédez à l'onglet "Processes" ou "Running Processes"
2. Examinez la liste des processus en cours d'exécution
3. Pour chaque processus suspect:
   - Vérifiez son chemin d'exécution et sa signature
   - Examinez sa lignée (processus parent/enfant)
   - Analysez sa consommation de ressources
   - Vérifiez les connexions réseau établies

### Analyse des fichiers:

Pour investiguer les fichiers présents sur l'endpoint:
1. Accédez à l'onglet "Files" ou "File Explorer"
2. Naviguez dans l'arborescence des fichiers ou utilisez la recherche
3. Pour les fichiers suspects:
   - Vérifiez les métadonnées (taille, date de création/modification)
   - Examinez la signature et le hash
   - Vérifiez la réputation du fichier
   - Soumettez le fichier à une analyse approfondie si nécessaire

### Analyse des connexions réseau:

Pour examiner l'activité réseau de l'endpoint:
1. Accédez à l'onglet "Network" ou "Connections"
2. Analysez les connexions actives et récentes
3. Pour chaque connexion suspecte:
   - Identifiez le processus associé
   - Vérifiez l'adresse IP/domaine distant
   - Examinez les ports utilisés
   - Analysez le volume de données échangées

### Timeline d'activité:

Pour comprendre la chronologie des événements:
1. Accédez à l'onglet "Timeline" ou "Activity"
2. Définissez la période d'intérêt
3. Filtrez par type d'événement si nécessaire
4. Analysez la séquence d'événements pour reconstituer l'incident

## 8.5 Actions de remédiation disponibles

Cortex XDR offre diverses actions de remédiation pour répondre aux menaces détectées sur les endpoints.

### Actions immédiates:

Pour les situations urgentes, vous pouvez:
1. Sélectionnez l'endpoint concerné
2. Cliquez sur "Actions" ou l'icône équivalente
3. Choisissez parmi les options disponibles:
   - **Isoler l'endpoint**: Déconnecte l'appareil du réseau tout en maintenant la connexion avec la console Cortex XDR
   - **Redémarrer l'endpoint**: Force un redémarrage de l'appareil
   - **Arrêter l'endpoint**: Éteint l'appareil

### Actions sur les processus:

Pour gérer les processus malveillants:
1. Dans la vue détaillée de l'endpoint, accédez à l'onglet "Processes"
2. Localisez le processus suspect
3. Cliquez sur l'icône d'actions à côté du processus
4. Sélectionnez:
   - **Terminer le processus**: Arrête immédiatement le processus
   - **Ajouter à la liste noire**: Empêche son exécution future
   - **Analyser le processus**: Soumet le processus à une analyse approfondie

### Actions sur les fichiers:

Pour gérer les fichiers malveillants:
1. Dans la vue détaillée de l'endpoint, accédez à l'onglet "Files"
2. Localisez le fichier suspect
3. Cliquez sur l'icône d'actions à côté du fichier
4. Sélectionnez:
   - **Mettre en quarantaine**: Isole le fichier dans un emplacement sécurisé
   - **Supprimer**: Efface définitivement le fichier
   - **Ajouter à la liste noire**: Bloque toute exécution future
   - **Collecter**: Récupère le fichier pour analyse approfondie

### Actions de collecte de données:

Pour les investigations approfondies:
1. Sélectionnez l'endpoint concerné
2. Cliquez sur "Actions" puis "Collect Data" ou l'option équivalente
3. Choisissez le type de collecte:
   - **Triage rapide**: Collecte basique des informations essentielles
   - **Collecte complète**: Acquisition approfondie de données forensiques
   - **Collecte personnalisée**: Sélection précise des éléments à collecter
4. Définissez la période d'intérêt
5. Lancez la collecte et attendez sa complétion
6. Analysez les données collectées dans la console ou exportez-les

### Automatisation des actions:

Pour une réponse cohérente et rapide:
1. Configurez des règles d'automatisation dans la section "Settings" > "Response Actions"
2. Définissez les conditions de déclenchement (type d'alerte, sévérité, etc.)
3. Sélectionnez les actions à exécuter automatiquement
4. Activez la règle et surveillez son efficacité

L'analyse et la gestion efficaces des endpoints sont essentielles pour maintenir un environnement sécurisé. Dans la section suivante, nous explorerons les requêtes XQL, un outil puissant pour l'investigation avancée et la chasse aux menaces.



# 9. Requêtes XQL - Guide Pratique

## 9.1 Introduction au langage XQL

XQL (eXtended Query Language) est le langage de requête propriétaire de Cortex XDR qui permet d'interroger et d'analyser les données collectées à travers votre environnement. Ce langage puissant offre aux analystes de sécurité la possibilité d'effectuer des recherches avancées, de chasser les menaces et de créer des rapports personnalisés.

### Principes fondamentaux de XQL:

XQL est conçu pour être à la fois puissant et accessible:
- Syntaxe inspirée du SQL, familière pour de nombreux professionnels
- Optimisé pour les requêtes de sécurité et l'analyse de logs
- Capable d'interroger des téraoctets de données en quelques secondes
- Adapté à l'analyse multi-sources (endpoints, réseau, cloud)

### Types de données accessibles via XQL:

Les requêtes XQL peuvent interroger diverses sources de données:
- Logs d'événements des endpoints (processus, fichiers, registre, etc.)
- Logs réseau (connexions, DNS, HTTP, etc.)
- Alertes et incidents
- Données cloud (AWS, Azure, GCP)
- Logs d'authentification et d'identité
- Données personnalisées ingérées dans la plateforme

## 9.2 Interface de création de requêtes

L'interface XQL de Cortex XDR offre un environnement complet pour créer, tester et affiner vos requêtes:

### Accès à l'interface XQL:

1. Connectez-vous à la console Cortex XDR
2. Dans la barre de navigation principale, cliquez sur "Query" ou "XQL"
3. L'interface de requête XQL s'affiche, généralement divisée en plusieurs zones:
   - Éditeur de requête (en haut)
   - Résultats de la requête (en bas)
   - Explorateur de schéma (généralement à gauche)
   - Contrôles d'exécution et options (en haut de l'éditeur)

### Composants de l'interface:

#### Éditeur de requête:
- Zone de texte pour saisir et modifier vos requêtes XQL
- Coloration syntaxique pour une meilleure lisibilité
- Auto-complétion pour les noms de tables et de champs
- Numérotation des lignes et indentation automatique

#### Explorateur de schéma:
- Arborescence des tables disponibles
- Description des champs pour chaque table
- Types de données et exemples de valeurs
- Documentation intégrée sur les tables et champs

#### Contrôles d'exécution:
- Bouton "Run" pour exécuter la requête
- Sélecteur de période temporelle
- Options de limitation des résultats
- Boutons pour enregistrer et charger des requêtes

#### Zone de résultats:
- Affichage tabulaire des résultats
- Options de tri et de filtrage
- Visualisations graphiques (selon le type de résultats)
- Options d'exportation des résultats

## 9.3 Exemples de requêtes courantes (avec captures)

Voici quelques exemples de requêtes XQL couramment utilisées pour différents scénarios d'investigation:

### Exemple 1: Recherche de processus suspects

```xql
dataset=xdr_data 
| filter event_type = "PROCESS" 
| filter action_process_image_name = "powershell.exe" 
| filter action_process_image_command_line contains "-enc" 
| fields action_process_image_command_line, actor_process_image_path, hostname 
| limit 100
```

Cette requête recherche les exécutions de PowerShell avec des commandes encodées (potentiellement malveillantes).

### Exemple 2: Détection de connexions réseau suspectes

```xql
dataset=xdr_data 
| filter event_type = "NETWORK" 
| filter (dest_port = 4444 or dest_port = 5555) 
| stats count() by src_ip, dest_ip, dest_port, hostname 
| sort count desc 
| limit 100
```

Cette requête identifie les connexions vers des ports souvent utilisés pour les communications de commande et contrôle.

### Exemple 3: Analyse des échecs d'authentification

```xql
dataset=xdr_data 
| filter event_type = "AUTH" 
| filter action_result = "FAILURE" 
| stats count() as failure_count by hostname, actor_user_name 
| filter failure_count > 5 
| sort failure_count desc
```

Cette requête détecte les tentatives répétées d'authentification échouées, potentiellement indicatives d'une attaque par force brute.

### Exemple 4: Recherche de logiciels non autorisés

```xql
dataset=xdr_data 
| filter event_type = "PROCESS" 
| filter action_process_image_name in ("torrent.exe", "utorrent.exe", "bittorrent.exe") 
| stats count() by hostname, action_process_image_path 
| sort count desc
```

Cette requête identifie les exécutions de logiciels de partage de fichiers potentiellement non autorisés.

### Exemple 5: Détection d'exfiltration de données

```xql
dataset=xdr_data 
| filter event_type = "NETWORK" 
| filter bytes_out > 100000000 
| stats sum(bytes_out) as total_bytes_out by hostname, src_ip, dest_ip 
| sort total_bytes_out desc 
| limit 20
```

Cette requête identifie les transferts sortants volumineux qui pourraient indiquer une exfiltration de données.

## 9.4 Analyse des résultats

Une fois votre requête XQL exécutée, l'analyse efficace des résultats est essentielle:

### Interprétation des résultats tabulaires:

1. **Examinez le nombre total de résultats**:
   - Un nombre très élevé peut indiquer une requête trop large
   - Un nombre nul peut signifier une erreur dans la requête ou l'absence du comportement recherché

2. **Analysez les colonnes clés**:
   - Identifiez les modèles récurrents (mêmes utilisateurs, endpoints, heures)
   - Recherchez les valeurs inhabituelles ou inattendues
   - Comparez avec les comportements normaux connus

3. **Utilisez les fonctionnalités de tri et filtrage**:
   - Triez par colonnes pertinentes (nombre d'occurrences, timestamps)
   - Appliquez des filtres supplémentaires pour affiner l'analyse
   - Groupez les résultats similaires pour identifier des tendances

### Visualisation des résultats:

Selon le type de données, différentes visualisations peuvent être disponibles:
1. **Chronologies**: Pour analyser l'évolution temporelle des événements
2. **Graphiques à barres**: Pour comparer des valeurs numériques
3. **Camemberts**: Pour visualiser des distributions
4. **Graphes de relations**: Pour comprendre les connexions entre entités

Pour activer les visualisations:
1. Exécutez votre requête
2. Dans la zone de résultats, recherchez l'onglet "Visualize" ou l'icône de graphique
3. Sélectionnez le type de visualisation approprié
4. Configurez les axes et paramètres selon vos besoins

### Pivotement et approfondissement:

Pour approfondir votre analyse:
1. **Pivotement**: Cliquez sur une valeur intéressante dans les résultats pour générer automatiquement une nouvelle requête centrée sur cette valeur
2. **Drill-down**: Ajoutez des filtres supplémentaires pour explorer un sous-ensemble spécifique des résultats
3. **Corrélation**: Créez des requêtes complémentaires pour explorer d'autres aspects liés à vos découvertes

## 9.5 Sauvegarde et partage des requêtes

Les requêtes XQL utiles peuvent être sauvegardées et partagées pour une utilisation future:

### Sauvegarde des requêtes:

1. Après avoir créé et testé une requête utile:
   - Cliquez sur "Save" ou l'icône de sauvegarde dans l'interface XQL
   - Donnez un nom descriptif à votre requête
   - Ajoutez une description détaillant son objectif et son fonctionnement
   - Choisissez un dossier ou une catégorie pour l'organiser
   - Définissez les permissions (privée ou partagée)

2. Pour accéder à vos requêtes sauvegardées:
   - Cliquez sur "Saved Queries" ou l'option équivalente
   - Naviguez dans l'arborescence des dossiers
   - Sélectionnez la requête souhaitée pour la charger dans l'éditeur

### Partage des requêtes:

Pour partager une requête avec d'autres analystes:
1. Localisez la requête sauvegardée dans votre liste
2. Cliquez sur l'icône de partage ou l'option "Share"
3. Sélectionnez les utilisateurs ou groupes avec qui partager
4. Définissez les permissions (lecture seule ou modification)
5. Ajoutez un message explicatif si nécessaire
6. Confirmez le partage

### Export et import:

Pour transférer des requêtes entre environnements:
1. **Export**:
   - Sélectionnez la ou les requêtes à exporter
   - Cliquez sur "Export" ou l'option équivalente
   - Choisissez le format (généralement JSON)
   - Enregistrez le fichier d'export

2. **Import**:
   - Dans l'environnement cible, cliquez sur "Import"
   - Sélectionnez le fichier précédemment exporté
   - Confirmez l'import et résolvez les éventuels conflits

### Création de rapports basés sur XQL:

Les requêtes XQL peuvent être transformées en rapports réguliers:
1. Créez et testez votre requête
2. Cliquez sur "Create Report" ou l'option équivalente
3. Configurez les paramètres du rapport:
   - Nom et description
   - Fréquence (quotidienne, hebdomadaire, mensuelle)
   - Format (PDF, CSV, etc.)
   - Destinataires
4. Activez le rapport programmé

La maîtrise de XQL est un atout majeur pour les analystes de sécurité utilisant Cortex XDR. Dans la section suivante, nous explorerons la configuration et l'administration de la plateforme pour optimiser son fonctionnement.



# 10. Configuration et Administration

## 10.1 Gestion des utilisateurs et des rôles

La gestion efficace des utilisateurs et des rôles est essentielle pour maintenir la sécurité et l'efficacité opérationnelle de votre déploiement Cortex XDR.

### Accès à la gestion des utilisateurs:

1. Connectez-vous à la console Cortex XDR avec un compte administrateur
2. Accédez à "Settings" ou "Administration" dans le menu principal
3. Sélectionnez "User Management" ou "Users & Roles"

### Création de nouveaux utilisateurs:

Pour ajouter un nouvel utilisateur:
1. Dans la section de gestion des utilisateurs, cliquez sur "Add User" ou "+"
2. Renseignez les informations requises:
   - Nom d'utilisateur (généralement l'adresse email)
   - Nom complet
   - Informations de contact
   - Rôle(s) attribué(s)
   - Groupes d'appartenance (facultatif)
3. Choisissez la méthode d'authentification:
   - Authentification locale (mot de passe défini dans Cortex XDR)
   - Authentification externe (SAML, LDAP, etc.)
4. Définissez les options supplémentaires:
   - Exigence de changement de mot de passe à la première connexion
   - Authentification à deux facteurs
   - Période d'expiration du compte (si applicable)
5. Cliquez sur "Save" ou "Create" pour finaliser

### Gestion des rôles:

Cortex XDR utilise un système de contrôle d'accès basé sur les rôles (RBAC) pour définir les permissions:

1. Pour accéder à la gestion des rôles:
   - Dans la section d'administration, sélectionnez "Roles" ou "Role Management"
   
2. Rôles prédéfinis typiques:
   - **Administrator**: Accès complet à toutes les fonctionnalités
   - **SOC Manager**: Supervision des incidents et alertes, accès aux rapports
   - **SOC Analyst**: Investigation des incidents et alertes, actions de remédiation
   - **Read-Only**: Visualisation sans capacité de modification
   - **Endpoint Administrator**: Gestion des agents et politiques endpoint

3. Création d'un rôle personnalisé:
   - Cliquez sur "Add Role" ou "Create Custom Role"
   - Donnez un nom et une description au rôle
   - Configurez les permissions spécifiques:
     * Accès en lecture/écriture par module
     * Capacité à exécuter des actions spécifiques
     * Restrictions sur certaines fonctionnalités
   - Définissez la portée du rôle (tous les endpoints ou groupes spécifiques)
   - Enregistrez le nouveau rôle

### Groupes d'utilisateurs:

Pour simplifier la gestion des permissions:
1. Créez des groupes logiques (par équipe, fonction, région, etc.)
2. Assignez des rôles aux groupes plutôt qu'aux utilisateurs individuels
3. Gérez l'appartenance aux groupes pour modifier rapidement les permissions

### Bonnes pratiques de gestion des utilisateurs:

- Appliquez le principe du moindre privilège (attribuez uniquement les permissions nécessaires)
- Révisez régulièrement les comptes et permissions
- Activez l'authentification à deux facteurs pour tous les comptes
- Configurez des politiques de mot de passe robustes
- Intégrez avec votre solution d'identité d'entreprise (SSO) si possible

## 10.2 Configuration des politiques de sécurité

Les politiques de sécurité définissent comment Cortex XDR protège votre environnement et répond aux menaces détectées.

### Accès aux politiques de sécurité:

1. Dans la console Cortex XDR, accédez à "Settings" ou "Administration"
2. Sélectionnez "Security Policies" ou "Protection Policies"

### Types de politiques:

#### Politiques de protection des endpoints:
Ces politiques définissent comment les agents Cortex XDR protègent les endpoints:

1. **Politiques antimalware**:
   - Configuration des analyses (temps réel, programmées, à la demande)
   - Définition des actions automatiques (mise en quarantaine, blocage, alerte)
   - Exclusions (fichiers, dossiers, processus)

2. **Politiques comportementales**:
   - Détection d'exploitation
   - Protection contre le ransomware
   - Détection d'élévation de privilèges
   - Surveillance des scripts et macros

3. **Politiques de contrôle des périphériques**:
   - Gestion des périphériques USB et amovibles
   - Restrictions sur les types de périphériques autorisés
   - Actions lors de la connexion de périphériques

#### Politiques de réponse:
Ces politiques définissent les actions automatiques en réponse aux menaces:

1. **Règles d'automatisation**:
   - Conditions de déclenchement (type d'alerte, sévérité, etc.)
   - Actions à exécuter (isolation, collecte de données, etc.)
   - Notifications à envoyer

2. **Politiques d'escalade**:
   - Définition des niveaux d'escalade
   - Délais avant escalade
   - Destinataires des notifications

### Création et modification de politiques:

Pour créer une nouvelle politique:
1. Dans la section des politiques, cliquez sur "Add Policy" ou "Create New"
2. Sélectionnez le type de politique à créer
3. Configurez les paramètres spécifiques à ce type de politique
4. Définissez la portée d'application:
   - Tous les endpoints
   - Groupes d'endpoints spécifiques
   - Systèmes d'exploitation spécifiques
5. Définissez la priorité si plusieurs politiques peuvent s'appliquer
6. Activez la politique et enregistrez-la

### Gestion des exceptions:

Pour gérer les cas particuliers:
1. Créez des listes d'exclusion pour les fichiers légitimes souvent détectés à tort
2. Définissez des exceptions pour des applications ou processus spécifiques
3. Documentez toutes les exceptions avec leur justification et durée prévue

## 10.3 Paramètres de notification

Les paramètres de notification déterminent comment et quand les utilisateurs sont informés des événements importants.

### Configuration des notifications:

1. Accédez à "Settings" > "Notifications" ou section équivalente
2. Configurez les différents canaux de notification:
   - Email
   - SMS
   - Webhooks (pour intégration avec d'autres systèmes)
   - Notifications dans la console

### Types d'événements notifiables:

Configurez quels événements déclenchent des notifications:
1. **Alertes et incidents**:
   - Nouveaux incidents de haute sévérité
   - Alertes spécifiques
   - Modifications du statut des incidents

2. **État du système**:
   - Problèmes de connectivité des agents
   - Dépassement des quotas de données
   - Mises à jour disponibles

3. **Actions administratives**:
   - Modifications de configuration
   - Création/suppression d'utilisateurs
   - Changements de politiques

### Personnalisation par utilisateur:

Permettez aux utilisateurs de personnaliser leurs préférences:
1. Chaque utilisateur peut accéder à ses préférences de notification
2. Options typiques:
   - Canaux préférés par type d'événement
   - Seuils de sévérité pour les notifications
   - Plages horaires pour recevoir des notifications

## 10.4 Configuration des sauvegardes

La sauvegarde régulière de la configuration de Cortex XDR est essentielle pour assurer la continuité opérationnelle.

### Éléments à sauvegarder:

1. **Configuration système**:
   - Paramètres généraux
   - Politiques de sécurité
   - Règles d'automatisation

2. **Données utilisateur**:
   - Comptes et rôles
   - Dashboards personnalisés
   - Requêtes XQL sauvegardées

3. **Intégrations**:
   - Configurations des connecteurs
   - Paramètres d'API
   - Webhooks

### Procédure de sauvegarde:

1. Accédez à "Settings" > "System" > "Backup & Restore" ou section équivalente
2. Sélectionnez les éléments à inclure dans la sauvegarde
3. Choisissez la destination:
   - Téléchargement local
   - Stockage cloud configuré
   - Serveur SFTP
4. Définissez les options de chiffrement si disponibles
5. Lancez la sauvegarde manuelle ou configurez une planification

### Planification des sauvegardes:

Pour les sauvegardes automatiques:
1. Définissez la fréquence (quotidienne, hebdomadaire)
2. Choisissez l'heure d'exécution (préférablement hors heures de pointe)
3. Configurez la rétention (nombre de sauvegardes à conserver)
4. Activez les notifications de réussite/échec

### Procédure de restauration:

En cas de besoin:
1. Accédez à "Settings" > "System" > "Backup & Restore"
2. Sélectionnez "Restore" ou option équivalente
3. Choisissez le fichier de sauvegarde à restaurer
4. Sélectionnez les éléments spécifiques à restaurer si nécessaire
5. Confirmez et lancez la restauration
6. Vérifiez l'intégrité du système après restauration

## 10.5 Gestion des mises à jour

Maintenir Cortex XDR à jour est crucial pour bénéficier des dernières fonctionnalités et protections.

### Types de mises à jour:

1. **Mises à jour de la console**:
   - Nouvelles fonctionnalités
   - Améliorations de l'interface
   - Corrections de bugs

2. **Mises à jour des agents**:
   - Nouvelles capacités de détection
   - Améliorations de performance
   - Correctifs de sécurité

3. **Mises à jour des contenus de sécurité**:
   - Signatures antimalware
   - Règles de détection comportementale
   - Indicateurs de compromission

### Vérification des mises à jour disponibles:

1. Accédez à "Settings" > "Updates" ou section équivalente
2. Consultez les mises à jour disponibles pour:
   - La console
   - Les agents par plateforme
   - Les contenus de sécurité

### Processus de mise à jour:

#### Pour la console:
1. Planifiez la mise à jour pendant une période de faible activité
2. Informez les utilisateurs du temps d'indisponibilité prévu
3. Effectuez une sauvegarde complète avant la mise à jour
4. Lancez la mise à jour depuis la section dédiée
5. Vérifiez le bon fonctionnement après la mise à jour

#### Pour les agents:
1. Testez d'abord sur un groupe pilote d'endpoints
2. Configurez la stratégie de déploiement:
   - Immédiate pour les mises à jour critiques
   - Progressive par groupes pour les mises à jour majeures
   - Planifiée pendant les heures creuses
3. Surveillez le déploiement et les éventuels problèmes
4. Vérifiez que tous les agents sont bien mis à jour

### Gestion des versions:

Pour une administration efficace:
1. Documentez les versions déployées (console et agents)
2. Consultez les notes de version avant chaque mise à jour
3. Maintenez une politique claire sur les délais d'application des mises à jour
4. Prévoyez une procédure de rollback en cas de problème

La configuration et l'administration appropriées de Cortex XDR sont essentielles pour maximiser la valeur de la plateforme. Dans la section suivante, nous explorerons les intégrations et connecteurs qui permettent d'étendre les capacités de Cortex XDR.



# 11. Intégrations et Connecteurs

## 11.1 Vue d'ensemble des intégrations disponibles

Cortex XDR offre de nombreuses possibilités d'intégration avec d'autres solutions de sécurité et systèmes d'entreprise, permettant d'étendre ses capacités et de créer un écosystème de cybersécurité unifié.

### Catégories d'intégrations:

1. **Intégrations avec d'autres produits Palo Alto Networks**:
   - Prisma Cloud pour la sécurité cloud
   - Prisma Access pour la sécurité SASE
   - Firewalls de nouvelle génération (NGFW)
   - Prisma SD-WAN

2. **Intégrations avec des solutions tierces**:
   - Solutions SIEM (Splunk, IBM QRadar, Microsoft Sentinel)
   - Plateformes SOAR (Demisto, Phantom, ServiceNow SecOps)
   - Solutions de gestion des vulnérabilités
   - Systèmes de ticketing et ITSM (ServiceNow, Jira)

3. **Intégrations cloud**:
   - AWS Security Hub
   - Microsoft Azure Sentinel
   - Google Cloud Security Command Center
   - Office 365 Security

4. **Intégrations de Threat Intelligence**:
   - MISP
   - ThreatConnect
   - Recorded Future
   - VirusTotal

### Méthodes d'intégration:

Cortex XDR propose plusieurs mécanismes d'intégration:
- API REST complète
- Webhooks pour les notifications en temps réel
- Connecteurs prédéfinis pour les solutions courantes
- Formats d'export standardisés (STIX/TAXII, CEF, JSON)

## 11.2 Configuration des intégrations SIEM/SOAR

L'intégration de Cortex XDR avec des solutions SIEM (Security Information and Event Management) et SOAR (Security Orchestration, Automation and Response) permet de centraliser la gestion des incidents et d'automatiser les workflows de réponse.

### Intégration avec les SIEM:

#### Étapes générales de configuration:
1. Accédez à "Settings" > "Integrations" ou section équivalente
2. Sélectionnez "SIEM Integrations" ou l'option spécifique à votre SIEM
3. Configurez les paramètres de connexion:
   - URL du serveur SIEM
   - Informations d'authentification
   - Format des données (CEF, JSON, Syslog)
4. Sélectionnez les types d'événements à transmettre:
   - Alertes
   - Incidents
   - Activités des endpoints
   - Événements d'audit
5. Définissez la fréquence de synchronisation
6. Testez la connexion et validez la réception des données

#### Exemple: Intégration avec Splunk
1. Installez l'application Cortex XDR sur votre instance Splunk
2. Configurez un index dédié pour les données Cortex XDR
3. Dans Cortex XDR, configurez l'intégration Splunk:
   - URL du collecteur HTTP (HEC)
   - Token HEC
   - Format des événements
4. Validez la réception des données dans Splunk
5. Configurez les tableaux de bord et alertes dans Splunk

### Intégration avec les plateformes SOAR:

#### Étapes générales de configuration:
1. Accédez à "Settings" > "Integrations" > "SOAR"
2. Sélectionnez votre plateforme SOAR
3. Configurez les paramètres de connexion:
   - URL de l'API SOAR
   - Clés d'API ou informations d'authentification
   - Paramètres de proxy si nécessaire
4. Définissez les règles de transmission:
   - Types d'incidents à transmettre
   - Seuils de sévérité
   - Enrichissement des données
5. Configurez la synchronisation bidirectionnelle:
   - Mise à jour des statuts d'incidents
   - Commentaires et notes
   - Actions de remédiation

#### Exemple: Intégration avec Cortex XSOAR (anciennement Demisto)
1. Dans XSOAR, installez et configurez l'intégration Cortex XDR
2. Créez une instance d'intégration avec les informations d'API de votre tenant XDR
3. Dans Cortex XDR, configurez l'intégration XSOAR
4. Testez la création d'un incident dans les deux directions
5. Configurez les playbooks d'automatisation dans XSOAR

## 11.3 Intégration avec les solutions cloud

L'intégration de Cortex XDR avec les environnements cloud permet d'étendre la visibilité et la protection aux ressources cloud.

### Intégration avec AWS:

1. **Prérequis**:
   - Compte AWS avec permissions administratives
   - Accès à AWS CloudTrail et AWS Config

2. **Étapes de configuration**:
   - Dans Cortex XDR, accédez à "Settings" > "Cloud Integrations" > "AWS"
   - Suivez l'assistant de configuration:
     * Créez un rôle IAM avec les permissions requises
     * Configurez les paramètres de collecte de logs
     * Sélectionnez les régions à surveiller
   - Validez la connexion et vérifiez la collecte des données

3. **Fonctionnalités activées**:
   - Surveillance des instances EC2
   - Détection des configurations à risque
   - Analyse des logs CloudTrail
   - Corrélation entre activités cloud et endpoints

### Intégration avec Microsoft Azure:

1. **Prérequis**:
   - Abonnement Azure avec droits administratifs
   - Azure Monitor configuré

2. **Étapes de configuration**:
   - Dans Cortex XDR, accédez à "Settings" > "Cloud Integrations" > "Azure"
   - Suivez l'assistant de configuration:
     * Créez une application Azure AD pour l'authentification
     * Configurez les permissions nécessaires
     * Sélectionnez les abonnements à surveiller
   - Validez la connexion et vérifiez la collecte des données

3. **Fonctionnalités activées**:
   - Surveillance des machines virtuelles
   - Analyse des journaux d'activité Azure
   - Détection des configurations à risque
   - Protection des identités Azure AD

### Intégration avec Google Cloud Platform:

1. **Prérequis**:
   - Projet GCP avec droits administratifs
   - API Cloud Logging activée

2. **Étapes de configuration**:
   - Dans Cortex XDR, accédez à "Settings" > "Cloud Integrations" > "GCP"
   - Suivez l'assistant de configuration:
     * Créez un compte de service avec les permissions requises
     * Configurez les paramètres de collecte de logs
     * Sélectionnez les projets à surveiller
   - Validez la connexion et vérifiez la collecte des données

3. **Fonctionnalités activées**:
   - Surveillance des instances Compute Engine
   - Analyse des journaux d'audit
   - Détection des configurations à risque
   - Visibilité sur les conteneurs et Kubernetes

## 11.4 Intégration avec les solutions de Threat Intelligence

L'intégration de sources de Threat Intelligence externe enrichit les capacités de détection de Cortex XDR avec des informations sur les menaces connues.

### Configuration des sources de Threat Intelligence:

1. Accédez à "Settings" > "Integrations" > "Threat Intelligence"
2. Sélectionnez "Add Source" ou option équivalente
3. Choisissez le type de source:
   - Flux STIX/TAXII
   - API propriétaire
   - Import de fichiers (CSV, JSON)
4. Configurez les paramètres spécifiques:
   - URL du service
   - Informations d'authentification
   - Collections ou flux à utiliser
5. Définissez la fréquence de mise à jour
6. Configurez les types d'indicateurs à importer:
   - Hashes de fichiers
   - URLs et domaines
   - Adresses IP
   - Autres indicateurs techniques

### Utilisation des données de Threat Intelligence:

Une fois configurées, les données de Threat Intelligence sont utilisées pour:
1. **Enrichissement des alertes**:
   - Ajout de contexte sur les menaces détectées
   - Évaluation de la réputation des entités
   - Liens vers des rapports détaillés

2. **Détection proactive**:
   - Recherche d'indicateurs connus dans votre environnement
   - Création d'alertes basées sur les correspondances
   - Blocage automatique des entités malveillantes connues

3. **Investigation**:
   - Enrichissement des artefacts lors des investigations
   - Visualisation des relations entre indicateurs
   - Évaluation de la sévérité basée sur le contexte de la menace

## 11.5 Développement d'intégrations personnalisées

Pour les besoins spécifiques non couverts par les intégrations prédéfinies, Cortex XDR offre des possibilités de développement d'intégrations personnalisées.

### Utilisation de l'API Cortex XDR:

1. **Accès à l'API**:
   - Dans Cortex XDR, accédez à "Settings" > "API Keys"
   - Créez une nouvelle clé API avec les permissions appropriées
   - Notez l'ID de clé et la clé secrète

2. **Documentation de l'API**:
   - Consultez la documentation officielle de l'API Cortex XDR
   - Familiarisez-vous avec les endpoints disponibles
   - Comprenez les mécanismes d'authentification et les limites de taux

3. **Développement d'intégrations**:
   - Utilisez les bibliothèques client disponibles (Python, etc.)
   - Implémentez l'authentification avec votre clé API
   - Développez les fonctionnalités requises:
     * Récupération d'alertes et incidents
     * Exécution d'actions de remédiation
     * Collecte de données forensiques
     * Mise à jour de statuts

### Utilisation des webhooks:

Pour les notifications en temps réel:
1. Configurez un endpoint HTTP dans votre application
2. Dans Cortex XDR, accédez à "Settings" > "Webhooks"
3. Créez un nouveau webhook:
   - URL de votre endpoint
   - Secret partagé pour la validation
   - Types d'événements à notifier
4. Implémentez la logique de traitement dans votre application
5. Testez la réception et le traitement des notifications

### Bonnes pratiques pour les intégrations personnalisées:

1. **Sécurité**:
   - Stockez les clés API de manière sécurisée
   - Utilisez HTTPS pour toutes les communications
   - Implémentez la validation des webhooks
   - Limitez les permissions au strict nécessaire

2. **Fiabilité**:
   - Implémentez une gestion robuste des erreurs
   - Prévoyez des mécanismes de retry
   - Surveillez les performances et la disponibilité
   - Mettez en place des alertes en cas de problème

3. **Maintenance**:
   - Documentez votre intégration
   - Prévoyez des tests automatisés
   - Suivez les mises à jour de l'API
   - Planifiez des revues régulières

Les intégrations étendent considérablement les capacités de Cortex XDR et permettent de l'incorporer dans votre écosystème de sécurité global. Dans la section suivante, nous explorerons les bonnes pratiques et optimisations pour tirer le meilleur parti de votre déploiement Cortex XDR.



# 12. Bonnes Pratiques et Optimisation

## 12.1 Optimisation des performances

Pour garantir un fonctionnement optimal de Cortex XDR dans votre environnement, plusieurs aspects peuvent être optimisés.

### Optimisation de la console:

1. **Gestion des données**:
   - Configurez des politiques de rétention adaptées à vos besoins et contraintes
   - Archivez régulièrement les données historiques peu consultées
   - Utilisez des filtres efficaces pour limiter le volume de données chargées

2. **Performance du navigateur**:
   - Utilisez un navigateur récent et à jour (Chrome, Firefox, Edge)
   - Évitez d'ouvrir trop d'onglets simultanément dans la console
   - Videz régulièrement le cache du navigateur
   - Disposez d'au moins 8 Go de RAM sur les postes des analystes

3. **Dashboards et requêtes**:
   - Limitez le nombre de widgets par dashboard
   - Optimisez les requêtes XQL en ajoutant des filtres pertinents
   - Évitez les requêtes trop larges sur de longues périodes
   - Programmez les rapports lourds pendant les heures creuses

### Optimisation des agents:

1. **Ressources système**:
   - Assurez-vous que les endpoints respectent les prérequis minimaux
   - Surveillez l'utilisation CPU et mémoire des agents
   - Ajustez les paramètres de scan pour les systèmes moins puissants

2. **Configuration réseau**:
   - Optimisez la bande passante utilisée par les agents
   - Configurez des proxys locaux pour les déploiements distribués
   - Définissez des politiques de synchronisation adaptées aux contraintes réseau

3. **Modules et fonctionnalités**:
   - Activez uniquement les modules nécessaires sur chaque endpoint
   - Adaptez la fréquence des scans selon la criticité des systèmes
   - Utilisez des profils de configuration différenciés selon les types d'endpoints

### Optimisation du stockage:

1. **Gestion des logs**:
   - Définissez des politiques de rétention par type de données
   - Configurez l'agrégation pour les événements répétitifs
   - Exportez les données historiques vers des solutions de stockage à long terme

2. **Collecte sélective**:
   - Ajustez la verbosité de la collecte selon les besoins
   - Limitez la collecte détaillée aux systèmes critiques
   - Filtrez les événements de faible valeur dès la source

## 12.2 Réduction des faux positifs

La réduction des faux positifs est essentielle pour maintenir l'efficacité opérationnelle de votre équipe de sécurité.

### Analyse des faux positifs:

1. **Identification systématique**:
   - Documentez chaque faux positif identifié
   - Analysez les caractéristiques communes
   - Recherchez des modèles récurrents

2. **Catégorisation**:
   - Classez les faux positifs par type (comportemental, signature, etc.)
   - Identifiez les sources les plus problématiques
   - Évaluez l'impact opérationnel de chaque catégorie

### Stratégies de réduction:

1. **Ajustement des règles**:
   - Affinez les seuils de détection
   - Modifiez les conditions de déclenchement
   - Ajoutez des critères supplémentaires pour améliorer la précision

2. **Création d'exceptions**:
   - Définissez des exceptions pour les applications légitimes souvent détectées
   - Créez des listes blanches pour les processus métier spécifiques
   - Documentez toutes les exceptions avec leur justification

3. **Apprentissage et amélioration continue**:
   - Utilisez le feedback des analystes pour améliorer les détections
   - Analysez régulièrement les statistiques de faux positifs
   - Mettez à jour les règles et exceptions en fonction des résultats

### Processus de gestion:

1. **Workflow de validation**:
   - Établissez un processus formel pour confirmer les faux positifs
   - Exigez une validation par un second analyste pour les cas ambigus
   - Documentez la justification de chaque classification

2. **Révision périodique**:
   - Examinez régulièrement les exceptions et listes blanches
   - Vérifiez que les justifications sont toujours valides
   - Supprimez les exceptions obsolètes

3. **Mesure et suivi**:
   - Suivez le taux de faux positifs dans le temps
   - Mesurez l'impact des ajustements effectués
   - Fixez des objectifs d'amélioration continue

## 12.3 Stratégies de déploiement efficaces

Un déploiement bien planifié et exécuté est fondamental pour le succès de Cortex XDR.

### Planification du déploiement:

1. **Évaluation initiale**:
   - Inventoriez votre environnement (endpoints, systèmes d'exploitation, etc.)
   - Identifiez les systèmes critiques et sensibles
   - Évaluez les contraintes techniques et organisationnelles

2. **Définition du périmètre**:
   - Déterminez les phases de déploiement
   - Priorisez les systèmes à protéger
   - Définissez les objectifs de couverture

3. **Préparation technique**:
   - Vérifiez la compatibilité des systèmes
   - Préparez l'infrastructure nécessaire
   - Testez dans un environnement de préproduction

### Approche par phases:

1. **Phase pilote**:
   - Déployez sur un groupe restreint d'endpoints non critiques
   - Incluez différents types de systèmes pour une représentativité maximale
   - Collectez les retours d'expérience et ajustez la configuration

2. **Déploiement progressif**:
   - Étendez par groupes logiques (départements, sites, etc.)
   - Surveillez attentivement les performances et les problèmes
   - Ajustez la stratégie en fonction des résultats

3. **Finalisation**:
   - Complétez le déploiement sur tous les systèmes planifiés
   - Documentez les exceptions et les systèmes exclus
   - Établissez les processus de maintenance continue

### Gestion du changement:

1. **Communication**:
   - Informez les utilisateurs et les équipes IT à l'avance
   - Expliquez les bénéfices et l'impact potentiel
   - Fournissez des points de contact pour les questions

2. **Formation**:
   - Formez l'équipe de sécurité à l'utilisation de la console
   - Préparez le support technique de premier niveau
   - Documentez les procédures opérationnelles

3. **Suivi post-déploiement**:
   - Organisez des sessions de retour d'expérience
   - Identifiez les problèmes récurrents
   - Partagez les bonnes pratiques identifiées

## 12.4 Maintenance et surveillance

Une maintenance régulière est nécessaire pour garantir l'efficacité continue de Cortex XDR.

### Surveillance quotidienne:

1. **Vérifications de routine**:
   - État de connexion des agents
   - Fonctionnement des intégrations
   - Performances du système

2. **Alertes opérationnelles**:
   - Configurez des alertes pour les problèmes de fonctionnement
   - Surveillez les déconnexions massives d'agents
   - Vérifiez les échecs de synchronisation

3. **Tableau de bord opérationnel**:
   - Créez un dashboard dédié à la santé du système
   - Incluez des indicateurs clés de performance
   - Affichez les tendances pour identifier les dégradations progressives

### Maintenance périodique:

1. **Mises à jour**:
   - Planifiez des fenêtres régulières pour les mises à jour
   - Testez les nouvelles versions avant déploiement général
   - Maintenez une matrice de compatibilité à jour

2. **Nettoyage des données**:
   - Archivez ou supprimez les données obsolètes
   - Optimisez les bases de données si nécessaire
   - Vérifiez l'utilisation du stockage

3. **Révision des configurations**:
   - Examinez régulièrement les politiques et règles
   - Mettez à jour les listes d'exceptions
   - Ajustez les paramètres selon l'évolution des besoins

### Audits et optimisation:

1. **Audits de couverture**:
   - Vérifiez que tous les systèmes prévus sont protégés
   - Identifiez les endpoints sans agent ou avec agents obsolètes
   - Comparez avec l'inventaire des actifs

2. **Audits de configuration**:
   - Vérifiez l'alignement avec les politiques de sécurité
   - Identifiez les déviations par rapport aux standards
   - Corrigez les configurations non conformes

3. **Optimisation continue**:
   - Analysez les performances et l'utilisation des ressources
   - Identifiez les opportunités d'amélioration
   - Implémentez les ajustements nécessaires

## 12.5 Checklist de configuration recommandée

Cette checklist vous aidera à vous assurer que votre déploiement Cortex XDR est correctement configuré et optimisé.

### Configuration de base:

- [ ] Console accessible uniquement via HTTPS
- [ ] Authentification forte activée pour tous les utilisateurs
- [ ] Rôles et permissions configurés selon le principe du moindre privilège
- [ ] Politiques de mot de passe conformes aux standards de l'organisation
- [ ] Notifications configurées pour les événements critiques
- [ ] Sauvegardes régulières de la configuration

### Configuration des agents:

- [ ] Dernière version des agents déployée
- [ ] Groupes d'endpoints logiques créés
- [ ] Politiques de protection adaptées à chaque groupe
- [ ] Exclusions configurées pour les applications métier légitimes
- [ ] Paramètres de performance ajustés selon les capacités des endpoints
- [ ] Mécanisme de mise à jour automatique configuré

### Configuration de la détection:

- [ ] Modules de protection activés selon les besoins
- [ ] Règles de détection personnalisées créées pour les menaces spécifiques
- [ ] Seuils de détection ajustés pour limiter les faux positifs
- [ ] Intégrations de Threat Intelligence configurées
- [ ] Corrélation d'alertes optimisée
- [ ] Règles d'automatisation testées et validées

### Configuration des réponses:

- [ ] Playbooks de réponse définis pour les incidents courants
- [ ] Actions automatiques configurées pour les menaces connues
- [ ] Procédures d'escalade documentées
- [ ] Intégrations avec les systèmes de ticketing
- [ ] Workflows de remédiation testés
- [ ] Permissions pour les actions de réponse correctement attribuées

### Configuration du reporting:

- [ ] Dashboards personnalisés créés pour différents publics
- [ ] Rapports périodiques configurés
- [ ] Métriques de performance et d'efficacité définies
- [ ] Rapports de conformité automatisés
- [ ] Distribution des rapports configurée
- [ ] Formats d'export adaptés aux besoins

L'application de ces bonnes pratiques et optimisations vous permettra de maximiser la valeur de votre investissement dans Cortex XDR et d'améliorer significativement votre posture de sécurité. Dans la section suivante, nous explorerons des cas d'usage concrets avec des tutoriels visuels détaillés.



# 13. Cas d'Usage Concrets - Tutoriels Visuels

## 13.1 Détection et analyse d'un malware

Ce cas d'usage illustre comment Cortex XDR détecte, analyse et permet de répondre à une infection par malware.

### Scénario:
Un poste de travail a exécuté un fichier malveillant reçu par email, déclenchant une alerte dans Cortex XDR.

### Étape 1: Identification de l'alerte

1. Connectez-vous à la console Cortex XDR
2. Observez la notification d'alerte sur le dashboard principal
3. Cliquez sur l'alerte pour accéder aux détails

L'alerte affiche les informations essentielles:
- Type de menace détectée (malware)
- Endpoint concerné
- Utilisateur connecté
- Heure de détection
- Sévérité de la menace

### Étape 2: Analyse initiale

1. Dans la vue détaillée de l'alerte, examinez:
   - Le nom et le type du malware détecté
   - Le fichier incriminé (nom, chemin, hash)
   - Le processus d'exécution
   - Les actions entreprises automatiquement (blocage, quarantaine)

2. Vérifiez si l'alerte fait partie d'un incident plus large:
   - Recherchez la section "Related Incident"
   - Si présent, cliquez sur l'ID d'incident pour voir le contexte global

### Étape 3: Investigation approfondie

1. Depuis la vue de l'alerte ou de l'incident, cliquez sur "Investigate" ou l'option équivalente

2. Analysez la chronologie des événements:
   - Comment le fichier est arrivé sur le système
   - Qui l'a exécuté et quand
   - Quelles actions le malware a tenté d'effectuer

3. Examinez le graphe de causalité:
   - Processus parent et enfants
   - Fichiers créés ou modifiés
   - Connexions réseau établies
   - Modifications du registre

4. Vérifiez si d'autres systèmes sont affectés:
   - Utilisez la recherche XQL pour trouver des occurrences similaires
   - Exemple de requête:
     ```xql
     dataset=xdr_data 
     | filter file_sha256 = "[hash du fichier malveillant]" 
     | stats count() by hostname
     ```

### Étape 4: Actions de remédiation

1. Isolez l'endpoint si nécessaire:
   - Dans la vue de l'incident, localisez l'endpoint concerné
   - Cliquez sur "Actions" > "Isolate Endpoint"
   - Confirmez l'action

2. Collectez des preuves forensiques:
   - Sélectionnez "Actions" > "Collect Data"
   - Choisissez les éléments à collecter
   - Lancez la collecte

3. Supprimez ou mettez en quarantaine les fichiers malveillants:
   - Dans la vue des artefacts, localisez le fichier
   - Sélectionnez "Actions" > "Quarantine File" ou "Delete File"
   - Confirmez l'action

4. Vérifiez l'efficacité des actions:
   - Exécutez un scan complet de l'endpoint
   - Surveillez les nouvelles alertes
   - Vérifiez les logs système

### Étape 5: Documentation et clôture

1. Documentez l'incident:
   - Ajoutez des notes détaillant l'analyse et les actions entreprises
   - Attachez des preuves pertinentes

2. Mettez à jour le statut:
   - Changez le statut de l'incident en "In Progress" puis "Resolved"
   - Sélectionnez la raison appropriée (ex: "True Positive - Remediated")
   - Ajoutez des commentaires de clôture

3. Identifiez les mesures préventives:
   - Mettez à jour les politiques de sécurité si nécessaire
   - Créez des règles de détection personnalisées pour des menaces similaires
   - Planifiez des formations de sensibilisation si l'incident résulte d'une erreur utilisateur

## 13.2 Investigation d'une attaque par mouvement latéral

Ce cas d'usage montre comment utiliser Cortex XDR pour détecter et analyser une attaque impliquant un mouvement latéral dans le réseau.

### Scénario:
Un attaquant a compromis un système initial et tente de se déplacer latéralement vers d'autres systèmes du réseau.

### Étape 1: Détection de l'activité suspecte

1. Un incident de sévérité élevée apparaît dans le dashboard Cortex XDR
2. L'incident regroupe plusieurs alertes liées à:
   - Utilisation d'outils d'administration à distance
   - Tentatives d'élévation de privilèges
   - Connexions réseau inhabituelles entre endpoints

3. Ouvrez l'incident pour examiner les alertes corrélées

### Étape 2: Analyse de la compromission initiale

1. Identifiez le point d'entrée:
   - Examinez la chronologie des alertes pour trouver la première détection
   - Analysez le système initialement compromis
   - Déterminez le vecteur d'attaque (ex: phishing, exploitation de vulnérabilité)

2. Évaluez l'étendue de la compromission initiale:
   - Quels comptes utilisateurs ont été compromis
   - Quels systèmes ont été directement affectés
   - Quelles données ont potentiellement été exposées

### Étape 3: Cartographie du mouvement latéral

1. Utilisez la vue "Network" de l'incident:
   - Identifiez les connexions inhabituelles entre systèmes
   - Notez les protocoles et ports utilisés
   - Observez la chronologie des connexions

2. Analysez les techniques de mouvement latéral:
   - Recherchez l'utilisation d'outils comme PsExec, WMI, PowerShell Remoting
   - Identifiez les tentatives d'extraction ou réutilisation de credentials
   - Détectez les créations de services à distance

3. Créez une requête XQL pour visualiser le mouvement:
   ```xql
   dataset=xdr_data 
   | filter event_type = "NETWORK" 
   | filter (src_ip in ("[IP1]", "[IP2]") or dest_ip in ("[IP1]", "[IP2]")) 
   | fields timestamp, src_ip, src_hostname, dest_ip, dest_hostname, dest_port 
   | sort timestamp
   ```

### Étape 4: Évaluation de l'impact

1. Déterminez quels systèmes ont été compromis:
   - Utilisez les alertes et les données de connexion
   - Recherchez des indicateurs de compromission sur chaque système suspect
   - Évaluez le niveau d'accès obtenu par l'attaquant

2. Identifiez les objectifs potentiels de l'attaquant:
   - Systèmes critiques ciblés
   - Données sensibles accessibles
   - Persistance établie (backdoors, tâches planifiées, etc.)

3. Évaluez la chronologie complète:
   - Durée totale de l'attaque
   - Périodes d'activité et d'inactivité
   - Progression de l'attaque dans le temps

### Étape 5: Confinement et remédiation

1. Isolez les systèmes compromis:
   - Utilisez la fonction d'isolation de Cortex XDR
   - Déconnectez les systèmes critiques si nécessaire
   - Bloquez les communications entre les segments réseau affectés

2. Supprimez les accès de l'attaquant:
   - Réinitialisez les credentials compromis
   - Supprimez les comptes créés par l'attaquant
   - Éliminez les mécanismes de persistance

3. Collectez les preuves forensiques:
   - Utilisez la fonction de collecte de données de Cortex XDR
   - Préservez les logs et artefacts pertinents
   - Documentez la chronologie complète

### Étape 6: Leçons apprises et renforcement

1. Documentez l'incident complet:
   - Vecteur initial d'attaque
   - Techniques de mouvement latéral utilisées
   - Systèmes et données affectés
   - Chronologie détaillée

2. Identifiez les améliorations nécessaires:
   - Segmentation réseau
   - Gestion des privilèges
   - Détection des outils d'administration détournés
   - Formation des utilisateurs

3. Implémentez des mesures préventives:
   - Créez des règles de détection personnalisées
   - Ajustez les politiques de sécurité
   - Renforcez la surveillance des activités similaires

## 13.3 Chasse aux menaces proactive

Ce cas d'usage illustre comment utiliser Cortex XDR pour la chasse aux menaces proactive, afin d'identifier des activités suspectes avant qu'elles ne déclenchent des alertes.

### Scénario:
Suite à la publication d'une nouvelle technique d'attaque, vous souhaitez vérifier si votre environnement présente des signes de cette activité.

### Étape 1: Définition de l'hypothèse

1. Identifiez les indicateurs et comportements à rechercher:
   - Techniques MITRE ATT&CK associées
   - Indicateurs de compromission (IoC)
   - Comportements suspects spécifiques

2. Formulez une hypothèse claire:
   "Des attaquants pourraient utiliser des scripts PowerShell obfusqués pour établir des connexions persistantes vers des serveurs de commande et contrôle."

### Étape 2: Création de requêtes XQL ciblées

1. Accédez à l'interface de requête XQL dans Cortex XDR

2. Créez une requête pour détecter les scripts PowerShell obfusqués:
   ```xql
   dataset=xdr_data 
   | filter event_type = "PROCESS" 
   | filter action_process_image_name = "powershell.exe" 
   | filter action_process_image_command_line contains "-enc" or action_process_image_command_line contains "-encodedcommand" 
   | fields timestamp, hostname, actor_user_name, action_process_image_command_line 
   | sort timestamp desc
   ```

3. Créez une requête pour détecter les connexions réseau suspectes:
   ```xql
   dataset=xdr_data 
   | filter event_type = "NETWORK" 
   | filter action_process_image_name = "powershell.exe" 
   | filter dest_port in (443, 8443, 4443) 
   | stats count() by src_hostname, dest_ip, dest_port 
   | sort count desc
   ```

### Étape 3: Analyse des résultats

1. Examinez les résultats des requêtes:
   - Identifiez les modèles récurrents
   - Recherchez les anomalies et outliers
   - Notez les systèmes qui apparaissent fréquemment

2. Approfondissez les cas suspects:
   - Cliquez sur un résultat pour voir les détails
   - Utilisez la fonction "Pivot" pour explorer les connexions
   - Créez des requêtes supplémentaires pour obtenir plus de contexte

3. Corrélation des données:
   - Combinez les résultats de différentes requêtes
   - Établissez une chronologie des activités
   - Identifiez les relations entre événements

### Étape 4: Validation des découvertes

1. Pour chaque activité suspecte:
   - Collectez des preuves supplémentaires
   - Vérifiez si l'activité est légitime (faux positif)
   - Évaluez le niveau de risque

2. Utilisez les outils d'investigation de Cortex XDR:
   - Examinez les processus parents et enfants
   - Analysez les fichiers associés
   - Vérifiez l'historique des activités sur les endpoints concernés

3. Documentez vos conclusions:
   - Activités confirmées comme légitimes
   - Activités suspectes nécessitant une investigation plus approfondie
   - Menaces confirmées nécessitant une réponse immédiate

### Étape 5: Réponse et amélioration

1. Pour les menaces confirmées:
   - Créez un incident manuellement
   - Appliquez les mesures de remédiation appropriées
   - Suivez le processus standard de réponse aux incidents

2. Améliorez vos capacités de détection:
   - Créez des règles de détection personnalisées basées sur vos découvertes
   - Configurez des alertes pour les comportements similaires
   - Ajustez les seuils de détection existants

3. Institutionnalisez les connaissances:
   - Documentez les techniques d'attaque identifiées
   - Partagez les requêtes XQL utiles avec l'équipe
   - Intégrez les leçons apprises dans vos processus de chasse aux menaces

### Étape 6: Chasse itérative

1. Planifiez des activités de chasse régulières:
   - Définissez un calendrier (hebdomadaire, mensuel)
   - Alternez entre différentes hypothèses et techniques
   - Suivez les nouvelles menaces et tendances

2. Automatisez quand c'est possible:
   - Transformez les requêtes de chasse efficaces en rapports programmés
   - Créez des playbooks pour les investigations récurrentes
   - Développez une bibliothèque de requêtes XQL réutilisables

3. Mesurez l'efficacité:
   - Suivez le nombre de menaces découvertes par la chasse proactive
   - Évaluez le temps gagné grâce à la détection précoce
   - Ajustez votre stratégie en fonction des résultats

La chasse aux menaces proactive est un complément essentiel aux détections automatisées, permettant d'identifier les menaces sophistiquées qui pourraient autrement passer inaperçues. En développant ces compétences dans votre équipe, vous renforcez significativement votre posture de sécurité.



# 14. Glossaire, FAQ et Ressources

## 14.1 Glossaire des termes techniques

**Agent Cortex XDR** : Logiciel léger installé sur les endpoints pour collecter des données et appliquer des politiques de protection.

**Alerte** : Notification générée lorsqu'une activité suspecte ou malveillante est détectée par Cortex XDR.

**Analytics** : Moteurs d'analyse avancée utilisant le machine learning pour détecter les comportements anormaux et les menaces potentielles.

**BIOC (Behavioral Indicator of Compromise)** : Indicateur comportemental de compromission, représentant un modèle d'activité suspect.

**Causality Chain** (Chaîne de causalité) : Représentation visuelle des relations entre processus, fichiers et connexions réseau impliqués dans un incident.

**Dashboard** : Interface visuelle présentant des données agrégées et des métriques de sécurité sous forme de graphiques et tableaux.

**EDR (Endpoint Detection and Response)** : Technologie de détection et réponse sur les endpoints, permettant la surveillance, l'analyse et la remédiation des menaces.

**Endpoint** : Tout appareil connecté au réseau d'entreprise (ordinateur, serveur, appareil mobile).

**Faux positif** : Alerte de sécurité incorrecte, identifiant une activité légitime comme malveillante.

**Incident** : Regroupement d'alertes et d'événements corrélés représentant une menace potentielle unique.

**IOC (Indicator of Compromise)** : Artefact observé sur un réseau ou système indiquant une intrusion ou une attaque potentielle.

**Isolation d'endpoint** : Fonction de sécurité permettant de déconnecter un endpoint du réseau tout en maintenant la communication avec la console de gestion.

**MITRE ATT&CK** : Framework documentant les tactiques, techniques et procédures utilisées par les attaquants.

**Mouvement latéral** : Technique utilisée par les attaquants pour se déplacer d'un système à un autre au sein d'un réseau.

**NGAV (Next-Generation Antivirus)** : Solution antivirus avancée utilisant le machine learning et l'analyse comportementale pour détecter les menaces.

**Playbook** : Ensemble prédéfini d'actions à exécuter en réponse à un type spécifique d'incident de sécurité.

**Politique de sécurité** : Ensemble de règles définissant comment Cortex XDR protège les endpoints et répond aux menaces.

**Quarantaine** : Isolation d'un fichier malveillant pour empêcher son exécution ou sa propagation.

**RBAC (Role-Based Access Control)** : Méthode de régulation de l'accès aux ressources en fonction du rôle des utilisateurs.

**Remédiation** : Actions entreprises pour éliminer une menace et restaurer les systèmes affectés à un état sécurisé.

**Sévérité** : Classification du niveau de gravité d'une alerte ou d'un incident (critique, élevée, moyenne, faible).

**SIEM (Security Information and Event Management)** : Système de gestion des informations et des événements de sécurité.

**SOAR (Security Orchestration, Automation and Response)** : Plateforme d'orchestration, d'automatisation et de réponse aux incidents de sécurité.

**Threat Hunting** : Recherche proactive de menaces qui ont échappé aux détections automatisées.

**XDR (Extended Detection and Response)** : Solution de sécurité qui unifie la visibilité et le contrôle à travers plusieurs couches de sécurité (endpoints, réseau, cloud, etc.).

**XQL (eXtended Query Language)** : Langage de requête propriétaire de Cortex XDR permettant d'interroger et d'analyser les données de sécurité.

## 14.2 FAQ - Questions fréquemment posées

### Questions générales

**Q: Quelle est la différence entre Cortex XDR et un antivirus traditionnel ?**

R: Contrairement à un antivirus traditionnel qui se concentre principalement sur la détection de fichiers malveillants connus via des signatures, Cortex XDR offre une protection complète incluant :
- Détection comportementale avancée
- Analyse de la chaîne d'exécution complète
- Corrélation d'événements à travers multiples sources de données
- Capacités d'investigation et de réponse
- Protection contre les menaces sans fichier et les attaques zero-day
- Visibilité sur le réseau et le cloud, pas uniquement sur l'endpoint

**Q: Cortex XDR remplace-t-il mon SIEM existant ?**

R: Cortex XDR n'est pas conçu pour remplacer entièrement un SIEM, mais pour le compléter. Alors qu'un SIEM collecte et analyse des logs de multiples sources, Cortex XDR se concentre sur la détection et la réponse aux menaces. De nombreuses organisations utilisent les deux solutions en parallèle, Cortex XDR alimentant le SIEM avec des données enrichies sur les menaces détectées.

**Q: Quelles sont les différentes éditions de Cortex XDR disponibles ?**

R: Cortex XDR est disponible en plusieurs éditions :
- **Cortex XDR Prevent** : Fonctionnalités NGAV de base
- **Cortex XDR Pro** : Suite complète incluant EDR, NGAV, et analyse réseau
- **Cortex XDR Enterprise** : Offre premium avec fonctionnalités avancées d'automatisation et d'investigation

Les licences peuvent être basées sur le nombre d'endpoints ou sur le volume de données ingérées (modèle par Go).

### Questions techniques

**Q: Quel est l'impact sur les performances des endpoints ?**

R: L'agent Cortex XDR est conçu pour être léger, avec une empreinte mémoire typique de 50-150 Mo et une utilisation CPU moyenne inférieure à 2% en fonctionnement normal. L'impact exact dépend de la configuration, des modules activés et de l'activité du système.

**Q: Cortex XDR fonctionne-t-il hors ligne ?**

R: Oui, l'agent Cortex XDR continue de protéger les endpoints même lorsqu'ils sont déconnectés du réseau. Les politiques de sécurité sont appliquées localement, et les événements sont mis en cache jusqu'à ce que la connexion soit rétablie.

**Q: Comment Cortex XDR gère-t-il les environnements virtualisés ?**

R: Cortex XDR propose des optimisations spécifiques pour les environnements virtualisés, notamment :
- Déduplication des scans pour réduire la charge sur l'infrastructure
- Mode léger pour les VDI (Virtual Desktop Infrastructure)
- Synchronisation des mises à jour pour éviter les "tempêtes d'analyse"
- Support des snapshots et des templates

**Q: Peut-on personnaliser les règles de détection ?**

R: Oui, Cortex XDR permet de créer des règles de détection personnalisées via :
- L'interface de création de règles dans la console
- Le langage XQL pour des détections avancées
- L'importation de règles YARA
- La création de listes blanches et d'exceptions

### Questions d'administration

**Q: Quelle est la fréquence recommandée pour les mises à jour ?**

R: Palo Alto Networks recommande :
- Mises à jour de la console : Dans les 30 jours suivant leur publication
- Mises à jour des agents : Dans les 60 jours suivant leur publication
- Mises à jour de sécurité critiques : Dès que possible après évaluation

**Q: Comment gérer les faux positifs ?**

R: Pour gérer efficacement les faux positifs :
1. Documentez chaque faux positif identifié
2. Créez des exceptions spécifiques plutôt que génériques
3. Utilisez les listes blanches pour les applications légitimes fréquemment détectées
4. Ajustez les seuils de détection si nécessaire
5. Soumettez les faux positifs récurrents au support Palo Alto Networks

**Q: Quelle est la capacité de stockage nécessaire ?**

R: Les besoins en stockage dépendent de plusieurs facteurs :
- Nombre d'endpoints surveillés
- Politiques de rétention des données
- Types d'événements collectés
- Niveau de verbosité configuré

En moyenne, comptez environ 1-3 Go par endpoint par mois pour une configuration standard.

**Q: Comment intégrer Cortex XDR avec Active Directory ?**

R: L'intégration avec Active Directory peut se faire de plusieurs façons :
1. Pour l'authentification : Configuration SAML ou LDAP
2. Pour la gestion des endpoints : Synchronisation avec les OUs AD
3. Pour le déploiement : Utilisation de GPOs
4. Pour l'enrichissement des données : Corrélation des événements avec les informations utilisateur AD

## 14.3 Checklist de configuration

Cette checklist vous aidera à vérifier que votre déploiement Cortex XDR est correctement configuré :

### Configuration initiale
- [ ] Console accessible uniquement via HTTPS
- [ ] Authentification multifacteur activée pour tous les utilisateurs administrateurs
- [ ] Rôles et permissions configurés selon le principe du moindre privilège
- [ ] Groupes d'endpoints créés selon la structure organisationnelle
- [ ] Politiques de notification configurées pour les événements critiques

### Déploiement des agents
- [ ] Dernière version des agents déployée sur tous les endpoints
- [ ] Modules appropriés activés selon les besoins (NGAV, EDR, etc.)
- [ ] Exclusions configurées pour les applications métier légitimes
- [ ] Paramètres de performance ajustés pour les systèmes critiques
- [ ] Tests de connectivité effectués sur différents segments réseau

### Configuration de la détection
- [ ] Politiques de protection adaptées à chaque groupe d'endpoints
- [ ] Règles de détection personnalisées créées pour les menaces spécifiques
- [ ] Intégrations de Threat Intelligence configurées
- [ ] Seuils de détection ajustés pour limiter les faux positifs
- [ ] Tests de détection effectués pour valider l'efficacité

### Configuration de la réponse
- [ ] Playbooks de réponse définis pour les incidents courants
- [ ] Actions automatiques configurées pour les menaces connues
- [ ] Intégrations avec les systèmes de ticketing
- [ ] Procédures d'escalade documentées
- [ ] Permissions pour les actions de réponse correctement attribuées

### Maintenance et surveillance
- [ ] Sauvegardes régulières de la configuration
- [ ] Processus de mise à jour documenté et testé
- [ ] Surveillance de la santé des agents configurée
- [ ] Alertes opérationnelles configurées (déconnexions massives, etc.)
- [ ] Révision périodique des exceptions et listes blanches planifiée

## 14.4 Ressources additionnelles

### Documentation officielle
- [Portail de documentation Cortex XDR](https://docs-cortex.paloaltonetworks.com/)
- [Base de connaissances Palo Alto Networks](https://knowledgebase.paloaltonetworks.com/)
- [Guides d'administration Cortex XDR](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Documentation/Administration-Guide)

### Formation et certification
- [Palo Alto Networks Education](https://www.paloaltonetworks.com/services/education)
- [Certification Cortex XDR](https://www.paloaltonetworks.com/services/education/certification)
- [Cortex XDR: Investigation and Response (EDU-318)](https://www.paloaltonetworks.com/services/education/cortex-xdr-investigation-and-response-edu-318)

### Communauté et support
- [Communauté Live Palo Alto Networks](https://live.paloaltonetworks.com/)
- [Forum Cortex XDR](https://live.paloaltonetworks.com/t5/Cortex-XDR/ct-p/CortexXDR)
- [Support technique Palo Alto Networks](https://support.paloaltonetworks.com/)

### Ressources techniques
- [Blog Unit 42 (Threat Intelligence)](https://unit42.paloaltonetworks.com/)
- [Rapports de recherche sur les menaces](https://www.paloaltonetworks.com/resources/research)
- [Webinaires et démonstrations](https://www.paloaltonetworks.com/resources/webinars)

### Mises à jour et nouveautés
- [Notes de version Cortex XDR](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Documentation/Release-Notes)
- [Roadmap produit](https://live.paloaltonetworks.com/t5/Cortex-XDR-Discussions/ct-p/CortexXDR_Discussions)
- [Blog Palo Alto Networks](https://www.paloaltonetworks.com/blog)

Ces ressources vous aideront à approfondir vos connaissances sur Cortex XDR et à rester informé des dernières évolutions et meilleures pratiques.



