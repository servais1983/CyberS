# 🔍 Moteur de Recherche Sémantique

Ce moteur de recherche sémantique permet de rechercher dans la documentation de manière intelligente, en comprenant le contexte et les concepts plutôt que de simples mots-clés.

## 🚀 Installation

1. Installez les dépendances :
```bash
pip install -r requirements.txt
```

2. Vérifiez la configuration dans `search-config.json`

## 💻 Utilisation

Lancez le moteur de recherche :
```bash
python search-engine.py
```

### Exemples de Recherche

- "détection d'intrusion" trouvera des documents sur :
  - Les systèmes de détection d'intrusion
  - Les logs et monitoring
  - Les APT et menaces avancées
  - Les outils de surveillance

- "analyse forensique" trouvera des documents sur :
  - L'investigation numérique
  - Les artefacts Windows
  - Les outils d'analyse
  - Les méthodologies d'enquête

## ⚙️ Configuration

Le fichier `search-config.json` permet de configurer :
- Les chemins à indexer
- Les exclusions
- Les paramètres de recherche
- Les mappings sémantiques

## 🔧 Personnalisation

### Ajouter de Nouveaux Concepts

Dans `search-config.json`, ajoutez de nouveaux concepts :
```json
"concepts": {
  "nouveau_concept": ["terme1", "terme2", "terme3"]
}
```

### Ajuster les Paramètres

Modifiez les paramètres de recherche :
```json
"settings": {
  "maxResults": 15,
  "minRelevance": 0.6,
  "language": "fr"
}
```

## 📊 Fonctionnalités

- Recherche sémantique
- Extraction de métadonnées
- Génération d'extraits pertinents
- Support multilingue
- Mapping de concepts

## 🔍 Comment ça marche ?

1. **Indexation**
   - Lecture des documents Markdown
   - Extraction des métadonnées
   - Vectorisation du contenu

2. **Recherche**
   - Analyse sémantique de la requête
   - Calcul de similarité
   - Tri des résultats

3. **Résultats**
   - Affichage des documents pertinents
   - Extraction de contexte
   - Métadonnées associées

## ⚠️ Limitations

- Nécessite Python 3.6+
- Dépend des métadonnées YAML
- Performance sur grands volumes

## 🔄 Mise à Jour

Pour mettre à jour l'index :
1. Modifiez les documents
2. Relancez le script
3. L'index sera automatiquement mis à jour

---

> ⚠️ Ce moteur de recherche est en constante évolution. N'hésitez pas à proposer des améliorations.

## 📅 Mise à Jour
- Dernière mise à jour : 2024-03-20
- Version : 1.0
- Statut : Actif 