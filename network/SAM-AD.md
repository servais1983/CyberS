

# La base SAM (Security Account Manager) dans Active Directory

## 🔐 Qu'est-ce que la base SAM ?

La **SAM (Security Account Manager)** est une base de données utilisée par les systèmes Windows pour stocker des **informations d'identification et de sécurité** des comptes utilisateurs et groupes locaux.

- Sur les **contrôleurs de domaine Active Directory (AD)**, les comptes sont stockés dans **Active Directory**.
- Sur les **machines indépendantes ou membres d’un domaine**, les comptes locaux sont stockés dans la **base SAM locale**.

---

## 🧠 Fonctionnement de la base SAM

- Située dans le registre Windows (`HKEY_LOCAL_MACHINE\SAM`), mais protégée et inaccessible directement même par l'administrateur.
- Utilisée par le **service LSA (Local Security Authority)** pour valider les connexions locales.
- Contient les **hashs des mots de passe**, les **SIDs** (Security Identifiers), et les **droits d'accès** associés à chaque compte.

---

## 🆔 SAM vs Active Directory

| Fonctionnalité                 | Base SAM locale                      | Active Directory (AD)                |
|-------------------------------|--------------------------------------|--------------------------------------|
| Portée                        | Locale (sur une seule machine)       | Réseau (multi-machines / domaine)    |
| Stockage                      | Fichier `C:\Windows\System32\config\SAM` | Base de données AD (NTDS.dit)    |
| Comptes                       | Utilisateurs et groupes locaux       | Comptes de domaine                   |
| Gestion                       | via `lusrmgr.msc`, `net user`        | via `dsa.msc`, PowerShell AD, etc.   |

---

## 🔍 Où la retrouve-t-on ?

- La **base SAM** existe **même sur les PC clients Windows**.
- Dans un **environnement d’entreprise**, les comptes d’utilisateurs sont généralement gérés via **Active Directory**, mais **les comptes locaux** (par exemple : `Administrateur`, `Invité`) restent stockés dans la **base SAM locale**.

---

## 🔒 Sécurité de la base SAM

- Très sensible : elle stocke les **hashs des mots de passe**.
- Accès restreint, même pour les administrateurs.
- Cible fréquente en cas d’**attaque** (ex. `mimikatz`, `pwdump`, `samdump2`).
- Recommandations :
  - Utiliser **BitLocker** pour chiffrer le disque.
  - Restreindre les **droits administratifs**.
  - Surveiller les accès au système de fichiers.

---

## 🛠️ Commandes utiles

- Afficher les utilisateurs locaux :
  ```bash
  net user
Gérer les comptes locaux :


lusrmgr.msc
Exporter les utilisateurs AD (si domaine) :

powershell

Get-ADUser -Filter * -Property * | Select-Object Name, SamAccountName
📌 Remarques importantes
sAMAccountName est aussi un attribut clé dans Active Directory :

C’est le nom de connexion compatible Windows NT.

Utilisé dans les scripts, authentifications, et outils hérités.

Ex : jdupont dans Domaine\jdupont.

✅ Conclusion
La base SAM est au cœur de la gestion des comptes locaux sous Windows. Dans un environnement d’entreprise, la gestion centralisée via Active Directory est privilégiée, mais la SAM locale reste active et critique. Bien comprendre son rôle est essentiel pour renforcer la sécurité des postes de travail et des serveurs Windows.

