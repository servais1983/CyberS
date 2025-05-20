# 🎯 Black Basta - Groupe de Ransomware

## 🧠 Présentation

**Black Basta** est un groupe cybercriminel apparu en **avril 2022**, spécialisé dans les attaques par **ransomware-as-a-service (RaaS)**. Ce groupe a rapidement gagné en notoriété pour ses campagnes d’extorsion double, combinant **chiffrement de données** et **menace de publication** sur son site de fuite (leak site).

---

## 🔎 Fonctionnement

Le modèle de Black Basta repose sur :

- **Chiffrement des fichiers** sur les systèmes infectés.
- **Vol de données sensibles** avant le chiffrement.
- **Extorsion** en menaçant de publier les données volées si la rançon n’est pas payée.
- Utilisation de **techniques de persistance et de déplacement latéral** pour compromettre toute l’infrastructure d’un réseau.

---

## 🧰 Tactiques, Techniques et Procédures (TTPs)

| Tactique MITRE ATT&CK | Description |
|------------------------|-------------|
| **Initial Access** | Phishing avec pièce jointe piégée, exploitation de vulnérabilités RDP ou VPN |
| **Execution** | Utilisation de scripts PowerShell ou DLL malveillantes |
| **Persistence** | Clés de registre Run/RunOnce |
| **Credential Access** | Dumping de LSASS avec Mimikatz |
| **Lateral Movement** | PSExec, SMB, RDP |
| **Exfiltration** | Protocole FTP ou outils personnalisés |
| **Impact** | Chiffrement à l’aide d’un ransomware personnalisé |

---

## 📊 Victimes et Impact

- **Cibles** : entreprises des secteurs critiques (santé, finance, industrie, services publics).
- **Méthode de pression** : site de fuite (leak site) affichant les noms des victimes refusant de payer.
- **Exemples récents** (selon les rapports publics) :
  - Entreprises en Amérique du Nord et en Europe.
  - Fuites de données RH, financières, juridiques.

---

## 🛡️ Recommandations de Protection

- ✅ Maintenir les systèmes à jour avec les derniers patchs.
- ✅ Sauvegardes régulières et hors-ligne.
- ✅ Sécuriser les accès RDP / VPN (MFA, segmentation réseau).
- ✅ Formation des employés au phishing.
- ✅ Surveillance du réseau et détection d’anomalies.

---

## 📚 Références

- [MITRE ATT&CK - Black Basta](https://attack.mitre.org)
- [Rapports de cybersécurité (CISA, FBI)](https://www.cisa.gov)
- [Site leak (via TOR) - À des fins de veille uniquement]

---

> ⚠️ Ce document est fourni à des fins d'information et de sensibilisation. L'analyse des menaces doit être faite dans un cadre légal et éthique.
