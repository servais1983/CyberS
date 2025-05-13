# 🧩 Guide Complet – Active Directory (AD) en Entreprise

## 📖 1. Qu'est-ce qu'Active Directory ?

**Active Directory (AD)** est un service d'annuaire développé par Microsoft, utilisé pour gérer de manière centralisée les utilisateurs, ordinateurs, groupes, permissions et ressources d’un réseau Windows.

Il est intégré dans les serveurs Windows Server (2000+), via le rôle **"Services de domaine Active Directory (AD DS)"**.

---

## 🧱 2. Architecture de base

| Élément        | Description                                          |
|----------------|------------------------------------------------------|
| **Contrôleur de domaine (DC)** | Serveur principal qui héberge AD       |
| **Objet (Object)**              | Éléments stockés : utilisateurs, PC, etc. |
| **Unité d’organisation (OU)**  | Regroupe logiquement les objets         |
| **Forêt (Forest)**              | Ensemble hiérarchique de domaines       |
| **Domaine**                     | Espace logique de gestion (ex: corp.lan)|
| **Arbre (Tree)**                | Ensemble de domaines dans une forêt     |

---

## 🔧 3. Installation & Configuration de base

### 🛠️ Ajouter AD DS sur Windows Server

```powershell
Install-WindowsFeature -Name AD-Domain-Services
🏗️ Promouvoir le serveur en tant que DC
powershell

Install-ADDSForest -DomainName "entreprise.local"
Cela installe DNS, crée la forêt et un premier domaine.

🧠 4. Les 5 rôles FSMO (Flexible Single Master Operation)
Rôle	Localisation	Fonction
Schema Master	Une par forêt	Modifie la structure AD
Domain Naming Master	Une par forêt	Gère les noms de domaine
RID Master	Une par domaine	Alloue les identifiants (SID) aux objets
PDC Emulator	Une par domaine	Synchronisation des mots de passe et GPO
Infrastructure Master	Une par domaine	Met à jour les références inter-domaines

powershell

netdom query fsmo
🛡️ 5. Sécurité et meilleures pratiques
🔐 Complexité des mots de passe (GPO)

🧱 Délégation par OU (principe du moindre privilège)

📛 Éviter les utilisateurs dans Users, utiliser des OU dédiées

🚫 Interdire le login RDP aux utilisateurs standards

🔄 Appliquer des GPO de verrouillage de session et MFA

💥 Journaliser et surveiller les accès sensibles (Admin, DC)

🧩 6. Intégration avec DNS, DHCP, GPO
📡 DNS
AD dépend d’un DNS interne (zone : entreprise.local)

Vérifier la configuration avec :

powershell

Resolve-DnsName entreprise.local
💻 DHCP
Ajout d’option 015 (nom DNS)

Sécuriser l’enregistrement dynamique DNS

🛠️ GPO (Group Policy)
Gérer les configurations à grande échelle : scripts, sécurité, logon, déploiement logiciels

powershell

gpedit.msc
gpmc.msc
🧑‍💻 7. Commandes PowerShell utiles
Tâche	Commande PowerShell
Créer un utilisateur	New-ADUser -Name "Toto" -SamAccountName toto
Créer une OU	New-ADOrganizationalUnit -Name "RH"
Ajouter un PC au domaine	Add-Computer -DomainName entreprise.local -Restart
Lister tous les utilisateurs	Get-ADUser -Filter *
Rechercher un compte bloqué	Search-ADAccount -LockedOut

🧾 8. Sauvegarde & Restauration
📦 Sauvegarde du système d'état
powershell

wbadmin start systemstatebackup -backuptarget:D:
🔄 Restauration (en mode DSRM)
Redémarrer en mode Directory Services Restore Mode (F8)

Restaurer avec wbadmin ou outil tiers

Re-synchroniser avec les autres DC (si plusieurs)

🧪 9. Supervision et Audit
Élément	Outils recommandés
Journalisation	Event Viewer > Security (ID 4625, 4768)
Monitoring	Wazuh, Zabbix, Nagios, Microsoft ATA
Alertes	Sur échecs d’authentification, GPO modifiée
Rapports AD	PowerShell + Export-CSV

🔐 10. Gérer les accès et permissions
Utiliser groupes de sécurité + GPO ciblées

Appliquer ACLs sur les objets (ADSI Edit)

Restreindre l’accès aux unités d’organisation sensibles

Activer audit des accès privilégiés (Admin, Domain Admin)

📑 11. Bonnes pratiques d’administration
✅ À FAIRE :

Utiliser des comptes "admin" séparés pour l'administration

Créer un OU "Workstations" dédiée pour les PC

Activer les stratégies de verrouillage de compte

Séparer les rôles FSMO entre plusieurs DC (en environnement critique)

❌ À ÉVITER :

Ne jamais connecter des DC à Internet directement

Ne jamais utiliser le compte Administrator au quotidien

Ne pas désactiver les logs de sécurité

📘 12. Annexes & Références
🔗 Microsoft Docs – Active Directory

🧾 AD Security – Hardening Guide

📚 Cheat Sheet AD – HackTricks

🛠️ PowerShell Gallery – AD Tools

yaml

