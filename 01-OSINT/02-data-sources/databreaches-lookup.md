# Data Breaches - Recherche dans les Fuites de Données

## 🎯 Présentation
Les bases de données de fuites (data breaches) sont des ressources cruciales pour l'OSINT, permettant d'identifier des comptes compromis, mots de passe, et informations personnelles exposées lors de cyberattaques.

## 📊 Principales Sources

### Have I Been Pwned (HIBP)
- **Créateur** : Troy Hunt
- **Couverture** : 11+ milliards de comptes
- **Types** : Emails, mots de passe, données personnelles
- **API** : Accès programmatique disponible

### Intelligence X
- **Base** : 30+ milliards d'enregistrements
- **Sources** : Breaches, leaks, dumps
- **Recherche** : Email, domaine, IP, hash
- **Historique** : Archives étendues

### Dehashed
- **Focus** : Mots de passe déhashés
- **Recherche** : Multi-critères
- **Formats** : Divers types de hash
- **API** : Intégration disponible

## 🔍 Méthodologies de Recherche

### Recherche par Email
```python
# Exemple de recherche HIBP
import requests

def check_email_breach(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        'hibp-api-key': 'YOUR_API_KEY',
        'User-Agent': 'OSINT-Tool'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return "No breaches found"
    else:
        return f"Error: {response.status_code}"
```

### Recherche par Domaine
```bash
# Recherche Intelligence X
curl -X GET "https://2.intelx.io/phonebook/search?k=API_KEY&term=@company.com&media=0&target=1"
```

### Recherche par Hash
```python
# Vérification de hash de mot de passe
import hashlib

def check_password_hash(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if suffix in response.text:
        return "Password found in breach"
    else:
        return "Password not found"
```

## 🎯 Applications OSINT

### Investigation de Personnes
1. **Recherche email principal** → Fuites associées
2. **Analyse des breaches** → Informations révélées
3. **Corrélation temporelle** → Timeline d'exposition
4. **Expansion recherche** → Emails/pseudos découverts

### Sécurité d'Entreprise
1. **Audit domaine** → Employés compromis
2. **Évaluation risque** → Niveau d'exposition
3. **Alertes proactives** → Nouvelles fuites
4. **Formations** → Sensibilisation staff

### Threat Intelligence
1. **Profiling attaquants** → Identification d'acteurs
2. **IOC extraction** → Indicateurs de compromission
3. **Campaign tracking** → Suivi de campagnes
4. **Attribution** → Liens entre attaques

## 🛠️ Outils et Scripts

### Outils Automatisés
```bash
# H8mail - Email OSINT tool
h8mail -t target@example.com --bc 

# Sherlock - Username search
sherlock username --timeout 30

# Holehe - Email to social media
holehe target@example.com
```

### Scripts Python
```python
#!/usr/bin/env python3
# Breach aggregator script

import requests
import json
from time import sleep

class BreachAggregator:
    def __init__(self):
        self.hibp_key = "YOUR_HIBP_KEY"
        self.intelx_key = "YOUR_INTELX_KEY"
    
    def search_all_sources(self, email):
        results = {
            'hibp': self.search_hibp(email),
            'intelx': self.search_intelx(email),
            'dehashed': self.search_dehashed(email)
        }
        return results
    
    def generate_report(self, results):
        # Génération de rapport
        pass
```

## 📈 Analyse des Résultats

### Métriques Importantes
- **Nombre de breaches** : Fréquence d'exposition
- **Types de données** : Nature des informations compromises
- **Dates de breach** : Chronologie des incidents
- **Gravité** : Niveau de sensibilité des données

### Corrélation Cross-Source
```python
# Exemple d'analyse corrélée
def correlate_breaches(email_results):
    common_breaches = set()
    unique_data = []
    
    for source, breaches in email_results.items():
        for breach in breaches:
            if breach['name'] not in common_breaches:
                unique_data.append({
                    'source': source,
                    'breach': breach['name'],
                    'date': breach['date'],
                    'data_types': breach['data_classes']
                })
                common_breaches.add(breach['name'])
    
    return unique_data
```

## ⚠️ Considérations Légales

### Cadre Légal
- **Usage légitime** : Objectif légal et justifié
- **Minimisation** : Collecte limitée au nécessaire
- **Protection** : Sécurisation des données collectées
- **Retention** : Durée de conservation limitée

### Bonnes Pratiques
- **Anonymisation** : Masquer les données sensibles
- **Accès restreint** : Limiter l'accès
- **Audit trail** : Traçabilité des accès
- **Notification** : Informer les personnes concernées si requis

## 💰 Coûts et Accès

### Services Gratuits
- **HIBP (limité)** : 1 requête/1.5 secondes
- **Leaked Source** : Recherche basique
- **BreachDirectory** : Accès limité

### Services Payants
- **HIBP API** : $3.50/mois pour usage personnel
- **Intelligence X** : $9-199/mois selon usage
- **Dehashed** : $5-200/mois selon volume

## 🔗 Ressources Complémentaires

### Bases de Données Spécialisées
- **Snusbase** : Recherche multi-critères
- **LeakCheck** : API simple d'utilisation
- **Weleakinfo** : (Fermé mais données archives)
- **RaidForums** : Archives de forums (légalité variable)

### Outils d'Analyse
- **Maltego** : Visualisation de liens
- **Shodan** : Infrastructure exposée
- **Censys** : Analyse de certificats
- **Pipl** : Recherche de personnes

---

*La recherche dans les fuites de données est un aspect crucial de l'OSINT moderne, mais doit être pratiquée dans le respect de la législation*