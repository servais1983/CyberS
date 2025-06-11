# SpiderFoot - Automatisation OSINT

## 🎯 Présentation
SpiderFoot est un framework OSINT open-source qui automatise la collecte d'informations sur des cibles en utilisant plus de 200 sources de données différentes.

## 🏗️ Architecture

### Composants Principaux
- **Scanner Engine** : Moteur de scan principal
- **Modules** : Plus de 200 modules spécialisés
- **Web Interface** : Interface graphique web
- **API** : Interface programmatique
- **Database** : Base de données SQLite intégrée

### Types de Modules
```
Passive Reconnaissance:
├── DNS enumeration
├── Subdomain discovery
├── Email harvesting
└── Social media profiling

Active Reconnaissance:
├── Port scanning
├── Web crawling
├── Service enumeration
└── Vulnerability scanning

Threat Intelligence:
├── Blacklist checking
├── Malware analysis
├── Reputation checking
└── IOC correlation
```

## 🚀 Installation et Configuration

### Installation Docker
```bash
# Pull de l'image officielle
docker pull spiderfoot/spiderfoot

# Lancement du conteneur
docker run -p 5001:5001 spiderfoot/spiderfoot
```

### Installation Source
```bash
# Clone du repository
git clone https://github.com/smicallef/spiderfoot.git
cd spiderfoot

# Installation des dépendances
pip3 install -r requirements.txt

# Lancement
python3 sf.py -l 127.0.0.1:5001
```

### Configuration API Keys
```python
# Configuration dans sf.py ou via interface web
api_keys = {
    'shodan': 'YOUR_SHODAN_API_KEY',
    'virustotal': 'YOUR_VT_API_KEY',
    'passivetotal': 'YOUR_PT_API_KEY',
    'hunter': 'YOUR_HUNTER_API_KEY',
    'hibp': 'YOUR_HIBP_API_KEY'
}
```

## 🎛️ Interface Web

### Dashboard Principal
```
┌─────────────────────────────────────────────┐
│             SpiderFoot v4.0                 │
├─────────────────────────────────────────────┤
│  New Scan                                   │
│  ┌─────────────────────────────────────────┐ │
│  │ Target: [_____________________]          │ │
│  │ Scan Name: [__________________]          │ │
│  │                                         │ │
│  │ Modules Selection:                      │ │
│  │ ☑ Passive DNS                          │ │
│  │ ☑ Email Harvesting                     │ │
│  │ ☑ Social Media                         │ │
│  │ ☑ Subdomain Discovery                  │ │
│  │ ☐ Port Scanning                        │ │
│  │                                         │ │
│  │ [Start Scan]                           │ │
│  └─────────────────────────────────────────┘ │
│                                             │
│  Recent Scans:                              │
│  • example.com (Complete) - 2024-01-15     │
│  • target.org (Running) - 2024-01-14       │
└─────────────────────────────────────────────┘
```

### Types de Scans
1. **By Category** : Sélection par catégorie de modules
2. **All** : Tous les modules disponibles
3. **Custom** : Sélection manuelle de modules
4. **Preset** : Configurations prédéfinies

## 🔍 Modules Essentiels

### Reconnaissance Passive
```python
# Exemple de module custom
class sfp_custom_osint(sfp_base):
    meta = {
        'name': "Custom OSINT Module",
        'summary': "Module personnalisé pour collecte OSINT",
        'flags': ["safe"],
        'useCases': ["Passive"],
        'categories': ["DNS"]
    }
    
    def setup(self, sfc, userOpts=dict()):
        self.sf = sfc
        self.results = dict()
        self.opts = userOpts
    
    def handleEvent(self, event):
        eventName = event.eventType
        srcModuleName = event.module
        eventData = event.data
        
        # Logique de traitement
        if eventName == "DOMAIN_NAME":
            subdomains = self.find_subdomains(eventData)
            
            for subdomain in subdomains:
                evt = SpiderFootEvent("DOMAIN_NAME", subdomain, 
                                    self.__name__, event)
                self.notifyListeners(evt)
```

### Modules de Threat Intelligence
- **Blacklist Checkers** : Vérification contre listes noires
- **Malware Scanners** : Détection de malware
- **Reputation Checkers** : Vérification de réputation
- **IOC Correlators** : Corrélation d'indicateurs

## 📊 Analyse des Résultats

### Visualisation des Données
```python
# Export des résultats
def export_scan_results(scan_id, format='json'):
    """
    Export des résultats d'un scan SpiderFoot
    """
    
    # Connexion à la base de données SpiderFoot
    db_path = "spiderfoot.db"
    conn = sqlite3.connect(db_path)
    
    # Requête des résultats
    query = """
    SELECT 
        se.event_type,
        se.event_data,
        se.event_module,
        se.created_time,
        st.scan_name
    FROM 
        scan_event_data se
    JOIN 
        scan_instance st ON se.scan_instance_id = st.guid
    WHERE 
        st.guid = ?
    ORDER BY 
        se.created_time
    """
    
    results = []
    for row in conn.execute(query, (scan_id,)):
        results.append({
            'event_type': row[0],
            'data': row[1],
            'module': row[2],
            'timestamp': row[3],
            'scan': row[4]
        })
    
    return results
```

### Types d'Événements
- **DOMAIN_NAME** : Noms de domaine découverts
- **IP_ADDRESS** : Adresses IP identifiées
- **EMAILADDR** : Adresses email collectées
- **SOCIAL_MEDIA** : Profils de réseaux sociaux
- **VULNERABILITY** : Vulnérabilités détectées

## 🤖 Automation et Scripting

### API Usage
```python
import requests
import json

class SpiderFootAPI:
    def __init__(self, base_url="http://localhost:5001"):
        self.base_url = base_url
    
    def start_scan(self, target, scan_name, modules=None):
        """Démarrage d'un nouveau scan"""
        
        payload = {
            'target': target,
            'scanname': scan_name,
            'modulelist': modules or 'all'
        }
        
        response = requests.post(
            f"{self.base_url}/startscan",
            data=payload
        )
        
        return response.json()
    
    def get_scan_status(self, scan_id):
        """Vérification du statut d'un scan"""
        
        response = requests.get(
            f"{self.base_url}/scanstatus",
            params={'id': scan_id}
        )
        
        return response.json()
    
    def get_scan_results(self, scan_id):
        """Récupération des résultats"""
        
        response = requests.get(
            f"{self.base_url}/scaneventresults",
            params={'id': scan_id}
        )
        
        return response.json()
```

### Script d'Automatisation
```python
#!/usr/bin/env python3
# Automation script pour SpiderFoot

import time
import json
from spiderfoot_api import SpiderFootAPI

def automated_osint_scan(targets, output_dir):
    """Scan OSINT automatisé pour multiple targets"""
    
    sf = SpiderFootAPI()
    scan_results = {}
    
    for target in targets:
        print(f"Démarrage scan pour {target}")
        
        # Configuration du scan
        scan_config = {
            'target': target,
            'scan_name': f"Auto_OSINT_{target}_{int(time.time())}",
            'modules': [
                'sfp_dnsresolve',
                'sfp_subdomains',
                'sfp_emailharvester',
                'sfp_social',
                'sfp_shodan',
                'sfp_virustotal'
            ]
        }
        
        # Démarrage du scan
        scan_response = sf.start_scan(**scan_config)
        scan_id = scan_response['id']
        
        # Attente de completion
        while True:
            status = sf.get_scan_status(scan_id)
            
            if status['status'] == 'FINISHED':
                break
            elif status['status'] == 'ERROR':
                print(f"Erreur lors du scan de {target}")
                break
            
            time.sleep(30)  # Attente 30 secondes
        
        # Récupération des résultats
        results = sf.get_scan_results(scan_id)
        scan_results[target] = results
        
        # Sauvegarde
        with open(f"{output_dir}/{target}_results.json", 'w') as f:
            json.dump(results, f, indent=2)
    
    return scan_results

# Usage
if __name__ == "__main__":
    targets = ['example.com', 'target.org', 'company.net']
    results = automated_osint_scan(targets, './results')
```

## 🎯 Cas d'Usage Spécialisés

### Investigation d'Entreprise
```python
# Configuration pour investigation d'entreprise
enterprise_modules = [
    'sfp_dnsresolve',           # Résolution DNS
    'sfp_subdomains',           # Découverte sous-domaines
    'sfp_emailharvester',       # Collecte d'emails
    'sfp_social',               # Profils sociaux
    'sfp_linkedin',             # Profils LinkedIn
    'sfp_certs',                # Certificats SSL
    'sfp_whois',                # Informations WHOIS
    'sfp_shodan',               # Devices Shodan
    'sfp_passivetotal',         # Intelligence passive
    'sfp_virustotal'            # Réputation VirusTotal
]
```

### Threat Intelligence
```python
# Configuration pour threat intelligence
threat_intel_modules = [
    'sfp_malwaredomains',       # Domaines malveillants
    'sfp_blacklist',            # Listes noires
    'sfp_reputation',           # Vérifications réputation
    'sfp_virustotal',           # Analyse VirusTotal
    'sfp_phishing',             # Détection phishing
    'sfp_badips',               # IPs malveillantes
    'sfp_tor',                  # Nodes Tor
    'sfp_abuseip'               # Base abuse IP
]
```

## 📈 Monitoring et Alertes

### Monitoring Continu
```python
# Script de monitoring continu
def continuous_monitoring(targets, interval_hours=24):
    """Monitoring continu de targets"""
    
    while True:
        for target in targets:
            # Nouveau scan
            scan_id = start_monitoring_scan(target)
            
            # Comparaison avec scan précédent
            previous_results = load_previous_results(target)
            current_results = get_scan_results(scan_id)
            
            # Détection de changements
            changes = compare_results(previous_results, current_results)
            
            if changes:
                send_alert(target, changes)
            
            # Sauvegarde des résultats
            save_results(target, current_results)
        
        # Attente prochaine itération
        time.sleep(interval_hours * 3600)
```

## 💡 Optimisation et Performance

### Configuration Avancée
```python
# Optimisation pour scans larges
optimized_config = {
    'threads': 20,              # Nombre de threads
    'timeout': 30,              # Timeout par module
    'maxthreads': 100,          # Max threads globaux
    'queuesize': 1000,          # Taille queue d'événements
    'delay': 0.5                # Délai entre requêtes
}
```

### Filtrage des Résultats
```python
# Filtrage intelligent des résultats
def filter_results(results, criteria):
    """Filtrage des résultats selon critères"""
    
    filtered = []
    
    for result in results:
        # Filtrage par type d'événement
        if result['event_type'] in criteria.get('event_types', []):
            continue
        
        # Filtrage par confiance
        if result.get('confidence', 100) < criteria.get('min_confidence', 50):
            continue
        
        # Filtrage par âge
        if is_too_old(result['timestamp'], criteria.get('max_age_days', 30)):
            continue
        
        filtered.append(result)
    
    return filtered
```

---

*SpiderFoot excelle dans l'automatisation de collecte OSINT multi-sources avec plus de 200 modules intégrés*