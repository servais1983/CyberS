# Google Dorking - Techniques de Recherche Avancée

## 🎯 Objectif
Google Dorking (ou Google Hacking) consiste à utiliser des opérateurs de recherche avancée pour trouver des informations spécifiques, souvent sensibles, indexées par Google.

## 🔍 Opérateurs de Base

### Opérateurs de Site
```
site:example.com          # Recherche sur un site spécifique
site:*.example.com        # Recherche sur tous les sous-domaines
-site:example.com         # Exclure un site des résultats
```

### Opérateurs de Fichier
```
filetype:pdf              # Rechercher des fichiers PDF
filetype:xls              # Rechercher des fichiers Excel
filetype:doc              # Rechercher des fichiers Word
filetype:txt              # Rechercher des fichiers texte
```

### Opérateurs de Contenu
```
intitle:"index of"        # Pages d'index de répertoires
inurl:admin               # URLs contenant "admin"
intext:password           # Pages contenant le mot "password"
allintitle:               # Tous les mots dans le titre
```

## 🎯 Dorks Populaires

### Fichiers Sensibles
```
filetype:sql "MySQL dump" (pass|password|passwd|pwd)
filetype:log username password email
intitle:"index of" "parent directory" "size" "last modified" "description"
```

### Caméras et Appareils
```
inurl:"/view/index.shtml"  # Caméras Axis
inurl:ViewerFrame?Mode=    # Caméras IP
intitle:"Live View / - AXIS"
```

### Pages de Configuration
```
intitle:"Configuration" AND inurl:"config"
inurl:"admin/configuration"
intitle:"Admin Panel" OR "Control Panel"
```

### Bases de Données
```
filetype:sql mysql dump
intitle:"phpMyAdmin" "Welcome to phpMyAdmin"
"Index of /backup"
```

## ⚡ Techniques Avancées

### Recherche par Date
```
after:2020-01-01 before:2021-01-01
```

### Recherche par Région
```
lr:lang_fr    # Langue française
cr:countryFR  # France
```

### Wildcards
```
"password is *"    # * remplace n'importe quoi
"username * password"
```

## 🛡️ Considérations Éthiques

⚠️ **Important** : Utilisez ces techniques uniquement :
- Sur vos propres systèmes
- Dans le cadre de tests autorisés
- Pour la recherche académique
- En respectant les lois locales

## 📚 Ressources

- [Google Hacking Database (GHDB)](https://www.exploit-db.com/google-hacking-database)
- [Advanced Google Search Operators](https://ahrefs.com/blog/google-advanced-search-operators/)
- [OSINT Framework](https://osintframework.com/)

---

*Utilisez ces techniques de manière éthique et légale*