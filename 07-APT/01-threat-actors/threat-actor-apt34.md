# 🎯 APT34 (OilRig)

## 🧠 Présentation

**APT34**, également connu sous le nom de "OilRig", est un groupe de menace avancée (APT) d'origine iranienne, présumé être lié au gouvernement iranien. Le groupe est spécialisé dans le cyber-espionnage et cible principalement les organisations du Moyen-Orient, notamment les gouvernements, les entreprises pétrolières et gazières, et les institutions financières.

---

## 🔎 Historique des Opérations

| Année | Opération | Description |
|-------|-----------|-------------|
| **2014-2015** | Espionnage | Campagnes contre des organisations gouvernementales |
| **2016** | Pétrole & Gaz | Attaques contre des entreprises pétrolières et gazières |
| **2017** | Cannon | Compromission de la chaîne d'approvisionnement |
| **2018** | Finance | Attaques contre des institutions financières |
| **2019** | TwoFace | Attaques contre des organisations de défense |
| **2020** | Zero-Day | Exploitation de vulnérabilités zero-day |
| **2021** | Santé | Attaques contre des organisations de santé |

---

## 🧰 Tactiques, Techniques et Procédures (TTPs)

| Tactique MITRE ATT&CK | Description |
|------------------------|-------------|
| **Initial Access** | Phishing ciblé, exploitation de vulnérabilités zero-day |
| **Execution** | PowerShell, DLL malveillantes, scripts personnalisés |
| **Persistence** | Backdoors personnalisés, modification du registre Windows |
| **Credential Access** | Dumping de LSASS, vol de tickets Kerberos |
| **Lateral Movement** | PSExec, WMI, RDP |
| **Exfiltration** | Protocoles chiffrés, DNS tunneling |
| **Impact** | Destruction de données, sabotage |

---

## 📊 Malware et Outils

### Malware Principaux
- **Helminth** : Backdoor principal
- **TwoFace** : Framework d'attaque
- **Cannon** : Outil de persistance
- **PowGoop** : Outil de post-exploitation
- **QuasarRAT** : Remote Access Tool

### Infrastructure C2
- Serveurs proxy
- Domaines de typosquatting
- Services cloud compromis
- Serveurs C2 personnalisés

---

## 🛡️ Recommandations de Protection

### Mesures Préventives
- ✅ Authentification à deux facteurs (2FA)
- ✅ Mise à jour régulière des systèmes
- ✅ Surveillance des accès VPN
- ✅ Formation au phishing
- ✅ Segmentation du réseau
- ✅ Sauvegardes régulières

### Détection
- 🔍 Surveillance des connexions sortantes
- 🔍 Analyse des logs d'authentification
- 🔍 Détection des comportements anormaux
- 🔍 Monitoring des modifications de registre
- 🔍 Analyse des trafics réseau suspects

### Réponse
- 🚨 Isolation des systèmes compromis
- 🚨 Réinitialisation des mots de passe
- 🚨 Analyse forensique
- 🚨 Mise à jour des signatures
- 🚨 Communication avec les parties prenantes

---

## 📚 Références

- [MITRE ATT&CK - APT34](https://attack.mitre.org/groups/G0049/)
- [FireEye - APT34](https://www.fireeye.com/blog/threat-research/2017/05/apt34-iranian-espionage-actor.html)
- [Kaspersky - APT34](https://securelist.com/apt34-oilrig/89538/)
- [Microsoft - APT34](https://www.microsoft.com/security/blog/2020/09/24/new-sophisticated-email-based-malware-from-actor-apt34-targets-organizations-in-14-countries/)

---

> ⚠️ Ce document est fourni à des fins d'information et de sensibilisation. L'analyse des menaces doit être faite dans un cadre légal et éthique.

## 📅 Mise à Jour
- Dernière mise à jour : [Date]
- Version : 1.0
- Statut : Actif

<div align="center">
  <img src="../../assets/logos/apt34-banner.png" alt="APT34 Banner" width="600"/>
</div> 