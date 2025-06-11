#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import yaml
import json
from pathlib import Path
from typing import Dict, List, Tuple
import requests
from bs4 import BeautifulSoup
import markdown
from markdown.extensions import fenced_code, tables

class ContentValidator:
    def __init__(self, config_path: str = "config/validation_config.yaml"):
        """Initialise le validateur de contenu."""
        self.config = self._load_config(config_path)
        self.results = {
            "valid": [],
            "invalid": [],
            "warnings": []
        }

    def _load_config(self, config_path: str) -> Dict:
        """Charge la configuration."""
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def validate_markdown(self, file_path: str) -> Dict:
        """Valide un fichier Markdown."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Vérification des métadonnées YAML
            metadata = self._extract_metadata(content)
            if not metadata:
                self.results["warnings"].append(f"{file_path}: Pas de métadonnées YAML")

            # Vérification de la structure
            if not self._check_structure(content):
                self.results["invalid"].append(f"{file_path}: Structure invalide")

            # Vérification des liens
            links = self._extract_links(content)
            for link in links:
                if not self._validate_link(link):
                    self.results["warnings"].append(f"{file_path}: Lien invalide - {link}")

            # Vérification des images
            images = self._extract_images(content)
            for image in images:
                if not self._validate_image(image):
                    self.results["warnings"].append(f"{file_path}: Image manquante - {image}")

            # Vérification du formatage
            if not self._check_formatting(content):
                self.results["warnings"].append(f"{file_path}: Problèmes de formatage")

            return {
                "file": file_path,
                "metadata": metadata,
                "links": links,
                "images": images,
                "status": "valid" if not self.results["invalid"] else "invalid"
            }

        except Exception as e:
            self.results["invalid"].append(f"{file_path}: Erreur - {str(e)}")
            return {"file": file_path, "status": "error", "error": str(e)}

    def _extract_metadata(self, content: str) -> Dict:
        """Extrait les métadonnées YAML."""
        metadata = {}
        if content.startswith('---'):
            try:
                end = content.find('---', 3)
                if end != -1:
                    yaml_content = content[3:end]
                    metadata = yaml.safe_load(yaml_content)
            except Exception as e:
                print(f"Erreur lors de l'extraction des métadonnées: {e}")
        return metadata

    def _check_structure(self, content: str) -> bool:
        """Vérifie la structure du document."""
        # Vérification des titres
        if not re.search(r'^#\s+.+$', content, re.MULTILINE):
            return False

        # Vérification des sections
        if not re.search(r'^##\s+.+$', content, re.MULTILINE):
            return False

        return True

    def _extract_links(self, content: str) -> List[str]:
        """Extrait les liens du document."""
        links = []
        # Liens Markdown
        links.extend(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content))
        # URLs brutes
        links.extend(re.findall(r'https?://\S+', content))
        return [link[1] if isinstance(link, tuple) else link for link in links]

    def _validate_link(self, link: str) -> bool:
        """Valide un lien."""
        if link.startswith('http'):
            try:
                response = requests.head(link, timeout=5)
                return response.status_code == 200
            except:
                return False
        else:
            return os.path.exists(link)

    def _extract_images(self, content: str) -> List[str]:
        """Extrait les images du document."""
        return re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)

    def _validate_image(self, image: str) -> bool:
        """Valide une image."""
        return os.path.exists(image[1])

    def _check_formatting(self, content: str) -> bool:
        """Vérifie le formatage du document."""
        # Vérification des listes
        if not re.search(r'^\s*[-*+]\s+.+$', content, re.MULTILINE):
            return False

        # Vérification du code
        if not re.search(r'```[\s\S]+?```', content):
            return False

        return True

    def generate_report(self) -> str:
        """Génère un rapport de validation."""
        report = "# Rapport de Validation\n\n"
        
        if self.results["invalid"]:
            report += "## ❌ Erreurs\n"
            for error in self.results["invalid"]:
                report += f"- {error}\n"
        
        if self.results["warnings"]:
            report += "\n## ⚠️ Avertissements\n"
            for warning in self.results["warnings"]:
                report += f"- {warning}\n"
        
        if self.results["valid"]:
            report += "\n## ✅ Documents Valides\n"
            for valid in self.results["valid"]:
                report += f"- {valid}\n"
        
        return report

def main():
    """Fonction principale."""
    validator = ContentValidator()
    
    # Validation de tous les fichiers Markdown
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                validator.validate_markdown(file_path)
    
    # Génération du rapport
    report = validator.generate_report()
    with open('validation_report.md', 'w', encoding='utf-8') as f:
        f.write(report)

if __name__ == "__main__":
    main() 