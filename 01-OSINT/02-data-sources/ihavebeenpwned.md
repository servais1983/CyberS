# Have I Been Pwned (HIBP) - Vérification de Compromission

## 🎯 Présentation
Have I Been Pwned est le service de référence créé par Troy Hunt pour vérifier si des comptes email ont été compromis lors de fuites de données. Il couvre plus de 11 milliards de comptes compromis.

## 📈 Statistiques

### Couverture Actuelle
- **11+ milliards** de comptes référencés
- **600+ breaches** répertoriées
- **30+ milliards** de mots de passe
- **Mise à jour** quotidienne

### Types de Données
- **Adresses email** : Principale identification
- **Mots de passe** : Hashés et plain text
- **Données personnelles** : Noms, téléphones, adresses
- **Informations financières** : Selon les breaches

## 🛠️ Utilisation

### Interface Web
1. **Accès** : [haveibeenpwned.com](https://haveibeenpwned.com/)
2. **Recherche email** : Saisie d'adresse email
3. **Résultats** : Liste des breaches trouvées
4. **Détails** : Informations par breach

### API Access
```python
import requests
import time

class HIBPChecker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://haveibeenpwned.com/api/v3"
        self.headers = {
            'hibp-api-key': api_key,
            'User-Agent': 'OSINT-Investigation-Tool'
        }
    
    def check_email(self, email):
        """Vérifier un email dans les breaches"""
        url = f"{self.base_url}/breachedaccount/{email}"
        
        try:
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return []
            else:
                print(f"Erreur: {response.status_code}")
                return None
                
        except requests.RequestException as e:
            print(f"Erreur requête: {e}")
            return None
    
    def check_password(self, password):
        """Vérifier un mot de passe (SHA-1)"""
        import hashlib
        
        sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                hashes = response.text.split('\n')
                for hash_entry in hashes:
                    if hash_entry.startswith(suffix):
                        count = hash_entry.split(':')[1]
                        return int(count)
                return 0
            else:
                return None
                
        except requests.RequestException as e:
            print(f"Erreur requête: {e}")
            return None
```

## 📊 Analyse des Résultats

### Structure des Données
```json
[
  {
    "Name": "Adobe",
    "Title": "Adobe",
    "Domain": "adobe.com",
    "BreachDate": "2013-10-04",
    "AddedDate": "2013-12-04T00:00:00Z",
    "ModifiedDate": "2022-05-15T23:52:49Z",
    "PwnCount": 152445165,
    "Description": "In October 2013, 153 million Adobe accounts were breached...",
    "LogoPath": "https://haveibeenpwned.com/Content/Images/PwnedLogos/Adobe.png",
    "DataClasses": [
      "Email addresses",
      "Password hints",
      "Passwords",
      "Usernames"
    ],
    "IsVerified": true,
    "IsFabricated": false,
    "IsSensitive": false,
    "IsRetired": false,
    "IsSpamList": false,
    "IsMalware": false
  }
]
```

### Métriques d'Analyse
- **PwnCount** : Nombre de comptes affectés
- **DataClasses** : Types de données compromises
- **BreachDate** : Date de la compromise
- **IsVerified** : Statut de vérification
- **IsSensitive** : Nature sensible des données

## 🎯 Applications OSINT

### Investigation Personnelle
```python
def investigate_person(email):
    hibp = HIBPChecker("YOUR_API_KEY")
    
    # Vérification email principal
    breaches = hibp.check_email(email)
    
    if breaches:
        print(f"Email {email} compromis dans {len(breaches)} fuites:")
        
        for breach in breaches:
            print(f"\n• {breach['Name']} ({breach['BreachDate']})")
            print(f"  - {breach['PwnCount']:,} comptes affectés")
            print(f"  - Données: {', '.join(breach['DataClasses'])}")
            
            # Analyse de sensibilité
            if breach['IsSensitive']:
                print("  ⚠️ SENSIBLE - Données particulièrement sensibles")
    else:
        print(f"Email {email} non trouvé dans les fuites répertoriées")
```

### Audit d'Entreprise
```python
def audit_company_domain(domain):
    """Audit des emails d'un domaine d'entreprise"""
    
    # Génération d'emails probables
    common_prefixes = ['admin', 'info', 'contact', 'support', 'sales']
    emails_to_check = [f"{prefix}@{domain}" for prefix in common_prefixes]
    
    # Ajout d'emails découverts via OSINT
    # (LinkedIn, site web, etc.)
    
    compromised_accounts = []
    
    for email in emails_to_check:
        breaches = hibp.check_email(email)
        if breaches:
            compromised_accounts.append({
                'email': email,
                'breaches': breaches,
                'risk_level': calculate_risk_level(breaches)
            })
        
        time.sleep(1.5)  # Respect rate limiting
    
    return compromised_accounts

def calculate_risk_level(breaches):
    """Calcul du niveau de risque"""
    risk_score = 0
    
    for breach in breaches:
        # Facteurs de risque
        if 'Passwords' in breach['DataClasses']:
            risk_score += 3
        if 'Credit cards' in breach['DataClasses']:
            risk_score += 5
        if breach['IsSensitive']:
            risk_score += 2
        if not breach['IsVerified']:
            risk_score += 1
    
    if risk_score >= 10:
        return "CRITIQUE"
    elif risk_score >= 5:
        return "ELEVE"
    elif risk_score >= 2:
        return "MOYEN"
    else:
        return "FAIBLE"
```

## 💰 Modèle Tarifaire

### Accès Gratuit
- **Interface web** : Recherche manuelle illimitée
- **Rate limiting** : 1 requête par 1.5 seconde
- **Pas d'API** : Accès API non inclus

### Abonnement API
- **Personnel** : $3.50/mois
- **Commercial** : Variable selon usage
- **Rate limit** : Plus élevé
- **Support** : Prioritaire

## 🔧 Outils Complémentaires

### Wrappers et Librairies
```bash
# Installation Python
pip install pyhunter
pip install h8mail
pip install holehe

# H8mail - Email OSINT
h8mail -t target@example.com

# Holehe - Email to social media
holehe target@example.com
```

### Intégration avec d'autres Outils
- **Maltego** : Transform HIBP
- **Shodan** : Corrélation infrastructure
- **TheHarvester** : Collecte d'emails
- **SpiderFoot** : Intégration native

## ⚠️ Limitations et Considérations

### Limitations Techniques
- **Rate limiting** : Limitation du taux de requêtes
- **Couverture** : Toutes les fuites ne sont pas incluses
- **Delayed inclusion** : Délai d'ajout de nouvelles fuites
- **False negatives** : Possible absence de résultats

### Considérations Éthiques
- **Vie privée** : Respect de la confidentialité
- **Usage légitime** : Justification de l'utilisation
- **Notification** : Informer les personnes concernées
- **Sécurisation** : Protection des résultats obtenus

---

*HIBP est devenu un standard de l'industrie pour la vérification de compromission de comptes*