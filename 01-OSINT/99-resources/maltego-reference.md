# Maltego - Guide de Référence Complet

## 🎯 Vue d'Ensemble
Guide complet des fonctionnalités Maltego pour l'OSINT professionnel, couvrant les entités, transforms, et techniques avancées.

## 📋 Types d'Entités Complètes

### Entités Personnes
```python
# Entités liées aux personnes
person_entities = {
    'Person': 'Personne physique',
    'PersonFull': 'Personne avec détails complets',
    'EmailAddress': 'Adresse email',
    'PhoneNumber': 'Numéro de téléphone',
    'Alias': 'Pseudonyme ou alias',
    'Document': 'Document associé',
    'Image': 'Photo de la personne',
    'Location': 'Localisation géographique'
}
```

### Entités Infrastructure
```python
# Entités techniques et infrastructure
infra_entities = {
    'Domain': 'Nom de domaine',
    'DNSName': 'Enregistrement DNS',
    'Website': 'Site web',
    'URL': 'URL spécifique',
    'IPAddress': 'Adresse IP',
    'IPv4Address': 'Adresse IPv4',
    'IPv6Address': 'Adresse IPv6',
    'Netblock': 'Bloc réseau',
    'ASNumber': 'Numéro AS',
    'Port': 'Port réseau',
    'Service': 'Service réseau'
}
```

### Entités Géographiques
```python
# Entités de localisation
geo_entities = {
    'Location': 'Lieu géographique',
    'GPS': 'Coordonnées GPS',
    'Country': 'Pays',
    'City': 'Ville',
    'StreetAddress': 'Adresse postale',
    'PostalCode': 'Code postal'
}
```

## 🔄 Transforms Essentiels

### Transforms de Base
```python
# Configuration des transforms principaux
core_transforms = {
    'DNS_resolution': {
        'input': 'Domain',
        'output': ['IPAddress', 'DNSName'],
        'description': 'Résolution DNS standard'
    },
    'Whois_lookup': {
        'input': ['Domain', 'IPAddress'],
        'output': ['Person', 'Organization', 'Location'],
        'description': 'Informations WHOIS'
    },
    'Subdomain_discovery': {
        'input': 'Domain',
        'output': 'Domain',
        'description': 'Découverte de sous-domaines'
    }
}
```

### Transforms Sociaux
```python
# Transforms pour réseaux sociaux
social_transforms = {
    'Email_to_social': {
        'input': 'EmailAddress',
        'output': ['TwitterAccount', 'FacebookProfile', 'LinkedInProfile'],
        'description': 'Recherche profils depuis email'
    },
    'Username_search': {
        'input': 'Alias',
        'output': ['SocialProfile', 'ForumProfile'],
        'description': 'Recherche username multi-plateformes'
    },
    'Social_connections': {
        'input': 'SocialProfile',
        'output': ['Person', 'SocialProfile'],
        'description': 'Mapping des connexions sociales'
    }
}
```

## 🎨 Techniques de Visualisation

### Layouts de Graphiques
```python
# Configurations de layouts
layout_configs = {
    'radial': {
        'center_node': 'main_target',
        'layers': 3,
        'spacing': 'automatic',
        'use_case': 'Investigation centrée sur une entité'
    },
    'hierarchical': {
        'direction': 'top_down',
        'levels': 'automatic',
        'alignment': 'center',
        'use_case': 'Structure organisationnelle'
    },
    'force_directed': {
        'attraction': 'medium',
        'repulsion': 'high',
        'iterations': 1000,
        'use_case': 'Relations complexes'
    },
    'circular': {
        'radius': 'adaptive',
        'clustering': True,
        'use_case': 'Groupes de connexions'
    }
}

# Application de layout
def apply_optimal_layout(graph_type, entity_count):
    if entity_count < 20:
        return 'radial'
    elif entity_count < 100:
        return 'force_directed'
    else:
        return 'hierarchical'
```

### Styling et Représentation
```python
# Configuration de styles
entity_styles = {
    'Person': {
        'color': '#4CAF50',
        'shape': 'circle',
        'icon': 'person',
        'size': 'medium'
    },
    'Domain': {
        'color': '#2196F3',
        'shape': 'rectangle',
        'icon': 'domain',
        'size': 'large'
    },
    'EmailAddress': {
        'color': '#FF9800',
        'shape': 'envelope',
        'icon': 'email',
        'size': 'small'
    },
    'SocialProfile': {
        'color': '#9C27B0',
        'shape': 'hexagon',
        'icon': 'social',
        'size': 'medium'
    }
}
```

## 🤖 Machines et Workflows

### Machine de Base - Email Investigation
```xml
<?xml version="1.0" encoding="UTF-8"?>
<MaltegoMachine version="1.0">
    <Name>Email Deep Investigation</Name>
    <Description>Investigation complète à partir d'une adresse email</Description>
    <StartingEntityType>maltego.EmailAddress</StartingEntityType>
    
    <TransformChain>
        <!-- Étape 1: Vérification email -->
        <Transform name="EmailToPersonTransform">
            <Settings>
                <Property name="confidence.threshold" value="80"/>
            </Settings>
        </Transform>
        
        <!-- Étape 2: Recherche domaine -->
        <Transform name="EmailToDomainTransform"/>
        
        <!-- Étape 3: Profils sociaux -->
        <Transform name="EmailToSocialProfilesTransform">
            <Settings>
                <Property name="platforms" value="all"/>
                <Property name="deep_search" value="true"/>
            </Settings>
        </Transform>
        
        <!-- Étape 4: Breach checking -->
        <Transform name="EmailToBreachTransform"/>
        
        <!-- Étape 5: Network expansion -->
        <Transform name="SocialToConnectionsTransform">
            <Conditions>
                <EntityType>SocialProfile</EntityType>
            </Conditions>
        </Transform>
    </TransformChain>
    
    <PostProcessing>
        <RemoveDuplicates enabled="true"/>
        <FilterLowConfidence threshold="50"/>
        <ApplyLayout type="radial"/>
    </PostProcessing>
    
</MaltegoMachine>
```

### Machine Avancée - Company Intelligence
```python
# Machine pour intelligence d'entreprise
class CompanyIntelligenceMachine:
    def __init__(self, company_domain):
        self.target = company_domain
        self.phases = [
            'infrastructure_mapping',
            'employee_discovery',
            'social_presence_analysis',
            'technology_stack_identification',
            'threat_surface_assessment'
        ]
    
    def execute_phase(self, phase_name):
        """Exécution d'une phase spécifique"""
        
        if phase_name == 'infrastructure_mapping':
            return self.map_infrastructure()
        elif phase_name == 'employee_discovery':
            return self.discover_employees()
        elif phase_name == 'social_presence_analysis':
            return self.analyze_social_presence()
        # ... autres phases
    
    def map_infrastructure(self):
        """Mapping de l'infrastructure"""
        transforms = [
            'DomainToSubdomainTransform',
            'DomainToIPTransform',
            'IPToNetblockTransform',
            'DomainToCertificateTransform',
            'DomainToTechnologyTransform'
        ]
        
        results = []
        for transform in transforms:
            result = self.run_transform(transform, self.target)
            results.extend(result)
        
        return results
    
    def discover_employees(self):
        """Découverte d'employés"""
        employee_sources = [
            'linkedin_company_search',
            'email_pattern_generation',
            'social_media_mentions',
            'conference_speakers',
            'github_organization_members'
        ]
        
        employees = []
        for source in employee_sources:
            found_employees = self.search_employees_via_source(source)
            employees.extend(found_employees)
        
        return self.deduplicate_employees(employees)
```

## 📊 Analyse de Données

### Métriques de Graphique
```python
class GraphAnalyzer:
    def __init__(self, graph_data):
        self.graph = graph_data
        self.metrics = {}
    
    def calculate_centrality_metrics(self):
        """Calcul des métriques de centralité"""
        
        import networkx as nx
        
        # Conversion en graph NetworkX
        G = self.convert_to_networkx()
        
        # Métriques de centralité
        self.metrics['degree_centrality'] = nx.degree_centrality(G)
        self.metrics['betweenness_centrality'] = nx.betweenness_centrality(G)
        self.metrics['closeness_centrality'] = nx.closeness_centrality(G)
        self.metrics['eigenvector_centrality'] = nx.eigenvector_centrality(G)
        
        return self.metrics
    
    def identify_key_entities(self, top_n=10):
        """Identification des entités clés"""
        
        key_entities = {}
        
        for metric_name, values in self.metrics.items():
            # Tri par valeur de centralité
            sorted_entities = sorted(values.items(), 
                                   key=lambda x: x[1], 
                                   reverse=True)
            
            key_entities[metric_name] = sorted_entities[:top_n]
        
        return key_entities
    
    def detect_communities(self):
        """Détection de communautés"""
        
        import networkx as nx
        from networkx.algorithms import community
        
        G = self.convert_to_networkx()
        
        # Détection de communautés
        communities = community.greedy_modularity_communities(G)
        
        return [
            {'id': i, 'members': list(comm), 'size': len(comm)}
            for i, comm in enumerate(communities)
        ]
```

### Export et Reporting
```python
class MaltegoExporter:
    def __init__(self, graph_data):
        self.graph = graph_data
    
    def export_to_json(self, include_metadata=True):
        """Export au format JSON"""
        
        export_data = {
            'nodes': [],
            'edges': [],
            'metadata': {}
        }
        
        # Export des entités
        for entity in self.graph.entities:
            node_data = {
                'id': entity.id,
                'type': entity.type,
                'value': entity.value,
                'properties': entity.properties if include_metadata else {}
            }
            export_data['nodes'].append(node_data)
        
        # Export des liens
        for link in self.graph.links:
            edge_data = {
                'source': link.source_id,
                'target': link.target_id,
                'type': link.type,
                'weight': link.weight
            }
            export_data['edges'].append(edge_data)
        
        # Métadonnées
        if include_metadata:
            export_data['metadata'] = {
                'created': datetime.now().isoformat(),
                'entity_count': len(export_data['nodes']),
                'relationship_count': len(export_data['edges']),
                'investigation_scope': self.graph.scope
            }
        
        return export_data
    
    def generate_html_report(self, template_path=None):
        """Génération de rapport HTML"""
        
        from jinja2 import Template
        
        # Template de base si non fourni
        default_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Maltego Investigation Report</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .header { background: #f5f5f5; padding: 20px; }
                .section { margin: 20px 0; }
                .entity { margin: 10px 0; padding: 10px; border-left: 3px solid #007cba; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>OSINT Investigation Report</h1>
                <p>Generated: {{ metadata.created }}</p>
                <p>Entities: {{ metadata.entity_count }} | Links: {{ metadata.relationship_count }}</p>
            </div>
            
            <div class="section">
                <h2>Key Entities</h2>
                {% for entity in key_entities %}
                <div class="entity">
                    <strong>{{ entity.type }}:</strong> {{ entity.value }}
                    <br><small>Connections: {{ entity.connection_count }}</small>
                </div>
                {% endfor %}
            </div>
            
            <div class="section">
                <h2>Network Analysis</h2>
                <p>Most connected entity: {{ most_connected.value }}</p>
                <p>Network density: {{ network_density }}</p>
            </div>
        </body>
        </html>
        """
        
        template = Template(default_template)
        
        # Préparation des données
        analysis_data = self.prepare_analysis_data()
        
        return template.render(**analysis_data)
```

## 🔧 Configuration Avancée

### Optimisation des Performances
```python
# Configuration optimisée pour investigations larges
performance_config = {
    'transform_settings': {
        'timeout': 60,              # Timeout par transform
        'max_entities': 1000,       # Limite d'entités par transform
        'concurrent_transforms': 5,  # Transforms simultanés
        'result_caching': True      # Cache des résultats
    },
    
    'memory_management': {
        'max_graph_size': 5000,     # Taille max du graphique
        'auto_cleanup': True,       # Nettoyage automatique
        'entity_limit_warning': 2000  # Alerte limite entités
    },
    
    'visualization': {
        'progressive_rendering': True,  # Rendu progressif
        'level_of_detail': True,       # Détail adaptatif
        'clustering_threshold': 100    # Seuil de clustering
    }
}
```

---

*Cette référence Maltego couvre les aspects essentiels pour une utilisation professionnelle en OSINT*