# Outils d'Intelligence pour le Repository CyberS

Ce dossier contient un ensemble d'outils pour rendre le repository CyberS plus intelligent et interactif.

## Structure des Outils

```
tools/
├── validation/           # Outils de validation de contenu
├── recommendation/       # Système de recommandation
├── interactive_docs/     # Documentation interactive
└── README.md            # Ce fichier
```

## 1. Système de Validation de Contenu

Le système de validation vérifie automatiquement la qualité et la cohérence du contenu.

### Installation

```bash
pip install -r requirements.txt
```

### Utilisation

```bash
python tools/validation/validate_content.py
```

### Fonctionnalités

- Vérification des métadonnées YAML
- Validation de la structure des documents
- Vérification des liens et images
- Contrôle du formatage
- Génération de rapports

## 2. Système de Recommandation

Le système de recommandation suggère du contenu pertinent basé sur le contexte et les préférences utilisateur.

### Installation

```bash
pip install -r requirements.txt
```

### Utilisation

```bash
python tools/recommendation/recommendation_engine.py
```

### Fonctionnalités

- Analyse sémantique du contenu
- Profils utilisateurs
- Recommandations personnalisées
- Suivi des intérêts
- Métriques de performance

## 3. Documentation Interactive

Le système de documentation interactive transforme le contenu Markdown en pages web interactives.

### Installation

```bash
pip install -r requirements.txt
```

### Utilisation

```bash
python tools/interactive_docs/interactive_docs.py
```

### Fonctionnalités

- Diagrammes Mermaid interactifs
- Blocs de code exécutables
- Quiz de validation
- Visualisations dynamiques
- Export vers notebooks Jupyter

## Configuration

Chaque outil possède son propre fichier de configuration dans le dossier `config/` :

- `validation_config.yaml` : Configuration de la validation
- `recommendation_config.yaml` : Configuration des recommandations
- `interactive_docs_config.yaml` : Configuration de la documentation interactive

## Exemples

Des exemples d'utilisation sont disponibles dans le dossier `examples/` :

- `interactive_doc_example.md` : Exemple de document interactif
- `validation_example.md` : Exemple de validation
- `recommendation_example.md` : Exemple de recommandation

## Dépendances

Les dépendances sont listées dans `requirements.txt` :

```
numpy>=1.21.0
scikit-learn>=1.0.0
pathlib>=1.0.1
pandas>=2.0.3
scipy>=1.10.1
joblib>=1.3.1
markdown>=3.3.0
jinja2>=3.0.0
nbformat>=5.1.0
matplotlib>=3.4.0
networkx>=2.6.0
pyyaml>=5.4.0
requests>=2.26.0
beautifulsoup4>=4.9.0
```

## Contribution

Pour contribuer à ces outils :

1. Fork le repository
2. Créer une branche pour votre fonctionnalité
3. Ajouter vos modifications
4. Soumettre une pull request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 