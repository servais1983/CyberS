# 🖥️ Contrôleur de Domaine (Domain Controller) – Active Directory

## 🔎 Définition

Un **contrôleur de domaine (Domain Controller - DC)** est un **serveur Windows** qui héberge **Active Directory Domain Services (AD DS)**. Il est responsable de :

- L’**authentification** des utilisateurs et ordinateurs.
- La **gestion centralisée des comptes et ressources**.
- L’**autorisation d'accès** aux ressources du réseau.
- La **réplication** des données entre sites et serveurs AD.

---

## 🧩 Rôle du Contrôleur de Domaine

| Fonction                     | Description |
|-----------------------------|-------------|
| **Authentification**        | Vérifie l'identité des utilisateurs via Kerberos/NTLM. |
| **Annuaire centralisé**     | Stocke tous les objets du domaine (utilisateurs, groupes, ordinateurs, etc.). |
| **Gestion des stratégies**  | Applique les GPO (stratégies de groupe) aux utilisateurs et machines. |
| **Sécurité**                | Gère les autorisations, groupes de sécurité, politiques de mot de passe, etc. |
| **Réplication AD**          | Synchronise les données avec d’autres DC du domaine. |

---

## 🛠️ Services clés sur un DC

- **Active Directory Domain Services (AD DS)**
- **Kerberos (authentification sécurisée)**
- **DNS intégré** (souvent pour résoudre les noms de domaine interne)
- **Replication SYSVOL** (scripts de connexion, GPO)

---

## 🖇️ Exemple de fonctionnement

1. Un utilisateur tente de se connecter à un poste.
2. Le poste contacte le **DC** pour vérifier les identifiants.
3. Le DC authentifie via **Kerberos**.
4. Une fois validé, l’utilisateur reçoit un **ticket de session**.
5. Les stratégies (GPO) sont appliquées.
6. L'utilisateur accède aux ressources réseau selon ses droits.

---

## 🏢 Utilité en entreprise

- Permet un **contrôle centralisé** des comptes et accès.
- Réduit les risques de configuration manuelle ou locale.
- Améliore la **sécurité**, la **traçabilité** et la **gestion des ressources**.

---

## 🔐 Bonnes pratiques

- Avoir **au moins 2 DCs** pour la redondance.
- Protéger les DCs physiquement et logiquement.
- Utiliser **des comptes administrateurs dédiés**.
- Sauvegarder régulièrement la base AD (`ntds.dit`).
- Mettre à jour les rôles FSMO et surveiller la réplication.

---

## 📌 Conclusion

Le **contrôleur de domaine** est le **cœur d'une infrastructure Active Directory**. Il garantit l'authentification, l'intégrité et la cohérence de l'environnement réseau d'une organisation. Une bonne gestion des DCs est essentielle à la **sécurité** et à la **stabilité** du système d’information.
