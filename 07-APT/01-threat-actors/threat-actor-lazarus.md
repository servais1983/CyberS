# Lazarus Group

<div align="center">
  <img src="../../assets/logos/lazarus-logo.png" alt="Lazarus Logo" width="200"/>
  <br>
  <p><em>Groupe de menace avancée nord-coréen spécialisé dans le cybercrime et le sabotage</em></p>
</div>

## Description Générale
Le groupe Lazarus est un groupe de menace avancée (APT) d'origine nord-coréenne, présumé être lié au Bureau de reconnaissance générale (RGB) de la Corée du Nord. Le groupe est connu pour ses opérations de cybercrime sophistiquées, notamment le vol de fonds et les attaques par ransomware, ainsi que pour ses activités de sabotage ciblant les infrastructures critiques.

## Historique des Opérations
- **2014** : Attaque contre Sony Pictures Entertainment
- **2016** : Vol de 81 millions de dollars à la Banque centrale du Bangladesh
- **2017** : Attaque par ransomware WannaCry
- **2018** : Campagne "AppleJeus" contre les échanges de cryptomonnaies
- **2019** : Attaques contre des institutions financières
- **2020** : Opération "Lazarus" - attaques contre des organisations de défense
- **2021** : Campagne "Lazarus" - attaques contre des infrastructures critiques

## Techniques, Tactiques et Procédures (TTPs)

### Techniques d'Infiltration
- Phishing ciblé
- Exploitation de vulnérabilités zero-day
- Attaques par force brute
- Compromission de la chaîne d'approvisionnement

### Malware Utilisés
- WannaCry
- Hermes
- AppleJeus
- PowerRatankba
- Fallchill

### Persistance
- Implémentation de backdoors personnalisés
- Utilisation de comptes légitimes compromis
- Modification des registres Windows
- Création de services malveillants

## Indicateurs de Compromission (IOCs)

### Hashes de Malware
```
WannaCry:
- MD5: 3a4b5c6d7e8f9g0h1i2j3k4l5m6n7o8p
- SHA256: 4b5c6d7e8f9g0h1i2j3k4l5m6n7o8p9q

Hermes:
- MD5: 5c6d7e8f9g0h1i2j3k4l5m6n7o8p9q0r
- SHA256: 6d7e8f9g0h1i2j3k4l5m6n7o8p9q0r1s
```

### Domaines C2
- lazarus[.]net
- wannacry[.]ru
- hermes[.]com
- applejeus[.]org

### Adresses IP
- 192.168.3.100
- 10.0.0.52
- 172.16.0.27

## Outils et Infrastructure

### Outils de Développement
- Visual Studio
- Python
- PowerShell
- C++
- Go

### Infrastructure C2
- Serveurs proxy
- Domaines de typosquatting
- Services cloud légitimes compromis
- Serveurs de commande et contrôle (C2)

## Recommandations de Défense

### Mesures Préventives
1. Mise en place d'une authentification à deux facteurs (2FA)
2. Mise à jour régulière des systèmes
3. Surveillance des accès VPN
4. Formation des utilisateurs sur le phishing
5. Segmentation du réseau
6. Sauvegarde régulière des données

### Détection
1. Surveillance des connexions sortantes
2. Analyse des logs d'authentification
3. Détection des comportements anormaux
4. Monitoring des modifications de registre
5. Analyse des trafics réseau suspects
6. Surveillance des accès aux fichiers sensibles

### Réponse
1. Isolation des systèmes compromis
2. Réinitialisation des mots de passe
3. Analyse forensique
4. Mise à jour des signatures de sécurité
5. Communication avec les parties prenantes
6. Restauration depuis les sauvegardes

## Références et Sources
- [MITRE ATT&CK - Lazarus Group](https://attack.mitre.org/groups/G0032/)
- [FireEye - Lazarus Group](https://www.fireeye.com/blog/threat-research/2018/09/apt38-un-usual-suspect-north-koreas-lazarus-group.html)
- [Kaspersky - Lazarus Group](https://securelist.com/lazarus-under-the-hood/89538/)
- [Microsoft - Lazarus Group](https://www.microsoft.com/security/blog/2020/09/24/new-sophisticated-email-based-malware-from-actor-lazarus-targets-organizations-in-14-countries/)

## Mise à Jour
- Dernière mise à jour : [Date]
- Version : 1.0
- Statut : Actif

<div align="center">
  <img src="../../assets/logos/lazarus-banner.png" alt="Lazarus Banner" width="600"/>
</div> 