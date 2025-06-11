#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any, Union
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from datetime import datetime

class RecommendationEngine:
    def __init__(self, config_path: str = "config/recommendation_config.yaml"):
        """Initialise le moteur de recommandation."""
        self.config = self._load_config(config_path)
        self.vectorizer = TfidfVectorizer(
            max_features=self.config.get('max_features', 1000),
            stop_words='english'
        )
        self.content_matrix = None
        self.content_metadata = {}
        
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Charge la configuration depuis un fichier YAML."""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Erreur lors du chargement de la configuration: {e}")
            return {}
            
    def _extract_content_features(self, content: str) -> Dict[str, Any]:
        """Extrait les caractéristiques du contenu."""
        # Extraction des mots-clés
        keywords = self._extract_keywords(content)
        
        # Analyse de la difficulté
        difficulty = self._analyze_difficulty(content)
        
        # Identification des concepts
        concepts = self._identify_concepts(content)
        
        return {
            'keywords': keywords,
            'difficulty': difficulty,
            'concepts': concepts
        }
        
    def _extract_keywords(self, content: str) -> List[str]:
        """Extrait les mots-clés du contenu."""
        # Implémentation de l'extraction de mots-clés
        return []
        
    def _analyze_difficulty(self, content: str) -> str:
        """Analyse la difficulté du contenu."""
        # Implémentation de l'analyse de difficulté
        return "intermediate"
        
    def _identify_concepts(self, content: str) -> List[str]:
        """Identifie les concepts dans le contenu."""
        # Implémentation de l'identification des concepts
        return []
        
    def _calculate_similarity(self, content1: str, content2: str) -> float:
        """Calcule la similarité entre deux contenus."""
        if not self.content_matrix:
            return 0.0
            
        # Vectorisation des contenus
        vectors = self.vectorizer.transform([content1, content2])
        
        # Calcul de la similarité cosinus
        similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        
        return float(similarity)
        
    def _get_user_profile(self, user_id: str) -> Dict[str, Any]:
        """Récupère le profil utilisateur."""
        try:
            profile_path = os.path.join(
                self.config.get('user_profiles_dir', 'data/profiles'),
                f"{user_id}.json"
            )
            with open(profile_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erreur lors du chargement du profil utilisateur: {e}")
            return {
                'interests': [],
                'skill_level': 'beginner',
                'preferred_topics': [],
                'learning_path': []
            }
            
    def _update_user_profile(self, user_id: str, profile: Dict[str, Any]) -> bool:
        """Met à jour le profil utilisateur."""
        try:
            profile_path = os.path.join(
                self.config.get('user_profiles_dir', 'data/profiles'),
                f"{user_id}.json"
            )
            os.makedirs(os.path.dirname(profile_path), exist_ok=True)
            with open(profile_path, 'w', encoding='utf-8') as f:
                json.dump(profile, f, indent=2)
            return True
        except Exception as e:
            print(f"Erreur lors de la mise à jour du profil utilisateur: {e}")
            return False
            
    def _calculate_relevance_score(self, 
                                 content: Dict[str, Any],
                                 user_profile: Dict[str, Any]) -> float:
        """Calcule le score de pertinence pour un utilisateur."""
        # Score basé sur les intérêts
        interest_score = self._calculate_interest_score(
            content.get('keywords', []),
            user_profile.get('interests', [])
        )
        
        # Score basé sur le niveau de compétence
        skill_score = self._calculate_skill_score(
            content.get('difficulty', 'beginner'),
            user_profile.get('skill_level', 'beginner')
        )
        
        # Score basé sur les sujets préférés
        topic_score = self._calculate_topic_score(
            content.get('concepts', []),
            user_profile.get('preferred_topics', [])
        )
        
        # Combinaison des scores
        weights = self.config.get('score_weights', {
            'interest': 0.4,
            'skill': 0.3,
            'topic': 0.3
        })
        
        return (
            weights['interest'] * interest_score +
            weights['skill'] * skill_score +
            weights['topic'] * topic_score
        )
        
    def _calculate_interest_score(self, 
                                content_keywords: List[str],
                                user_interests: List[str]) -> float:
        """Calcule le score d'intérêt."""
        if not content_keywords or not user_interests:
            return 0.0
            
        # Calcul de l'intersection des mots-clés
        common_keywords = set(content_keywords) & set(user_interests)
        
        return len(common_keywords) / max(len(content_keywords), len(user_interests))
        
    def _calculate_skill_score(self, 
                             content_difficulty: str,
                             user_skill: str) -> float:
        """Calcule le score de compétence."""
        difficulty_levels = {
            'beginner': 1,
            'intermediate': 2,
            'advanced': 3
        }
        
        content_level = difficulty_levels.get(content_difficulty, 1)
        user_level = difficulty_levels.get(user_skill, 1)
        
        # Pénalité si le contenu est trop difficile
        if content_level > user_level + 1:
            return 0.0
            
        return 1.0 - abs(content_level - user_level) / 2.0
        
    def _calculate_topic_score(self,
                             content_concepts: List[str],
                             preferred_topics: List[str]) -> float:
        """Calcule le score de sujet."""
        if not content_concepts or not preferred_topics:
            return 0.0
            
        # Calcul de l'intersection des concepts
        common_concepts = set(content_concepts) & set(preferred_topics)
        
        return len(common_concepts) / max(len(content_concepts), len(preferred_topics))
        
    def get_recommendations(self,
                          user_id: str,
                          current_content: Optional[Dict[str, Any]] = None,
                          limit: int = 5) -> List[Dict[str, Any]]:
        """Génère des recommandations pour un utilisateur."""
        # Récupération du profil utilisateur
        user_profile = self._get_user_profile(user_id)
        
        # Calcul des scores de pertinence
        recommendations = []
        for content_id, content in self.content_metadata.items():
            if current_content and content_id == current_content.get('id'):
                continue
                
            score = self._calculate_relevance_score(content, user_profile)
            
            if current_content:
                # Ajout d'un bonus pour le contenu similaire
                similarity = self._calculate_similarity(
                    current_content.get('content', ''),
                    content.get('content', '')
                )
                score = score * (1 + similarity)
                
            recommendations.append({
                'content_id': content_id,
                'score': score,
                'metadata': content
            })
            
        # Tri et limitation des recommandations
        recommendations.sort(key=lambda x: x['score'], reverse=True)
        return recommendations[:limit]
        
    def update_content(self, content: Dict[str, Any]) -> bool:
        """Met à jour le contenu dans le système."""
        try:
            content_id = content.get('id')
            if not content_id:
                return False
                
            # Extraction des caractéristiques
            features = self._extract_content_features(content.get('content', ''))
            content.update(features)
            
            # Mise à jour des métadonnées
            self.content_metadata[content_id] = content
            
            # Mise à jour de la matrice de contenu
            if self.content_matrix is None:
                self.content_matrix = self.vectorizer.fit_transform(
                    [content.get('content', '')]
                )
            else:
                self.content_matrix = self.vectorizer.transform(
                    [content.get('content', '')]
                )
                
            return True
            
        except Exception as e:
            print(f"Erreur lors de la mise à jour du contenu: {e}")
            return False
            
    def track_user_interaction(self,
                             user_id: str,
                             content_id: str,
                             interaction_type: str) -> bool:
        """Enregistre une interaction utilisateur."""
        try:
            # Mise à jour du profil utilisateur
            user_profile = self._get_user_profile(user_id)
            
            # Mise à jour des intérêts
            content = self.content_metadata.get(content_id, {})
            if content:
                user_profile['interests'].extend(content.get('keywords', []))
                user_profile['interests'] = list(set(user_profile['interests']))
                
            # Mise à jour du niveau de compétence
            if interaction_type == 'complete':
                content_difficulty = content.get('difficulty', 'beginner')
                if content_difficulty == user_profile.get('skill_level'):
                    # Passage au niveau suivant
                    difficulty_levels = ['beginner', 'intermediate', 'advanced']
                    current_index = difficulty_levels.index(content_difficulty)
                    if current_index < len(difficulty_levels) - 1:
                        user_profile['skill_level'] = difficulty_levels[current_index + 1]
                        
            # Mise à jour du chemin d'apprentissage
            user_profile['learning_path'].append({
                'content_id': content_id,
                'interaction_type': interaction_type,
                'timestamp': datetime.now().isoformat()
            })
            
            return self._update_user_profile(user_id, user_profile)
            
        except Exception as e:
            print(f"Erreur lors du suivi de l'interaction utilisateur: {e}")
            return False
            
    def get_user_stats(self, user_id: str) -> Dict[str, Any]:
        """Récupère les statistiques d'un utilisateur."""
        user_profile = self._get_user_profile(user_id)
        
        return {
            'total_interactions': len(user_profile.get('learning_path', [])),
            'skill_level': user_profile.get('skill_level', 'beginner'),
            'interests_count': len(user_profile.get('interests', [])),
            'preferred_topics_count': len(user_profile.get('preferred_topics', [])),
            'last_interaction': user_profile.get('learning_path', [{}])[-1].get('timestamp')
            if user_profile.get('learning_path') else None
        }

def main():
    """Fonction principale."""
    recommender = RecommendationEngine()
    
    # Exemple d'utilisation
    content = {
        'id': 'example-1',
        'content': 'Contenu de test',
        'title': 'Document de test',
        'author': 'Test User',
        'date': datetime.now().isoformat()
    }
    
    # Mise à jour du contenu
    recommender.update_content(content)
    
    # Génération de recommandations
    recommendations = recommender.get_recommendations('user-1', content)
    print("Recommandations:", recommendations)
    
    # Suivi d'une interaction
    recommender.track_user_interaction('user-1', 'example-1', 'view')
    
    # Statistiques utilisateur
    stats = recommender.get_user_stats('user-1')
    print("Statistiques utilisateur:", stats)

if __name__ == "__main__":
    main() 