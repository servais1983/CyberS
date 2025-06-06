# 🛡️ DeTT&CT — Évaluer et Renforcer votre Couverture de Détection avec MITRE ATT&CK

🔗 **GitHub** : [github.com/rabobank-cdc/DeTTECT](https://github.com/rabobank-cdc/DeTTECT)

> _"Detect Tactics, Techniques & Combat Threats"_

---

## 🧠 Qu'est-ce que DeTT&CT ?

**DeTT&CT** est un outil open-source développé par le Cyber Defence Center de Rabobank. Il permet aux équipes de sécurité (Blue Teams) de :

- 📊 **Cartographier** la couverture de détection selon le framework MITRE ATT&CK.
- 🧩 **Évaluer** la qualité des sources de données et la visibilité sur les techniques d'attaque.
- 🔍 **Identifier** les lacunes dans la détection et prioriser les améliorations.

---

## ⚙️ Composants Principaux

- **CLI Python (`dettect.py`)** : Outil en ligne de commande pour gérer les fichiers d'administration et générer des visualisations.
- **Fichiers YAML** : Définissent les sources de données, la visibilité, les techniques et les groupes d'acteurs.
- **DeTT&CT Editor** : Interface web pour créer et modifier les fichiers YAML.
- **Tables de notation** : Évaluent la qualité des données, la visibilité et la détection.:contentReference[oaicite:12]{index=12}

---

## 🔍 Fonctionnalités Clés

- **Évaluation des Sources de Données** : :contentReference[oaicite:14]{index=14}
- **Cartographie de la Visibilité** : :contentReference[oaicite:17]{index=17}
- **Évaluation de la Détection** : :contentReference[oaicite:20]{index=20}
- **Analyse des Lacunes** : :contentReference[oaicite:23]{index=23}
- **Intégration avec ATT&CK Navigator** : :contentReference[oaicite:26]{index=26}:contentReference[oaicite:28]{index=28}

---

## 🛠️ Modes d'Utilisation

- `editor` : :contentReference[oaicite:30]{index=30}
- `ds` : :contentReference[oaicite:33]{index=33}
- `v` : :contentReference[oaicite:36]{index=36}
- `d` : :contentReference[oaicite:39]{index=39}
- `g` : :contentReference[oaicite:42]{index=42}
- `generic` : :contentReference[oaicite:45]{index=45}:contentReference[oaicite:47]{index=47}

---

## 🚀 Exemple d'Utilisation

1. **Installation** :

   ```bash
   git clone https://github.com/rabobank-cdc/DeTTECT.git
   cd DeTTECT
   pip install -r requirements.txt
