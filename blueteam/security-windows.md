# 🛡️ Guide Complet – Sécurisation des Systèmes Windows

## 🎯 Objectif

Appliquer des **mesures de sécurité techniques et organisationnelles** sur les systèmes Windows (clients & serveurs) afin de **réduire la surface d’attaque**, **protéger les comptes sensibles** et **renforcer la résilience** face aux menaces internes et externes.

---

## 🧱 1. Principes de base

| Action                             | But                                           |
|------------------------------------|-----------------------------------------------|
| 🔒 Appliquer les mises à jour      | Corriger les vulnérabilités connues           |
| 🧑‍💻 Utiliser des comptes limités  | Principe du moindre privilège                 |
| 🛑 Désactiver services inutiles     | Réduire la surface d’exposition               |
| 🧩 Séparer les rôles (admin/user)   | Éviter les élévations de privilège non justifiées |
| 📋 Activer la journalisation       | Tracer les comportements anormaux             |

---

## ⚙️ 2. Durcissement système

### 🔧 Désactiver services non nécessaires (PowerShell)

```powershell
Get-Service | Where-Object {$_.Status -eq "Running"} | Out-GridView
Stop-Service -Name 'Fax'
Set-Service -Name 'Fax' -StartupType Disabled
🔐 Activer le pare-feu Windows
powershell

Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
🗃️ Activer le chiffrement BitLocker
powershell

Enable-BitLocker -MountPoint "C:" -EncryptionMethod XtsAes256 -UsedSpaceOnlyEncryption
👥 3. Sécurisation des comptes
🛡️ Politiques de mot de passe
powershell

net accounts /minpwlen:12 /maxpwage:90 /lockoutthreshold:5
⚠️ Éviter les mots de passe partagés

🔐 Utiliser Windows Hello, carte à puce ou MFA

👮 Activer LAPS (Local Administrator Password Solution)
Permet de générer des mots de passe locaux uniques par machine, stockés dans Active Directory de façon sécurisée.

📥 Télécharger LAPS

🛠️ 4. GPO de sécurité essentielles
Objectif	Paramètre GPO recommandé
🔐 Interdire USB	Computer Config > Policies > Removable Storage
🛑 Bloquer RDP aux utilisateurs	Deny log on through Remote Desktop Services
📈 Activer l’audit sécurité	Audit logon events, Audit object access
🕵️ Désactiver exécution scripts	Turn off Windows Script Host
📋 Supprimer comptes invités	Accounts: Guest account status = Disabled

🧰 5. Outils intégrés à utiliser
Outil	Usage
Windows Defender	Antivirus, EDR
Exploit Guard	Protection mémoire, contrôle des applis
Firewall	Pare-feu intégré
Event Viewer	Journalisation locale
AppLocker	Restriction des applications exécutables
Security Baselines	GPO préconfigurées de Microsoft

🔍 6. Supervision et détection
📈 Logs utiles à surveiller
ID	Description
4624	Connexion réussie
4625	Échec de connexion
4648	Connexion avec identifiants explicites
4688	Création de processus
4672	Connexion admin

🧪 Outils de supervision recommandés
🔍 Sysmon : journalisation approfondie

📦 Wazuh, ELK, Splunk : corrélation et alertes

🔐 Defender for Endpoint (EDR Microsoft)

💣 7. Blocage de vecteurs d’attaque fréquents
Vecteur	Contre-mesure
Pass-the-Hash	Credential Guard, LAPS, audit des accès
PowerShell abuse	Constrained Language Mode, journalisation
RDP bruteforce	GPO + MFA + timeout connexion
Macros malveillantes	Bloquer via GPO ou politique Office
USB/autorun	Désactiver autorun, GPO

🚀 8. Commandes de vérification rapide
powershell

Get-WindowsFeature | Where-Object Installed
Get-EventLog -LogName Security -Newest 100
Get-LocalUser | Where-Object Enabled -eq $true
Get-NetFirewallRule -Enabled True
📋 9. Checklist de sécurité Windows
🔐 Mesure	État
BitLocker activé	✅ / ❌
Mots de passe forts et expirables	✅ / ❌
LAPS déployé	✅ / ❌
RDP sécurisé + MFA	✅ / ❌
Journaux sécurité actifs	✅ / ❌
Antivirus/EDR actif	✅ / ❌
Services inutiles désactivés	✅ / ❌
AppLocker ou WDAC actif	✅ / ❌

📚 10. Ressources utiles
🔗 Microsoft Security Baselines

📘 Securing Windows Workstations (AD Security)

🔐 Windows Hardening Guide (NSA)

⚙️ Microsoft LAPS

🧠 MITRE ATT&CK – Windows Techniques
