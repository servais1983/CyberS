# 🎯 APT29 (Cozy Bear)

## 🧠 Présentation

**APT29**, également connu sous le nom de "Cozy Bear", est un groupe de menace avancée (APT) d'origine russe, présumé être lié au SVR (Service de renseignement extérieur russe). Le groupe est spécialisé dans le cyber-espionnage et cible principalement les gouvernements, les organisations diplomatiques, et les institutions de recherche.

---

## 🔎 Historique des Opérations

| Année | Opération | Description |
|-------|-----------|-------------|
| **2014-2015** | Infiltration DNC | Compromission du réseau du Parti Démocrate américain |
| **2016** | Campagne présidentielle | Compromission de la campagne présidentielle américaine |
| **2017** | Attaques européennes | Attaques contre des organisations gouvernementales européennes |
| **2018** | WellMess | Attaques contre des institutions de recherche |
| **2019** | SNAKE | Compromission de réseaux diplomatiques |
| **2020** | SolarWinds | Compromission de la chaîne d'approvisionnement |
| **2021** | WellMail | Attaques par email |

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
- **WellMess** : Backdoor personnalisé
- **WellMail** : Outil d'exfiltration
- **SNAKE** : Framework d'attaque
- **CozyCar** : Outil de persistance
- **MiniDuke** : Malware de première génération

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

- [MITRE ATT&CK - APT29](https://attack.mitre.org/groups/G0016/)
- [FireEye - APT29](https://www.fireeye.com/blog/threat-research/2017/03/apt29_domain_techniques.html)
- [Kaspersky - APT29](https://securelist.com/apt29-cozybear/89538/)
- [Microsoft - APT29](https://www.microsoft.com/security/blog/2020/12/13/solarwinds-supply-chain-attack/)

---

> ⚠️ Ce document est fourni à des fins d'information et de sensibilisation. L'analyse des menaces doit être faite dans un cadre légal et éthique.

## 📅 Mise à Jour
- Dernière mise à jour : [Date]
- Version : 1.0
- Statut : Actif

<div align="center">
  <img src="../../assets/logos/apt29-banner.png" alt="APT29 Banner" width="600"/>
</div> 