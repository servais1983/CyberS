# Maltego - Plateforme d'Investigation et d'Analyse de Liens

## 🎯 Présentation
Maltego est une plateforme de visualisation et d'analyse de liens développée par Paterva, considérée comme l'un des outils OSINT les plus puissants pour mapper les relations entre entités.

## 🏗️ Architecture

### Concepts Clés
- **Entités** : Objets d'investigation (personnes, domaines, IPs, etc.)
- **Liens** : Relations entre entités
- **Transforms** : Scripts de collecte de données
- **Graphiques** : Visualisations des relations
- **Machines** : Workflows automatisés

### Types d'Entités
```
Personnes:
├── Person
├── EmailAddress
├── PhoneNumber
└── Alias

Infrastructure:
├── Domain
├── Website
├── IPAddress
├── Netblock
└── ASNumber

Social Media:
├── FacebookObject
├── TwitterAccount
├── LinkedInProfile
└── InstagramProfile
```

## 🔧 Installation et Configuration

### Versions Disponibles
- **Maltego CE** : Version communautaire gratuite
- **Maltego Classic** : Version standard payante
- **Maltego XL** : Version enterprise

### Configuration Initiale
```python
# Installation des transforms via Python
pip install maltego-trx

# Structure basique d'un transform
from maltego_trx.entities import Person, EmailAddress
from maltego_trx.transform import MaltegoTransform

class EmailToPersonTransform(MaltegoTransform):
    @classmethod
    def create_entities_on_graph(cls, request):
        # Logique de transformation
        email = request.entity
        
        # Recherche OSINT pour trouver la personne
        person_data = cls.lookup_person_by_email(email.value)
        
        if person_data:
            person = request.response.addEntity(Person)
            person.value = person_data['name']
            person.addProperty('email', email.value)
            
        return request.response
```

## 🎯 Cas d'Usage OSINT

### Investigation de Personnes
1. **Point de départ** : Email ou nom
2. **Expansion réseau** : Comptes sociaux associés
3. **Analyse relationnelle** : Connexions et associations
4. **Timeline** : Évolution temporelle des relations

### Analyse d'Infrastructure
```
Domaine cible:
├── Sous-domaines
├── Adresses IP
├── Certificats SSL
├── Enregistrements DNS
└── Technologies utilisées
```

### Investigation d'Entreprises
- **Mapping organisationnel** : Structure de l'entreprise
- **Analyse concurrentielle** : Relations sectorielles
- **Due diligence** : Vérification de partenaires
- **Threat intelligence** : Identification d'acteurs malveillants

## 🔄 Transforms Essentiels

### Transforms Intégrés
- **DNS Resolution** : Résolution de noms de domaine
- **Whois Lookup** : Informations de registration
- **Search Engine** : Requêtes moteurs de recherche
- **Social Networks** : Recherche réseaux sociaux

### Transforms Communautaires
- **VirusTotal** : Analyse de malware
- **Shodan** : Recherche d'appareils connectés
- **Have I Been Pwned** : Vérification de compromission
- **ThreatCrowd** : Threat intelligence

### Développement de Transforms Custom
```python
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform
from maltego_trx.entities import Domain, IPAddress
import requests

class CustomDomainToIPTransform(MaltegoTransform):
    @classmethod
    def create_entities_on_graph(cls, request):
        domain = request.entity.value
        
        # Résolution DNS custom
        try:
            import socket
            ip = socket.gethostbyname(domain)
            
            # Ajout de l'entité IP au graphique
            ip_entity = request.response.addEntity(IPAddress)
            ip_entity.value = ip
            ip_entity.addProperty('resolved_from', domain)
            
            # Informations additionnelles
            geoloc_data = cls.get_ip_geolocation(ip)
            if geoloc_data:
                ip_entity.addProperty('country', geoloc_data['country'])
                ip_entity.addProperty('city', geoloc_data['city'])
                
        except Exception as e:
            request.response.addUIMessage(f"Erreur: {str(e)}")
            
        return request.response
    
    @staticmethod
    def get_ip_geolocation(ip):
        # Implémentation géolocalisation
        pass
```

## 📊 Analyse et Visualisation

### Types de Graphiques
- **Graphique radial** : Entité centrale avec connexions
- **Graphique hiérarchique** : Structure organisationnelle
- **Graphique temporel** : Évolution dans le temps
- **Graphique géographique** : Répartition géographique

### Techniques d'Analyse
```python
# Analyse de centralité
def analyze_graph_centrality(graph):
    """
    Identification des entités les plus importantes
    """
    centrality_metrics = {
        'degree_centrality': {},  # Nombre de connexions
        'betweenness_centrality': {},  # Position d'intermédiaire
        'closeness_centrality': {},  # Proximité moyenne
        'eigenvector_centrality': {}  # Influence des connexions
    }
    
    # Calculs de centralité
    for entity in graph.entities:
        centrality_metrics['degree_centrality'][entity.id] = len(entity.links)
        # Autres métriques...
    
    return centrality_metrics
```

## 🤖 Machines et Automation

### Création de Machines
```xml
<!-- Exemple de machine XML -->
<MaltegoMachine version="1.0">
    <Name>Email Investigation Machine</Name>
    <Description>Investigation complète à partir d'un email</Description>
    <StartingEntityType>maltego.EmailAddress</StartingEntityType>
    
    <TransformChain>
        <Transform name="EmailToPersonTransform"/>
        <Transform name="PersonToSocialProfilesTransform"/>
        <Transform name="SocialProfileToContactsTransform"/>
    </TransformChain>
</MaltegoMachine>
```

### Workflow Automatisé
1. **Input** : Email address
2. **Étape 1** : Recherche personne associée
3. **Étape 2** : Identification profils sociaux
4. **Étape 3** : Mapping du réseau de contacts
5. **Étape 4** : Analyse des relations
6. **Output** : Graphique complet des relations

## 💡 Bonnes Pratiques

### Organisation des Investigations
- **Graphiques séparés** : Un graphique par enquête
- **Naming conventions** : Nommage cohérent des entités
- **Couches (Layers)** : Organisation par types d'information
- **Annotations** : Documentation des découvertes

### Gestion des Données
```python
# Export des données d'investigation
def export_investigation_data(graph, format='json'):
    """
    Export des données d'un graphique Maltego
    """
    export_data = {
        'entities': [],
        'links': [],
        'metadata': {
            'created': datetime.now().isoformat(),
            'investigator': 'OSINT_Analyst',
            'case_id': graph.case_id
        }
    }
    
    for entity in graph.entities:
        export_data['entities'].append({
            'id': entity.id,
            'type': entity.type,
            'value': entity.value,
            'properties': entity.properties
        })
    
    for link in graph.links:
        export_data['links'].append({
            'source': link.source_id,
            'target': link.target_id,
            'relationship': link.type
        })
    
    return export_data
```

## 🔗 Intégrations Avancées

### API Integration
- **Shodan API** : Recherche d'appareils IoT
- **VirusTotal** : Analyse de malware
- **PassiveTotal** : Intelligence DNS
- **Social Media APIs** : Données de réseaux sociaux

### Bases de Données Externes
```python
# Intégration base de données threat intelligence
class ThreatIntelTransform(MaltegoTransform):
    @classmethod
    def create_entities_on_graph(cls, request):
        ip_address = request.entity.value
        
        # Requête base de données TI
        threat_data = cls.query_threat_database(ip_address)
        
        if threat_data and threat_data['malicious']:
            # Ajout d'entité malware
            malware = request.response.addEntity('maltego.Malware')
            malware.value = threat_data['malware_family']
            malware.addProperty('first_seen', threat_data['first_seen'])
            malware.addProperty('threat_level', threat_data['severity'])
            
        return request.response
```

## 💰 Coûts et Licensing

### Maltego CE (Gratuit)
- **Limitations** : 12 transforms par graphique
- **Entités** : Limitées
- **Usage** : Personnel/éducatif

### Maltego Classic ($999/an)
- **Transforms illimités**
- **Toutes les entités**
- **Support commercial**
- **Machines avancées**

### Maltego XL (Sur devis)
- **Usage enterprise**
- **Intégrations custom**
- **Support dédié**
- **Formation incluse**

---

*Maltego reste l'outil de référence pour la visualisation de relations complexes en OSINT*