# 🧠 Stratégie de Détection avec XDR (Extended Detection and Response)

## 🎯 Objectif

Déployer une détection étendue et corrélée à travers les endpoints, le réseau, les services cloud, les emails et les identités pour améliorer la visibilité, automatiser la détection et accélérer la réponse aux incidents.

---

## 1. 🔎 Qu’est-ce que le XDR ?

| Élément               | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **Définition**         | Une solution unifiée de détection et de réponse, intégrant plusieurs vecteurs |
| **Sources couvertes** | Endpoints, réseau, cloud, email, identité                                  |
| **Avantages**         | Corrélation automatique, visibilité centralisée, détection proactive       |

---

## 2. 🛠️ Architecture typique XDR

[Endpoint / EDR] [NDR / Réseau] [Cloud / SaaS] [Email] [Identité / IAM]
│ │ │ │ │
└──────► Ingestion dans le moteur XDR (agents, API, intégrations) ◄────────────┘
│
► Corrélation multivecteur (SIEM ou moteur XDR natif)
│
► Détection + Scoring de menace
│
► Automatisation de la réponse (SOAR)

markdown
Copier
Modifier

---

## 3. 🧩 Types de détection dans un XDR

### 3.1. Corrélation entre domaines

- **Exemple** : alerte EDR + login cloud inhabituel + transfert de données
- Détection impossible en silo
- Basé sur des **règles dynamiques** ou **détection comportementale**

### 3.2. Use Cases spécifiques XDR

| Cas d’usage                         | Données XDR impliquées                                     |
|------------------------------------|------------------------------------------------------------|
| Compromission de compte (BEC, MFA) | Logs IAM + Email + Endpoint                               |
| Exfiltration lente de données      | Réseau + Cloud + DLP                                      |
| Mouvements latéraux                | Endpoint + Réseau + Active Directory                      |
| Shadow IT / Applications non gérées| Cloud (CASB) + Endpoint                                   |

---

## 4. 📋 Playbook d’investigation (ex. compromission de compte)

### Étapes automatisables dans XDR :

1. **Déclencheur** : Authentification MFA échouée depuis pays rare + login réussi après
2. **Corrélation** :
   - Lien avec accès à SharePoint / OneDrive
   - Activité inhabituelle sur endpoint (powershell.exe)
3. **Réponse** :
   - Isolation de l’endpoint
   - Réinitialisation du mot de passe
   - Notification à la cellule IR / utilisateur
4. **Post-mortem** :
   - Recherche d'autres sessions similaires
   - Mise à jour de règles XDR

---

## 5. ✅ Bonnes pratiques pour une stratégie XDR efficace

- Intégrer toutes les sources critiques (EDR, NDR, Cloud, Email, IAM)
- Définir des **use cases de détection** prioritaires (MITRE, D3FEND)
- Utiliser les fonctionnalités SOAR (playbooks automatisés, réponse adaptative)
- Évaluer régulièrement les **métriques clés** :
  - Taux de corrélation utile
  - Réduction du MTTR
  - Couverture ATT&CK
- Maintenir une **veille active sur les techniques d’évasion** et mettre à jour les règles

---

## 6. 📚 Références

- [MITRE ATT&CK for Enterprise](https://attack.mitre.org/)
- [MITRE D3FEND – Défense active](https://d3fend.mitre.org/)
- [XDR vs SIEM vs SOAR – Comparatif](https://www.csoonline.com/)
- [MITRE Engenuity – XDR Evaluations](https://attackevals.mitre-engenuity.org/xdr/)
