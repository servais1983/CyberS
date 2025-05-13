# 🛡️ Guide Complet – Pass-the-Hash (PtH)

## 🎯 Objectif

Comprendre la technique **Pass-the-Hash**, ses risques pour les environnements Active Directory, et appliquer les bonnes pratiques pour **s’en protéger**.

---

## 🧠 1. Qu’est-ce que Pass-the-Hash ?

**Pass-the-Hash (PtH)** est une **technique d’authentification abusive** qui permet à un attaquant d’utiliser le **hash (empreinte)** d’un mot de passe NTLM au lieu du mot de passe réel, pour s’authentifier sur d'autres machines.

➡️ Il **n’est pas nécessaire de cracker le mot de passe**, seulement d’extraire son hash.

---

## 🔧 2. Fonctionnement technique

### 📌 En résumé :
1. Un utilisateur s’authentifie → son **hash NTLM est mis en cache** en mémoire (LSASS).
2. Un attaquant avec les droits SYSTEM accède à ce hash (via Mimikatz par exemple).
3. Il l’utilise pour se connecter à un autre système, comme si c’était le mot de passe.

---

## 📦 3. Prérequis pour une attaque PtH

| Élément                              | Détail                                  |
|--------------------------------------|-----------------------------------------|
| Accès admin local (ou SYSTEM)        | Pour lire la mémoire (LSASS)            |
| Cible utilise l'authentification NTLM| Encore présent dans de nombreux domaines|
| Hash récupéré du compte cible        | Via outil ou dump mémoire               |

---

## 🧪 4. Outils d’attaque courants

| Outil        | Usage                              |
|--------------|------------------------------------|
| **Mimikatz** | Dump des hash, Pass-the-Hash direct|
| **Impacket** | Scripts `psexec.py`, `wmiexec.py`  |
| **pth-winexe** | Exécution de commande avec hash  |
| **Rubeus**   | Kerberos abuse, TGT Pass-the-Hash  |

Exemple avec Mimikatz :

```text
sekurlsa::logonpasswords
sekurlsa::pth /user:admin /domain:corp.local /ntlm:<hash> /run:cmd.exe
🔥 5. Démo simplifiée (scénario théorique)
L’attaquant prend le contrôle d’un poste utilisateur via phishing.

Il exécute mimikatz pour extraire les hash en mémoire.

Il obtient un hash NTLM d’un compte admin de domaine.

Il utilise le hash pour ouvrir une session RDP ou SMB sur un autre poste.

🛡️ 6. Comment se défendre contre Pass-the-Hash
🔒 6.1 Réduire les expositions
Segmenter les comptes administrateurs

Éviter que les comptes Domain Admins se connectent à des postes utilisateurs

Mettre en place Local Admins uniques par machine (LAPS)

🧹 6.2 Réduire les hash en mémoire
Activer Credential Guard (Windows 10+)

Utiliser Remote Credential Guard (RDP sans hash local)

Désactiver l’utilisation de WDigest :

powershell

Set-ItemProperty -Path HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest -Name UseLogonCredential -Value 0
🧩 6.3 Surveiller les anomalies
Journaliser les connexions NTLM

Événements Windows utiles :

4624 (Logon)

4672 (Admin logon)

4648 (logon avec identifiants explicites)

🚧 7. Bonnes pratiques Active Directory
Pratique	Description
🔐 MFA	Imposer MFA pour tous les accès admin
💼 Tiering (Admin Tier 0/1/2)	Séparer les rôles et comptes d'administration
👥 LAPS (Local Administrator Password Solution)	MDP locaux uniques et gérés automatiquement
📋 GPO : Interdire logon RDP à Domain Admins	Éviter leur cache de hash
🔎 Audit des comptes privilégiés	Journaliser tout accès inattendu

📦 8. Détection et réponse
Utiliser un EDR (Defender ATP, CrowdStrike, etc.)

Corrélation dans un SIEM (Wazuh, Splunk, ELK)

Détecter :

Création d’un process par un utilisateur distant

Authentifications NTLM à des heures/logs suspects

Script de détection Mimikatz en mémoire (via YARA, Sysmon)

📚 9. Références et ressources
🛠️ Mimikatz GitHub

📖 Microsoft – PtH Mitigation

🔍 Attack MITRE T1550.002 – Pass the Hash

📦 LAPS – Microsoft

📌 10. Résumé
✅ PtH abuse le protocole NTLM et les hash mémoire

❌ Pas besoin de mot de passe en clair

🔐 Défense = séparation des privilèges, Credential Guard, LAPS, MFA

🧠 Surveiller, durcir, auditer régulièrement
