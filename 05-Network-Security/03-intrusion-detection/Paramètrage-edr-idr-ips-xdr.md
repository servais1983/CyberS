# 🛡️ Paramétrage des solutions EDR, IDR, IPS et XDR

## 1. 🖥️ EDR – Endpoint Detection and Response

### 📌 Objectif :
Surveiller, détecter et répondre aux menaces sur les postes de travail et serveurs.

### ⚙️ Étapes de paramétrage :

- **Déploiement des agents** :  
  Installer les agents EDR sur tous les terminaux via GPO, script ou outil de déploiement (SCCM, Intune...).

- **Définition des politiques de sécurité** :
  - Surveillance des processus
  - Blocage des applications non autorisées
  - Protection contre les ransomwares

- **Alerting et réponses automatiques** :
  - Création de règles de détection personnalisées
  - Configuration de réponses automatisées (isolation réseau, suppression fichier)

- **Intégration avec SIEM et SOC** :
  - Transfert des logs vers un SIEM
  - Envoi d’alertes au centre de supervision

## 2. 🧑‍💼 IDR – Identity Detection and Response

### 📌 Objectif :
Surveiller et sécuriser les identités (AD, Azure AD, MFA, SSO...).

### ⚙️ Étapes de paramétrage :

- **Connexion aux annuaires** :
  - Intégration Active Directory / Azure AD
  - Surveillance des comptes à privilèges

- **Détection des comportements anormaux** :
  - Tentatives de connexion suspectes
  - Accès en dehors des heures de travail
  - Utilisation inhabituelle des privilèges

- **Réponses automatisées** :
  - Blocage ou mise en quarantaine de comptes
  - Réinitialisation forcée de mot de passe

- **Intégration MFA / IAM** :
  - Renforcement des accès par MFA
  - Gestion centralisée des identités

## 3. 🔥 IPS – Intrusion Prevention System

### 📌 Objectif :
Bloquer les attaques réseau en temps réel.

### ⚙️ Étapes de paramétrage :

- **Positionnement dans l’architecture** :
  - En ligne (inline) ou en mode passif
  - Segment clé : entre réseau interne et DMZ/internet

- **Mise à jour des signatures** :
  - Programmation de mises à jour automatiques
  - Activation des signatures critiques

- **Règles personnalisées** :
  - Autorisation/blocage de ports spécifiques
  - Blocage par adresse IP, pays, ou protocole

- **Surveillance & alertes** :
  - Configuration des niveaux de gravité
  - Intégration avec les journaux SIEM

## 4. 🌐 XDR – Extended Detection and Response

### 📌 Objectif :
Corréler les données de plusieurs sources (EDR, réseau, e-mail, cloud...) pour une réponse unifiée.

### ⚙️ Étapes de paramétrage :

- **Intégration des sources de données** :
  - EDR, IDR, IPS, logs cloud, messagerie, etc.
  - Connexion API ou agents

- **Création de scénarios de détection corrélée** :
  - Exemple : alerte EDR + tentative d’accès IDR = incident critique
  - Règles multi-vecteurs

- **Orchestration des réponses** :
  - Isolation automatique des machines
  - Révocation d’accès d’un utilisateur
  - Notification à l’équipe sécurité

- **Dashboards et reporting unifiés** :
  - Visualisation centralisée des menaces
  - Rapports par vecteur d’attaque

## ✅ Bonnes pratiques communes

- Toujours tester en environnement de pré-production
- Définir une stratégie d’escalade des alertes
- Mettre à jour régulièrement les signatures, règles et agents
- Former les équipes à l’analyse et à la réponse
- Documenter tous les paramétrages
