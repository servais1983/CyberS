# Exalyze : Plateforme d’analyse et de corrélation de malwares

## Présentation
Exalyze est une plateforme SaaS qui permet d’analyser, rechercher et apparier des fichiers suspects afin de détecter des malwares au moyen d’algorithmes avancés d’analyse statique et de code. :contentReference[oaicite:0]{index=0}

---

## Principales fonctionnalités

### Analyse statique avancée
- Comparaison **Machoc Hash**  
- Analyse de la structure du code  
- Détection d’obfuscation :contentReference[oaicite:1]{index=1}  

### Analyse de code
- Désassemblage complet des binaires (PE, ELF, .NET, x86/x64)  
- Reconstruction automatique des fonctions  
- Détection d’API malveillantes :contentReference[oaicite:2]{index=2}  

### Renseignement sur la menace
- Identification algorithmique des familles de malwares  
- Cartographie **MITRE ATT&CK**  
- Recherche par similarité de code :contentReference[oaicite:3]{index=3}  

#### Boîte à outils d’investigation
| Outil                       | À quoi ça sert ? |
|-----------------------------|------------------|
| **Extraction de séquences** | Traverse les chaînes & appels API pour révéler rapidement les capacités d’un binaire |
| **Extraction de capacités** | Associe chaque capacité détectée à ses TTP MITRE ATT&CK |
| **Entropy Map**             | Visualise la structure du binaire (sections packées, chiffrées, etc.) |
| **Génération YARA**         | Crée en un clic des règles YARA pertinentes |
| **Analyse de similarité**   | Compare un échantillon à l’intégralité de la base pour trouver des dérivés | :contentReference[oaicite:4]{index=4}  

---

## Chiffres clés (juin 2025)
| Indicateur            | Valeur |
|-----------------------|--------|
| Échantillons analysés | **155 900 +** |
| Fonctions analysées   | **148 M** |
| Fonctions PE          | **114,7 M** |
| Fonctions ELF         | **4,5 M** | :contentReference[oaicite:5]{index=5}  

---

## Cas d’usage emblématiques
- **Mélofée** – détection de variantes Linux APT chinoises  
- **PlugX** – identification rapide des capacités d’un backdoor historique  
- **Agent.BTZ / ComRAT** – recherche de variantes russes  
- **Dark Crystal RAT**, **SysJoker**, **Lambert** – pivot sur des familles complexes à forte évolution :contentReference[oaicite:6]{index=6}  

---

## Démarrage rapide
1. Glissez-déposez jusqu’à **10 fichiers** (≤ 25 MB chacun)  
2. Choisissez le niveau de confidentialité : *Public*, *Sensible* ou *Confidentiel*  
3. Lancez l’analyse et explorez les résultats (structure de code, séquences, similitudes, etc.) :contentReference[oaicite:7]{index=7}  

---

## Modèle d’abonnement
- **Gratuit** : envoi d’échantillons publics, accès aux analyses de base  
- **Groupes collaboratifs** : chasse en équipe sur des jeux d’échantillons partagés  
- **Plans privés** : analyse de fichiers sensibles/confidentiels hors partage :contentReference[oaicite:8]{index=8}  

---

## Ressources
- Documentation : <https://docs.exalyze.io/>  
- API REST : <https://docs.exalyze.io/api.html>  
- Blog Exatrack : <https://blog.exatrack.com>  
- Compte X (Twitter) : <https://twitter.com/Exalyze_io> :contentReference[oaicite:9]{index=9}  

---

> *Exalyze est développé par des analystes malware pour des analystes ; il accélère le reverse engineering sans sacrifier la profondeur technique.*
