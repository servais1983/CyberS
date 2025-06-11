#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SemanticSearch:
    def __init__(self, config_path: str = "search-config.json"):
        """Initialise le moteur de recherche sémantique."""
        self.config = self._load_config(config_path)
        self.documents = {}
        self.vectorizer = TfidfVectorizer(
            stop_words='english',
            ngram_range=(1, 2),
            max_features=5000
        )
        self._index_documents()

    def _load_config(self, config_path: str) -> Dict:
        """Charge la configuration depuis le fichier JSON."""
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _index_documents(self) -> None:
        """Indexe tous les documents Markdown."""
        for pattern in self.config['indexing']['paths']:
            for file_path in Path('.').glob(pattern):
                if self._should_index(file_path):
                    self._process_document(file_path)

    def _should_index(self, file_path: Path) -> bool:
        """Vérifie si le fichier doit être indexé."""
        for exclude in self.config['indexing']['exclude']:
            if re.match(exclude, str(file_path)):
                return False
        return True

    def _process_document(self, file_path: Path) -> None:
        """Traite un document Markdown."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extraction des métadonnées YAML
            metadata = self._extract_metadata(content)
            
            # Stockage du document
            self.documents[str(file_path)] = {
                'content': content,
                'metadata': metadata,
                'path': str(file_path)
            }
        except Exception as e:
            print(f"Erreur lors du traitement de {file_path}: {e}")

    def _extract_metadata(self, content: str) -> Dict:
        """Extrait les métadonnées YAML du document."""
        metadata = {}
        if content.startswith('---'):
            try:
                end = content.find('---', 3)
                if end != -1:
                    yaml_content = content[3:end]
                    # Parsing simple des métadonnées
                    for line in yaml_content.split('\n'):
                        if ':' in line:
                            key, value = line.split(':', 1)
                            metadata[key.strip()] = value.strip()
            except Exception as e:
                print(f"Erreur lors de l'extraction des métadonnées: {e}")
        return metadata

    def search(self, query: str, max_results: int = None) -> List[Dict]:
        """Effectue une recherche sémantique."""
        if not max_results:
            max_results = self.config['searchEngine']['settings']['maxResults']

        # Préparation des documents pour la recherche
        docs = list(self.documents.values())
        contents = [doc['content'] for doc in docs]
        
        # Ajout de la requête
        contents.append(query)
        
        # Vectorisation
        tfidf_matrix = self.vectorizer.fit_transform(contents)
        
        # Calcul de la similarité
        query_vector = tfidf_matrix[-1]
        doc_vectors = tfidf_matrix[:-1]
        similarities = cosine_similarity(query_vector, doc_vectors).flatten()
        
        # Tri des résultats
        results = []
        for idx, score in enumerate(similarities):
            if score >= self.config['searchEngine']['settings']['minRelevance']:
                doc = docs[idx]
                results.append({
                    'path': doc['path'],
                    'score': float(score),
                    'metadata': doc['metadata'],
                    'snippet': self._generate_snippet(doc['content'], query)
                })
        
        # Tri par score et limitation du nombre de résultats
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:max_results]

    def _generate_snippet(self, content: str, query: str, max_length: int = 200) -> str:
        """Génère un extrait pertinent du document."""
        # Suppression du YAML front matter
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                content = content[end + 3:]

        # Recherche du contexte autour des mots de la requête
        words = query.lower().split()
        for word in words:
            pos = content.lower().find(word)
            if pos != -1:
                start = max(0, pos - max_length // 2)
                end = min(len(content), pos + max_length // 2)
                return content[start:end].strip() + "..."
        
        # Si aucun mot n'est trouvé, retourner le début du document
        return content[:max_length].strip() + "..."

def main():
    """Fonction principale pour tester le moteur de recherche."""
    search_engine = SemanticSearch()
    
    while True:
        query = input("\nEntrez votre recherche (ou 'q' pour quitter): ")
        if query.lower() == 'q':
            break
            
        results = search_engine.search(query)
        
        print(f"\nRésultats pour '{query}':")
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result['path']} (Score: {result['score']:.2f})")
            print(f"   {result['snippet']}")
            if result['metadata']:
                print("   Métadonnées:", result['metadata'])

if __name__ == "__main__":
    main() 