# Yandex - Moteur de Recherche Russe pour OSINT

## 🎯 Présentation
Yandex est le principal moteur de recherche russe, particulièrement efficace pour :
- Reconnaissance faciale avancée
- Recherche d'images inversée
- Contenu en cyrillique
- Géolocalisation précise

## 🔍 Fonctionnalités Clés

### Recherche d'Images
- **Reconnaissance faciale** : Plus précise que Google Images
- **Recherche inversée** : Upload d'image pour trouver des sources
- **Détection d'objets** : Identification automatique d'éléments
- **Images similaires** : Variations et versions alternatives

### Yandex Maps
- **Street View russe** : Panoramiques détaillés
- **Géolocalisation** : Identification de lieux spécifiques
- **Trafic temps réel** : Données de circulation
- **Photos utilisateurs** : Contenu géolocalisé

## 🛠️ Techniques OSINT

### Reconnaissance Faciale
1. Accéder à [yandex.com/images](https://yandex.com/images)
2. Cliquer sur l'icône appareil photo
3. Upload de l'image cible
4. Analyser les résultats pour profils sociaux

### Recherche Géographique
```
site:yandex.ru [location]
[landmark] site:maps.yandex.ru
"[address]" filetype:kml
```

### Opérateurs Spéciaux
```
host:example.com          # Recherche sur un domaine
lang:ru                   # Contenu en russe
date:                     # Filtrage par date
rhost:                    # Recherche par serveur
```

## 🎯 Cas d'Usage OSINT

### Investigation de Profils
1. **Upload photo de profil** → Recherche autres comptes
2. **Analyse de métadonnées** → Localisation possible
3. **Recherche croisée** → Vérification d'identité

### Géolocalisation
1. **Photo de lieu** → Identification géographique
2. **Street View** → Confirmation visuelle
3. **Données historiques** → Évolution temporelle

### Surveillance Médias
1. **Monitoring de marque** en russe
2. **Veille concurrentielle** marchés slaves
3. **Analyse de sentiment** populations russophones

## 💡 Conseils Avancés

### Optimisation des Résultats
- Utiliser des mots-clés en cyrillique
- Combiner avec d'autres moteurs
- Vérifier les métadonnées d'images
- Explorer les suggestions automatiques

### Contournement de Restrictions
- VPN vers la Russie pour résultats locaux
- Interface en russe pour plus d'options
- Recherche sur versions mobiles

## ⚠️ Limitations

- **Biais géographique** : Favorise le contenu russe/slave
- **Barrière linguistique** : Interface principalement en russe
- **Restrictions légales** : Certains contenus filtrés
- **Protection données** : Réglementations locales

## 🔗 Ressources

- [Yandex Images](https://yandex.com/images/)
- [Yandex Maps](https://yandex.com/maps/)
- [Guide Yandex OSINT](https://osintcurio.us/2019/01/15/search-yandex/)
- [Techniques Avancées](https://www.bellingcat.com/resources/how-tos/2019/12/26/guide-to-using-reverse-image-search-for-investigations/)

---

*Yandex excelle pour la reconnaissance faciale et la géolocalisation dans l'espace post-soviétique*