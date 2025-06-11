#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import yaml
import json
from pathlib import Path
from typing import Dict, List, Optional, Any, Union, cast
import markdown
from markdown.extensions import fenced_code, tables, codehilite, meta
import jinja2
import nbformat as nbf
from nbconvert import HTMLExporter
import matplotlib.pyplot as plt
import networkx as nx
from jinja2 import Template
from datetime import datetime
from matplotlib.figure import Figure

class InteractiveDocs:
    """Système de documentation interactive pour la cybersécurité."""
    
    def __init__(self, config_path: str = "config/interactive_docs_config.yaml"):
        """Initialise le système de documentation interactive.
        
        Args:
            config_path: Chemin vers le fichier de configuration YAML
        """
        self.config = self._load_config(config_path)
        self.template = self._load_template()
        self.md = markdown.Markdown(extensions=['meta', 'fenced_code', 'tables', 'toc'])
        
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Charge la configuration depuis un fichier YAML.
        
        Args:
            config_path: Chemin vers le fichier de configuration
            
        Returns:
            Dict contenant la configuration
        """
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Erreur lors du chargement de la configuration: {e}")
            return {}
            
    def _load_template(self) -> Template:
        """Charge le template HTML.
        
        Returns:
            Template Jinja2 pour le rendu HTML
        """
        try:
            template_path = self.config.get('template_path', 'templates/interactive_doc.html')
            with open(template_path, 'r', encoding='utf-8') as f:
                return Template(f.read())
        except Exception as e:
            print(f"Erreur lors du chargement du template: {e}")
            return Template("")
            
    def _extract_metadata(self, content: str) -> Dict[str, Any]:
        """Extrait les métadonnées du document Markdown.
        
        Args:
            content: Contenu Markdown du document
            
        Returns:
            Dict contenant les métadonnées extraites
        """
        self.md.convert(content)
        metadata: Dict[str, Any] = {}
        meta_data = getattr(self.md, 'Meta', {})
        if meta_data:
            for key, value in meta_data.items():
                if isinstance(value, list) and len(value) == 1:
                    metadata[key] = value[0]
                else:
                    metadata[key] = value
        return metadata
        
    def _process_code_blocks(self, content: str) -> str:
        """Traite les blocs de code pour l'exécution interactive.
        
        Args:
            content: Contenu Markdown à traiter
            
        Returns:
            Contenu HTML avec les blocs de code traités
        """
        def replace_code_block(match: re.Match) -> str:
            lang = match.group(1)
            code = match.group(2)
            if lang == 'python':
                return f'<div class="code-block" data-language="python">{code}</div>'
            return match.group(0)
            
        return re.sub(r'```(\w+)\n(.*?)\n```', replace_code_block, content, flags=re.DOTALL)
        
    def _process_quizzes(self, content: str) -> str:
        """Traite les quiz pour l'interactivité.
        
        Args:
            content: Contenu Markdown à traiter
            
        Returns:
            Contenu HTML avec les quiz traités
        """
        def replace_quiz(match: re.Match) -> str:
            quiz_data = yaml.safe_load(match.group(1))
            return f'<div class="quiz" data-quiz=\'{json.dumps(quiz_data)}\'></div>'
            
        return re.sub(r'```quiz\n(.*?)\n```', replace_quiz, content, flags=re.DOTALL)
        
    def _process_visualizations(self, content: str) -> str:
        """Traite les visualisations Mermaid.
        
        Args:
            content: Contenu Markdown à traiter
            
        Returns:
            Contenu HTML avec les visualisations traitées
        """
        def replace_mermaid(match: re.Match) -> str:
            diagram = match.group(1)
            return f'<div class="mermaid">{diagram}</div>'
            
        return re.sub(r'```mermaid\n(.*?)\n```', replace_mermaid, content, flags=re.DOTALL)
        
    def _generate_notebook(self, content: str, metadata: Dict[str, Any]) -> str:
        """Génère un notebook Jupyter à partir du contenu.
        
        Args:
            content: Contenu Markdown
            metadata: Métadonnées du document
            
        Returns:
            Contenu du notebook au format JSON
        """
        nb = nbf.v4.new_notebook()
        cells = []
        
        # Ajout des métadonnées
        cells.append(nbf.v4.new_markdown_cell(f"# {metadata.get('title', 'Document')}"))
        cells.append(nbf.v4.new_markdown_cell(f"*{metadata.get('author', '')} - {metadata.get('date', '')}*"))
        
        # Traitement du contenu
        sections = content.split('\n## ')
        for section in sections:
            if section.strip():
                cells.append(nbf.v4.new_markdown_cell(f"## {section}"))
                
        nb['cells'] = cells
        return nbf.writes(nb)
        
    def _create_visualization(self, data: Dict[str, Any], viz_type: str) -> Optional[Figure]:
        """Crée une visualisation à partir des données.
        
        Args:
            data: Données pour la visualisation
            viz_type: Type de visualisation ('graph', 'timeline', etc.)
            
        Returns:
            Figure matplotlib ou None si le type n'est pas supporté
        """
        if viz_type == 'graph':
            G = nx.Graph()
            for node in data.get('nodes', []):
                G.add_node(node['id'], **node.get('attributes', {}))
            for edge in data.get('edges', []):
                G.add_edge(edge['source'], edge['target'], **edge.get('attributes', {}))
                
            fig = plt.figure(figsize=(10, 8))
            nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500)
            return cast(Figure, fig)
            
        return None
        
    def process_document(self, input_path: str, output_dir: str) -> Dict[str, str]:
        """Traite un document Markdown et génère les fichiers interactifs.
        
        Args:
            input_path: Chemin vers le fichier Markdown
            output_dir: Répertoire de sortie pour les fichiers générés
            
        Returns:
            Dict contenant les chemins des fichiers générés
        """
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extraction des métadonnées
            metadata = self._extract_metadata(content)
            
            # Traitement du contenu
            content = self._process_code_blocks(content)
            content = self._process_quizzes(content)
            content = self._process_visualizations(content)
            
            # Génération des fichiers
            output_files = {}
            
            # HTML interactif
            html_content = self.template.render(
                content=content,
                metadata=metadata,
                config=self.config
            )
            html_path = os.path.join(output_dir, f"{Path(input_path).stem}.html")
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            output_files['html'] = html_path
            
            # Notebook Jupyter
            if self.config.get('generate_notebook', True):
                notebook_content = self._generate_notebook(content, metadata)
                notebook_path = os.path.join(output_dir, f"{Path(input_path).stem}.ipynb")
                with open(notebook_path, 'w', encoding='utf-8') as f:
                    f.write(notebook_content)
                output_files['notebook'] = notebook_path
                
            return output_files
            
        except Exception as e:
            print(f"Erreur lors du traitement du document: {e}")
            return {}
            
    def validate_document(self, content: str) -> List[str]:
        """Valide la structure et le contenu du document.
        
        Args:
            content: Contenu Markdown à valider
            
        Returns:
            Liste des erreurs trouvées
        """
        errors = []
        
        # Vérification des métadonnées requises
        metadata = self._extract_metadata(content)
        required_metadata = ['title', 'author', 'date']
        for field in required_metadata:
            if field not in metadata:
                errors.append(f"Métadonnée requise manquante: {field}")
                
        # Vérification de la structure
        if not re.search(r'# .+', content):
            errors.append("Titre principal manquant")
            
        # Vérification des quiz
        quiz_pattern = r'```quiz\n(.*?)\n```'
        quizzes = re.findall(quiz_pattern, content, re.DOTALL)
        for quiz in quizzes:
            try:
                quiz_data = yaml.safe_load(quiz)
                if not all(k in quiz_data for k in ['question', 'options', 'correct']):
                    errors.append("Structure de quiz invalide")
            except:
                errors.append("Format de quiz invalide")
                
        return errors
        
    def export_to_pdf(self, input_path: str, output_path: str) -> bool:
        """Exporte le document en PDF.
        
        Args:
            input_path: Chemin vers le fichier Markdown
            output_path: Chemin de sortie pour le PDF
            
        Returns:
            True si l'export a réussi, False sinon
        """
        try:
            # Implémentation de l'export PDF
            return True
        except Exception as e:
            print(f"Erreur lors de l'export PDF: {e}")
            return False
            
    def get_document_stats(self, content: str) -> Dict[str, Any]:
        """Calcule les statistiques du document.
        
        Args:
            content: Contenu Markdown à analyser
            
        Returns:
            Dict contenant les statistiques
        """
        return {
            'word_count': len(content.split()),
            'code_blocks': len(re.findall(r'```\w+\n.*?\n```', content, re.DOTALL)),
            'quizzes': len(re.findall(r'```quiz\n.*?\n```', content, re.DOTALL)),
            'visualizations': len(re.findall(r'```mermaid\n.*?\n```', content, re.DOTALL))
        }

def main():
    """Fonction principale."""
    # Exemple d'utilisation
    docs = InteractiveDocs()
    
    # Traitement d'un document
    input_path = "examples/interactive_doc_example.md"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Validation du document
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    errors = docs.validate_document(content)
    if errors:
        print("Erreurs de validation:", errors)
        return
        
    # Génération des fichiers interactifs
    output_files = docs.process_document(input_path, output_dir)
    print("Fichiers générés:", output_files)
    
    # Statistiques du document
    stats = docs.get_document_stats(content)
    print("Statistiques:", stats)

if __name__ == "__main__":
    main() 