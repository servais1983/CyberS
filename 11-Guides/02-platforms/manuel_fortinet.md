<div align="center">
<img src="fortinet_logo.png" alt="Logo Fortinet" width="300"/>
</div>

<h1 style="color:#E23237; text-align:center;">Guide complet Fortinet</h1>

<h2 style="color:#0D274D; text-align:center;">Pour professionnels IT, administrateurs réseau et experts en cybersécurité</h2>

<div style="text-align:center;">
<p>Par <strong>Lejeune Geoffrey</strong></p>
<p>Consultant en Cybersécurité</p>
<p>Mai 2025</p>
</div>

---

<h1 id="sommaire" style="color:#E23237;">Sommaire</h1>

*   [1. Introduction à Fortinet & FortiGate](#introduction)
    *   [1.1 Présentation de Fortinet](#presentation)
    *   [1.2 Architecture FortiOS](#architecture)
    *   [1.3 Gamme de produits FortiGate](#gamme)
    *   [1.4 Cas d'usage typiques](#cas-usage)
*   [2. Installation et configuration initiale](#installation)
    *   [2.1 Démarrage depuis un FortiGate neuf](#demarrage)
    *   [2.2 Connexion via GUI (web)](#connexion-gui)
    *   [2.3 Connexion via CLI (console/SSH)](#connexion-cli)
    *   [2.4 Configuration des interfaces réseau](#config-interfaces)
    *   [2.5 Accès administrateur sécurisé](#admin-securise)
*   [3. Réseau & Routage](#reseau)
    *   [3.1 Types d'interfaces et configuration](#interfaces)
    *   [3.2 Création de VLANs et zones](#vlans)
    *   [3.3 Agrégation de liens](#agregation)
    *   [3.4 Routage statique](#routage-statique)
    *   [3.5 Routage dynamique (OSPF, BGP)](#routage-dynamique)
    *   [3.6 SD-WAN](#sd-wan)
*   [4. Pare-feu et politiques de sécurité](#pare-feu)
    *   [4.1 Concepts fondamentaux du pare-feu FortiGate](#concepts-fondamentaux)
    *   [4.2 Création et gestion des politiques de sécurité](#politiques-securite)
    *   [4.3 Objets d'adresses et groupes](#objets-adresses)
    *   [4.4 Services et applications](#services-applications)
    *   [4.5 Network Address Translation (NAT)](#nat)
    *   [4.6 Inspection SSL/TLS](#inspection-ssl)
    *   [4.7 Règles IPv6 et coexistence IPv4/IPv6](#regles-ipv6)
    *   [4.8 Traffic shaping et QoS](#shaping)
*   [5. VPNs Fortinet](#vpn)
    *   [5.1 Concepts fondamentaux des VPNs](#vpn-concepts)
    *   [5.2 IPsec VPN Site-to-Site](#ipsec-vpn)
    *   [5.3 IPsec VPN Dial-up (accès distant)](#ipsec-dialup)
    *   [5.4 SSL VPN (tunnel et web mode)](#ssl-vpn)
    *   [5.5 Configurations VPN avancées](#vpn-avances)
    *   [5.6 Dépannage des VPNs](#vpn-troubleshooting)
*   [6. Fonctionnalités UTM (Unified Threat Management)](#utm)
    *   [6.1 Vue d'ensemble des fonctionnalités UTM](#utm-overview)
    *   [6.2 Antivirus](#antivirus)
    *   [6.3 Filtrage Web](#web-filter)
    *   [6.4 Filtrage DNS](#dns-filter)
    *   [6.5 Contrôle d'application](#app-control)
    *   [6.6 Système de prévention d'intrusion (IPS)](#ips)
    *   [6.7 Filtrage de fichiers](#file-filter)
    *   [6.8 Filtrage d'emails](#email-filter)
    *   [6.9 Prévention de fuite de données (DLP)](#dlp)
    *   [6.10 Bonnes pratiques UTM](#utm-best-practices)
*   [7. Haute Disponibilité (HA)](#ha)
    *   [7.1 Concepts fondamentaux de la haute disponibilité](#ha-concepts)
    *   [7.2 Configuration d'un cluster Actif-Passif](#ha-actif-passif)
    *   [7.3 Configuration d'un cluster Actif-Actif](#ha-actif-actif)
    *   [7.4 Paramètres avancés de haute disponibilité](#ha-parametres)
    *   [7.5 Tests de basculement et scénarios de défaillance](#ha-basculement)
    *   [7.6 Dépannage de la haute disponibilité](#ha-troubleshooting)
    *   [7.7 Bonnes pratiques pour la haute disponibilité](#ha-best-practices)
*   [8. Monitoring & Logs](#monitoring)
    *   [8.1 Vue d'ensemble du monitoring FortiGate](#monitoring-overview)
    *   [8.2 Tableaux de bord et widgets](#tableaux-bord)
    *   [8.3 Configuration de la journalisation](#logs-config)
    *   [8.4 FortiAnalyzer et solutions de gestion centralisée](#fortianalyzer)
    *   [8.5 Analyse des logs et dépannage](#logs-analyse)
    *   [8.6 Création de rapports personnalisés](#rapports)
    *   [8.7 Configuration des alertes et notifications](#alertes)
    *   [8.8 Monitoring via SNMP](#snmp)
    *   [8.9 Bonnes pratiques de monitoring](#monitoring-best-practices)
*   [9. Commandes CLI FortiGate](#cli)
    *   [9.1 Introduction à l'interface en ligne de commande](#cli-intro)
    *   [9.2 Navigation et commandes de base](#cli-navigation)
    *   [9.3 Configuration via CLI](#cli-config)
    *   [9.4 Commandes de monitoring et diagnostic](#cli-monitoring)
    *   [9.5 Scripts et automatisation](#cli-scripts)
    *   [9.6 Exemples de configurations complètes](#cli-exemples)
    *   [9.7 Bonnes pratiques pour l'utilisation de la CLI](#cli-best-practices)
*   [10. Annexes](#annexes)
    *   [10.1 Tableau des ports et services Fortinet](#ports-services)
    *   [10.2 Glossaire des termes Fortinet](#glossaire)
    *   [10.3 Liens vers documentation officielle](#documentation)
    *   [10.4 Modèles de configurations typiques](#modeles-config)
    *   [10.5 Guide de dépannage rapide](#depannage)

---


<h1 id="introduction" style="color:#E23237;">1. Introduction à Fortinet & FortiGate</h1>

<h2 id="presentation" style="color:#0D274D;">1.1 Présentation de Fortinet</h2>

Fortinet est un leader mondial dans le domaine de la cybersécurité, offrant des solutions de sécurité réseau intégrées et automatisées. Fondée en 2000 par les frères Ken et Michael Xie, l'entreprise s'est rapidement imposée comme un acteur majeur dans le secteur de la sécurité informatique.

Fortinet propose une gamme complète de produits et services de sécurité, dont le fleuron est la série FortiGate, des appliances de sécurité réseau multifonctions. La vision de Fortinet est de fournir une protection intelligente et continue contre un paysage de menaces en constante évolution, tout en simplifiant l'infrastructure de sécurité informatique.

### Histoire et évolution

Depuis sa création, Fortinet a connu une croissance remarquable, passant d'une start-up spécialisée dans les solutions de sécurité réseau à une entreprise mondiale cotée en bourse. Voici quelques étapes clés de son évolution :

* **2000** : Fondation de Fortinet par Ken et Michael Xie
* **2002** : Lancement de la première appliance FortiGate
* **2004** : Introduction des services FortiGuard
* **2009** : Introduction de l'architecture ASIC personnalisée
* **2009** : Entrée en bourse (NASDAQ: FTNT)
* **2016** : Lancement de la Security Fabric
* **2018** : Expansion majeure dans le SD-WAN
* **2020** : Développement des solutions SASE (Secure Access Service Edge)

### Position sur le marché

Aujourd'hui, Fortinet est reconnu comme l'un des leaders du marché de la cybersécurité, régulièrement positionné dans le quadrant des leaders du Magic Quadrant de Gartner pour les pare-feu réseau d'entreprise. L'entreprise se distingue par :

* Sa capacité à intégrer de multiples fonctions de sécurité dans une seule plateforme
* Ses performances élevées grâce à des processeurs de sécurité dédiés (ASIC)
* Son approche de sécurité unifiée via la Security Fabric
* Son rapport qualité-prix compétitif

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 FortiGuard Labs</h4>
<p>FortiGuard Labs est l'équipe de recherche en sécurité de Fortinet, composée d'experts qui surveillent en permanence le paysage des menaces et développent des protections contre les nouvelles vulnérabilités. Cette équipe alimente les services de sécurité par abonnement qui enrichissent les produits Fortinet.</p>
</div>

<h2 id="architecture" style="color:#0D274D;">1.2 Architecture FortiOS</h2>

FortiOS est le système d'exploitation propriétaire qui alimente les appliances FortiGate. Il constitue le cœur de l'écosystème Fortinet et intègre de nombreuses fonctionnalités de sécurité dans une interface unifiée.

### Caractéristiques principales de FortiOS

FortiOS se distingue par plusieurs caractéristiques clés :

* **Architecture modulaire** : Permet d'activer uniquement les fonctionnalités nécessaires
* **Interface unifiée** : Administration centralisée de toutes les fonctions de sécurité
* **Performances optimisées** : Conçu pour tirer parti des processeurs de sécurité dédiés
* **Mises à jour régulières** : Cycle de développement continu pour intégrer les nouvelles fonctionnalités et protections
* **Flexibilité de déploiement** : Fonctionne sur des appliances physiques, des machines virtuelles ou dans le cloud

### Composants de l'architecture

L'architecture FortiOS s'articule autour de plusieurs composants clés :

#### 1. Noyau et services de base

Le noyau de FortiOS est basé sur Linux, mais fortement personnalisé et optimisé pour les fonctions de sécurité. Il gère :

* Le routage et la commutation
* La gestion des sessions
* L'authentification et l'autorisation
* La journalisation et le reporting

#### 2. Moteurs de traitement

FortiOS utilise différents moteurs spécialisés pour traiter efficacement le trafic :

* **Moteur de pare-feu** : Filtrage du trafic basé sur les politiques
* **Moteur d'inspection de contenu** : Analyse approfondie des paquets
* **Moteur d'inspection SSL/TLS** : Déchiffrement et inspection du trafic chiffré
* **Moteur de prévention d'intrusion** : Détection et blocage des attaques
* **Moteur antivirus** : Détection et élimination des malwares

#### 3. Accélération matérielle

Une caractéristique distinctive de l'architecture FortiOS est son intégration étroite avec le matériel spécialisé :

* **FortiASIC** : Processeurs dédiés pour l'accélération des fonctions de sécurité
* **CP (Content Processor)** : Accélération du chiffrement et du VPN
* **NP (Network Processor)** : Accélération du traitement des paquets réseau
* **SPU (Security Processing Unit)** : Nouvelle génération de processeurs combinant les fonctions CP et NP

![Architecture FortiOS](fortinet_sdwan_architecture.png)
*Figure 1.1 : Architecture simplifiée de FortiOS avec ses différents composants*

#### 4. Security Fabric

La Security Fabric est l'architecture de sécurité intégrée de Fortinet qui permet la communication et la coordination entre les différents produits Fortinet et des solutions tierces compatibles. Elle offre :

* Une visibilité unifiée sur l'ensemble du réseau
* Un contrôle centralisé des politiques de sécurité
* Une détection et une réponse automatisées aux menaces
* Une intégration avec l'écosystème de sécurité plus large

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Versions de FortiOS</h4>
<p>Fortinet publie régulièrement de nouvelles versions de FortiOS. Pour les environnements de production, il est recommandé d'utiliser des versions stables et éprouvées plutôt que les toutes dernières versions. Consultez toujours les notes de version et testez dans un environnement de laboratoire avant de mettre à niveau vos appareils de production.</p>
</div>

<h2 id="gamme" style="color:#0D274D;">1.3 Gamme de produits FortiGate</h2>

La gamme FortiGate comprend une large variété d'appliances de sécurité réseau, allant des petits appareils pour les succursales ou les PME jusqu'aux systèmes haute performance pour les grands centres de données et les fournisseurs de services.

### Classification des modèles

Les appliances FortiGate sont généralement classées en plusieurs catégories :

#### Série E - Entry Level (Niveau d'entrée)

Destinée aux petites entreprises, aux bureaux à domicile et aux déploiements de petite taille :

* **FortiGate 40F/60F/80F** : Pour les très petites entreprises et les bureaux à domicile
* **FortiGate 100E/100F** : Pour les petites entreprises et les succursales
* Débit : de 1 Gbps à 10 Gbps
* Nombre de ports : généralement 4 à 14 ports

#### Série M - Mid-Range (Milieu de gamme)

Adaptée aux entreprises de taille moyenne et aux succursales importantes :

* **FortiGate 200E/200F** : Pour les entreprises de taille moyenne
* **FortiGate 300E/400E** : Pour les grandes succursales
* **FortiGate 500E/600E** : Pour les sièges de taille moyenne
* Débit : de 10 Gbps à 40 Gbps
* Nombre de ports : généralement 8 à 20 ports, avec options pour modules d'extension

#### Série H - High-End (Haut de gamme)

Conçue pour les grandes entreprises, les centres de données et les fournisseurs de services :

* **FortiGate 1000/2000 Series** : Pour les grandes entreprises
* **FortiGate 3000/4000 Series** : Pour les centres de données
* **FortiGate 5000/6000/7000 Series** : Pour les très grands centres de données et les fournisseurs de services
* Débit : de 40 Gbps à plusieurs Tbps
* Architecture modulaire avec châssis et lames
* Redondance intégrée pour haute disponibilité

#### Série V - Virtual (Virtuelle)

Versions virtuelles des appliances FortiGate pour les environnements virtualisés et cloud :

* **FortiGate-VM** : Disponible pour VMware, Hyper-V, KVM, Xen, etc.
* **FortiGate-VM pour cloud public** : AWS, Azure, Google Cloud, Oracle Cloud, etc.
* Différentes tailles de licences basées sur le nombre de vCPU
* Fonctionnalités identiques aux appliances physiques

### Nomenclature des modèles

La nomenclature des modèles FortiGate suit généralement ce format :

```
FortiGate-[Numéro de modèle][Lettre de série]
```

Par exemple :

* **FortiGate-60F** : Modèle 60 de la série F (entrée de gamme)
* **FortiGate-200E** : Modèle 200 de la série E (milieu de gamme)
* **FortiGate-3400E** : Modèle 3400 de la série E (haut de gamme)

Les lettres de série (D, E, F, etc.) indiquent la génération du matériel, F étant plus récent que E.

### Facteurs de choix d'un modèle

Plusieurs facteurs doivent être pris en compte lors du choix d'un modèle FortiGate :

* **Débit requis** : Trafic total, débit de pare-feu, débit VPN, débit UTM
* **Nombre de sessions simultanées** : Capacité à gérer les connexions concurrentes
* **Fonctionnalités nécessaires** : Pare-feu, VPN, SD-WAN, UTM, etc.
* **Nombre d'utilisateurs/appareils** : Échelle du déploiement
* **Interfaces réseau requises** : Types et nombre de ports
* **Besoins de stockage** : Pour la journalisation locale
* **Contraintes physiques** : Espace rack, alimentation, refroidissement

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>🔍 Dimensionnement</h4>
<p>Lors du dimensionnement d'un FortiGate, tenez compte non seulement des besoins actuels mais aussi de la croissance future. Il est recommandé de choisir un modèle offrant au moins 50% de capacité supplémentaire par rapport aux besoins actuels pour anticiper la croissance du trafic et l'activation de fonctionnalités supplémentaires.</p>
</div>

<h2 id="cas-usage" style="color:#0D274D;">1.4 Cas d'usage typiques</h2>

Les appliances FortiGate sont polyvalentes et peuvent être déployées dans divers scénarios. Voici les cas d'usage les plus courants :

### Pare-feu de nouvelle génération (NGFW)

Le cas d'usage le plus fondamental est celui du pare-feu de nouvelle génération, qui combine :

* Filtrage du trafic basé sur les politiques
* Inspection approfondie des paquets
* Contrôle des applications
* Prévention des intrusions
* Filtrage des URL
* Inspection du trafic chiffré (SSL/TLS)

Ce déploiement est typique pour sécuriser le périmètre réseau d'une entreprise, filtrant le trafic entre les réseaux internes et externes.

### Unified Threat Management (UTM)

Dans ce scénario, FortiGate est utilisé comme une solution de sécurité tout-en-un, intégrant :

* Toutes les fonctionnalités NGFW
* Antivirus et anti-malware
* Anti-spam
* Filtrage de contenu web
* Prévention de fuite de données (DLP)
* Sandboxing (avec FortiSandbox)

Ce déploiement est particulièrement adapté aux PME qui recherchent une solution de sécurité complète et intégrée.

### Connectivité VPN sécurisée

FortiGate offre des capacités VPN robustes pour différents scénarios :

* **VPN site-à-site** : Connexion sécurisée entre différents sites d'entreprise
* **VPN d'accès distant** : Connexion sécurisée pour les utilisateurs mobiles
* **SSL VPN** : Accès web sécurisé aux ressources internes
* **ADVPN (Auto-Discovery VPN)** : Création dynamique de tunnels VPN entre sites

Ces déploiements sont essentiels pour les entreprises distribuées et les organisations avec une main-d'œuvre mobile.

### SD-WAN (Software-Defined Wide Area Network)

FortiGate peut servir de solution SD-WAN complète, offrant :

* Agrégation de plusieurs connexions WAN
* Sélection de chemin intelligent basée sur la qualité
* Équilibrage de charge et basculement automatique
* Optimisation des applications
* Sécurité intégrée

Ce déploiement est idéal pour les entreprises cherchant à optimiser leurs connexions WAN tout en maintenant un niveau élevé de sécurité.

### Segmentation interne du réseau

FortiGate peut être utilisé pour segmenter les réseaux internes :

* Création de zones de sécurité distinctes
* Micro-segmentation pour isoler les systèmes critiques
* Contrôle du trafic est-ouest (entre segments internes)
* Application de politiques de sécurité granulaires

Ce déploiement est particulièrement pertinent pour les organisations ayant des exigences de conformité strictes ou souhaitant limiter la propagation latérale des menaces.

### Sécurité cloud et multi-cloud

Les FortiGate virtuels peuvent être déployés dans divers environnements cloud :

* Protection des charges de travail cloud
* Sécurisation des connexions entre environnements cloud et on-premise
* Application cohérente des politiques de sécurité dans les environnements hybrides
* Inspection du trafic nord-sud et est-ouest dans le cloud

Ce déploiement est essentiel pour les organisations adoptant des stratégies cloud ou multi-cloud.

### Sécurité des succursales

FortiGate peut servir de solution de sécurité tout-en-un pour les succursales :

* Connectivité sécurisée au siège social
* Sécurité Internet locale
* Optimisation WAN
* Contrôle d'accès Wi-Fi (avec FortiAP)
* Commutation locale (avec FortiSwitch)

Ce déploiement simplifie l'infrastructure IT des succursales tout en maintenant un niveau élevé de sécurité.

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Approche Security Fabric</h4>
<p>Pour maximiser l'efficacité de FortiGate, envisagez de l'intégrer dans une approche Security Fabric plus large, en combinant d'autres produits Fortinet comme FortiAnalyzer pour la journalisation et l'analyse, FortiManager pour la gestion centralisée, FortiClient pour la sécurité des endpoints, et FortiSandbox pour l'analyse avancée des menaces.</p>
</div>

---

<h1 id="installation" style="color:#E23237;">2. Installation et configuration initiale</h1>

<h2 id="demarrage" style="color:#0D274D;">2.1 Démarrage depuis un FortiGate neuf</h2>

La mise en service d'un appareil FortiGate neuf est une étape cruciale qui détermine la base de votre infrastructure de sécurité. Cette section vous guide à travers le processus de démarrage initial d'un FortiGate.

### Déballage et vérification physique

Avant de commencer l'installation, il est important de vérifier l'état physique de l'appareil :

1. Déballez soigneusement l'appareil FortiGate et vérifiez qu'il n'y a pas de dommages visibles
2. Vérifiez que tous les composants sont présents :
   * Appliance FortiGate
   * Câble(s) d'alimentation
   * Câble console (généralement RJ45 vers DB9 ou USB)
   * Guide de démarrage rapide
   * Informations de licence et d'enregistrement
3. Notez le numéro de série de l'appareil (généralement situé à l'arrière ou sous l'appareil)

### Installation physique

L'installation physique dépend du modèle de FortiGate et de votre environnement :

1. Pour les modèles de bureau :
   * Placez l'appareil sur une surface stable et plane
   * Assurez une ventilation adéquate (au moins 10 cm d'espace libre autour de l'appareil)
2. Pour les modèles montables en rack :
   * Installez les supports de montage fournis
   * Montez l'appareil dans le rack à l'aide des vis appropriées
   * Assurez une ventilation adéquate et respectez les recommandations de flux d'air

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Précautions électriques</h4>
<p>Assurez-vous que l'alimentation électrique correspond aux spécifications de l'appareil. Les FortiGate peuvent avoir des alimentations redondantes ou des exigences de tension spécifiques selon les modèles. Une alimentation inappropriée peut endommager l'appareil.</p>
</div>

### Connexions initiales

Pour démarrer la configuration, vous devez établir les connexions de base :

1. Connectez le câble d'alimentation à l'appareil et à une source d'alimentation appropriée
2. Connectez un câble Ethernet entre le port de gestion (généralement étiqueté MGMT ou port1) et votre ordinateur ou un commutateur réseau
3. Optionnellement, connectez le câble console entre le port console du FortiGate et le port série ou USB de votre ordinateur

### Premier démarrage

Lors du premier démarrage d'un FortiGate neuf :

1. Allumez l'appareil en appuyant sur le bouton d'alimentation (si présent) ou simplement en branchant l'alimentation
2. Observez les voyants LED sur le panneau avant :
   * Le voyant d'alimentation doit s'allumer en vert
   * Les voyants d'activité réseau peuvent clignoter
   * Le voyant d'état peut passer par différentes couleurs pendant le démarrage
3. Le démarrage complet peut prendre plusieurs minutes, surtout pour les modèles plus grands

### Configuration par défaut

Un FortiGate neuf est livré avec une configuration par défaut qui comprend généralement :

* Adresse IP par défaut sur l'interface de gestion : 192.168.1.99/24
* Nom d'utilisateur administrateur par défaut : admin
* Mot de passe par défaut : (vide) ou le numéro de série de l'appareil selon le modèle et la version
* DHCP activé sur l'interface interne (généralement port1)
* Accès administratif HTTPS et SSH activé sur l'interface interne
* Une politique de pare-feu de base permettant le trafic sortant

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Versions récentes de FortiOS</h4>
<p>Dans les versions récentes de FortiOS (6.4 et ultérieures), le FortiGate peut démarrer en mode "installation guidée" lors de la première connexion, ce qui simplifie la configuration initiale à travers une série d'étapes guidées.</p>
</div>

### Enregistrement du produit

Il est important d'enregistrer votre FortiGate auprès de Fortinet pour activer les services et garantir le support :

1. Créez un compte sur le [portail de support Fortinet](https://support.fortinet.com) si vous n'en avez pas déjà un
2. Enregistrez votre appareil en utilisant le numéro de série
3. Activez les licences et abonnements achetés
4. Téléchargez la dernière version stable de FortiOS recommandée pour votre modèle

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Mise à jour du firmware</h4>
<p>Il est recommandé de mettre à jour le firmware de votre FortiGate vers la dernière version stable avant de commencer la configuration de production. Cela garantit que vous disposez des dernières fonctionnalités et correctifs de sécurité. Cependant, vérifiez toujours la compatibilité avec vos autres produits Fortinet si vous utilisez la Security Fabric.</p>
</div>

<h2 id="connexion-gui" style="color:#0D274D;">2.2 Connexion via GUI (web)</h2>

L'interface graphique web (GUI) est le moyen le plus courant et le plus convivial pour configurer et gérer un FortiGate. Cette section explique comment accéder à l'interface web et présente ses principales caractéristiques.

### Prérequis pour la connexion

Avant de vous connecter à l'interface web, assurez-vous que :

* Votre ordinateur est connecté au réseau du FortiGate (directement ou via un commutateur)
* Votre ordinateur est configuré pour obtenir une adresse IP automatiquement (DHCP) ou a une adresse IP statique dans le même sous-réseau que l'interface de gestion du FortiGate
* Vous disposez d'un navigateur web moderne (Chrome, Firefox, Edge ou Safari récent)

### Accès à l'interface web

1. Ouvrez votre navigateur web
2. Entrez l'adresse IP de l'interface de gestion du FortiGate dans la barre d'adresse (par défaut : https://192.168.1.99)
3. Acceptez l'avertissement de sécurité concernant le certificat auto-signé (vous pourrez configurer un certificat valide ultérieurement)
4. Sur la page de connexion, entrez les identifiants par défaut :
   * Nom d'utilisateur : admin
   * Mot de passe : (vide) ou le numéro de série de l'appareil

![Page de connexion FortiGate](fortinet_gui_login.png)
*Figure 2.1 : Page de connexion à l'interface web FortiGate*

### Premier accès et changement de mot de passe

Lors de votre première connexion :

1. Le système vous demandera de changer le mot de passe administrateur par défaut
2. Choisissez un mot de passe fort qui respecte les critères de complexité :
   * Au moins 8 caractères
   * Au moins une lettre majuscule
   * Au moins une lettre minuscule
   * Au moins un chiffre
   * Au moins un caractère spécial
3. Selon la version de FortiOS, vous pourriez être guidé à travers un assistant de configuration initiale

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Sécurité des identifiants</h4>
<p>Ne conservez jamais les identifiants par défaut sur un appareil en production. Changez immédiatement le mot de passe et envisagez de créer un compte administrateur distinct avec un nom d'utilisateur différent pour une sécurité renforcée.</p>
</div>

### Présentation de l'interface web

L'interface web FortiGate est organisée en plusieurs sections principales :

#### 1. Tableau de bord

Le tableau de bord est la page d'accueil par défaut et offre une vue d'ensemble de l'état du système :

* Widgets d'état du système (CPU, mémoire, sessions)
* Informations sur les licences et abonnements
* État des interfaces
* Statistiques de trafic
* Alertes et notifications

Le tableau de bord est personnalisable : vous pouvez ajouter, supprimer et réorganiser les widgets selon vos besoins.

#### 2. Menu principal

Le menu principal, situé sur le côté gauche de l'interface, donne accès à toutes les fonctionnalités du FortiGate :

* **Dashboard** : Tableaux de bord et widgets
* **Network** : Interfaces, routage, SD-WAN
* **Policy & Objects** : Politiques de pare-feu, objets d'adresse, services
* **Security Profiles** : Antivirus, filtrage web, IPS, etc.
* **VPN** : Configuration IPsec et SSL VPN
* **User & Authentication** : Utilisateurs, groupes, authentification
* **WiFi & Switch Controller** : Gestion des points d'accès et commutateurs
* **Log & Report** : Journaux et rapports
* **System** : Paramètres système, administrateurs, certificats

#### 3. Barre d'outils supérieure

La barre d'outils en haut de l'interface contient :

* Bouton de menu pour réduire/étendre le menu principal
* Nom d'hôte du FortiGate
* Bouton de recherche pour trouver rapidement des fonctionnalités
* Notifications et alertes
* Menu utilisateur (déconnexion, préférences)
* Sélecteur de VDOM (si les VDOMs sont activés)

#### 4. Zone de travail principale

La zone centrale de l'interface affiche le contenu de la section sélectionnée :

* Tableaux pour les listes d'éléments (politiques, objets, etc.)
* Formulaires pour la configuration
* Graphiques et statistiques
* Assistants de configuration

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>🔍 Mode d'affichage</h4>
<p>FortiOS propose deux modes d'affichage : le mode NGFW (orienté sécurité) et le mode VDOM (orienté virtualisation). Vous pouvez changer ce mode dans System > Settings. Le mode NGFW est recommandé pour la plupart des déploiements, tandis que le mode VDOM est utile pour les environnements multi-locataires.</p>
</div>

### Personnalisation de l'interface

L'interface web FortiGate offre plusieurs options de personnalisation :

* **Thème** : Vous pouvez choisir entre le thème clair et le thème sombre
* **Disposition du tableau de bord** : Ajout, suppression et réorganisation des widgets
* **Colonnes des tableaux** : Personnalisation des colonnes affichées dans les listes
* **Favoris** : Marquer des pages fréquemment utilisées comme favoris
* **Langue** : Changement de la langue de l'interface

### Bonnes pratiques pour l'utilisation de l'interface web

* Utilisez toujours le bouton "Apply" ou "OK" pour enregistrer vos modifications
* Utilisez la fonction de recherche pour trouver rapidement des paramètres spécifiques
* Consultez les infobulles (en survolant les icônes d'information) pour obtenir des explications sur les options
* Utilisez le mode de prévisualisation des politiques pour tester les règles de pare-feu
* Sauvegardez régulièrement la configuration après des modifications importantes

<h2 id="connexion-cli" style="color:#0D274D;">2.3 Connexion via CLI (console/SSH)</h2>

L'interface en ligne de commande (CLI) offre un contrôle plus précis et plus complet que l'interface web. Elle est essentielle pour certaines configurations avancées et pour le dépannage.

### Méthodes d'accès à la CLI

Il existe plusieurs façons d'accéder à la CLI d'un FortiGate :

#### 1. Connexion via le port console

1. Connectez le câble console (RJ45 vers DB9 ou USB) entre le FortiGate et votre ordinateur
2. Lancez un programme de terminal sur votre ordinateur (PuTTY, TeraTerm, SecureCRT, ou Terminal sur macOS)
3. Configurez les paramètres de connexion série :
   * Vitesse (Baud rate) : 9600
   * Bits de données : 8
   * Parité : Aucune
   * Bits d'arrêt : 1
   * Contrôle de flux : Aucun
4. Appuyez sur Entrée pour afficher l'invite de connexion
5. Entrez vos identifiants (par défaut : admin / pas de mot de passe ou numéro de série)

#### 2. Connexion via SSH

1. Assurez-vous que l'accès SSH est activé sur l'interface à laquelle vous vous connectez
2. Utilisez un client SSH (PuTTY, OpenSSH, etc.) pour vous connecter à l'adresse IP du FortiGate
3. Spécifiez le port 22 (port SSH par défaut)
4. Entrez vos identifiants lorsque vous y êtes invité

```bash
# Exemple de connexion SSH sous Linux/macOS
ssh admin@192.168.1.99
```

#### 3. CLI via l'interface web

1. Connectez-vous à l'interface web du FortiGate
2. Cliquez sur l'icône de terminal dans le coin supérieur droit de l'interface
3. Une fenêtre de CLI s'ouvrira directement dans votre navigateur

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Accès CLI restreint</h4>
<p>L'accès CLI via l'interface web peut avoir des fonctionnalités limitées par rapport à une connexion SSH ou console directe. Certaines commandes avancées ou certains modes de débogage peuvent ne pas être disponibles.</p>
</div>

### Structure de la CLI

La CLI FortiGate est organisée de manière hiérarchique :

* **Mode global** : Le niveau supérieur, accessible après la connexion
* **Branches de configuration** : Sections spécifiques (system, firewall, vpn, etc.)
* **Sous-branches** : Sections plus spécifiques dans chaque branche

### Commandes de base

Voici quelques commandes essentielles pour débuter avec la CLI :

```
# Afficher l'aide
?

# Afficher la configuration actuelle
show

# Entrer dans une branche de configuration
config system interface

# Modifier un élément spécifique
edit port1

# Définir une valeur
set ip 192.168.1.1 255.255.255.0

# Supprimer une valeur
unset allowaccess

# Sortir d'un niveau de configuration
end

# Afficher l'état du système
get system status

# Sauvegarder la configuration
execute backup config
```

### Complétion automatique et raccourcis

La CLI FortiGate offre plusieurs fonctionnalités pour faciliter son utilisation :

* **Tab** : Complète automatiquement les commandes
* **?** : Affiche l'aide contextuelle
* **Flèches haut/bas** : Navigue dans l'historique des commandes
* **Ctrl+A** : Déplace le curseur au début de la ligne
* **Ctrl+E** : Déplace le curseur à la fin de la ligne
* **Ctrl+W** : Supprime le mot avant le curseur
* **Ctrl+U** : Supprime toute la ligne
* **Ctrl+C** : Annule la commande actuelle

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Documentation des commandes</h4>
<p>Lorsque vous utilisez des commandes CLI pour configurer votre FortiGate, documentez-les dans un fichier texte. Cela vous permettra de reproduire facilement la configuration en cas de besoin et servira de référence pour le dépannage ou les futures modifications.</p>
</div>

<h2 id="config-interfaces" style="color:#0D274D;">2.4 Configuration des interfaces réseau</h2>

La configuration des interfaces réseau est l'une des premières étapes essentielles après le démarrage initial d'un FortiGate. Cette section explique comment configurer les différents types d'interfaces et leurs paramètres.

### Types d'interfaces FortiGate

FortiGate prend en charge plusieurs types d'interfaces :

* **Interfaces physiques** : Ports Ethernet physiques sur l'appareil
* **VLAN** : Interfaces virtuelles basées sur le balisage 802.1Q
* **Agrégation de liens** : Regroupement de plusieurs interfaces physiques (LAG/802.3ad)
* **Loopback** : Interfaces virtuelles pour des services internes
* **Tunnel** : Interfaces pour les connexions VPN
* **Zones** : Regroupements logiques d'interfaces
* **Software switch** : Commutateur virtuel regroupant plusieurs interfaces

### Configuration des interfaces physiques

Pour configurer une interface physique via l'interface web :

1. Accédez à **Network > Interfaces**
2. Cliquez sur l'interface que vous souhaitez configurer (par exemple, port1)
3. Configurez les paramètres de base :
   * **Interface Name** : Nom de l'interface (par défaut, portX)
   * **Alias** : Nom descriptif optionnel (par exemple, "WAN" ou "LAN")
   * **Type** : Physical Interface (par défaut pour les ports physiques)
   * **Role** : Rôle de l'interface (WAN, LAN, DMZ, etc.)
   * **Addressing Mode** : Static, DHCP, PPPoE, etc.
   * **IP/Netmask** : Adresse IP et masque de sous-réseau (si mode statique)
   * **Administrative Access** : Services d'administration autorisés (HTTPS, SSH, etc.)
4. Configurez les paramètres avancés si nécessaire :
   * **Status** : Up ou Down
   * **Device Detection** : Détection des appareils connectés
   * **Miscellaneous** : MTU, mode, vitesse, etc.
5. Cliquez sur **OK** pour appliquer les modifications

Pour configurer une interface physique via la CLI :

```
config system interface
    edit "port1"
        set vdom "root"
        set ip 192.168.1.1 255.255.255.0
        set allowaccess ping https ssh
        set type physical
        set alias "LAN"
        set role lan
        set device-identification enable
        set speed auto
        set status up
    next
end
```

### Configuration d'une interface VLAN

Pour créer et configurer une interface VLAN via l'interface web :

1. Accédez à **Network > Interfaces**
2. Cliquez sur **Create New > Interface**
3. Configurez les paramètres VLAN :
   * **Interface Name** : Nom de l'interface VLAN (par exemple, VLAN20)
   * **Type** : VLAN
   * **Interface** : Interface physique parent
   * **VLAN ID** : Identifiant VLAN (1-4094)
   * **Addressing Mode** : Static, DHCP, etc.
   * **IP/Netmask** : Adresse IP et masque de sous-réseau
   * **Administrative Access** : Services d'administration autorisés
4. Cliquez sur **OK** pour créer l'interface VLAN

Pour configurer une interface VLAN via la CLI :

```
config system interface
    edit "VLAN20"
        set vdom "root"
        set ip 10.20.0.1 255.255.255.0
        set allowaccess ping
        set type vlan
        set interface "port2"
        set vlanid 20
    next
end
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>🔍 Nommage des interfaces</h4>
<p>Utilisez des noms descriptifs pour vos interfaces VLAN afin de faciliter leur identification. Par exemple, "VLAN_Finance" ou "VLAN20_Serveurs" est plus explicite que simplement "VLAN20".</p>
</div>

### Configuration du serveur DHCP

Pour configurer un serveur DHCP sur une interface :

1. Accédez à **Network > Interfaces**
2. Modifiez l'interface sur laquelle vous souhaitez activer le serveur DHCP
3. Dans la section **DHCP Server**, activez **Create/Edit**
4. Configurez les paramètres DHCP :
   * **Address Range** : Plage d'adresses IP à attribuer
   * **Netmask** : Masque de sous-réseau
   * **Default Gateway** : Passerelle par défaut (généralement l'IP de l'interface)
   * **DNS Server** : Serveurs DNS
   * **Lease Time** : Durée du bail DHCP
5. Configurez les options avancées si nécessaire (réservations, options DHCP, etc.)
6. Cliquez sur **OK** pour appliquer les modifications

Pour configurer un serveur DHCP via la CLI :

```
config system dhcp server
    edit 1
        set interface "port2"
        set default-gateway 192.168.1.1
        set netmask 255.255.255.0
        set dns-service default
        config ip-range
            edit 1
                set start-ip 192.168.1.100
                set end-ip 192.168.1.199
            next
        end
        set lease-time 86400
    next
end
```

### Zones d'interface

Les zones permettent de regrouper logiquement plusieurs interfaces pour simplifier la configuration des politiques de sécurité :

1. Accédez à **Network > Interfaces**
2. Cliquez sur **Create New > Zone**
3. Configurez les paramètres de la zone :
   * **Name** : Nom de la zone (par exemple, "Internal_Networks")
   * **Block intra-zone traffic** : Bloquer ou autoriser le trafic entre les interfaces de la zone
   * **Interface Members** : Interfaces à inclure dans la zone
4. Cliquez sur **OK** pour créer la zone

Pour configurer une zone via la CLI :

```
config system zone
    edit "Internal_Networks"
        set intrazone allow
        set interface "port2" "port3" "VLAN20"
    next
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Organisation des interfaces</h4>
<p>Organisez vos interfaces selon leur fonction et leur niveau de sécurité. Par exemple, créez des zones distinctes pour WAN, LAN, DMZ, et les réseaux invités. Cela simplifie la gestion des politiques de sécurité et améliore la lisibilité de la configuration.</p>
</div>

<h2 id="admin-securise" style="color:#0D274D;">2.5 Accès administrateur sécurisé</h2>

La sécurisation de l'accès administratif est cruciale pour protéger votre FortiGate contre les accès non autorisés. Cette section présente les meilleures pratiques pour configurer un accès administrateur sécurisé.

### Création de comptes administrateurs

Il est recommandé de créer des comptes administrateurs dédiés plutôt que d'utiliser le compte admin par défaut :

1. Accédez à **System > Administrators**
2. Cliquez sur **Create New > Administrator**
3. Configurez les paramètres du compte :
   * **Username** : Nom d'utilisateur unique
   * **Password** : Mot de passe fort
   * **Admin Profile** : Profil d'accès (super_admin, prof_admin, etc.)
   * **Comments** : Description optionnelle
4. Configurez les options avancées si nécessaire :
   * **Trusted Hosts** : Adresses IP autorisées à se connecter
   * **Two-factor Authentication** : Authentification à deux facteurs
   * **PKI Group** : Authentification par certificat
5. Cliquez sur **OK** pour créer le compte

Pour créer un compte administrateur via la CLI :

```
config system admin
    edit "secadmin"
        set password "StrongPassword123!"
        set accprofile "super_admin"
        set comments "Compte administrateur sécurisé"
        set trusthost1 192.168.1.100 255.255.255.255
        set two-factor enable
        set two-factor-authentication fortitoken
        set fortitoken "FTK0123456789"
    next
end
```

### Profils d'accès administrateur

Les profils d'accès définissent les permissions accordées aux administrateurs :

1. Accédez à **System > Admin Profiles**
2. Cliquez sur **Create New**
3. Configurez le profil :
   * **Name** : Nom du profil
   * **Permissions** : Droits d'accès pour chaque section (None, Read Only, Read/Write)
4. Cliquez sur **OK** pour créer le profil

Pour créer un profil d'accès via la CLI :

```
config system accprofile
    edit "network_admin"
        set scope global
        set secfabgrp read-write
        set netgrp read-write
        set fwgrp read-write
        set vpngrp read-write
        set loggrp read
        set sysgrp read
        set admintimeout-override enable
        set admintimeout 60
    next
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Principe du moindre privilège</h4>
<p>Appliquez le principe du moindre privilège en accordant uniquement les permissions nécessaires à chaque administrateur pour accomplir ses tâches. Par exemple, créez des profils distincts pour les administrateurs réseau, les administrateurs de sécurité et les opérateurs de surveillance.</p>
</div>

### Authentification à deux facteurs

L'authentification à deux facteurs (2FA) renforce considérablement la sécurité des accès administratifs :

1. Accédez à **System > FortiTokens**
2. Importez ou activez des FortiTokens (physiques ou mobiles)
3. Accédez à **System > Administrators**
4. Modifiez un compte administrateur existant ou créez-en un nouveau
5. Activez **Two-factor Authentication**
6. Sélectionnez la méthode (FortiToken, Email, SMS)
7. Associez un FortiToken au compte si cette méthode est choisie
8. Cliquez sur **OK** pour appliquer les modifications

### Restriction d'accès par adresse IP

Limitez les adresses IP depuis lesquelles l'accès administratif est autorisé :

1. Accédez à **System > Administrators**
2. Modifiez un compte administrateur
3. Dans la section **Trusted Hosts**, spécifiez jusqu'à 10 adresses IP ou plages d'adresses
4. Cliquez sur **OK** pour appliquer les modifications

Pour configurer les hôtes de confiance via la CLI :

```
config system admin
    edit "admin"
        set trusthost1 192.168.1.0 255.255.255.0
        set trusthost2 10.0.0.5 255.255.255.255
    next
end
```

### Paramètres globaux de sécurité administrative

Configurez les paramètres globaux pour renforcer la sécurité de tous les accès administratifs :

1. Accédez à **System > Settings**
2. Dans la section **Administration Settings**, configurez :
   * **HTTP Port** : Port pour l'accès HTTP (si activé)
   * **HTTPS Port** : Port pour l'accès HTTPS
   * **Idle Timeout** : Délai d'inactivité avant déconnexion
   * **Admin Password Policy** : Politique de mot de passe
   * **Enable Strong Cryptography** : Utilisation de chiffrements forts
3. Cliquez sur **Apply** pour enregistrer les modifications

Pour configurer les paramètres globaux via la CLI :

```
config system global
    set admin-https-redirect enable
    set admin-port 8443
    set admin-sport 8443
    set admin-ssh-port 2222
    set admin-telnet-port 0
    set admin-idle-timeout 30
    set strong-crypto enable
end

config system password-policy
    set status enable
    set minimum-length 12
    set min-lower-case-letter 1
    set min-upper-case-letter 1
    set min-number 1
    set min-non-alphanumeric 1
    set change-4-characters enable
    set expire-status enable
    set expire-day 90
end
```

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Accès administratif sur les interfaces externes</h4>
<p>Évitez d'activer l'accès administratif sur les interfaces externes (WAN) dans la mesure du possible. Si cela est nécessaire, utilisez des ports non standard, limitez l'accès à des adresses IP spécifiques, activez l'authentification à deux facteurs et utilisez uniquement des protocoles sécurisés (HTTPS, SSH).</p>
</div>

### Certificats administratifs

Remplacez le certificat auto-signé par défaut par un certificat valide pour l'interface d'administration :

1. Accédez à **System > Certificates**
2. Importez un certificat existant ou générez une demande de signature de certificat (CSR)
3. Une fois le certificat obtenu, accédez à **System > Settings**
4. Dans la section **HTTPS Server Certificate**, sélectionnez votre certificat
5. Cliquez sur **Apply** pour enregistrer les modifications

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Journalisation des activités administratives</h4>
<p>Activez la journalisation complète des activités administratives pour assurer la traçabilité des actions effectuées sur le FortiGate. Configurez l'envoi de ces journaux vers un serveur syslog externe ou un FortiAnalyzer pour une conservation à long terme et une analyse centralisée.</p>
</div>

---

<h1 id="reseau" style="color:#E23237;">3. Réseau & Routage</h1>

<h2 id="interfaces" style="color:#0D274D;">3.1 Types d'interfaces et configuration</h2>

Les interfaces réseau sont les points de connexion entre le FortiGate et les différents segments de réseau. Cette section détaille les différents types d'interfaces disponibles et leur configuration.

### Types d'interfaces disponibles

FortiGate prend en charge plusieurs types d'interfaces pour répondre à divers besoins de déploiement :

* **Interfaces physiques** : Ports Ethernet intégrés à l'appliance
* **Interfaces VLAN** : Interfaces virtuelles basées sur le standard 802.1Q
* **Interfaces d'agrégation** : Regroupement de plusieurs interfaces physiques (802.3ad)
* **Interfaces de tunnel** : Pour les connexions VPN et autres tunnels
* **Interfaces loopback** : Interfaces virtuelles pour les services internes
* **Interfaces redondantes** : Paires d'interfaces en redondance active/passive
* **Interfaces sans fil** : Pour les modèles avec capacités WiFi intégrées
* **Interfaces SSL VPN** : Portails d'accès VPN pour les utilisateurs distants

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Capacités des interfaces</h4>
<p>Les capacités des interfaces varient selon les modèles FortiGate. Les modèles haut de gamme disposent généralement de ports à plus haute vitesse (10/40/100 Gbps) et de modules d'extension pour des types d'interfaces supplémentaires (fibre, QSFP+, etc.).</p>
</div>

### Configuration des interfaces physiques

La configuration de base d'une interface physique comprend :

1. **Paramètres de base** :
   * Nom et alias de l'interface
   * Adressage IP (statique, DHCP, PPPoE)
   * Masque de sous-réseau
   * Rôle (WAN, LAN, DMZ, etc.)
   * État administratif (up/down)

2. **Paramètres de sécurité** :
   * Services d'administration autorisés (HTTPS, SSH, PING, etc.)
   * Détection de dispositifs
   * Contrôle d'accès

3. **Paramètres avancés** :
   * MTU (Maximum Transmission Unit)
   * Vitesse et mode duplex
   * Priorité de QoS
   * Paramètres de conservation MAC

Exemple de configuration CLI pour une interface physique :

```
config system interface
    edit "port1"
        set vdom "root"
        set mode static
        set ip 192.168.1.1 255.255.255.0
        set allowaccess ping https ssh
        set type physical
        set role lan
        set snmp-index 1
        set mtu-override enable
        set mtu 1500
    next
end
```

### Modes d'adressage

Les interfaces FortiGate prennent en charge plusieurs modes d'adressage :

* **Statique** : Adresse IP fixe configurée manuellement
* **DHCP** : Obtention automatique d'une adresse IP depuis un serveur DHCP
* **PPPoE** : Pour les connexions DSL nécessitant une authentification PPP
* **Sans adresse IP** : Pour les interfaces utilisées uniquement en mode pont

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Bonnes pratiques pour les interfaces</h4>
<p>Utilisez des noms et des alias descriptifs pour vos interfaces afin de faciliter l'identification de leur fonction. Par exemple, renommez "port1" en "WAN1" ou "INTERNET" pour une interface connectée à Internet.</p>
</div>

<h2 id="vlans" style="color:#0D274D;">3.2 Création de VLANs et zones</h2>

Les VLANs (Virtual Local Area Networks) permettent de segmenter logiquement un réseau physique en plusieurs réseaux virtuels isolés. Les zones, quant à elles, regroupent plusieurs interfaces pour simplifier la gestion des politiques de sécurité.

### Configuration des VLANs

Pour créer un VLAN sur FortiGate :

1. Accédez à **Network > Interfaces**
2. Cliquez sur **Create New > Interface**
3. Configurez les paramètres suivants :
   * **Interface Name** : Nom du VLAN (ex: VLAN_Finance)
   * **Type** : VLAN
   * **Interface** : Interface physique parent
   * **VLAN ID** : Identifiant numérique du VLAN (1-4094)
   * **Addressing Mode** : Mode d'adressage (généralement statique)
   * **IP/Netmask** : Adresse IP et masque de sous-réseau
   * **Administrative Access** : Services d'administration autorisés
4. Cliquez sur **OK** pour créer le VLAN

Exemple de configuration CLI pour un VLAN :

```
config system interface
    edit "VLAN_Finance"
        set vdom "root"
        set ip 10.10.20.1 255.255.255.0
        set allowaccess ping
        set type vlan
        set interface "port2"
        set vlanid 20
    next
end
```

### Considérations pour les VLANs

* Les VLANs doivent être configurés de manière cohérente sur tous les équipements du réseau
* L'interface physique parent doit être configurée en mode "trunk" ou "hybrid" sur les commutateurs connectés
* Chaque VLAN doit avoir un ID unique dans le réseau
* Les VLANs peuvent être utilisés pour isoler différents types de trafic (voix, données, gestion, etc.)

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Sécurité des VLANs</h4>
<p>Ne considérez pas les VLANs comme une mesure de sécurité complète. Bien qu'ils fournissent une isolation logique, ils peuvent être vulnérables aux attaques de "VLAN hopping". Utilisez des politiques de pare-feu entre VLANs pour renforcer la sécurité.</p>
</div>

### Création et utilisation des zones

Les zones regroupent plusieurs interfaces sous une entité logique unique, ce qui simplifie la création de politiques de sécurité :

1. Accédez à **Network > Interfaces**
2. Cliquez sur **Create New > Zone**
3. Configurez les paramètres suivants :
   * **Name** : Nom de la zone (ex: Internal_Networks)
   * **Block Intra-zone Traffic** : Autoriser ou bloquer le trafic entre les membres de la zone
   * **Interface Members** : Interfaces à inclure dans la zone
4. Cliquez sur **OK** pour créer la zone

Exemple de configuration CLI pour une zone :

```
config system zone
    edit "Internal_Networks"
        set intrazone allow
        set interface "port3" "VLAN_Finance" "VLAN_HR"
    next
end
```

### Avantages des zones

* Simplification des politiques de pare-feu (une règle pour toute la zone au lieu d'une règle par interface)
* Gestion plus facile lors de l'ajout ou de la suppression d'interfaces
* Possibilité de contrôler le trafic intra-zone
* Organisation logique des interfaces selon leur fonction ou leur niveau de sécurité

<h2 id="agregation" style="color:#0D274D;">3.3 Agrégation de liens</h2>

L'agrégation de liens (Link Aggregation) permet de combiner plusieurs interfaces physiques en une seule interface logique pour augmenter la bande passante et/ou la redondance.

### Types d'agrégation

FortiGate prend en charge deux types principaux d'agrégation :

1. **Agrégation 802.3ad (LACP)** : Utilise le protocole LACP (Link Aggregation Control Protocol) pour négocier dynamiquement l'agrégation avec le commutateur connecté.

2. **Agrégation statique** : Configuration manuelle de l'agrégation sans négociation dynamique.

### Configuration d'une agrégation de liens

Pour créer une agrégation de liens via l'interface web :

1. Accédez à **Network > Interfaces**
2. Cliquez sur **Create New > Interface**
3. Configurez les paramètres suivants :
   * **Interface Name** : Nom de l'agrégation (ex: AGGREGATE1)
   * **Type** : 802.3ad Aggregate ou Redundant
   * **Member** : Sélectionnez les interfaces physiques à inclure
   * **Addressing Mode** : Mode d'adressage
   * **IP/Netmask** : Adresse IP et masque de sous-réseau
   * **Administrative Access** : Services d'administration autorisés
4. Pour une agrégation 802.3ad, configurez également :
   * **LACP Mode** : Active (initie les négociations) ou Passive (répond uniquement)
   * **LACP Speed** : Slow (30s) ou Fast (1s) pour les intervalles de mise à jour
5. Cliquez sur **OK** pour créer l'agrégation

Exemple de configuration CLI pour une agrégation 802.3ad :

```
config system interface
    edit "AGGREGATE1"
        set vdom "root"
        set ip 192.168.10.1 255.255.255.0
        set allowaccess ping https ssh
        set type aggregate
        set member "port3" "port4"
        set lacp-mode active
        set lacp-speed fast
    next
end
```

### Algorithmes de distribution de charge

FortiGate prend en charge plusieurs algorithmes pour distribuer le trafic sur les liens agrégés :

* **Layer 2 (src-mac, dst-mac, src-dst-mac)** : Distribution basée sur les adresses MAC
* **Layer 2-3 (src-ip, dst-ip, src-dst-ip)** : Distribution basée sur les adresses IP
* **Layer 3-4 (src-port, dst-port, src-dst-port)** : Distribution basée sur les ports TCP/UDP

Pour configurer l'algorithme via la CLI :

```
config system interface
    edit "AGGREGATE1"
        set algorithm "layer3-4"
    next
end
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Compatibilité LACP</h4>
<p>Pour que l'agrégation LACP fonctionne correctement, le commutateur connecté doit également prendre en charge le protocole LACP et être configuré de manière compatible. Vérifiez que les paramètres LACP (mode, vitesse, algorithme) sont cohérents des deux côtés.</p>
</div>

<h2 id="routage-statique" style="color:#0D274D;">3.4 Routage statique</h2>

Le routage statique consiste à configurer manuellement les routes pour diriger le trafic vers les destinations spécifiques. C'est la méthode la plus simple pour configurer le routage sur un FortiGate.

### Configuration des routes statiques

Pour créer une route statique via l'interface web :

1. Accédez à **Network > Static Routes**
2. Cliquez sur **Create New**
3. Configurez les paramètres suivants :
   * **Destination** : Réseau de destination (adresse IP/masque)
   * **Gateway** : Adresse IP de la passerelle
   * **Interface** : Interface de sortie
   * **Administrative Distance** : Valeur de distance administrative (priorité)
   * **Priority** : Priorité pour les routes de même distance
   * **Comment** : Description optionnelle
4. Cliquez sur **OK** pour créer la route

Exemple de configuration CLI pour une route statique :

```
config router static
    edit 1
        set dst 10.0.0.0 255.0.0.0
        set gateway 192.168.1.254
        set device "port1"
        set distance 10
        set priority 5
        set comment "Route vers réseau interne"
    next
end
```

### Route par défaut

La route par défaut (0.0.0.0/0) est utilisée pour diriger tout le trafic qui ne correspond à aucune autre route plus spécifique. C'est généralement la route vers Internet :

```
config router static
    edit 0
        set dst 0.0.0.0 0.0.0.0
        set gateway 203.0.113.1
        set device "wan1"
    next
end
```

### Routes statiques avec surveillance de passerelle

FortiGate peut surveiller l'état de la passerelle pour les routes statiques et basculer automatiquement vers une route de secours si la passerelle devient inaccessible :

```
config router static
    edit 1
        set dst 0.0.0.0 0.0.0.0
        set gateway 203.0.113.1
        set device "wan1"
        set distance 10
        set gwdetect enable
        set pingserver 203.0.113.1
        set weight 10
    next
    edit 2
        set dst 0.0.0.0 0.0.0.0
        set gateway 198.51.100.1
        set device "wan2"
        set distance 20
        set gwdetect enable
        set pingserver 198.51.100.1
        set weight 5
    next
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Bonnes pratiques pour le routage statique</h4>
<p>Utilisez des distances administratives différentes pour créer une hiérarchie de routes. Les routes avec une distance plus faible sont préférées. Pour les routes de même distance, utilisez le paramètre de priorité pour définir l'ordre de préférence.</p>
</div>

<h2 id="routage-dynamique" style="color:#0D274D;">3.5 Routage dynamique (OSPF, BGP)</h2>

Les protocoles de routage dynamique permettent aux routeurs d'échanger automatiquement des informations de routage et de s'adapter aux changements de topologie réseau.

### Open Shortest Path First (OSPF)

OSPF est un protocole de routage à état de lien utilisé principalement dans les réseaux internes :

#### Configuration de base d'OSPF

1. Accédez à **Network > OSPF**
2. Configurez les paramètres de base :
   * **Router ID** : Identifiant unique du routeur (généralement une adresse IP)
   * **Areas** : Zones OSPF (généralement area 0 pour la zone backbone)
   * **Networks** : Réseaux à annoncer via OSPF
   * **Interfaces** : Interfaces participant à OSPF

Exemple de configuration CLI pour OSPF :

```
config router ospf
    set router-id 10.0.0.1
    config area
        edit 0.0.0.0
        next
    end
    config network
        edit 1
            set prefix 192.168.1.0 255.255.255.0
            set area 0.0.0.0
        next
        edit 2
            set prefix 10.0.0.0 255.255.255.0
            set area 0.0.0.0
        next
    end
    config interface
        edit "port2"
            set network-type broadcast
            set cost 100
            set priority 1
        next
    end
end
```

### Border Gateway Protocol (BGP)

BGP est le protocole de routage principal utilisé sur Internet et pour les connexions entre différents systèmes autonomes :

#### Configuration de base de BGP

1. Accédez à **Network > BGP**
2. Configurez les paramètres de base :
   * **AS Number** : Numéro de système autonome local
   * **Router ID** : Identifiant unique du routeur
   * **Networks** : Réseaux à annoncer via BGP
   * **Neighbors** : Routeurs BGP voisins

Exemple de configuration CLI pour BGP :

```
config router bgp
    set as 65001
    set router-id 10.0.0.1
    config neighbor
        edit "203.0.113.2"
            set remote-as 65002
            set keepalive-timer 30
            set holdtime-timer 90
        next
    end
    config network
        edit 1
            set prefix 192.168.0.0 255.255.0.0
        next
    end
end
```

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Sécurité du routage dynamique</h4>
<p>Configurez toujours l'authentification pour les protocoles de routage dynamique afin d'éviter les attaques par injection de routes. Pour OSPF, utilisez l'authentification MD5, et pour BGP, utilisez l'authentification MD5 ou les filtres de préfixes.</p>
</div>

### Redistribution de routes

La redistribution permet d'échanger des routes entre différents protocoles de routage :

```
config router ospf
    config redistribute "static"
        set status enable
        set metric 10
        set metric-type 2
    end
    config redistribute "connected"
        set status enable
        set metric 10
        set metric-type 2
    end
end
```

<h2 id="sd-wan" style="color:#0D274D;">3.6 SD-WAN</h2>

SD-WAN (Software-Defined Wide Area Network) est une fonctionnalité qui permet d'agréger plusieurs connexions WAN et d'optimiser le routage du trafic en fonction de règles définies.

### Principes de base du SD-WAN

Le SD-WAN FortiGate offre plusieurs avantages :

* Agrégation de plusieurs liens WAN (MPLS, Internet, 4G/5G, etc.)
* Sélection intelligente du chemin basée sur la qualité de service
* Équilibrage de charge et basculement automatique
* Optimisation des applications
* Routage basé sur les applications ou les utilisateurs

### Configuration du SD-WAN

Pour configurer le SD-WAN via l'interface web :

1. Accédez à **Network > SD-WAN**
2. Activez le SD-WAN
3. Configurez les interfaces membres :
   * Ajoutez les interfaces WAN au SD-WAN
   * Définissez la priorité et le coût de chaque interface
4. Créez des règles SD-WAN pour définir comment le trafic doit être routé
5. Configurez les SLA (Service Level Agreement) pour surveiller la qualité des liens

Exemple de configuration CLI pour SD-WAN :

```
config system sdwan
    set status enable
    config members
        edit 1
            set interface "wan1"
            set gateway 203.0.113.1
            set priority 1
        next
        edit 2
            set interface "wan2"
            set gateway 198.51.100.1
            set priority 2
        next
    end
    config health-check
        edit "Internet_Check"
            set server "8.8.8.8"
            set protocol ping
            set interval 1000
            set failtime 3
            set recoverytime 5
            set members 1 2
        next
    end
    config service
        edit 1
            set name "Critical_Apps"
            set mode priority
            set src "all"
            set dst "all"
            set protocol 6
            set app-category 17
            set priority-members 1 2
        next
        edit 2
            set name "Regular_Traffic"
            set mode load-balance
            set src "all"
            set dst "all"
            set priority-members 1 2
        next
    end
end
```

### Modes de fonctionnement SD-WAN

FortiGate prend en charge plusieurs modes de fonctionnement pour les règles SD-WAN :

* **Mode priorité** : Utilise les liens dans l'ordre de priorité défini
* **Mode équilibrage de charge** : Distribue le trafic sur plusieurs liens
* **Mode basé sur les SLA** : Sélectionne les liens en fonction des mesures de qualité
* **Mode manuel** : Permet de spécifier explicitement l'interface à utiliser

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Surveillance SD-WAN</h4>
<p>Utilisez les tableaux de bord SD-WAN pour surveiller les performances des liens WAN, y compris la latence, la gigue, la perte de paquets et la bande passante. Ces informations sont essentielles pour optimiser les règles SD-WAN et résoudre les problèmes de performance.</p>
</div>

### Intégration avec la Security Fabric

Le SD-WAN FortiGate s'intègre à la Security Fabric pour offrir une visibilité et un contrôle centralisés :

* Gestion centralisée via FortiManager
* Rapports détaillés via FortiAnalyzer
* Intégration avec FortiExtender pour les connexions 4G/5G
* Orchestration SD-WAN via FortiOrchestrator

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Bonnes pratiques SD-WAN</h4>
<p>Commencez par une configuration SD-WAN simple, puis affinez-la progressivement. Créez d'abord des règles pour les applications critiques, puis ajoutez des règles plus spécifiques pour d'autres types de trafic. Utilisez plusieurs méthodes de vérification d'état (ping, HTTP, DNS) pour une détection plus précise des problèmes de connectivité.</p>
</div>

---

<h1 id="pare-feu" style="color:#E23237;">4. Pare-feu et politiques de sécurité</h1>

<h2 id="concepts-fondamentaux" style="color:#0D274D;">4.1 Concepts fondamentaux du pare-feu FortiGate</h2>

Le pare-feu est la fonction principale d'un FortiGate. Cette section explique les concepts fondamentaux du fonctionnement du pare-feu FortiGate.

### Architecture du pare-feu FortiGate

Le pare-feu FortiGate utilise une architecture de traitement du trafic en plusieurs étapes :

1. **Inspection de paquets** : Vérification de l'intégrité des paquets
2. **Correspondance de session** : Vérification si le paquet appartient à une session existante
3. **Routage** : Détermination de l'interface de sortie
4. **Évaluation des politiques** : Application des règles de pare-feu
5. **Inspection de contenu** : Analyse approfondie du contenu (si configurée)
6. **Transmission** : Envoi du paquet vers sa destination

### Modes de fonctionnement

FortiGate peut fonctionner dans différents modes :

* **Mode NAT/Route** (par défaut) : Fonctionne comme un routeur avec des interfaces dans différents sous-réseaux
* **Mode Transparent** : Fonctionne comme un pont de niveau 2, sans modifier les adresses IP
* **Mode NGFW** (Next-Generation Firewall) : Organisation des politiques basée sur les applications et les utilisateurs
* **Mode Proxy** : Inspection approfondie du trafic avec terminaison des connexions

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Choix du mode</h4>
<p>Le mode NAT/Route est le plus couramment utilisé car il offre le meilleur équilibre entre fonctionnalités et performances. Le mode Transparent est utile pour déployer un FortiGate dans un réseau existant sans modifier l'architecture IP.</p>
</div>

### Flux de traitement des paquets

Le traitement des paquets par FortiGate suit un flux précis :

1. Un paquet arrive sur une interface
2. Le FortiGate vérifie s'il appartient à une session existante
   * Si oui, il applique les actions déjà déterminées pour cette session
   * Si non, il crée une nouvelle session et poursuit l'évaluation
3. Le FortiGate détermine l'interface de sortie via la table de routage
4. Il évalue les politiques de pare-feu applicables (de haut en bas)
5. Si une correspondance est trouvée, il applique les actions définies dans la politique
6. Si des profils de sécurité sont attachés à la politique, il effectue l'inspection de contenu
7. Le paquet est transmis ou rejeté selon le résultat de l'évaluation

### Tables de sessions

FortiGate maintient des tables de sessions pour suivre les connexions actives :

* Chaque session contient des informations sur les adresses source/destination, les ports, le protocole, etc.
* Les sessions ont une durée de vie limitée et sont supprimées après un certain temps d'inactivité
* Les tables de sessions permettent un traitement rapide des paquets appartenant à des connexions établies

Pour afficher les sessions actives via la CLI :

```
diagnose sys session list
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Optimisation des performances</h4>
<p>Pour optimiser les performances du pare-feu, organisez vos politiques de manière à ce que les règles les plus fréquemment utilisées soient placées en haut de la liste. Cela réduit le temps nécessaire pour trouver une correspondance.</p>
</div>

<h2 id="politiques-securite" style="color:#0D274D;">4.2 Création et gestion des politiques de sécurité</h2>

Les politiques de sécurité (ou règles de pare-feu) définissent quels types de trafic sont autorisés ou bloqués entre les différentes interfaces ou zones.

### Structure d'une politique de sécurité

Une politique de sécurité FortiGate comprend généralement les éléments suivants :

* **Nom/ID** : Identifiant unique de la politique
* **Interfaces/Zones** : Source et destination du trafic
* **Adresses** : Objets d'adresses source et destination
* **Services/Ports** : Services ou ports autorisés
* **Action** : Accept, Deny, IPsec
* **Profils de sécurité** : Antivirus, Filtrage Web, IPS, etc.
* **Journalisation** : Options de journalisation du trafic
* **NAT** : Options de traduction d'adresses
* **Authentification** : Exigences d'authentification utilisateur

### Création d'une politique de base

Pour créer une politique de sécurité via l'interface web :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Cliquez sur **Create New**
3. Configurez les paramètres de base :
   * **Name** : Nom descriptif de la politique
   * **Incoming Interface** : Interface ou zone source
   * **Outgoing Interface** : Interface ou zone destination
   * **Source** : Adresses source
   * **Destination** : Adresses destination
   * **Service** : Services ou ports autorisés
   * **Action** : Accept, Deny, IPsec
4. Configurez les options avancées si nécessaire :
   * **Security Profiles** : Profils de sécurité à appliquer
   * **NAT** : Options de NAT
   * **Logging** : Options de journalisation
5. Cliquez sur **OK** pour créer la politique

Exemple de configuration CLI pour une politique de base :

```
config firewall policy
    edit 1
        set name "LAN to Internet"
        set srcintf "port2"
        set dstintf "port1"
        set srcaddr "LAN_Subnet"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
        set nat enable
    next
end
```

### Ordre des politiques

L'ordre des politiques est crucial car FortiGate évalue les politiques de haut en bas et applique la première correspondance :

* Les politiques plus spécifiques doivent être placées avant les politiques plus générales
* Les politiques de refus explicites doivent être placées avant la politique de refus implicite
* Les politiques peuvent être réorganisées par glisser-déposer dans l'interface web

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Politique "ANY-ANY"</h4>
<p>Évitez de créer des politiques trop permissives (source "any", destination "any", service "any"). Ces politiques représentent un risque de sécurité important et compliquent le dépannage. Préférez des politiques plus spécifiques et restrictives.</p>
</div>

### Politiques implicites

FortiGate applique des politiques implicites qui ne sont pas visibles dans la liste des politiques :

* Tout le trafic entre interfaces est refusé par défaut
* Le trafic provenant du FortiGate lui-même est autorisé
* Le trafic de gestion vers le FortiGate est contrôlé par les paramètres d'accès administratif des interfaces

### Sections de politique

Dans les déploiements complexes, les politiques peuvent être organisées en sections pour une meilleure gestion :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Cliquez sur **Create New > Section**
3. Donnez un nom à la section
4. Organisez vos politiques dans les sections appropriées

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Documentation des politiques</h4>
<p>Utilisez le champ "Comments" pour documenter l'objectif de chaque politique, qui l'a créée et pourquoi. Cela facilite grandement la maintenance et le dépannage, surtout dans les environnements avec plusieurs administrateurs.</p>
</div>

<h2 id="objets-adresses" style="color:#0D274D;">4.3 Objets d'adresses et groupes</h2>

Les objets d'adresses permettent de définir des hôtes, des réseaux ou des plages d'adresses IP qui peuvent être utilisés dans les politiques de pare-feu.

### Types d'objets d'adresses

FortiGate prend en charge plusieurs types d'objets d'adresses :

* **Adresse IP/Masque** : Réseau ou hôte unique (ex: 192.168.1.0/24)
* **Plage d'adresses IP** : Plage continue d'adresses (ex: 192.168.1.10-192.168.1.50)
* **Géographique** : Adresses IP associées à un pays ou une région
* **FQDN** : Nom de domaine complet résolu dynamiquement
* **Dynamique** : Adresses associées à des connecteurs cloud ou SDN
* **MAC** : Adresses basées sur l'adresse MAC (mode transparent uniquement)

### Création d'objets d'adresses

Pour créer un objet d'adresse via l'interface web :

1. Accédez à **Policy & Objects > Addresses**
2. Cliquez sur **Create New > Address**
3. Configurez les paramètres :
   * **Name** : Nom unique et descriptif
   * **Type** : Type d'adresse (Subnet, Range, etc.)
   * **Subnet/IP Range** : Valeur de l'adresse selon le type
   * **Interface** : Interface associée (optionnel)
   * **Comment** : Description de l'objet
4. Cliquez sur **OK** pour créer l'objet

Exemple de configuration CLI pour différents types d'objets d'adresses :

```
config firewall address
    edit "Internal_Servers"
        set subnet 10.0.0.0 255.255.255.0
        set comment "Serveurs internes"
    next
    edit "Admin_Workstations"
        set type iprange
        set start-ip 192.168.1.100
        set end-ip 192.168.1.150
        set comment "Postes administrateurs"
    next
    edit "Company_Website"
        set type fqdn
        set fqdn "www.example.com"
    next
    edit "France_IPs"
        set type geography
        set country "FR"
    next
end
```

### Groupes d'adresses

Les groupes d'adresses permettent de regrouper plusieurs objets d'adresses pour simplifier la gestion des politiques :

1. Accédez à **Policy & Objects > Addresses**
2. Cliquez sur **Create New > Address Group**
3. Configurez les paramètres :
   * **Name** : Nom du groupe
   * **Members** : Objets d'adresses à inclure
   * **Comment** : Description du groupe
4. Cliquez sur **OK** pour créer le groupe

Exemple de configuration CLI pour un groupe d'adresses :

```
config firewall addrgrp
    edit "Internal_Resources"
        set member "Internal_Servers" "Admin_Workstations" "Database_Servers"
        set comment "Ressources internes critiques"
    next
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Organisation des objets</h4>
<p>Utilisez une convention de nommage cohérente pour vos objets d'adresses et groupes. Par exemple, préfixez les noms avec le type d'objet ou sa fonction (SRV_ pour les serveurs, NET_ pour les réseaux, GRP_ pour les groupes, etc.).</p>
</div>

### Objets d'adresses dynamiques

Les objets d'adresses dynamiques sont particulièrement utiles dans les environnements cloud ou SDN :

* **Adresses AWS** : Instances, VPC, sous-réseaux AWS
* **Adresses Azure** : Ressources Azure
* **Adresses GCP** : Ressources Google Cloud
* **Adresses Fabric Connector** : Ressources définies par les connecteurs Security Fabric

Pour utiliser ces objets, vous devez d'abord configurer les connecteurs cloud appropriés dans **Security Fabric > External Connectors**.

<h2 id="services-applications" style="color:#0D274D;">4.4 Services et applications</h2>

Les objets de service définissent les protocoles et les ports utilisés dans les politiques de pare-feu, tandis que les applications représentent des applications spécifiques indépendamment des ports utilisés.

### Objets de service

Les objets de service peuvent être de plusieurs types :

* **TCP/UDP/SCTP** : Services basés sur des ports
* **ICMP** : Types et codes ICMP
* **IP** : Protocoles IP spécifiques
* **Proxy** : Services proxy explicites

Pour créer un objet de service via l'interface web :

1. Accédez à **Policy & Objects > Services**
2. Cliquez sur **Create New > Service**
3. Configurez les paramètres :
   * **Name** : Nom du service
   * **Category** : Catégorie du service
   * **Protocol Type** : TCP/UDP/SCTP, ICMP, IP, etc.
   * **Port Range** : Plage de ports (pour TCP/UDP/SCTP)
   * **ICMP Type/Code** : Type et code (pour ICMP)
   * **Protocol Number** : Numéro de protocole (pour IP)
4. Cliquez sur **OK** pour créer le service

Exemple de configuration CLI pour différents types de services :

```
config firewall service custom
    edit "Custom_Web"
        set tcp-portrange 8080-8090
        set comment "Serveurs web personnalisés"
    next
    edit "Custom_DNS"
        set udp-portrange 53
        set tcp-portrange 53
    next
    edit "Custom_Ping"
        set protocol ICMP
        set icmptype 8
        set icmpcode 0
    next
end
```

### Groupes de services

Les groupes de services permettent de regrouper plusieurs services pour simplifier la gestion des politiques :

1. Accédez à **Policy & Objects > Services**
2. Cliquez sur **Create New > Service Group**
3. Configurez les paramètres :
   * **Name** : Nom du groupe
   * **Members** : Services à inclure
4. Cliquez sur **OK** pour créer le groupe

Exemple de configuration CLI pour un groupe de services :

```
config firewall service group
    edit "Web_Services"
        set member "HTTP" "HTTPS" "Custom_Web"
    next
end
```

### Contrôle d'application

Le contrôle d'application permet d'identifier et de contrôler les applications indépendamment des ports utilisés :

1. Accédez à **Security Profiles > Application Control**
2. Créez ou modifiez un profil de contrôle d'application
3. Configurez les catégories et applications à contrôler
4. Appliquez le profil aux politiques de pare-feu pertinentes

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Services prédéfinis</h4>
<p>FortiGate inclut de nombreux services prédéfinis pour les protocoles courants. Vérifiez toujours si un service prédéfini existe avant de créer un service personnalisé. Les services prédéfinis sont régulièrement mis à jour par Fortinet pour refléter les dernières normes.</p>
</div>

<h2 id="nat" style="color:#0D274D;">4.5 Network Address Translation (NAT)</h2>

La traduction d'adresses réseau (NAT) permet de modifier les adresses IP source et/ou destination des paquets. FortiGate prend en charge plusieurs types de NAT.

### Source NAT (SNAT)

Le SNAT modifie l'adresse IP source des paquets, généralement utilisé pour permettre aux réseaux privés d'accéder à Internet :

#### NAT intégré aux politiques

Le moyen le plus simple d'activer le SNAT est via l'option NAT dans les politiques de pare-feu :

1. Créez ou modifiez une politique de pare-feu
2. Dans la section **NAT**, activez **Enable NAT**
3. Sélectionnez **Use Outgoing Interface Address** pour utiliser l'IP de l'interface sortante
4. Alternativement, sélectionnez **Dynamic IP Pool** et choisissez un pool d'adresses IP

Exemple de configuration CLI pour le NAT intégré aux politiques :

```
config firewall policy
    edit 1
        set srcintf "port2"
        set dstintf "port1"
        set srcaddr "Internal_Network"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set nat enable
    next
end
```

#### Pools d'IP pour NAT

Pour des scénarios plus avancés, vous pouvez créer des pools d'adresses IP pour le NAT :

1. Accédez à **Policy & Objects > IP Pools**
2. Cliquez sur **Create New**
3. Configurez les paramètres :
   * **Name** : Nom du pool
   * **Type** : Overload (plusieurs clients partagent les mêmes IPs) ou One-to-One
   * **External IP Range** : Plage d'adresses IP publiques
4. Utilisez ce pool dans vos politiques de pare-feu

Exemple de configuration CLI pour un pool IP :

```
config firewall ippool
    edit "Public_IPs"
        set startip 203.0.113.10
        set endip 203.0.113.20
        set comment "Pool d'adresses IP publiques"
    next
end

config firewall policy
    edit 1
        set srcintf "port2"
        set dstintf "port1"
        set srcaddr "Internal_Network"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set nat enable
        set ippool enable
        set poolname "Public_IPs"
    next
end
```

### Destination NAT (DNAT)

Le DNAT modifie l'adresse IP de destination des paquets, généralement utilisé pour rediriger le trafic vers des serveurs internes :

#### Virtual IP (VIP)

Les VIPs permettent de mapper une adresse IP externe à une adresse IP interne :

1. Accédez à **Policy & Objects > Virtual IPs**
2. Cliquez sur **Create New > Virtual IP**
3. Configurez les paramètres :
   * **Name** : Nom du VIP
   * **Interface** : Interface externe
   * **External IP Address** : Adresse IP publique
   * **Map to IPv4 Address** : Adresse IP interne
   * **Port Forwarding** : Activez pour mapper des ports spécifiques
   * **Protocol** : TCP, UDP ou SCTP
   * **External Service Port** : Port externe
   * **Map to Port** : Port interne
4. Utilisez ce VIP comme destination dans une politique de pare-feu

Exemple de configuration CLI pour un VIP :

```
config firewall vip
    edit "Web_Server_VIP"
        set extip 203.0.113.100
        set mappedip 192.168.1.10
        set portforward enable
        set extport 80
        set mappedport 80
    next
end

config firewall policy
    edit 2
        set srcintf "port1"
        set dstintf "port2"
        set srcaddr "all"
        set dstaddr "Web_Server_VIP"
        set action accept
        set schedule "always"
        set service "HTTP"
        set nat enable
    next
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Bonnes pratiques NAT</h4>
<p>Pour les serveurs accessibles depuis Internet, utilisez des VIPs avec port forwarding plutôt que d'exposer tous les ports. Cela limite la surface d'attaque en n'exposant que les services nécessaires.</p>
</div>

<h2 id="inspection-ssl" style="color:#0D274D;">4.6 Inspection SSL/TLS</h2>

L'inspection SSL/TLS permet au FortiGate d'inspecter le trafic chiffré pour détecter les menaces et appliquer les politiques de sécurité.

### Modes d'inspection SSL

FortiGate propose deux modes d'inspection SSL :

* **Inspection SSL en flux (Certificate Inspection)** : Inspecte uniquement les métadonnées du certificat sans déchiffrer le contenu
* **Inspection SSL profonde (Deep Inspection)** : Déchiffre, inspecte et rechiffre le trafic

### Configuration de l'inspection SSL

Pour configurer l'inspection SSL via l'interface web :

1. Accédez à **Security Profiles > SSL/SSH Inspection**
2. Créez un nouveau profil ou modifiez le profil par défaut
3. Sélectionnez le mode d'inspection (Certificate Inspection ou Deep Inspection)
4. Configurez les paramètres avancés :
   * **Ports** : Ports à inspecter
   * **Exemptions** : Sites à exempter de l'inspection
   * **Options de certificat** : Gestion des erreurs de certificat
5. Appliquez le profil aux politiques de pare-feu pertinentes

Exemple de configuration CLI pour l'inspection SSL :

```
config firewall ssl-ssh-profile
    edit "deep-inspection"
        set comment "Inspection SSL profonde"
        set ssl-anomalies-log enable
        set ssl-exemptions-log enable
        set ssl-negotiation-log enable
        config https
            set ports 443
            set status deep-inspection
        end
        config ftps
            set ports 990
            set status deep-inspection
        end
        config imaps
            set ports 993
            set status deep-inspection
        end
        config pop3s
            set ports 995
            set status deep-inspection
        end
        config smtps
            set ports 465
            set status deep-inspection
        end
        config ssh
            set ports 22
            set status deep-inspection
        end
    next
end
```

### Certificat CA pour l'inspection SSL

Pour l'inspection SSL profonde, FortiGate utilise son propre certificat CA pour signer les certificats présentés aux clients :

1. Accédez à **Security Profiles > SSL/SSH Inspection**
2. Dans la section **Certificate** du profil, vous pouvez :
   * Utiliser le certificat CA FortiGate par défaut
   * Importer un certificat CA personnalisé

Pour que l'inspection SSL fonctionne correctement, ce certificat CA doit être ajouté aux magasins de certificats de confiance des clients.

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Considérations légales et de confidentialité</h4>
<p>L'inspection SSL profonde peut soulever des questions légales et de confidentialité. Assurez-vous de respecter les lois et réglementations applicables, et informez les utilisateurs que leur trafic chiffré est inspecté. Créez des exemptions pour les sites sensibles comme les services bancaires et médicaux.</p>
</div>

### Exemptions d'inspection SSL

Certains sites ou applications peuvent ne pas fonctionner correctement avec l'inspection SSL ou peuvent contenir des données sensibles qui ne devraient pas être inspectées :

1. Accédez à **Security Profiles > SSL Exemptions**
2. Cliquez sur **Create New**
3. Ajoutez les adresses ou catégories de sites à exempter
4. Ces exemptions seront appliquées à tous les profils d'inspection SSL

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Dépannage SSL</h4>
<p>Si des applications ou sites web ne fonctionnent pas correctement avec l'inspection SSL profonde, vérifiez les journaux SSL pour identifier les problèmes. Les erreurs courantes incluent les certificats épinglés (certificate pinning) et les suites de chiffrement non prises en charge.</p>
</div>

<h2 id="regles-ipv6" style="color:#0D274D;">4.7 Règles IPv6 et coexistence IPv4/IPv6</h2>

FortiGate prend en charge à la fois IPv4 et IPv6, permettant de sécuriser les réseaux dans des environnements mixtes ou de transition.

### Activation d'IPv6

Pour activer la prise en charge d'IPv6 :

1. Accédez à **System > Feature Visibility**
2. Activez **IPv6**
3. Cliquez sur **Apply**

### Configuration des interfaces IPv6

Pour configurer une interface avec une adresse IPv6 :

1. Accédez à **Network > Interfaces**
2. Modifiez l'interface souhaitée
3. Dans la section **IPv6**, configurez :
   * **Addressing Mode** : Static, DHCP, Delegated, etc.
   * **IPv6 Address** : Adresse IPv6 et préfixe (si mode statique)
   * **IPv6 Administrative Access** : Services d'administration autorisés

Exemple de configuration CLI pour une interface IPv6 :

```
config system interface
    edit "port2"
        config ipv6
            set ip6-address 2001:db8:1::1/64
            set ip6-allowaccess ping https ssh
            set ip6-mode static
        end
    next
end
```

### Objets d'adresses IPv6

Pour créer des objets d'adresses IPv6 :

1. Accédez à **Policy & Objects > Addresses**
2. Cliquez sur **Create New > Address**
3. Sélectionnez **IPv6 Address** comme type
4. Configurez l'adresse IPv6 et le préfixe

Exemple de configuration CLI pour un objet d'adresse IPv6 :

```
config firewall address6
    edit "IPv6_Internal_Network"
        set ip6 2001:db8:1::/64
        set comment "Réseau interne IPv6"
    next
end
```

### Politiques de pare-feu IPv6

Les politiques IPv6 sont configurées séparément des politiques IPv4 :

1. Accédez à **Policy & Objects > IPv6 Policy**
2. Cliquez sur **Create New**
3. Configurez la politique comme vous le feriez pour IPv4, mais en utilisant des objets d'adresses IPv6

Exemple de configuration CLI pour une politique IPv6 :

```
config firewall policy6
    edit 1
        set name "IPv6_Outbound"
        set srcintf "port2"
        set dstintf "port1"
        set srcaddr "IPv6_Internal_Network"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
        set nat enable
    next
end
```

### Stratégies de transition IPv4/IPv6

FortiGate prend en charge plusieurs mécanismes de transition IPv4/IPv6 :

* **Double pile (Dual Stack)** : Exécution simultanée d'IPv4 et IPv6
* **Tunnels 6to4** : Encapsulation d'IPv6 dans IPv4
* **NAT64/DNS64** : Traduction entre IPv6 et IPv4

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Bonnes pratiques IPv6</h4>
<p>Appliquez les mêmes principes de sécurité à IPv6 qu'à IPv4. De nombreuses organisations négligent la sécurité IPv6, créant des failles potentielles. Assurez-vous que vos politiques IPv6 sont aussi strictes que vos politiques IPv4.</p>
</div>

<h2 id="shaping" style="color:#0D274D;">4.8 Traffic shaping et QoS</h2>

Le traffic shaping et la qualité de service (QoS) permettent de contrôler la bande passante et de prioriser certains types de trafic sur le réseau.

### Politiques de traffic shaping

FortiGate propose deux approches pour le traffic shaping :

* **Shaping par politique** : Appliqué directement dans les politiques de pare-feu
* **Shaping par interface** : Appliqué à tout le trafic traversant une interface

#### Shaping par politique

Pour configurer le shaping par politique :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Créez ou modifiez une politique
3. Dans la section **Traffic Shaping**, configurez :
   * **Shared Shaper** : Limite la bande passante totale
   * **Reverse Shared Shaper** : Limite la bande passante dans la direction inverse
   * **Per-IP Shaper** : Limite la bande passante par adresse IP

Exemple de configuration CLI pour le shaping par politique :

```
config firewall shaper traffic-shaper
    edit "Web_Traffic"
        set guaranteed-bandwidth 1000
        set maximum-bandwidth 2000
        set priority medium
    next
end

config firewall policy
    edit 1
        set srcintf "port2"
        set dstintf "port1"
        set srcaddr "Internal_Network"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "Web_Services"
        set traffic-shaper "Web_Traffic"
        set traffic-shaper-reverse "Web_Traffic"
    next
end
```

### Politiques de shaping

Les politiques de shaping permettent un contrôle plus granulaire basé sur des critères multiples :

1. Accédez à **Policy & Objects > Traffic Shaping Policy**
2. Cliquez sur **Create New**
3. Configurez les critères de correspondance (adresses, services, applications, etc.)
4. Définissez les actions de shaping (bande passante, priorité, etc.)

Exemple de configuration CLI pour une politique de shaping :

```
config firewall shaping-policy
    edit 1
        set name "Prioritize_VoIP"
        set service "SIP" "RTP"
        set dstintf "port1"
        set traffic-shaper "VoIP_Traffic"
        set traffic-shaper-reverse "VoIP_Traffic"
        set priority high
    next
end
```

### Classes de service et marquage DSCP

FortiGate peut marquer le trafic avec des valeurs DSCP (Differentiated Services Code Point) pour la QoS de bout en bout :

1. Accédez à **Policy & Objects > Traffic Shaping Policy**
2. Créez ou modifiez une politique de shaping
3. Dans la section **DSCP**, configurez le marquage DSCP

Exemple de configuration CLI pour le marquage DSCP :

```
config firewall shaping-policy
    edit 1
        set name "Mark_VoIP"
        set service "SIP" "RTP"
        set ip-version 4
        set dscp-marking enable
        set dscp-value 46
    next
end
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Valeurs DSCP courantes</h4>
<p>Quelques valeurs DSCP courantes : EF (46) pour la voix, AF41 (34) pour la vidéo, AF31 (26) pour les applications critiques, AF21 (18) pour les applications importantes, et BE (0) pour le trafic standard.</p>
</div>

### Surveillance du traffic shaping

Pour surveiller l'efficacité de vos politiques de traffic shaping :

1. Accédez à **Dashboard > Status**
2. Ajoutez le widget **Top Applications** ou **Traffic** pour voir la distribution du trafic
3. Utilisez la CLI pour des statistiques détaillées :

```
diagnose firewall shaper traffic-shaper list
diagnose firewall shaper policy list
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Approche progressive</h4>
<p>Adoptez une approche progressive pour le traffic shaping. Commencez par surveiller le trafic pour comprendre les modèles d'utilisation, puis appliquez des limites généreuses. Affinez progressivement les paramètres en fonction des besoins réels et des retours des utilisateurs.</p>
</div>

---

<h1 id="vpn" style="color:#E23237;">5. VPNs Fortinet</h1>

<h2 id="vpn-concepts" style="color:#0D274D;">5.1 Concepts fondamentaux des VPNs</h2>

Les réseaux privés virtuels (VPN) permettent de créer des connexions sécurisées à travers des réseaux non sécurisés comme Internet. Cette section présente les concepts fondamentaux des VPNs dans l'environnement Fortinet.

### Types de VPN pris en charge par FortiGate

FortiGate prend en charge plusieurs types de VPN pour répondre à différents besoins :

* **IPsec VPN** : Protocole standard pour les connexions site-à-site et d'accès distant
* **SSL VPN** : Solution d'accès distant basée sur SSL/TLS
* **PPTP/L2TP** : Protocoles VPN plus anciens (moins sécurisés)
* **GRE** : Tunnels génériques pour l'encapsulation de protocoles

### Modes de déploiement VPN

Les VPNs FortiGate peuvent être déployés dans différents modes :

* **Site-à-site** : Connexion entre deux ou plusieurs sites
* **Accès distant (client-to-site)** : Connexion d'utilisateurs individuels au réseau d'entreprise
* **Hub-and-spoke** : Topologie en étoile avec un site central
* **Maillé (mesh)** : Connexions entre tous les sites
* **ADVPN (Auto-Discovery VPN)** : Création dynamique de tunnels directs entre sites

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Choix du type de VPN</h4>
<p>Le choix entre IPsec et SSL VPN dépend principalement du cas d'usage. IPsec est généralement préféré pour les connexions site-à-site et les clients VPN permanents, tandis que SSL VPN est plus adapté pour l'accès distant occasionnel, notamment depuis des appareils non gérés ou des réseaux restreints.</p>
</div>

### Composants d'un VPN

Un VPN FortiGate comprend généralement les éléments suivants :

* **Interfaces** : Interfaces physiques ou virtuelles pour les connexions
* **Phase 1** : Établissement d'un canal sécurisé (IKE)
* **Phase 2** : Négociation des paramètres de chiffrement pour les données
* **Politiques** : Règles de pare-feu autorisant le trafic à travers le VPN
* **Routes** : Configuration du routage pour diriger le trafic vers le VPN
* **Authentification** : Méthodes pour vérifier l'identité des utilisateurs ou des appareils

### Considérations de sécurité

Plusieurs facteurs influencent la sécurité d'un VPN :

* **Algorithmes de chiffrement** : AES, 3DES, etc.
* **Longueur de clé** : 128, 256 bits, etc.
* **Algorithmes d'intégrité** : SHA-1, SHA-256, etc.
* **Groupes Diffie-Hellman** : Déterminent la force de l'échange de clés
* **Perfect Forward Secrecy (PFS)** : Garantit que la compromission d'une clé n'affecte pas les sessions passées
* **Mode d'authentification** : Clé pré-partagée, certificats, etc.

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Bonnes pratiques de sécurité VPN</h4>
<p>Privilégiez les algorithmes de chiffrement forts (AES-256), les algorithmes d'intégrité robustes (SHA-256 ou supérieur), les groupes DH élevés (14 ou supérieur), et activez le Perfect Forward Secrecy. Pour une sécurité maximale, utilisez l'authentification par certificat plutôt que par clé pré-partagée.</p>
</div>

<h2 id="ipsec-vpn" style="color:#0D274D;">5.2 IPsec VPN Site-to-Site</h2>

Les VPNs IPsec site-à-site permettent de connecter de manière sécurisée deux ou plusieurs réseaux distants, comme si ces réseaux étaient directement connectés.

### Configuration d'un VPN IPsec site-à-site

Pour configurer un VPN IPsec site-à-site via l'interface web :

1. Accédez à **VPN > IPsec Wizard**
2. Sélectionnez **Site to Site**
3. Configurez les paramètres de la **Phase 1** :
   * **Name** : Nom du tunnel
   * **Template Type** : Custom
   * **Remote Device** : FortiGate ou autre appareil
   * **Authentication Method** : Pre-shared Key ou Certificate
   * **Pre-shared Key** : Clé partagée (si cette méthode est choisie)
   * **Outgoing Interface** : Interface connectée à Internet
   * **Remote Gateway** : Adresse IP publique du site distant
   * **IKE Version** : IKEv1 ou IKEv2
   * **Mode** : Main (plus sécurisé) ou Aggressive (plus rapide)
   * **Proposal** : Algorithmes de chiffrement et d'intégrité
   * **Diffie-Hellman Group** : Groupe pour l'échange de clés
   * **Key Lifetime** : Durée de vie de la clé
4. Configurez les paramètres de la **Phase 2** :
   * **Name** : Nom de la phase 2
   * **Proposal** : Algorithmes de chiffrement et d'intégrité
   * **Diffie-Hellman Group** : Groupe pour PFS (si activé)
   * **Key Lifetime** : Durée de vie de la clé
5. Configurez les paramètres réseau :
   * **Local Address** : Réseau local derrière ce FortiGate
   * **Remote Address** : Réseau distant derrière le FortiGate distant
6. Cliquez sur **OK** pour créer le VPN

Exemple de configuration CLI pour un VPN IPsec site-à-site :

```
config vpn ipsec phase1-interface
    edit "Site_B_VPN"
        set interface "wan1"
        set ike-version 2
        set peertype any
        set net-device disable
        set proposal aes256-sha256
        set dhgrp 14
        set remote-gw 203.0.113.2
        set psksecret "SecurePreSharedKey123!"
    next
end

config vpn ipsec phase2-interface
    edit "Site_B_VPN_P2"
        set phase1name "Site_B_VPN"
        set proposal aes256-sha256
        set dhgrp 14
        set pfs enable
        set src-addr-type subnet
        set dst-addr-type subnet
        set src-subnet 192.168.1.0 255.255.255.0
        set dst-subnet 192.168.2.0 255.255.255.0
    next
end
```

### Politiques de pare-feu pour VPN

Pour permettre le trafic à travers le VPN, vous devez créer des politiques de pare-feu :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Créez une politique pour le trafic sortant vers le VPN :
   * **Name** : Nom descriptif
   * **Incoming Interface** : Interface interne
   * **Outgoing Interface** : Interface virtuelle du VPN
   * **Source** : Réseau local
   * **Destination** : Réseau distant
   * **Service** : Services autorisés
   * **Action** : Accept
3. Créez une politique pour le trafic entrant depuis le VPN :
   * **Name** : Nom descriptif
   * **Incoming Interface** : Interface virtuelle du VPN
   * **Outgoing Interface** : Interface interne
   * **Source** : Réseau distant
   * **Destination** : Réseau local
   * **Service** : Services autorisés
   * **Action** : Accept

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Sécurité des politiques VPN</h4>
<p>N'autorisez que le trafic nécessaire à travers le VPN. Évitez les politiques trop permissives (comme "any" pour la source, la destination ou les services). Spécifiez précisément les réseaux et services qui doivent communiquer à travers le VPN.</p>
</div>

### Routage pour VPN

Pour que le trafic soit correctement dirigé vers le VPN, vous devez configurer le routage :

1. Accédez à **Network > Static Routes**
2. Créez une route statique vers le réseau distant via l'interface VPN :
   * **Destination** : Réseau distant
   * **Interface** : Interface virtuelle du VPN
   * **Gateway** : Laissez vide pour les VPNs
   * **Distance** : Valeur de distance administrative

Alternativement, vous pouvez activer l'option "Add Route" dans la configuration de la phase 2 pour que FortiGate crée automatiquement la route.

<h2 id="ipsec-dialup" style="color:#0D274D;">5.3 IPsec VPN Dial-up (accès distant)</h2>

Les VPNs IPsec dial-up permettent aux utilisateurs distants de se connecter au réseau d'entreprise de manière sécurisée à l'aide d'un client VPN.

### Configuration d'un VPN IPsec dial-up

Pour configurer un VPN IPsec dial-up via l'interface web :

1. Accédez à **VPN > IPsec Wizard**
2. Sélectionnez **Remote Access**
3. Configurez les paramètres de la **Phase 1** :
   * **Name** : Nom du tunnel
   * **Template Type** : Custom
   * **Remote Device** : Client FortiClient ou autre client
   * **Authentication Method** : Pre-shared Key ou Certificate
   * **Pre-shared Key** : Clé partagée (si cette méthode est choisie)
   * **Outgoing Interface** : Interface connectée à Internet
   * **IKE Version** : IKEv1 ou IKEv2
   * **Mode** : Aggressive (généralement pour dial-up)
   * **Proposal** : Algorithmes de chiffrement et d'intégrité
   * **Diffie-Hellman Group** : Groupe pour l'échange de clés
   * **Key Lifetime** : Durée de vie de la clé
4. Configurez les paramètres de la **Phase 2** :
   * **Name** : Nom de la phase 2
   * **Proposal** : Algorithmes de chiffrement et d'intégrité
   * **Diffie-Hellman Group** : Groupe pour PFS (si activé)
   * **Key Lifetime** : Durée de vie de la clé
5. Configurez les paramètres réseau :
   * **Local Address** : Réseau local derrière ce FortiGate
   * **Client Address Range** : Plage d'adresses IP à attribuer aux clients
   * **DNS Server** : Serveurs DNS pour les clients
6. Cliquez sur **OK** pour créer le VPN

### Authentification des utilisateurs

Pour les VPNs dial-up, vous pouvez configurer l'authentification des utilisateurs :

1. Accédez à **User & Authentication > User Definition**
2. Créez des comptes utilisateur locaux ou configurez un serveur d'authentification externe (LDAP, RADIUS, etc.)
3. Accédez à **User & Authentication > User Groups**
4. Créez un groupe d'utilisateurs pour le VPN
5. Dans la configuration du VPN, associez ce groupe d'utilisateurs à la phase 1

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Authentification à deux facteurs</h4>
<p>Pour renforcer la sécurité des VPNs dial-up, envisagez d'activer l'authentification à deux facteurs (2FA) en utilisant FortiToken, des tokens TOTP tiers, ou l'authentification par SMS/email.</p>
</div>

### Configuration du client FortiClient

FortiClient est le client VPN officiel de Fortinet. Pour configurer une connexion VPN IPsec dans FortiClient :

1. Ouvrez FortiClient
2. Accédez à la section **Remote Access**
3. Cliquez sur **Add a new connection**
4. Sélectionnez **IPsec VPN**
5. Configurez les paramètres :
   * **Connection Name** : Nom de la connexion
   * **Remote Gateway** : Adresse IP ou FQDN du FortiGate
   * **Authentication Method** : Pre-shared Key ou Certificate
   * **Pre-shared Key** : Clé partagée (si cette méthode est choisie)
   * **Username** : Nom d'utilisateur
   * **Password** : Mot de passe (saisi lors de la connexion)
6. Configurez les paramètres avancés si nécessaire
7. Cliquez sur **Save** pour enregistrer la configuration

<h2 id="ssl-vpn" style="color:#0D274D;">5.4 SSL VPN (tunnel et web mode)</h2>

Le SSL VPN FortiGate offre un accès distant sécurisé via HTTPS, sans nécessiter de client VPN dédié dans certains cas. Il propose deux modes de fonctionnement : le mode web et le mode tunnel.

### Modes SSL VPN

* **Mode web** : Accès aux ressources internes via un portail web, sans client VPN
* **Mode tunnel** : Connexion complète au réseau interne via un client VPN, similaire à IPsec

### Configuration du SSL VPN

Pour configurer le SSL VPN via l'interface web :

1. Accédez à **VPN > SSL-VPN Settings**
2. Configurez les paramètres de base :
   * **Listen on Interface(s)** : Interface(s) sur laquelle le service SSL VPN écoute
   * **Listen on Port** : Port pour le service SSL VPN (généralement 443)
   * **Restrict Access** : Limitation d'accès par adresse IP source (optionnel)
   * **Certificate** : Certificat SSL pour le portail
   * **Authentication Portal** : Apparence du portail d'authentification
3. Configurez les paramètres du **Mode Web** :
   * **Enable Web Mode** : Activer/désactiver le mode web
   * **Portal Message** : Message d'accueil sur le portail
   * **Theme** : Thème visuel du portail
   * **Predefined Bookmarks** : Signets prédéfinis pour les ressources internes
4. Configurez les paramètres du **Mode Tunnel** :
   * **Enable Tunnel Mode** : Activer/désactiver le mode tunnel
   * **Tunnel Mode Client Address Range** : Plage d'adresses IP pour les clients
   * **Tunnel Mode Split Tunneling** : Activation du split tunneling
   * **DNS Server** : Serveurs DNS pour les clients
   * **Idle Timeout** : Délai d'inactivité avant déconnexion
5. Cliquez sur **Apply** pour enregistrer la configuration

Exemple de configuration CLI pour SSL VPN :

```
config vpn ssl settings
    set servercert "Fortinet_Factory"
    set tunnel-ip-pools "SSLVPN_TUNNEL_ADDR1"
    set tunnel-ipv6-pools "SSLVPN_TUNNEL_IPv6_ADDR1"
    set dns-server1 192.168.1.1
    set dns-server2 8.8.8.8
    set port 443
    set source-interface "port1"
    set default-portal "full-access"
    set authentication-rule-name "sslvpn-auth"
end
```

### Portails SSL VPN

Les portails définissent l'expérience utilisateur et les ressources disponibles :

1. Accédez à **VPN > SSL-VPN Portals**
2. Créez ou modifiez un portail
3. Configurez les paramètres :
   * **Name** : Nom du portail
   * **Tunnel Mode** : Paramètres du mode tunnel
   * **Web Mode** : Paramètres du mode web
   * **Bookmarks** : Signets vers les ressources internes
   * **Widget Settings** : Widgets à afficher sur le portail

### Politiques de pare-feu pour SSL VPN

Pour permettre l'accès via SSL VPN, vous devez créer des politiques de pare-feu :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Créez une politique pour l'accès au portail SSL VPN :
   * **Name** : Nom descriptif
   * **Incoming Interface** : Interface externe
   * **Outgoing Interface** : Interface SSL VPN
   * **Source** : all ou adresses IP spécifiques
   * **Source Address** : all ou adresses IP spécifiques
   * **Destination** : all
   * **Service** : HTTPS (pour le portail) ou ALL
   * **Action** : Accept
   * **SSL VPN Authentication** : Activez et sélectionnez le portail et les groupes d'utilisateurs
3. Créez une politique pour l'accès aux ressources internes :
   * **Name** : Nom descriptif
   * **Incoming Interface** : Interface SSL VPN
   * **Outgoing Interface** : Interface interne
   * **Source** : Adresses IP des clients SSL VPN
   * **Destination** : Ressources internes
   * **Service** : Services autorisés
   * **Action** : Accept

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Bonnes pratiques SSL VPN</h4>
<p>Utilisez un certificat SSL valide pour le portail SSL VPN afin d'éviter les avertissements de sécurité dans les navigateurs des utilisateurs. Configurez des portails différents pour différents groupes d'utilisateurs afin de limiter l'accès aux ressources selon les besoins.</p>
</div>

<h2 id="vpn-avances" style="color:#0D274D;">5.5 Configurations VPN avancées</h2>

Cette section couvre les configurations VPN avancées pour répondre à des besoins spécifiques ou améliorer les déploiements existants.

### ADVPN (Auto-Discovery VPN)

ADVPN permet la création dynamique de tunnels directs entre sites distants, optimisant ainsi le routage du trafic dans les topologies hub-and-spoke :

1. Configurez un VPN IPsec standard sur le hub
2. Sur le hub, activez l'option **auto-discovery-sender**
3. Sur les spokes, activez l'option **auto-discovery-receiver**
4. Configurez le routage dynamique (BGP ou OSPF) sur tous les sites
5. Lorsque deux spokes ont besoin de communiquer, un tunnel direct est automatiquement établi

Exemple de configuration CLI pour ADVPN :

```
# Configuration du hub
config vpn ipsec phase1-interface
    edit "Hub_VPN"
        set type dynamic
        set interface "wan1"
        set ike-version 2
        set peertype any
        set net-device enable
        set auto-discovery-sender enable
        set tunnel-search nexthop
        set proposal aes256-sha256
        set dhgrp 14
        set psksecret "SecurePreSharedKey123!"
    next
end

# Configuration d'un spoke
config vpn ipsec phase1-interface
    edit "Spoke_to_Hub"
        set interface "wan1"
        set ike-version 2
        set peertype any
        set net-device enable
        set auto-discovery-receiver enable
        set proposal aes256-sha256
        set dhgrp 14
        set remote-gw 203.0.113.1
        set psksecret "SecurePreSharedKey123!"
    next
end
```

### VPN redondants

Pour assurer la haute disponibilité des connexions VPN, vous pouvez configurer des tunnels redondants :

1. Créez plusieurs tunnels VPN entre les mêmes sites, via différentes interfaces ou passerelles
2. Configurez le routage avec des métriques différentes pour définir les priorités
3. Utilisez le health monitoring pour détecter les défaillances de tunnel
4. Configurez le basculement automatique en cas de panne

Exemple de configuration CLI pour des VPNs redondants :

```
# Premier tunnel (principal)
config vpn ipsec phase1-interface
    edit "Site_B_Primary"
        set interface "wan1"
        set remote-gw 203.0.113.2
        # autres paramètres...
    next
end

# Second tunnel (secondaire)
config vpn ipsec phase1-interface
    edit "Site_B_Secondary"
        set interface "wan2"
        set remote-gw 198.51.100.2
        # autres paramètres...
    next
end

# Routes avec priorités différentes
config router static
    edit 1
        set dst 192.168.2.0 255.255.255.0
        set device "Site_B_Primary"
        set distance 10
    next
    edit 2
        set dst 192.168.2.0 255.255.255.0
        set device "Site_B_Secondary"
        set distance 20
    next
end
```

### VPN avec authentification par certificat

L'authentification par certificat offre une sécurité supérieure à celle des clés pré-partagées :

1. Configurez une infrastructure à clés publiques (PKI) :
   * Importez un certificat CA racine
   * Générez ou importez des certificats pour chaque FortiGate
2. Configurez le VPN pour utiliser l'authentification par certificat :
   * Sélectionnez **Certificate** comme méthode d'authentification
   * Spécifiez le certificat local à utiliser
   * Configurez les paramètres de vérification du certificat distant

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Avantages des certificats</h4>
<p>L'authentification par certificat offre plusieurs avantages : révocation possible des certificats compromis, rotation plus facile des identifiants, et possibilité d'intégration avec une PKI d'entreprise existante.</p>
</div>

### Mode XAuth pour IPsec

XAuth (Extended Authentication) ajoute une couche d'authentification utilisateur aux VPNs IPsec :

1. Configurez un VPN IPsec standard
2. Activez XAuth dans la configuration de la phase 1
3. Configurez le mode XAuth (client ou serveur)
4. Spécifiez le groupe d'utilisateurs pour l'authentification

Exemple de configuration CLI pour XAuth :

```
config vpn ipsec phase1-interface
    edit "Dialup_VPN"
        # paramètres standard...
        set xauthtype auto
        set authusrgrp "VPN_Users"
    next
end
```

### Split tunneling

Le split tunneling permet de diriger seulement certains trafics à travers le VPN, tandis que les autres trafics passent directement par la connexion Internet locale :

1. Pour IPsec, configurez les réseaux spécifiques dans la phase 2
2. Pour SSL VPN, activez le split tunneling et spécifiez les routes :
   * Accédez à **VPN > SSL-VPN Settings**
   * Activez **Enable Split Tunneling**
   * Configurez les **Routing Address** pour spécifier les réseaux accessibles via le VPN

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Considérations de sécurité</h4>
<p>Le split tunneling peut introduire des risques de sécurité, car l'appareil client est simultanément connecté au réseau d'entreprise et à Internet. Évaluez soigneusement ces risques avant d'activer cette fonctionnalité.</p>
</div>

<h2 id="vpn-troubleshooting" style="color:#0D274D;">5.6 Dépannage des VPNs</h2>

Le dépannage des VPNs est une compétence essentielle pour maintenir des connexions fiables et sécurisées. Cette section présente les outils et méthodes pour diagnostiquer et résoudre les problèmes VPN courants.

### Outils de diagnostic VPN

FortiGate offre plusieurs outils pour diagnostiquer les problèmes VPN :

#### 1. Vérification de l'état du VPN

Pour vérifier l'état des tunnels VPN via l'interface web :

1. Accédez à **Monitor > IPsec Monitor** pour les VPNs IPsec
2. Accédez à **Monitor > SSL-VPN Monitor** pour les VPNs SSL

Pour vérifier l'état via la CLI :

```
# Pour IPsec
diagnose vpn ike gateway list
diagnose vpn tunnel list

# Pour SSL VPN
diagnose vpn ssl list
```

#### 2. Capture de paquets

La capture de paquets permet d'analyser le trafic VPN :

```
# Capture des paquets IKE
diagnose sniffer packet any "host 203.0.113.2 and port 500" 4 0 a

# Capture des paquets ESP
diagnose sniffer packet any "host 203.0.113.2 and esp" 4 0 a

# Capture des paquets SSL VPN
diagnose sniffer packet any "host 203.0.113.2 and port 443" 4 0 a
```

#### 3. Journaux de débogage

Les journaux de débogage fournissent des informations détaillées sur les négociations VPN :

```
# Débogage IKE
diagnose debug application ike -1
diagnose debug enable

# Débogage SSL VPN
diagnose debug application sslvpn -1
diagnose debug enable

# Désactiver le débogage après utilisation
diagnose debug disable
```

### Problèmes courants et solutions

#### 1. Échec de la phase 1 (IPsec)

Causes possibles et solutions :

* **Paramètres incompatibles** : Vérifiez que les paramètres IKE (version, mode, proposition, groupe DH) correspondent des deux côtés
* **Problème d'authentification** : Vérifiez la clé pré-partagée ou les certificats
* **Problème de connectivité** : Vérifiez que les ports UDP 500 et 4500 sont ouverts
* **NAT traversal** : Activez NAT-T si l'un des pairs est derrière un NAT

#### 2. Échec de la phase 2 (IPsec)

Causes possibles et solutions :

* **Paramètres incompatibles** : Vérifiez que les propositions de chiffrement correspondent
* **Problème de réseaux** : Vérifiez que les réseaux locaux et distants sont correctement définis
* **PFS** : Assurez-vous que le paramètre PFS est cohérent des deux côtés

#### 3. Le tunnel s'établit mais pas de trafic

Causes possibles et solutions :

* **Politiques de pare-feu manquantes** : Vérifiez les politiques des deux côtés
* **Problème de routage** : Vérifiez les routes statiques ou dynamiques
* **MTU/fragmentation** : Ajustez la MTU ou activez la fragmentation
* **Proxy IDs incompatibles** : Vérifiez que les réseaux de phase 2 correspondent

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Approche méthodique</h4>
<p>Adoptez une approche méthodique pour le dépannage VPN : vérifiez d'abord la connectivité de base, puis la négociation de la phase 1, puis la phase 2, et enfin les politiques et le routage. Isolez chaque composant pour identifier précisément la source du problème.</p>
</div>

#### 4. Problèmes de SSL VPN

Causes possibles et solutions :

* **Problème de certificat** : Vérifiez la validité et la chaîne de confiance du certificat
* **Problème d'authentification** : Vérifiez les paramètres d'authentification et les comptes utilisateur
* **Problème de routage** : Vérifiez les routes et le split tunneling
* **Problème de politique** : Vérifiez les politiques de pare-feu pour l'accès au portail et aux ressources internes

### Commandes de dépannage avancées

Voici quelques commandes CLI avancées pour le dépannage VPN :

```
# Vérifier les SAs IKE
diagnose vpn ike gateway list name <phase1_name>

# Vérifier les SAs IPsec
diagnose vpn tunnel list name <phase2_name>

# Effacer les SAs pour forcer une renégociation
diagnose vpn tunnel flush name <phase1_name>

# Vérifier les routes
get router info routing-table all

# Vérifier les politiques actives
diagnose firewall policy list

# Vérifier les sessions actives
diagnose sys session list

# Vérifier les statistiques SSL VPN
get vpn ssl monitor
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Documentation des configurations</h4>
<p>Documentez soigneusement vos configurations VPN, y compris tous les paramètres des deux côtés. Cette documentation est inestimable lors du dépannage et facilite la communication avec le support technique si nécessaire.</p>
</div>

---

<h1 id="utm" style="color:#E23237;">6. Fonctionnalités UTM (Unified Threat Management)</h1>

<h2 id="utm-overview" style="color:#0D274D;">6.1 Vue d'ensemble des fonctionnalités UTM</h2>

L'Unified Threat Management (UTM) est un ensemble de fonctionnalités de sécurité intégrées qui permettent de protéger le réseau contre diverses menaces. Cette section présente une vue d'ensemble des capacités UTM de FortiGate.

### Concept d'UTM

L'UTM regroupe plusieurs technologies de sécurité dans une solution unifiée :

* Protection contre les logiciels malveillants (antivirus)
* Filtrage de contenu web
* Contrôle d'applications
* Prévention d'intrusion
* Filtrage d'emails
* Prévention de fuite de données (DLP)
* Inspection SSL/TLS

Cette approche intégrée offre plusieurs avantages :

* Gestion centralisée des politiques de sécurité
* Visibilité unifiée sur les menaces
* Réduction de la complexité opérationnelle
* Corrélation des événements de sécurité
* Performance optimisée par rapport à des solutions distinctes

### Profils de sécurité

Les fonctionnalités UTM sont configurées via des profils de sécurité, qui sont ensuite appliqués aux politiques de pare-feu :

1. Vous créez et configurez des profils pour chaque type de protection (antivirus, filtrage web, etc.)
2. Vous appliquez ces profils aux politiques de pare-feu pertinentes
3. Le trafic correspondant à ces politiques est inspecté selon les profils configurés

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Mode d'inspection</h4>
<p>FortiGate propose deux modes d'inspection pour les profils de sécurité : le mode proxy et le mode flux (flow). Le mode proxy offre une inspection plus approfondie mais peut avoir un impact sur les performances, tandis que le mode flux privilégie les performances avec une inspection légèrement moins détaillée.</p>
</div>

### Services FortiGuard

Les fonctionnalités UTM s'appuient sur les services FortiGuard pour obtenir des informations à jour sur les menaces :

* **Antivirus** : Signatures de malwares et détection heuristique
* **Web Filtering** : Base de données de catégorisation d'URLs
* **Application Control** : Signatures d'applications
* **IPS** : Signatures d'attaques et vulnérabilités
* **IP Reputation** : Listes d'adresses IP malveillantes
* **Spam Filtering** : Filtres anti-spam et listes noires

Ces services sont mis à jour régulièrement via des abonnements FortiGuard.

### Impact sur les performances

L'activation des fonctionnalités UTM peut avoir un impact sur les performances du FortiGate :

* Chaque fonctionnalité activée consomme des ressources supplémentaires
* L'inspection SSL a généralement l'impact le plus important
* Les modèles FortiGate plus puissants peuvent gérer plus de fonctionnalités UTM simultanément
* Les processeurs de sécurité dédiés (SPU) accélèrent certaines fonctions UTM

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Approche progressive</h4>
<p>Adoptez une approche progressive pour l'activation des fonctionnalités UTM. Commencez par les protections les plus essentielles pour votre environnement, surveillez l'impact sur les performances, puis activez progressivement d'autres fonctionnalités selon vos besoins et les capacités de votre appareil.</p>
</div>

<h2 id="antivirus" style="color:#0D274D;">6.2 Antivirus</h2>

La protection antivirus FortiGate analyse le trafic réseau pour détecter et bloquer les logiciels malveillants avant qu'ils n'atteignent les systèmes d'extrémité.

### Types de protection antivirus

FortiGate propose plusieurs méthodes de détection des malwares :

* **Analyse basée sur les signatures** : Détection des malwares connus via des signatures FortiGuard
* **Analyse heuristique** : Détection des malwares inconnus basée sur leur comportement
* **Machine learning** : Utilisation d'algorithmes d'apprentissage automatique pour identifier les menaces
* **Analyse de fichiers dans le cloud** : Soumission de fichiers suspects à FortiSandbox pour analyse approfondie

### Configuration d'un profil antivirus

Pour configurer un profil antivirus via l'interface web :

1. Accédez à **Security Profiles > AntiVirus**
2. Cliquez sur **Create New** ou modifiez un profil existant
3. Configurez les paramètres de base :
   * **Name** : Nom du profil
   * **Inspection Mode** : Proxy ou Flow
   * **Feature Set** : Extended ou Standard
4. Configurez les options pour chaque protocole (HTTP, FTP, IMAP, POP3, SMTP, etc.) :
   * **Virus Scan** : Activer/désactiver l'analyse antivirus
   * **Block Malicious URLs** : Bloquer les URLs malveillantes (pour HTTP)
   * **Scan Outgoing Connections** : Analyser les connexions sortantes
   * **Quarantine** : Options de mise en quarantaine
5. Configurez les options avancées si nécessaire
6. Cliquez sur **OK** pour enregistrer le profil

Exemple de configuration CLI pour un profil antivirus :

```
config antivirus profile
    edit "default"
        set comment "Default antivirus profile"
        config http
            set av-scan enable
            set outbreak-prevention enable
            set content-disarm enable
        end
        config ftp
            set av-scan enable
            set outbreak-prevention enable
        end
        config imap
            set av-scan enable
            set outbreak-prevention enable
            set executables block
        end
        config pop3
            set av-scan enable
            set outbreak-prevention enable
            set executables block
        end
        config smtp
            set av-scan enable
            set outbreak-prevention enable
            set executables block
        end
        config mapi
            set av-scan enable
            set outbreak-prevention enable
        end
    next
end
```

### Application du profil antivirus

Pour appliquer un profil antivirus à une politique de pare-feu :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Créez ou modifiez une politique
3. Dans la section **Security Profiles**, activez **AntiVirus** et sélectionnez le profil
4. Cliquez sur **OK** pour enregistrer la politique

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Limites de taille</h4>
<p>Par défaut, FortiGate limite la taille des fichiers analysés (généralement à 10-45 Mo selon le modèle). Les fichiers dépassant cette limite ne seront pas analysés. Vous pouvez ajuster cette limite, mais cela peut affecter les performances.</p>
</div>

### Quarantaine et journalisation

FortiGate peut mettre en quarantaine les fichiers infectés et journaliser les détections :

1. Pour configurer la quarantaine :
   * Accédez à **Security Profiles > AntiVirus**
   * Dans les options avancées, configurez les paramètres de quarantaine
   * Spécifiez la durée de quarantaine et les options de notification

2. Pour consulter les journaux antivirus :
   * Accédez à **Log & Report > AntiVirus**
   * Filtrez les journaux selon vos besoins
   * Analysez les détections pour identifier les tendances ou les systèmes compromis

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Complémentarité des protections</h4>
<p>L'antivirus FortiGate est conçu comme une couche de protection complémentaire, et non comme un remplacement des solutions antivirus sur les postes clients. Une approche de défense en profondeur, combinant protection réseau et protection des terminaux, offre la meilleure sécurité.</p>
</div>

<h2 id="web-filter" style="color:#0D274D;">6.3 Filtrage Web</h2>

Le filtrage web permet de contrôler l'accès aux sites web en fonction de diverses catégories, d'URLs spécifiques ou de contenus, protégeant ainsi les utilisateurs contre les sites malveillants et appliquant les politiques d'utilisation acceptable.

### Méthodes de filtrage web

FortiGate propose plusieurs méthodes de filtrage web :

* **Filtrage par catégorie** : Blocage basé sur les catégories de sites web FortiGuard
* **Filtrage par URL** : Blocage ou autorisation d'URLs spécifiques
* **Filtrage par mot-clé** : Blocage basé sur des mots-clés dans les URLs ou le contenu
* **Filtrage basé sur le contenu** : Analyse du contenu des pages web
* **Filtrage par réputation web** : Évaluation de la réputation des sites web

### Configuration d'un profil de filtrage web

Pour configurer un profil de filtrage web via l'interface web :

1. Accédez à **Security Profiles > Web Filter**
2. Cliquez sur **Create New** ou modifiez un profil existant
3. Configurez les paramètres de base :
   * **Name** : Nom du profil
   * **Inspection Mode** : Proxy ou Flow
   * **Options** : Options générales comme le filtrage HTTPS
4. Configurez le **FortiGuard Category Based Filter** :
   * Sélectionnez l'action (Allow, Block, Monitor, Warning, Authenticate) pour chaque catégorie
   * Regroupez les catégories par thème (Adult, Security Risk, General Interest, etc.)
5. Configurez les **URL Filter** :
   * Ajoutez des URLs spécifiques à bloquer ou autoriser
   * Utilisez des caractères génériques si nécessaire
6. Configurez les **Web Content Filter** :
   * Ajoutez des mots-clés à bloquer dans les URLs ou le contenu
7. Configurez les options avancées si nécessaire
8. Cliquez sur **OK** pour enregistrer le profil

Exemple de configuration CLI pour un profil de filtrage web :

```
config webfilter profile
    edit "default"
        set comment "Default web filter profile"
        config ftgd-wf
            set options https-scan
            config filters
                edit 1
                    set category 2
                    set action block
                next
                edit 2
                    set category 7
                    set action block
                next
                # autres catégories...
            end
        end
        config web
            set whitelist enable
            config entries
                edit 1
                    set url "example.com"
                    set type wildcard
                    set action allow
                next
                edit 2
                    set url "badsite.com"
                    set type wildcard
                    set action block
                next
            end
        end
    next
end
```

### Application du profil de filtrage web

Pour appliquer un profil de filtrage web à une politique de pare-feu :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Créez ou modifiez une politique
3. Dans la section **Security Profiles**, activez **Web Filter** et sélectionnez le profil
4. Cliquez sur **OK** pour enregistrer la politique

### Authentification web et override

FortiGate permet de configurer l'authentification pour certaines catégories web et d'autoriser les utilisateurs à outrepasser temporairement les restrictions :

1. Dans le profil de filtrage web, sélectionnez **Authenticate** comme action pour certaines catégories
2. Configurez les paramètres d'override :
   * Accédez à **Authentication > Web Auth**
   * Configurez les groupes autorisés à effectuer des overrides
   * Définissez la durée de validité des overrides

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Listes blanches et noires</h4>
<p>Utilisez judicieusement les listes blanches (URLs autorisées) et noires (URLs bloquées) pour affiner le filtrage basé sur les catégories. Les entrées spécifiques dans ces listes ont priorité sur les catégories générales, ce qui permet d'autoriser des sites spécifiques dans une catégorie bloquée ou de bloquer des sites spécifiques dans une catégorie autorisée.</p>
</div>

### Journalisation et rapports

Le filtrage web génère des journaux détaillés qui peuvent être utilisés pour surveiller l'activité web :

1. Accédez à **Log & Report > Web Filter**
2. Filtrez les journaux selon vos besoins
3. Analysez les tentatives d'accès bloquées et les sites visités
4. Créez des rapports personnalisés pour suivre l'utilisation web

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Filtrage HTTPS</h4>
<p>Pour filtrer efficacement le trafic HTTPS, vous devez activer l'inspection SSL. Sans inspection SSL, le filtrage web ne peut se baser que sur le nom de domaine (SNI) et non sur le contenu complet des pages HTTPS.</p>
</div>

<h2 id="dns-filter" style="color:#0D274D;">6.4 Filtrage DNS</h2>

Le filtrage DNS bloque l'accès aux domaines malveillants au niveau des requêtes DNS, offrant une couche de protection supplémentaire et complémentaire au filtrage web.

### Fonctionnement du filtrage DNS

Le filtrage DNS intercepte les requêtes DNS et les compare à diverses listes :

* Base de données de catégories de domaines FortiGuard
* Listes de domaines malveillants connus
* Listes personnalisées de domaines autorisés ou bloqués

Si un domaine est identifié comme malveillant ou appartient à une catégorie bloquée, FortiGate peut :
* Bloquer la requête DNS
* Rediriger la requête vers une page de blocage
* Journaliser l'événement

### Configuration d'un profil de filtrage DNS

Pour configurer un profil de filtrage DNS via l'interface web :

1. Accédez à **Security Profiles > DNS Filter**
2. Cliquez sur **Create New** ou modifiez un profil existant
3. Configurez les paramètres de base :
   * **Name** : Nom du profil
   * **Comment** : Description optionnelle
4. Configurez les **FortiGuard Category Based Filter** :
   * Sélectionnez l'action (Allow, Block, Monitor) pour chaque catégorie
5. Configurez les **Domain Filter** :
   * Ajoutez des domaines spécifiques à bloquer ou autoriser
6. Configurez les options avancées si nécessaire
7. Cliquez sur **OK** pour enregistrer le profil

Exemple de configuration CLI pour un profil de filtrage DNS :

```
config dnsfilter profile
    edit "default"
        set comment "Default DNS filter profile"
        config ftgd-dns
            set options error-allow
            config filters
                edit 1
                    set category 26
                    set action block
                next
                edit 2
                    set category 61
                    set action block
                next
                # autres catégories...
            end
        end
        config domain-filter
            set domain-filter-table 1
        end
    next
end
```

### Application du profil de filtrage DNS

Pour appliquer un profil de filtrage DNS à une politique de pare-feu :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Créez ou modifiez une politique
3. Dans la section **Security Profiles**, activez **DNS Filter** et sélectionnez le profil
4. Cliquez sur **OK** pour enregistrer la politique

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Complémentarité avec le filtrage web</h4>
<p>Le filtrage DNS est complémentaire au filtrage web et non un remplacement. Le filtrage DNS est plus léger en termes de ressources et peut bloquer les connexions malveillantes avant même qu'elles ne soient établies, tandis que le filtrage web offre un contrôle plus granulaire du contenu.</p>
</div>

### DNS over HTTPS (DoH) et DNS over TLS (DoT)

Les protocoles DoH et DoT chiffrent les requêtes DNS, ce qui peut contourner le filtrage DNS traditionnel. FortiGate propose des options pour gérer ces protocoles :

1. Bloquer les serveurs DoH/DoT connus
2. Rediriger les requêtes DNS vers un serveur contrôlé
3. Inspecter le trafic HTTPS pour détecter les requêtes DoH

Pour configurer ces options :

1. Accédez à **Security Profiles > DNS Filter**
2. Dans les options avancées, configurez les paramètres relatifs à DoH/DoT
3. Assurez-vous que l'inspection SSL est activée pour détecter le trafic DoH

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Proxy DNS</h4>
<p>Pour un filtrage DNS plus efficace, envisagez de configurer FortiGate comme proxy DNS pour votre réseau. Cela garantit que toutes les requêtes DNS passent par FortiGate et sont soumises au filtrage.</p>
</div>

<h2 id="app-control" style="color:#0D274D;">6.5 Contrôle d'application</h2>

Le contrôle d'application permet d'identifier et de gérer les applications réseau indépendamment des ports ou protocoles utilisés, offrant un contrôle granulaire sur les applications autorisées dans votre réseau.

### Fonctionnement du contrôle d'application

Le contrôle d'application utilise l'inspection approfondie des paquets (DPI) pour identifier les applications en analysant :

* Les signatures d'applications
* Les modèles de trafic
* Les comportements réseau
* Les certificats et métadonnées

FortiGate peut identifier des milliers d'applications différentes, regroupées en catégories comme :

* Réseaux sociaux
* Messagerie instantanée
* Partage de fichiers P2P
* Applications cloud
* Streaming vidéo/audio
* Jeux en ligne
* Applications d'entreprise

### Configuration d'un profil de contrôle d'application

Pour configurer un profil de contrôle d'application via l'interface web :

1. Accédez à **Security Profiles > Application Control**
2. Cliquez sur **Create New** ou modifiez un profil existant
3. Configurez les paramètres de base :
   * **Name** : Nom du profil
   * **Comment** : Description optionnelle
4. Configurez les **Application and Filter Overrides** :
   * Recherchez des applications spécifiques ou parcourez les catégories
   * Définissez l'action pour chaque application ou catégorie (Allow, Block, Monitor)
   * Configurez des quotas de trafic si nécessaire
5. Configurez les options avancées si nécessaire
6. Cliquez sur **OK** pour enregistrer le profil

Exemple de configuration CLI pour un profil de contrôle d'application :

```
config application list
    edit "default"
        set comment "Default application control profile"
        config entries
            edit 1
                set category 15
                set action block
            next
            edit 2
                set application 327
                set action block
            next
            edit 3
                set category 23
                set action pass
            next
            # autres applications/catégories...
        end
    next
end
```

### Application du profil de contrôle d'application

Pour appliquer un profil de contrôle d'application à une politique de pare-feu :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Créez ou modifiez une politique
3. Dans la section **Security Profiles**, activez **Application Control** et sélectionnez le profil
4. Cliquez sur **OK** pour enregistrer la politique

### Contrôle granulaire des applications

Le contrôle d'application permet une gestion très fine des applications :

* **Contrôle par fonction** : Autoriser certaines fonctions d'une application tout en en bloquant d'autres (par exemple, autoriser la messagerie Facebook mais bloquer les jeux Facebook)
* **Contrôle par comportement** : Bloquer les comportements à risque comme le transfert de fichiers dans les applications de messagerie
* **Contrôle par utilisateur/groupe** : Appliquer différentes règles selon les utilisateurs ou groupes
* **Quotas de bande passante** : Limiter la bande passante utilisée par certaines applications

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Applications chiffrées</h4>
<p>Pour contrôler efficacement les applications utilisant du trafic chiffré (comme la plupart des applications modernes), l'inspection SSL doit être activée. Sans inspection SSL, le contrôle d'application aura une efficacité limitée sur le trafic chiffré.</p>
</div>

### Journalisation et surveillance

Le contrôle d'application génère des journaux détaillés sur l'utilisation des applications :

1. Accédez à **Log & Report > Application Control**
2. Filtrez les journaux selon vos besoins
3. Analysez les applications utilisées et les actions appliquées
4. Utilisez ces informations pour affiner vos politiques de contrôle d'application

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Approche progressive</h4>
<p>Commencez par configurer le contrôle d'application en mode "monitor only" pour comprendre quelles applications sont utilisées dans votre réseau. Analysez les journaux pendant une période représentative, puis configurez progressivement des règles de blocage ou de limitation en fonction de vos politiques de sécurité et des besoins métier.</p>
</div>

<h2 id="ips" style="color:#0D274D;">6.6 Système de prévention d'intrusion (IPS)</h2>

Le système de prévention d'intrusion (IPS) surveille le trafic réseau pour détecter et bloquer les tentatives d'exploitation de vulnérabilités et autres activités malveillantes.

### Fonctionnement de l'IPS

L'IPS FortiGate analyse le trafic réseau en utilisant plusieurs méthodes :

* **Détection basée sur les signatures** : Identification des attaques connues via des signatures FortiGuard
* **Détection d'anomalies** : Identification des comportements anormaux
* **Détection basée sur la réputation** : Blocage basé sur la réputation des adresses IP
* **Protection contre les attaques par déni de service** : Détection et atténuation des attaques DoS/DDoS

### Configuration d'un profil IPS

Pour configurer un profil IPS via l'interface web :

1. Accédez à **Security Profiles > Intrusion Prevention**
2. Cliquez sur **Create New** ou modifiez un profil existant
3. Configurez les paramètres de base :
   * **Name** : Nom du profil
   * **Comment** : Description optionnelle
4. Configurez les **IPS Signatures** :
   * Recherchez des signatures spécifiques ou parcourez les catégories
   * Filtrez par sévérité, cible, OS, protocole, etc.
   * Définissez l'action pour chaque signature (Pass, Block, Default, Reset)
5. Configurez les **IPS Filters** pour créer des ensembles de signatures basés sur des critères
6. Configurez les options avancées si nécessaire
7. Cliquez sur **OK** pour enregistrer le profil

Exemple de configuration CLI pour un profil IPS :

```
config ips sensor
    edit "default"
        set comment "Default IPS profile"
        config entries
            edit 1
                set severity high
                set status enable
                set action block
            next
            edit 2
                set severity medium
                set status enable
                set action block
            next
            edit 3
                set severity low
                set status enable
                set action pass
            next
            edit 4
                set severity info
                set status enable
                set action pass
            next
        end
    next
end
```

### Application du profil IPS

Pour appliquer un profil IPS à une politique de pare-feu :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Créez ou modifiez une politique
3. Dans la section **Security Profiles**, activez **IPS** et sélectionnez le profil
4. Cliquez sur **OK** pour enregistrer la politique

### Personnalisation des signatures IPS

FortiGate permet de créer des signatures IPS personnalisées pour des besoins spécifiques :

1. Accédez à **Security Profiles > Intrusion Prevention > Custom Signature**
2. Cliquez sur **Create New**
3. Configurez les paramètres :
   * **Name** : Nom de la signature
   * **Signature** : Code de la signature au format FortiGate
   * **Action** : Action à effectuer lorsque la signature est détectée
4. Cliquez sur **OK** pour enregistrer la signature personnalisée

Exemple de signature personnalisée pour détecter un motif spécifique dans le trafic HTTP :

```
F-SBID(--name "Custom.HTTP.Malicious.Pattern";
--protocol tcp;
--service HTTP;
--pattern "malicious_pattern";
--no_case;
--context uri;
--severity high;)
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Faux positifs</h4>
<p>Les signatures IPS peuvent parfois générer des faux positifs, bloquant du trafic légitime. Surveillez attentivement les journaux IPS après l'activation d'un nouveau profil et ajustez les signatures si nécessaire. Vous pouvez désactiver des signatures spécifiques ou modifier leur action de "block" à "pass" si elles causent des problèmes.</p>
</div>

### Protection contre les attaques DoS

FortiGate inclut des fonctionnalités de protection contre les attaques par déni de service :

1. Accédez à **Policy & Objects > IPv4 DoS Policy**
2. Créez une nouvelle politique DoS
3. Configurez les seuils pour différents types d'attaques DoS
4. Appliquez la politique aux interfaces appropriées

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Optimisation des performances</h4>
<p>Pour optimiser les performances de l'IPS, activez uniquement les signatures pertinentes pour votre environnement. Par exemple, si vous n'avez pas de serveurs Windows, vous pouvez désactiver les signatures spécifiques à Windows. De même, activez les signatures de haute sévérité en priorité, puis ajoutez progressivement des signatures de moindre sévérité selon vos besoins et les capacités de votre appareil.</p>
</div>

<h2 id="file-filter" style="color:#0D274D;">6.7 Filtrage de fichiers</h2>

Le filtrage de fichiers permet de contrôler les types de fichiers qui peuvent être transférés à travers le réseau, offrant une protection supplémentaire contre les menaces et les fuites de données.

### Fonctionnement du filtrage de fichiers

Le filtrage de fichiers examine les fichiers transférés via différents protocoles (HTTP, FTP, SMTP, etc.) et peut :

* Bloquer ou autoriser des fichiers en fonction de leur type
* Bloquer les fichiers dépassant une certaine taille
* Désarmer les contenus potentiellement dangereux (CDR - Content Disarm and Reconstruction)
* Mettre en quarantaine les fichiers suspects

### Configuration du filtrage de fichiers

Le filtrage de fichiers est intégré dans plusieurs profils de sécurité :

#### Dans les profils antivirus

1. Accédez à **Security Profiles > AntiVirus**
2. Créez ou modifiez un profil
3. Pour chaque protocole (HTTP, FTP, etc.), configurez les options de filtrage de fichiers :
   * **File Filter** : Activez le filtrage de fichiers
   * **Select File Types** : Choisissez les types de fichiers à bloquer
   * **Block Files Larger Than** : Définissez une taille maximale

Exemple de configuration CLI pour le filtrage de fichiers dans un profil antivirus :

```
config antivirus profile
    edit "default"
        config http
            set av-scan enable
            set file-filter enable
            config file-type
                edit "executable"
                    set action block
                next
                edit "document"
                    set action log
                next
            end
        end
        config ftp
            set av-scan enable
            set file-filter enable
            config file-type
                edit "executable"
                    set action block
                next
            end
        end
        # autres protocoles...
    next
end
```

#### Dans les profils DLP

1. Accédez à **Security Profiles > Data Leak Prevention**
2. Créez ou modifiez un profil
3. Créez une règle basée sur le type de fichier :
   * **Type** : File Type
   * **File Type** : Sélectionnez les types de fichiers
   * **Action** : Définissez l'action à effectuer

### Content Disarm and Reconstruction (CDR)

La fonctionnalité CDR permet de "désarmer" les fichiers potentiellement dangereux en supprimant les éléments actifs :

1. Accédez à **Security Profiles > AntiVirus**
2. Créez ou modifiez un profil
3. Activez **Content Disarm and Reconstruction**
4. Configurez les options CDR :
   * Types de fichiers à traiter (Office, PDF, etc.)
   * Éléments à supprimer (macros, scripts, etc.)

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Fonctionnement du CDR</h4>
<p>Le CDR fonctionne en reconstruisant les fichiers plutôt qu'en tentant de détecter et supprimer le contenu malveillant. Par exemple, pour un document Word, FortiGate extrait le texte et les images, puis crée un nouveau document sans les macros ou autres éléments actifs potentiellement dangereux.</p>
</div>

### Application du filtrage de fichiers

Pour appliquer le filtrage de fichiers, appliquez le profil antivirus ou DLP configuré à une politique de pare-feu :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Créez ou modifiez une politique
3. Dans la section **Security Profiles**, activez **AntiVirus** et/ou **DLP** et sélectionnez les profils configurés
4. Cliquez sur **OK** pour enregistrer la politique

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Équilibre sécurité/fonctionnalité</h4>
<p>Trouvez un équilibre entre sécurité et fonctionnalité lors de la configuration du filtrage de fichiers. Un filtrage trop restrictif peut perturber les opérations légitimes, tandis qu'un filtrage trop permissif peut laisser passer des menaces. Commencez par bloquer les types de fichiers les plus risqués (exécutables, scripts) et ajustez progressivement selon les besoins de votre organisation.</p>
</div>

<h2 id="email-filter" style="color:#0D274D;">6.8 Filtrage d'emails</h2>

Le filtrage d'emails protège contre les spams, les phishings et les emails malveillants en analysant le trafic SMTP, POP3 et IMAP.

### Fonctionnement du filtrage d'emails

FortiGate peut filtrer les emails de plusieurs façons :

* **Filtrage anti-spam** : Détection des spams via diverses techniques
* **Filtrage antivirus** : Analyse des pièces jointes pour détecter les malwares
* **Filtrage de contenu** : Analyse du contenu des emails pour détecter les phishings ou contenus inappropriés
* **Filtrage d'URL** : Vérification des liens dans les emails

### Configuration du filtrage d'emails

Le filtrage d'emails est configuré via plusieurs profils de sécurité :

#### Profil anti-spam

1. Accédez à **Security Profiles > Anti-Spam**
2. Cliquez sur **Create New** ou modifiez un profil existant
3. Configurez les paramètres pour chaque protocole (SMTP, POP3, IMAP) :
   * **Spam Detection** : Activez la détection de spam
   * **FortiGuard Spam Filtering** : Utilisez la base de données FortiGuard
   * **IP Reputation** : Vérifiez la réputation des serveurs d'envoi
   * **URL Filter** : Vérifiez les URLs dans les emails
   * **Spam Action** : Définissez l'action pour les spams détectés
4. Configurez les listes blanches et noires si nécessaire
5. Cliquez sur **OK** pour enregistrer le profil

Exemple de configuration CLI pour un profil anti-spam :

```
config emailfilter profile
    edit "default"
        set comment "Default anti-spam profile"
        config smtp
            set action tag
            set tag-type subject
            set tag-value "[SPAM] "
        end
        config imap
            set action tag
            set tag-type subject
            set tag-value "[SPAM] "
        end
        config pop3
            set action tag
            set tag-type subject
            set tag-value "[SPAM] "
        end
        config options
            set spam-filtering enable
            set url-check enable
        end
    next
end
```

#### Profil antivirus pour les emails

1. Accédez à **Security Profiles > AntiVirus**
2. Créez ou modifiez un profil
3. Configurez les options pour les protocoles d'email (SMTP, POP3, IMAP) :
   * **Virus Scan** : Activez l'analyse antivirus
   * **Content Disarm** : Activez le désarmement de contenu
   * **Quarantine** : Configurez les options de quarantaine

### Application du filtrage d'emails

Pour appliquer le filtrage d'emails, appliquez les profils configurés à une politique de pare-feu :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Créez ou modifiez une politique qui gère le trafic email
3. Dans la section **Security Profiles**, activez **AntiVirus** et **Anti-Spam** et sélectionnez les profils configurés
4. Cliquez sur **OK** pour enregistrer la politique

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Emails chiffrés</h4>
<p>Le filtrage d'emails a des limitations avec les emails chiffrés. Les emails utilisant TLS pour le transport peuvent être inspectés si l'inspection SSL est activée, mais les emails avec chiffrement de contenu (PGP, S/MIME) ne peuvent pas être analysés en profondeur.</p>
</div>

### Considérations pour le filtrage d'emails

* **Positionnement** : FortiGate peut filtrer les emails en transit, mais n'est généralement pas conçu comme une solution anti-spam principale. Pour une protection complète, envisagez une solution dédiée comme FortiMail.
* **Faux positifs** : Surveillez les faux positifs et ajustez les paramètres ou utilisez des listes blanches si nécessaire.
* **Performance** : Le filtrage d'emails peut être intensif en ressources, surtout avec de gros volumes d'emails ou de nombreuses pièces jointes.

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Approche multi-niveaux</h4>
<p>Pour une protection optimale contre les menaces par email, adoptez une approche multi-niveaux : filtrage au niveau de la passerelle (FortiMail ou solution similaire), filtrage au niveau du pare-feu (FortiGate), et protection au niveau des terminaux (antivirus, sensibilisation des utilisateurs).</p>
</div>

<h2 id="dlp" style="color:#0D274D;">6.9 Prévention de fuite de données (DLP)</h2>

La prévention de fuite de données (Data Leak Prevention - DLP) permet d'identifier et de bloquer la transmission non autorisée d'informations sensibles hors du réseau.

### Fonctionnement du DLP

Le DLP FortiGate analyse le trafic sortant pour détecter les informations sensibles en utilisant plusieurs méthodes :

* **Correspondance de motifs** : Recherche de motifs spécifiques (numéros de carte de crédit, numéros de sécurité sociale, etc.)
* **Empreintes de fichiers** : Détection de fichiers spécifiques basée sur leur empreinte numérique
* **Empreintes de documents** : Détection de contenu sensible dans les documents
* **Filtrage par type de fichier** : Contrôle des types de fichiers pouvant être transmis

### Configuration du DLP

Pour configurer le DLP via l'interface web :

1. Accédez à **Security Profiles > Data Leak Prevention**
2. Cliquez sur **Create New** ou modifiez un profil existant
3. Configurez les règles DLP :
   * Cliquez sur **Create New Rule**
   * Sélectionnez le **Type** de règle (Regular Expression, File Type, File Size, etc.)
   * Configurez les paramètres spécifiques au type de règle
   * Définissez l'**Action** à effectuer (Allow, Log Only, Block, Quarantine)
4. Répétez pour ajouter d'autres règles si nécessaire
5. Cliquez sur **OK** pour enregistrer le profil

Exemple de configuration CLI pour un profil DLP :

```
config dlp sensor
    edit "default"
        set comment "Default DLP sensor"
        config filter
            edit 1
                set name "Credit Card Numbers"
                set type regex
                set pattern "[3-6]\\d{3}[- ]?\\d{4}[- ]?\\d{4}[- ]?\\d{4}"
                set action block
            next
            edit 2
                set name "Block Executables"
                set type file-type
                set file-type 1
                set action block
            next
            edit 3
                set name "Large Files"
                set type file-size
                set file-size 10000
                set action log
            next
        end
    next
end
```

### Création de capteurs DLP personnalisés

Pour des besoins plus avancés, vous pouvez créer des capteurs DLP personnalisés :

#### Empreintes de documents

1. Accédez à **Security Profiles > Custom Signatures > Document Fingerprinting**
2. Cliquez sur **Create New**
3. Téléchargez des documents modèles contenant des informations sensibles
4. FortiGate créera des empreintes de ces documents
5. Utilisez ces empreintes dans vos règles DLP

#### Dictionnaires personnalisés

1. Accédez à **Security Profiles > Custom Signatures > Custom Dictionary**
2. Créez un dictionnaire contenant des termes sensibles
3. Utilisez ce dictionnaire dans vos règles DLP

### Application du DLP

Pour appliquer le DLP, associez le profil configuré à une politique de pare-feu :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Créez ou modifiez une politique pour le trafic sortant
3. Dans la section **Security Profiles**, activez **DLP** et sélectionnez le profil
4. Cliquez sur **OK** pour enregistrer la politique

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Bonnes pratiques DLP</h4>
<p>Commencez par identifier clairement les types d'informations sensibles à protéger (données personnelles, propriété intellectuelle, informations financières, etc.). Créez ensuite des règles spécifiques pour chaque type, en commençant par le mode "log only" pour évaluer l'impact avant de passer au mode "block".</p>
</div>

### Limitations du DLP

Le DLP FortiGate présente certaines limitations :

* **Trafic chiffré** : Nécessite l'inspection SSL pour analyser le trafic HTTPS
* **Formats complexes** : Certains formats de fichiers complexes peuvent être difficiles à analyser
* **Faux positifs** : Les règles trop génériques peuvent générer des faux positifs
* **Contournements** : Les utilisateurs déterminés peuvent trouver des moyens de contourner le DLP

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 DLP complet</h4>
<p>Pour une solution DLP complète, le DLP FortiGate devrait faire partie d'une stratégie plus large incluant des contrôles aux niveaux des terminaux, des serveurs et du cloud, ainsi que des politiques et formations pour les utilisateurs.</p>
</div>

<h2 id="utm-best-practices" style="color:#0D274D;">6.10 Bonnes pratiques UTM</h2>

Cette section présente les meilleures pratiques pour déployer et maintenir efficacement les fonctionnalités UTM sur FortiGate.

### Planification et déploiement

#### Évaluation des besoins et des capacités

* **Analyse des besoins** : Identifiez les menaces spécifiques à votre environnement et les fonctionnalités UTM nécessaires
* **Évaluation des performances** : Assurez-vous que votre modèle FortiGate peut gérer les fonctionnalités UTM requises avec votre volume de trafic
* **Dimensionnement** : Consultez les guides de dimensionnement Fortinet pour vérifier que votre modèle est adapté

#### Déploiement progressif

* **Approche par phases** : Activez les fonctionnalités UTM progressivement, en commençant par les plus critiques
* **Mode surveillance** : Commencez en mode "monitor only" avant de passer au blocage actif
* **Tests** : Testez chaque fonctionnalité dans un environnement contrôlé avant le déploiement en production

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Ordre de déploiement recommandé</h4>
<p>1. Antivirus (menaces de base)<br>
2. Filtrage web (contrôle d'accès)<br>
3. IPS (protection contre les exploits)<br>
4. Contrôle d'application (visibilité et contrôle)<br>
5. Filtrage DNS (couche supplémentaire)<br>
6. DLP (protection des données)<br>
7. Inspection SSL (visibilité du trafic chiffré)</p>
</div>

### Optimisation des performances

#### Gestion des ressources

* **Surveillance des ressources** : Surveillez régulièrement l'utilisation du CPU, de la mémoire et des sessions
* **Profils ciblés** : Appliquez les profils UTM uniquement aux flux de trafic pertinents
* **Équilibrage des fonctionnalités** : Trouvez un équilibre entre le nombre de fonctionnalités activées et les performances

#### Optimisation des profils

* **Signatures pertinentes** : Activez uniquement les signatures IPS pertinentes pour votre environnement
* **Exceptions** : Créez des exceptions pour les applications critiques qui pourraient être affectées
* **Taille des fichiers** : Ajustez les limites de taille des fichiers analysés selon vos besoins et capacités

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Impact de l'inspection SSL</h4>
<p>L'inspection SSL est la fonctionnalité qui a généralement le plus grand impact sur les performances. Activez-la de manière sélective, en commençant par les catégories de sites les plus risquées, et augmentez progressivement la couverture en fonction des capacités de votre appareil.</p>
</div>

### Maintenance et surveillance

#### Mises à jour régulières

* **Mises à jour de firmware** : Maintenez votre FortiGate à jour avec les dernières versions stables
* **Mises à jour de signatures** : Assurez-vous que les signatures FortiGuard sont régulièrement mises à jour
* **Révision des profils** : Révisez périodiquement vos profils UTM pour les adapter aux nouvelles menaces

#### Surveillance et journalisation

* **Centralisation des journaux** : Utilisez FortiAnalyzer ou un serveur syslog pour centraliser les journaux
* **Alertes** : Configurez des alertes pour les événements critiques
* **Rapports réguliers** : Générez et analysez des rapports réguliers sur l'activité UTM
* **Analyse des tendances** : Identifiez les tendances et ajustez vos politiques en conséquence

### Gestion des faux positifs

* **Période d'observation** : Surveillez les journaux pendant une période initiale pour identifier les faux positifs
* **Ajustement progressif** : Ajustez les profils progressivement pour réduire les faux positifs
* **Listes blanches** : Utilisez des listes blanches pour les sites et applications légitimes qui sont incorrectement bloqués
* **Exceptions** : Créez des politiques d'exception pour les cas particuliers

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Documentation des exceptions</h4>
<p>Documentez soigneusement toutes les exceptions et listes blanches que vous créez, en incluant la raison de l'exception et une date de révision. Révisez régulièrement ces exceptions pour déterminer si elles sont toujours nécessaires.</p>
</div>

### Intégration avec la Security Fabric

* **Visibilité centralisée** : Intégrez votre FortiGate à la Security Fabric pour une visibilité centralisée
* **FortiAnalyzer** : Utilisez FortiAnalyzer pour une analyse approfondie des journaux et des rapports détaillés
* **FortiSandbox** : Intégrez FortiSandbox pour une analyse avancée des fichiers suspects
* **FortiClient** : Déployez FortiClient sur les terminaux pour une protection de bout en bout

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Défense en profondeur</h4>
<p>Les fonctionnalités UTM de FortiGate sont plus efficaces lorsqu'elles font partie d'une stratégie de défense en profondeur. Combinez-les avec d'autres mesures de sécurité comme la segmentation réseau, la protection des terminaux, la gestion des correctifs et la sensibilisation des utilisateurs pour une protection complète.</p>
</div>

---

<h1 id="haute-disponibilite" style="color:#E23237;">7. Haute Disponibilité (HA)</h1>

<h2 id="ha-concepts" style="color:#0D274D;">7.1 Concepts fondamentaux de la haute disponibilité</h2>

La haute disponibilité (HA) permet de garantir la continuité des services réseau en cas de défaillance d'un équipement FortiGate. Cette section présente les concepts fondamentaux de la haute disponibilité dans l'environnement Fortinet.

### Objectifs de la haute disponibilité

La mise en place d'une solution HA vise plusieurs objectifs :

* **Élimination des points uniques de défaillance** : Assurer la continuité du service en cas de panne matérielle
* **Maintenance sans interruption** : Permettre la maintenance d'un appareil sans impact sur le service
* **Répartition de charge** : Optimiser les performances en distribuant le trafic (dans certains modes)
* **Récupération automatique** : Restaurer automatiquement le service après une défaillance

### Modes de haute disponibilité FortiGate

FortiGate propose plusieurs modes de haute disponibilité :

* **Actif-Passif (A-P)** : Un appareil traite le trafic, l'autre est en veille
* **Actif-Actif (A-A)** : Tous les appareils traitent le trafic simultanément
* **Cluster** : Configuration de plus de deux appareils en HA

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Choix du mode</h4>
<p>Le mode Actif-Passif est généralement recommandé pour la plupart des déploiements car il offre une configuration plus simple et un comportement plus prévisible. Le mode Actif-Actif peut offrir de meilleures performances mais nécessite une planification plus minutieuse et peut présenter des comportements complexes lors des basculements.</p>
</div>

### Mécanismes de synchronisation et de surveillance

Les appareils FortiGate en HA utilisent plusieurs mécanismes pour maintenir la synchronisation et surveiller l'état du cluster :

* **Heartbeat** : Communication régulière entre les membres du cluster pour vérifier leur disponibilité
* **Synchronisation de configuration** : Réplication automatique des modifications de configuration
* **Synchronisation de session** : Partage des informations de session pour maintenir les connexions lors d'un basculement
* **Surveillance des liens** : Vérification de l'état des interfaces réseau
* **Surveillance des services** : Vérification de l'état des services critiques

### Rôles dans un cluster HA

Dans un cluster FortiGate HA, chaque appareil peut avoir l'un des rôles suivants :

* **Maître (Primary)** : Appareil qui contrôle le cluster et, en mode A-P, traite tout le trafic
* **Esclave (Secondary)** : Appareil(s) qui suit(vent) le maître et prend(nent) le relais en cas de défaillance
* **Actif** : Appareil qui traite activement le trafic (peut être maître ou esclave en mode A-A)
* **Passif** : Appareil en veille qui ne traite pas de trafic (en mode A-P)

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Bonnes pratiques pour les interfaces heartbeat</h4>
<p>Utilisez des interfaces dédiées pour la communication heartbeat entre les appareils FortiGate. Idéalement, configurez au moins deux interfaces heartbeat pour la redondance. Connectez ces interfaces directement entre les appareils ou via un commutateur dédié pour éviter les interférences avec le trafic normal.</p>
</div>

<h2 id="ha-actif-passif" style="color:#0D274D;">7.2 Configuration d'un cluster Actif-Passif</h2>

Le mode Actif-Passif est le mode HA le plus couramment utilisé dans les déploiements FortiGate. Cette section détaille la configuration d'un cluster HA en mode Actif-Passif.

### Prérequis pour la configuration HA

Avant de configurer un cluster HA, assurez-vous que :

* Les appareils FortiGate sont du même modèle et exécutent la même version de firmware
* Chaque appareil dispose d'une licence valide
* Les interfaces réseau sont correctement câblées
* Au moins une interface est disponible pour la communication heartbeat
* Les appareils sont accessibles via leurs interfaces de gestion

### Configuration du premier FortiGate (futur maître)

Pour configurer le premier FortiGate via l'interface web :

1. Accédez à **System > HA**
2. Configurez les paramètres de base :
   * **Mode** : Sélectionnez **Active-Passive**
   * **Device Priority** : Définissez une priorité élevée (par exemple 200) pour ce FortiGate
   * **Group Name** : Nom du cluster HA
   * **Password** : Mot de passe pour la communication HA
3. Configurez les interfaces heartbeat :
   * Sélectionnez au moins une interface pour la communication heartbeat
   * Idéalement, configurez deux interfaces pour la redondance
4. Configurez les options avancées si nécessaire :
   * **Override** : Activez cette option pour que l'appareil reprenne le rôle de maître après une récupération
   * **Session Pickup** : Activez pour maintenir les sessions lors d'un basculement
   * **Monitor Interfaces** : Sélectionnez les interfaces à surveiller
5. Cliquez sur **OK** pour appliquer la configuration

Exemple de configuration CLI pour le premier FortiGate :

```
config system ha
    set mode a-p
    set group-name "FortiHA-Cluster"
    set password "HASecurePassword123"
    set priority 200
    set override enable
    set session-pickup enable
    set hbdev "port3" 0 "port4" 0
    set monitor "port1" "port2"
    set ha-mgmt-status enable
    config ha-mgmt-interfaces
        edit 1
            set interface "port5"
            set gateway 192.168.0.1
        next
    end
end
```

### Configuration du second FortiGate (futur esclave)

La configuration du second FortiGate est similaire, mais avec une priorité plus basse :

1. Accédez à **System > HA**
2. Configurez les mêmes paramètres que pour le premier FortiGate, mais avec :
   * **Device Priority** : Définissez une priorité plus basse (par exemple 100)
3. Assurez-vous que tous les autres paramètres (Group Name, Password, Heartbeat Interfaces, etc.) sont identiques
4. Cliquez sur **OK** pour appliquer la configuration

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Attention au basculement</h4>
<p>Lorsque vous appliquez la configuration HA, les appareils redémarrent et négocient leurs rôles. Cela peut entraîner une brève interruption du service. Planifiez cette opération pendant une fenêtre de maintenance.</p>
</div>

### Vérification de la configuration HA

Après avoir configuré les deux FortiGate, vérifiez que le cluster fonctionne correctement :

1. Connectez-vous à l'interface web du FortiGate maître
2. Accédez à **System > HA**
3. Vérifiez que :
   * Le statut du cluster est **In Sync**
   * Les rôles sont correctement attribués (Primary/Secondary)
   * Les interfaces heartbeat sont actives

Via la CLI, vous pouvez utiliser les commandes suivantes :

```
# Vérifier l'état du cluster
get system ha status

# Vérifier la synchronisation
diagnose sys ha checksum show

# Vérifier les interfaces heartbeat
diagnose hardware deviceinfo nic <interface_name>
```

### Configuration de l'adresse de gestion HA

Pour faciliter la gestion du cluster, configurez une adresse de gestion HA :

1. Accédez à **System > HA**
2. Dans la section **Management Interface**, configurez :
   * **Interface** : Interface dédiée à la gestion
   * **Gateway** : Passerelle par défaut pour cette interface
   * **Management IP** : Adresse IP fixe pour la gestion du cluster

Cette adresse reste accessible quel que soit le FortiGate qui assume le rôle de maître.

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Accès aux appareils individuels</h4>
<p>Même en configuration HA, chaque FortiGate conserve son adresse IP individuelle sur son interface de gestion. Vous pouvez utiliser ces adresses pour accéder directement à un appareil spécifique si nécessaire, par exemple pour des diagnostics.</p>
</div>

<h2 id="ha-actif-actif" style="color:#0D274D;">7.3 Configuration d'un cluster Actif-Actif</h2>

Le mode Actif-Actif permet à tous les appareils du cluster de traiter le trafic simultanément, offrant potentiellement de meilleures performances. Cette section détaille la configuration d'un cluster HA en mode Actif-Actif.

### Principes du mode Actif-Actif

En mode Actif-Actif :

* Tous les appareils du cluster traitent activement le trafic
* Le trafic est distribué entre les appareils selon une méthode configurable
* Un appareil reste le maître du cluster et gère la configuration
* En cas de défaillance d'un appareil, les autres prennent en charge son trafic

### Configuration du cluster Actif-Actif

La configuration d'un cluster Actif-Actif est similaire à celle d'un cluster Actif-Passif, avec quelques différences clés :

1. Accédez à **System > HA**
2. Configurez les paramètres de base :
   * **Mode** : Sélectionnez **Active-Active**
   * **Device Priority** : Définissez des priorités pour déterminer le maître
   * **Group Name** et **Password** : Identiques pour tous les membres
3. Configurez les interfaces heartbeat comme pour un cluster Actif-Passif
4. Configurez les options spécifiques au mode Actif-Actif :
   * **Load Balancing Algorithm** : Méthode de répartition du trafic
   * **Session Pickup** : Crucial en mode A-A pour maintenir les sessions
5. Cliquez sur **OK** pour appliquer la configuration

Exemple de configuration CLI pour un cluster Actif-Actif :

```
config system ha
    set mode a-a
    set group-name "FortiHA-Cluster-AA"
    set password "HASecurePassword123"
    set priority 200
    set override enable
    set session-pickup enable
    set load-balance-all enable
    set load-balance-tcp enable
    set load-balance-udp enable
    set hbdev "port3" 0 "port4" 0
    set monitor "port1" "port2"
end
```

### Algorithmes de répartition de charge

FortiGate propose plusieurs algorithmes pour répartir le trafic entre les membres du cluster :

* **Source IP** : Basé sur l'adresse IP source
* **Session** : Basé sur les sessions
* **Volume** : Basé sur le volume de trafic
* **Packets** : Basé sur le nombre de paquets
* **Round Robin** : Distribution séquentielle

Choisissez l'algorithme en fonction de vos besoins spécifiques et du type de trafic dans votre réseau.

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Considérations pour le mode Actif-Actif</h4>
<p>Le mode Actif-Actif est plus complexe à gérer et peut présenter des comportements inattendus lors des basculements. Il est particulièrement adapté aux environnements à haut débit où les performances sont critiques. Pour la plupart des déploiements standard, le mode Actif-Passif offre un meilleur équilibre entre simplicité et fiabilité.</p>
</div>

### Surveillance du cluster Actif-Actif

La surveillance d'un cluster Actif-Actif est similaire à celle d'un cluster Actif-Passif, avec quelques métriques supplémentaires à surveiller :

1. Accédez à **System > HA**
2. Vérifiez la répartition du trafic entre les membres
3. Surveillez les performances de chaque appareil

Via la CLI, vous pouvez utiliser des commandes supplémentaires :

```
# Vérifier la répartition des sessions
get system performance status

# Vérifier les statistiques de load balancing
diagnose sys ha load-balance status
```

<h2 id="ha-monitoring" style="color:#0D274D;">7.4 Surveillance et dépannage HA</h2>

Une surveillance efficace et des compétences de dépannage sont essentielles pour maintenir un cluster HA en bon état de fonctionnement. Cette section couvre les outils et techniques pour surveiller et dépanner un cluster FortiGate HA.

### Surveillance du cluster HA

#### Via l'interface web

1. Accédez à **System > HA**
2. Vérifiez le statut général du cluster :
   * **Status** : État de synchronisation
   * **Role** : Rôle de chaque appareil (Primary/Secondary)
   * **Uptime** : Temps écoulé depuis le dernier basculement
3. Accédez à **Dashboard > Status**
4. Vérifiez le widget **HA Status** pour une vue d'ensemble rapide

#### Via la CLI

Utilisez ces commandes pour une surveillance détaillée :

```
# État général du cluster
get system ha status

# Vérifier la synchronisation
diagnose sys ha checksum show

# Vérifier les interfaces heartbeat
diagnose sys ha heartbeat

# Vérifier les statistiques de basculement
diagnose sys ha history
```

### Journalisation des événements HA

Configurez la journalisation des événements HA pour faciliter le dépannage :

1. Accédez à **Log & Report > Log Settings**
2. Assurez-vous que **System Events** est activé
3. Configurez la destination des journaux (mémoire, disque, serveur syslog, FortiAnalyzer)

Pour consulter les journaux HA :

1. Accédez à **Log & Report > System Events**
2. Filtrez les journaux avec le terme "HA" pour voir les événements liés à la haute disponibilité

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Journalisation externe</h4>
<p>Il est fortement recommandé de configurer une destination de journalisation externe (comme FortiAnalyzer ou un serveur syslog) pour les clusters HA. Cela permet de conserver les journaux même en cas de basculement et facilite l'analyse des événements qui ont conduit à un basculement.</p>
</div>

### Tests de basculement

Testez régulièrement le basculement pour vous assurer que le cluster fonctionne correctement :

#### Test manuel

1. Accédez à **System > HA**
2. Cliquez sur **Switch Device** pour forcer un basculement
3. Vérifiez que le trafic continue à circuler sans interruption significative

#### Test physique

1. Déconnectez une interface surveillée du FortiGate maître
2. Vérifiez que le basculement se produit comme prévu
3. Reconnectez l'interface et vérifiez si le maître d'origine reprend son rôle (selon la configuration override)

### Problèmes courants et solutions

#### Problèmes de synchronisation

**Symptômes** : Statut "Out of Sync", configurations différentes entre les appareils

**Solutions** :
* Vérifiez la connectivité des interfaces heartbeat
* Vérifiez que les checksums de configuration correspondent
* Forcez une synchronisation manuelle via la CLI : `execute ha synchronize start`

#### Basculements fréquents ou inattendus

**Symptômes** : Le cluster bascule fréquemment sans raison apparente

**Solutions** :
* Vérifiez les journaux système pour identifier la cause des basculements
* Ajustez les seuils de surveillance des interfaces
* Vérifiez la stabilité des liens réseau
* Augmentez le délai avant basculement si nécessaire

```
config system ha
    set link-failed-signal disable
    set ha-mgmt-status enable
    set monitor-interface-threshold 30
end
```

#### Problèmes de heartbeat

**Symptômes** : Perte de communication entre les membres du cluster

**Solutions** :
* Vérifiez le câblage des interfaces heartbeat
* Assurez-vous que les interfaces sont correctement configurées
* Augmentez l'intervalle heartbeat si le réseau est instable

```
config system ha
    set hb-interval 2
    set hb-lost-threshold 10
end
```

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Split-brain</h4>
<p>Une situation de "split-brain" se produit lorsque les deux appareils d'un cluster pensent être le maître. Cela peut arriver si la communication heartbeat est perdue mais que les deux appareils restent fonctionnels. Cette situation peut causer des problèmes réseau graves comme des conflits d'adresses IP. Assurez-vous que vos interfaces heartbeat sont redondantes et fiables pour éviter ce problème.</p>
</div>

### Commandes de dépannage avancées

Voici quelques commandes CLI avancées pour le dépannage HA :

```
# Afficher les statistiques détaillées du cluster
diagnose sys ha dump-by group

# Vérifier l'état des sessions synchronisées
diagnose sys ha session-stats

# Vérifier les messages heartbeat
diagnose debug application hatalk -1
diagnose debug enable

# Vérifier les événements de basculement
diagnose debug application ha -1
diagnose debug enable

# Désactiver le débogage après utilisation
diagnose debug disable
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Documentation du cluster</h4>
<p>Documentez soigneusement votre configuration HA, y compris les adresses IP, les connexions physiques, les priorités et les paramètres spécifiques. Cette documentation est précieuse lors du dépannage ou lors de l'ajout/remplacement d'un appareil dans le cluster.</p>
</div>

<h2 id="ha-upgrade" style="color:#0D274D;">7.5 Mise à niveau d'un cluster HA</h2>

La mise à niveau d'un cluster HA nécessite une planification et une exécution soigneuses pour minimiser les interruptions de service. Cette section détaille les procédures recommandées pour mettre à niveau un cluster FortiGate HA.

### Préparation de la mise à niveau

Avant de commencer la mise à niveau, effectuez ces étapes préparatoires :

1. **Vérifiez la compatibilité** : Consultez les notes de version pour vous assurer que la nouvelle version est compatible avec votre matériel et vos fonctionnalités
2. **Sauvegardez la configuration** : Créez une sauvegarde complète de la configuration actuelle
3. **Planifiez une fenêtre de maintenance** : Même si la mise à niveau HA est conçue pour minimiser les interruptions, prévoyez une fenêtre de maintenance
4. **Téléchargez le firmware** : Téléchargez le fichier de firmware depuis le site de support Fortinet
5. **Vérifiez l'état du cluster** : Assurez-vous que le cluster est en bon état et synchronisé

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Chemin de mise à niveau</h4>
<p>Vérifiez le chemin de mise à niveau recommandé. Dans certains cas, vous ne pouvez pas passer directement d'une version ancienne à la plus récente et devez suivre un chemin spécifique avec des versions intermédiaires.</p>
</div>

### Méthodes de mise à niveau

FortiGate propose deux méthodes principales pour mettre à niveau un cluster HA :

#### Méthode 1 : Mise à niveau automatique du cluster

Cette méthode met à niveau tous les membres du cluster automatiquement :

1. Connectez-vous à l'interface web du FortiGate maître
2. Accédez à **System > Firmware**
3. Cliquez sur **Upgrade Firmware**
4. Sélectionnez le fichier de firmware téléchargé
5. Activez l'option **Upgrade all members in this HA cluster**
6. Cliquez sur **Upload and Upgrade**

Le processus se déroule comme suit :
* Le maître installe le nouveau firmware et redémarre
* Un esclave devient temporairement maître
* Lorsque l'ancien maître revient en ligne, il reprend son rôle (si override est activé)
* Les esclaves sont mis à niveau un par un

#### Méthode 2 : Mise à niveau manuelle séquentielle

Cette méthode vous donne plus de contrôle sur le processus :

1. Mettez d'abord à niveau un esclave :
   * Connectez-vous directement à l'interface de gestion de l'esclave
   * Accédez à **System > Firmware**
   * Effectuez la mise à niveau et attendez que l'appareil redémarre et rejoigne le cluster
2. Forcez un basculement pour que l'esclave mis à niveau devienne maître :
   * Connectez-vous au maître actuel
   * Accédez à **System > HA**
   * Cliquez sur **Switch Device**
3. Mettez à niveau l'ancien maître (maintenant esclave) :
   * Connectez-vous directement à son interface de gestion
   * Effectuez la mise à niveau comme à l'étape 1

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Avantages de la méthode manuelle</h4>
<p>La mise à niveau manuelle séquentielle permet de vérifier le bon fonctionnement après chaque étape et de revenir en arrière plus facilement en cas de problème. Elle est recommandée pour les environnements critiques ou lorsque vous passez à une version majeure du firmware.</p>
</div>

### Vérification post-mise à niveau

Après la mise à niveau, effectuez ces vérifications :

1. **Vérifiez la version du firmware** sur tous les membres du cluster
2. **Vérifiez l'état du cluster** pour vous assurer qu'il est synchronisé
3. **Testez les fonctionnalités clés** pour confirmer qu'elles fonctionnent correctement
4. **Vérifiez les journaux** pour détecter d'éventuelles erreurs
5. **Surveillez les performances** pendant plusieurs heures pour détecter d'éventuels problèmes

### Retour à la version précédente

Si vous rencontrez des problèmes après la mise à niveau, vous pouvez revenir à la version précédente :

1. Téléchargez le firmware de la version précédente
2. Suivez la même procédure que pour la mise à niveau, mais avec l'ancien firmware
3. Restaurez la configuration sauvegardée si nécessaire

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Compatibilité des configurations</h4>
<p>Les configurations ne sont pas toujours rétrocompatibles entre les versions majeures. Si vous revenez à une version antérieure, vous devrez peut-être restaurer une sauvegarde de configuration compatible avec cette version.</p>
</div>

### Bonnes pratiques pour les mises à niveau HA

* **Testez dans un environnement de laboratoire** si possible avant de mettre à niveau la production
* **Lisez attentivement les notes de version** pour connaître les problèmes connus et les changements de comportement
* **Effectuez les mises à niveau pendant les périodes de faible trafic**
* **Vérifiez l'espace disque disponible** avant la mise à niveau
* **Conservez les anciennes versions de firmware** disponibles pour un retour en arrière rapide
* **Documentez chaque mise à niveau** avec les versions, dates et problèmes rencontrés

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Mises à niveau progressives</h4>
<p>Pour les réseaux critiques avec plusieurs clusters FortiGate, envisagez de mettre à niveau les clusters progressivement plutôt que tous en même temps. Commencez par les clusters moins critiques pour identifier d'éventuels problèmes avant de mettre à niveau les clusters les plus importants.</p>
</div>

---

<h1 id="monitoring" style="color:#E23237;">8. Monitoring & Logs</h1>

<h2 id="monitoring-overview" style="color:#0D274D;">8.1 Vue d'ensemble du monitoring FortiGate</h2>

Le monitoring est essentiel pour comprendre l'état de votre réseau, détecter les problèmes potentiels et assurer la sécurité de votre infrastructure. Cette section présente une vue d'ensemble des capacités de monitoring de FortiGate.

### Objectifs du monitoring

Le monitoring d'un FortiGate vise plusieurs objectifs :

* **Surveillance de l'état** : Vérifier le bon fonctionnement de l'appareil et des services
* **Détection des menaces** : Identifier les activités suspectes ou malveillantes
* **Analyse des performances** : Évaluer les performances et identifier les goulots d'étranglement
* **Conformité** : Collecter des preuves pour les audits de conformité
* **Planification des capacités** : Anticiper les besoins futurs en ressources
* **Dépannage** : Diagnostiquer et résoudre les problèmes

### Types de monitoring disponibles

FortiGate propose plusieurs types de monitoring :

* **Tableaux de bord** : Vues graphiques personnalisables de l'état du système
* **Journaux (logs)** : Enregistrements détaillés des événements et du trafic
* **Surveillance du trafic** : Analyse en temps réel du trafic réseau
* **Rapports** : Synthèses périodiques des activités et événements
* **Alertes** : Notifications en cas d'événements critiques
* **SNMP** : Intégration avec des systèmes de monitoring tiers
* **Syslog** : Exportation des journaux vers des serveurs externes

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Approche multi-niveaux</h4>
<p>Une stratégie de monitoring efficace combine plusieurs niveaux : monitoring en temps réel pour la détection rapide des problèmes, journalisation détaillée pour l'analyse approfondie, et rapports périodiques pour l'analyse des tendances à long terme.</p>
</div>

### Destinations de journalisation

FortiGate peut envoyer ses journaux vers différentes destinations :

* **Mémoire** : Stockage temporaire, perdu au redémarrage
* **Disque local** : Stockage persistant sur le FortiGate (si équipé d'un disque)
* **FortiAnalyzer** : Solution dédiée de Fortinet pour la gestion centralisée des journaux
* **FortiCloud** : Service cloud de Fortinet pour le stockage et l'analyse des journaux
* **Serveur Syslog** : Serveur syslog tiers
* **Serveur SNMP** : Système de monitoring SNMP

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Bonnes pratiques de journalisation</h4>
<p>Pour une journalisation efficace, utilisez une destination externe comme FortiAnalyzer ou un serveur syslog. Cela permet de conserver les journaux même en cas de défaillance du FortiGate, d'augmenter la capacité de stockage, et de centraliser les journaux de plusieurs appareils pour une analyse corrélée.</p>
</div>

### Types de journaux

FortiGate génère plusieurs types de journaux, chacun couvrant un aspect spécifique :

* **Traffic** : Enregistrements des sessions réseau
* **Event** : Événements système et administratifs
* **Security** : Événements liés à la sécurité (virus, intrusions, etc.)
* **VPN** : Activités des tunnels VPN
* **Web Filtering** : Accès web filtrés
* **Application Control** : Activités des applications
* **DNS Filter** : Requêtes DNS filtrées
* **IPS** : Événements de prévention d'intrusion
* **User** : Activités des utilisateurs
* **WAF** : Événements du pare-feu d'applications web
* **FortiSandbox** : Résultats d'analyse de fichiers suspects

<h2 id="dashboard" style="color:#0D274D;">8.2 Tableaux de bord et widgets</h2>

Les tableaux de bord FortiGate offrent une vue graphique et personnalisable de l'état et des performances de votre appareil et de votre réseau.

### Tableau de bord par défaut

Le tableau de bord par défaut de FortiGate comprend plusieurs widgets essentiels :

* **System Information** : Informations de base sur le FortiGate (modèle, version, etc.)
* **License Information** : État des licences et abonnements
* **CPU Usage** : Utilisation du processeur
* **Memory Usage** : Utilisation de la mémoire
* **Session Information** : Nombre de sessions actives
* **Network Bandwidth** : Utilisation de la bande passante
* **Top Sources/Destinations** : Principales sources et destinations de trafic
* **Top Applications** : Applications les plus utilisées
* **Security Recommendations** : Recommandations pour améliorer la sécurité

### Personnalisation des tableaux de bord

Pour personnaliser un tableau de bord via l'interface web :

1. Accédez à **Dashboard**
2. Cliquez sur le menu déroulant en haut à droite et sélectionnez **Add Dashboard**
3. Donnez un nom à votre nouveau tableau de bord
4. Cliquez sur **Add Widget** pour ajouter des widgets
5. Organisez les widgets par glisser-déposer
6. Redimensionnez les widgets selon vos besoins
7. Configurez chaque widget en cliquant sur l'icône d'engrenage

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Tableaux de bord thématiques</h4>
<p>Créez des tableaux de bord thématiques pour différents aspects de votre réseau : un tableau de bord pour la sécurité, un autre pour les performances, un autre pour les VPNs, etc. Cela facilite la surveillance ciblée et l'analyse.</p>
</div>

### Widgets disponibles

FortiGate propose de nombreux widgets pour différents besoins de monitoring :

#### Widgets système
* **System Resources** : Utilisation des ressources système
* **HA Status** : État du cluster haute disponibilité
* **DHCP Monitor** : Baux DHCP actifs
* **Routing Monitor** : État des routes

#### Widgets réseau
* **Interface Bandwidth** : Utilisation de la bande passante par interface
* **Traffic** : Vue graphique du trafic
* **Policy & Objects Usage** : Utilisation des politiques et objets
* **Firewall User Monitor** : Activité des utilisateurs authentifiés

#### Widgets sécurité
* **Security Fabric** : État de la Security Fabric
* **FortiGuard** : État des services FortiGuard
* **Security Ratings** : Évaluation de la sécurité
* **Botnet Activity** : Activité de botnets détectée
* **Threat Map** : Carte des menaces en temps réel

#### Widgets UTM
* **Top Threats** : Principales menaces détectées
* **Top Allowed/Blocked Web Sites** : Sites web les plus visités/bloqués
* **Top Allowed/Blocked Applications** : Applications les plus utilisées/bloquées
* **Top Virus** : Virus les plus détectés

### Widgets personnalisés

FortiGate permet également de créer des widgets personnalisés :

1. Cliquez sur **Add Widget**
2. Sélectionnez **CLI Console** pour un widget de console CLI
3. Ou sélectionnez **Text** pour un widget de texte personnalisé
4. Configurez le widget selon vos besoins

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Widget CLI pour le monitoring avancé</h4>
<p>Utilisez le widget CLI Console pour créer des vues personnalisées basées sur des commandes CLI spécifiques. Par exemple, vous pouvez créer un widget qui exécute régulièrement "get system performance status" pour surveiller les performances système en détail.</p>
</div>

<h2 id="logs-config" style="color:#0D274D;">8.3 Configuration de la journalisation</h2>

Une configuration appropriée de la journalisation est essentielle pour collecter les informations nécessaires à la surveillance et à l'analyse de votre réseau.

### Configuration des paramètres de journalisation

Pour configurer les paramètres généraux de journalisation via l'interface web :

1. Accédez à **Log & Report > Log Settings**
2. Configurez les options générales :
   * **Local Log Disk Settings** : Paramètres du stockage local
   * **Log Rotation** : Rotation des fichiers journaux
   * **GUI Preferences** : Préférences d'affichage des journaux
3. Configurez les destinations de journalisation :
   * **Memory** : Journalisation en mémoire
   * **Disk** : Journalisation sur disque local
   * **FortiAnalyzer/FortiManager** : Journalisation vers FortiAnalyzer
   * **FortiCloud** : Journalisation vers FortiCloud
   * **Syslog** : Journalisation vers un serveur syslog
4. Sélectionnez les types de journaux à envoyer à chaque destination
5. Cliquez sur **Apply** pour enregistrer la configuration

Exemple de configuration CLI pour la journalisation :

```
config log disk setting
    set status enable
    set storage-policy circular
    set maximum-log-age 7
    set upload enable
    set upload-time 00:00
    set full-first-warning-threshold 75
    set full-second-warning-threshold 90
    set full-final-warning-threshold 95
end

config log fortianalyzer setting
    set status enable
    set server "192.168.1.100"
    set upload-option realtime
    set reliable enable
end

config log syslogd setting
    set status enable
    set server "192.168.1.200"
    set facility local7
    set format rfc5424
    set port 514
    set mode udp
end
```

### Niveaux de journalisation

FortiGate propose plusieurs niveaux de journalisation, du moins détaillé au plus détaillé :

* **Emergency (0)** : Système inutilisable
* **Alert (1)** : Action immédiate requise
* **Critical (2)** : Conditions critiques
* **Error (3)** : Conditions d'erreur
* **Warning (4)** : Conditions d'avertissement
* **Notification (5)** : Conditions normales mais significatives
* **Information (6)** : Messages d'information
* **Debug (7)** : Messages de débogage

Pour configurer le niveau de journalisation :

1. Accédez à **Log & Report > Log Settings**
2. Dans la section **Global Log Settings**, sélectionnez le niveau approprié
3. Cliquez sur **Apply**

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Équilibre entre détail et volume</h4>
<p>Trouvez un équilibre entre le niveau de détail des journaux et le volume généré. Un niveau trop élevé (comme Debug) génère un volume important de journaux qui peut être difficile à gérer et à analyser, tandis qu'un niveau trop bas peut omettre des informations importantes.</p>
</div>

### Journalisation dans les politiques de pare-feu

La journalisation peut être configurée individuellement pour chaque politique de pare-feu :

1. Accédez à **Policy & Objects > Firewall Policy**
2. Créez ou modifiez une politique
3. Dans la section **Logging Options**, configurez :
   * **Log Allowed Traffic** : Journalisation du trafic autorisé
   * **Log Security Events** : Journalisation des événements de sécurité
   * **Generate Logs when Session Starts** : Journalisation au début de la session
   * **Generate Logs when Session Ends** : Journalisation à la fin de la session
4. Cliquez sur **OK** pour enregistrer la politique

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Impact sur les performances</h4>
<p>La journalisation de tout le trafic, en particulier au début et à la fin de chaque session, peut avoir un impact significatif sur les performances. Pour les politiques à haut volume de trafic, envisagez de journaliser uniquement les événements de sécurité ou d'utiliser l'échantillonnage.</p>
</div>

### Filtres de journalisation

Pour réduire le volume de journaux et se concentrer sur les informations pertinentes, configurez des filtres de journalisation :

1. Accédez à **Log & Report > Log Settings**
2. Dans la section **Filters**, configurez :
   * **Filter Mode** : Inclusion ou exclusion
   * **Filters** : Critères de filtrage (adresses, services, etc.)
3. Cliquez sur **Apply** pour enregistrer la configuration

Exemple de configuration CLI pour les filtres de journalisation :

```
config log filter
    set severity information
    set forward-traffic enable
    set local-traffic enable
    set multicast-traffic enable
    set sniffer-traffic disable
    set anomaly enable
    set voip disable
    set filter "srcip 10.0.0.0/24"
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Journalisation ciblée</h4>
<p>Plutôt que d'activer la journalisation pour tout le trafic, adoptez une approche ciblée : journalisez en détail le trafic critique ou suspect, et utilisez une journalisation minimale pour le trafic normal à haut volume. Cela réduit le volume de journaux tout en conservant les informations importantes.</p>
</div>

<h2 id="log-analysis" style="color:#0D274D;">8.4 Analyse des journaux</h2>

L'analyse des journaux permet d'extraire des informations précieuses à partir des données brutes collectées par votre FortiGate.

### Visualisation des journaux dans l'interface web

Pour visualiser les journaux via l'interface web :

1. Accédez à **Log & Report**
2. Sélectionnez le type de journal à visualiser :
   * **Traffic** : Journaux de trafic
   * **Security** : Journaux de sécurité
   * **Event** : Journaux d'événements
   * Etc.
3. Utilisez les filtres pour affiner l'affichage :
   * **Add Filter** : Ajouter des critères de filtrage
   * **Time Range** : Sélectionner une période
   * **Refresh** : Actualiser l'affichage
4. Cliquez sur un journal spécifique pour voir les détails

### Recherche avancée dans les journaux

Pour effectuer des recherches avancées dans les journaux :

1. Dans la vue des journaux, cliquez sur **Add Filter**
2. Sélectionnez le champ sur lequel filtrer
3. Choisissez l'opérateur (égal, contient, etc.)
4. Entrez la valeur recherchée
5. Ajoutez d'autres filtres si nécessaire
6. Utilisez les opérateurs logiques (AND, OR) pour combiner les filtres

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Recherche par expressions régulières</h4>
<p>Pour des recherches plus puissantes, vous pouvez utiliser des expressions régulières dans certains champs de filtrage. Par exemple, pour trouver tous les journaux contenant des adresses IP d'un certain sous-réseau, vous pouvez utiliser une expression comme "192\.168\.1\.[0-9]+".</p>
</div>

### Analyse des journaux de trafic

Les journaux de trafic enregistrent les sessions réseau et sont utiles pour :

* Comprendre les modèles de trafic
* Identifier les utilisateurs ou applications consommant beaucoup de bande passante
* Vérifier l'application des politiques de pare-feu
* Dépanner les problèmes de connectivité

Champs importants dans les journaux de trafic :

* **Date/Time** : Horodatage de l'événement
* **Source/Destination** : Adresses IP source et destination
* **Service/Port** : Service ou port utilisé
* **Action** : Action appliquée (accept, deny, etc.)
* **Policy ID** : ID de la politique de pare-feu appliquée
* **Application** : Application identifiée
* **Sent/Received** : Quantité de données envoyées/reçues

### Analyse des journaux de sécurité

Les journaux de sécurité enregistrent les événements liés à la sécurité et sont utiles pour :

* Détecter les tentatives d'intrusion
* Identifier les infections par malware
* Surveiller les activités suspectes
* Analyser les incidents de sécurité

Types de journaux de sécurité :

* **Virus** : Détections de virus et malwares
* **IPS** : Événements de prévention d'intrusion
* **Anomaly** : Comportements réseau anormaux
* **Web Filter** : Accès web filtrés
* **Application Control** : Applications bloquées
* **DLP** : Événements de prévention de fuite de données

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Corrélation des journaux</h4>
<p>Pour une analyse efficace, corrélez différents types de journaux. Par exemple, si un journal IPS indique une tentative d'exploitation, recherchez les journaux de trafic correspondants pour identifier la source et la destination, puis vérifiez les journaux d'application pour comprendre le contexte de l'attaque.</p>
</div>

### Exportation et analyse externe

Pour une analyse plus approfondie, vous pouvez exporter les journaux :

1. Dans la vue des journaux, sélectionnez les journaux à exporter
2. Cliquez sur **Download** ou **Export**
3. Choisissez le format d'exportation (CSV, JSON, etc.)
4. Analysez les journaux avec des outils externes comme Excel, Python, ou des solutions SIEM

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Informations sensibles</h4>
<p>Les journaux peuvent contenir des informations sensibles comme des adresses IP internes, des noms d'utilisateurs, ou des détails sur votre infrastructure. Assurez-vous de traiter les journaux exportés avec les précautions de sécurité appropriées.</p>
</div>

<h2 id="reports" style="color:#0D274D;">8.5 Rapports</h2>

Les rapports FortiGate fournissent des synthèses structurées des activités et événements, facilitant l'analyse des tendances et la communication avec les parties prenantes.

### Types de rapports disponibles

FortiGate propose plusieurs types de rapports prédéfinis :

* **FortiView** : Rapports interactifs en temps réel
* **Rapports système** : État et performances du système
* **Rapports de trafic** : Analyse du trafic réseau
* **Rapports de menaces** : Synthèse des menaces détectées
* **Rapports VPN** : Activité des tunnels VPN
* **Rapports d'utilisation web** : Analyse de la navigation web
* **Rapports d'applications** : Utilisation des applications
* **Rapports de conformité** : Conformité aux normes de sécurité

### Génération de rapports

Pour générer un rapport via l'interface web :

1. Accédez à **Log & Report > Reports**
2. Cliquez sur **Generate Report**
3. Sélectionnez un modèle de rapport
4. Configurez les paramètres du rapport :
   * **Time Period** : Période couverte par le rapport
   * **Devices** : Appareils inclus dans le rapport
   * **Schedule** : Planification du rapport (unique ou récurrent)
   * **Output** : Format de sortie (PDF, HTML, etc.)
5. Cliquez sur **Generate Report** pour lancer la génération

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Rapports planifiés</h4>
<p>Pour un monitoring régulier, configurez des rapports planifiés qui seront générés automatiquement à intervalles réguliers (quotidien, hebdomadaire, mensuel). Ces rapports peuvent être envoyés par email aux parties prenantes concernées.</p>
</div>

### Personnalisation des rapports

FortiGate permet de personnaliser les rapports selon vos besoins :

1. Accédez à **Log & Report > Reports**
2. Cliquez sur **Report Templates**
3. Cliquez sur **Create New** pour créer un nouveau modèle
4. Configurez les sections du rapport :
   * **Layout** : Disposition des éléments
   * **Sections** : Sections à inclure
   * **Charts** : Graphiques à afficher
   * **Cover Page** : Page de couverture personnalisée
   * **Header/Footer** : En-tête et pied de page
5. Enregistrez le modèle pour une utilisation future

Exemple de configuration CLI pour un modèle de rapport personnalisé :

```
config report layout
    edit "Custom_Security_Report"
        set title "Custom Security Report"
        set page-orientation portrait
        set cutoff-level 2
        config body-item
            edit 1
                set type text
                set content "Executive Summary"
                set style heading1
            next
            edit 2
                set type chart
                set chart "top-threats"
                set style table
            next
            edit 3
                set type chart
                set chart "top-attacks"
                set style graph
            next
        end
    next
end
```

### FortiView

FortiView est un outil d'analyse interactif qui offre des vues en temps réel et historiques de votre réseau :

1. Accédez à **FortiView**
2. Sélectionnez la vue souhaitée :
   * **Sources** : Principales sources de trafic
   * **Destinations** : Principales destinations de trafic
   * **Applications** : Applications les plus utilisées
   * **Web Sites** : Sites web les plus visités
   * **Threats** : Menaces détectées
   * **Cloud Applications** : Applications cloud utilisées
   * Et bien d'autres...
3. Configurez les paramètres d'affichage :
   * **Time Range** : Période à analyser
   * **Device** : Appareil à analyser
   * **View Type** : Type de visualisation (table, bulle, carte, etc.)
4. Explorez les données en cliquant sur les éléments pour voir les détails

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Utilisation de FortiView pour le dépannage</h4>
<p>FortiView est particulièrement utile pour le dépannage rapide. Par exemple, si un utilisateur signale des problèmes de connectivité, vous pouvez utiliser FortiView pour voir rapidement son trafic, identifier les sessions bloquées, et déterminer quelle politique ou quel profil de sécurité cause le problème.</p>
</div>

### Exportation et partage des rapports

Une fois générés, les rapports peuvent être exportés et partagés :

1. Accédez à **Log & Report > Reports**
2. Dans l'onglet **Generated Reports**, trouvez le rapport souhaité
3. Cliquez sur l'icône de téléchargement pour exporter le rapport
4. Partagez le rapport exporté avec les parties prenantes concernées

Vous pouvez également configurer l'envoi automatique des rapports par email :

1. Lors de la création ou de la modification d'un rapport planifié
2. Configurez la section **Email Sending Options**
3. Spécifiez les destinataires et le sujet du message
4. Le rapport sera automatiquement envoyé après sa génération

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Rapports pour différentes audiences</h4>
<p>Créez différents modèles de rapports adaptés à différentes audiences : rapports techniques détaillés pour les équipes IT, rapports de synthèse pour la direction, rapports de conformité pour les auditeurs, etc. Chaque audience a des besoins d'information différents.</p>
</div>

<h2 id="snmp-syslog" style="color:#0D274D;">8.6 SNMP et Syslog</h2>

SNMP (Simple Network Management Protocol) et Syslog sont des protocoles standard pour le monitoring et la journalisation, permettant d'intégrer FortiGate à des systèmes de gestion réseau tiers.

### Configuration SNMP

SNMP permet à des systèmes de gestion réseau de surveiller l'état et les performances de votre FortiGate.

#### Activation et configuration de SNMP

Pour configurer SNMP via l'interface web :

1. Accédez à **System > SNMP**
2. Activez SNMP et configurez les paramètres généraux :
   * **SNMP Agent** : Activez l'agent SNMP
   * **Description** : Description de l'appareil
   * **Location** : Emplacement physique de l'appareil
   * **Contact** : Informations de contact
3. Configurez les communautés SNMP (pour SNMPv1/v2c) ou les utilisateurs (pour SNMPv3)
4. Spécifiez les hôtes autorisés à interroger l'agent SNMP
5. Configurez les traps SNMP pour les notifications d'événements
6. Cliquez sur **Apply** pour enregistrer la configuration

Exemple de configuration CLI pour SNMP :

```
config system snmp sysinfo
    set status enable
    set description "FortiGate Datacenter"
    set location "Server Room A"
    set contact-info "admin@example.com"
end

config system snmp community
    edit 1
        set name "public"
        set access read-only
        config hosts
            edit 1
                set ip 192.168.1.100 255.255.255.255
            next
        end
    next
end

config system snmp user
    edit "snmpuser"
        set security-level auth-priv
        set auth-proto sha
        set auth-pwd "Auth_Password123"
        set priv-proto aes
        set priv-pwd "Priv_Password456"
        set queries enable
        set trap-status enable
        set events cpu-high mem-low log-full intf-ip vpn-tun-up vpn-tun-down
    next
end
```

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Sécurité SNMP</h4>
<p>SNMP, en particulier les versions 1 et 2c, présente des risques de sécurité. Limitez strictement les hôtes autorisés à interroger l'agent SNMP, utilisez des communautés non triviales, et préférez SNMPv3 avec authentification et chiffrement lorsque possible.</p>
</div>

#### MIBs FortiGate

FortiGate prend en charge plusieurs MIBs (Management Information Bases) :

* **MIBs standard** : MIB-II, IF-MIB, IP-MIB, etc.
* **MIBs Fortinet** : FORTINET-CORE-MIB, FORTINET-FORTIGATE-MIB

Pour télécharger les MIBs Fortinet :

1. Accédez à **System > SNMP**
2. Cliquez sur **Download FortiGate MIB File** et **Download Fortinet Core MIB File**
3. Importez ces MIBs dans votre système de gestion SNMP

### Configuration Syslog

Syslog permet d'envoyer les journaux FortiGate vers un serveur de journalisation centralisé.

#### Configuration d'un serveur Syslog

Pour configurer un serveur Syslog via l'interface web :

1. Accédez à **Log & Report > Log Settings**
2. Dans la section **Remote Logging and Archiving**, activez **Syslog**
3. Configurez les paramètres du serveur :
   * **IP/FQDN** : Adresse IP ou nom de domaine du serveur Syslog
   * **Port** : Port Syslog (généralement 514)
   * **Protocol** : UDP ou TCP
   * **Format** : Format des messages (par défaut, CSV, CEF)
   * **Facility** : Facility Syslog à utiliser
   * **Source IP** : Adresse IP source pour les messages Syslog
4. Sélectionnez les types de journaux à envoyer
5. Cliquez sur **Apply** pour enregistrer la configuration

Exemple de configuration CLI pour Syslog :

```
config log syslogd setting
    set status enable
    set server "192.168.1.200"
    set port 514
    set facility local7
    set format rfc5424
    set mode udp
    set filter "severity>=information"
end

config log syslogd filter
    set forward-traffic enable
    set local-traffic enable
    set multicast-traffic enable
    set sniffer-traffic disable
    set anomaly enable
    set voip disable
    set filter "srcip 10.0.0.0/24"
end
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Formats Syslog</h4>
<p>FortiGate prend en charge plusieurs formats de messages Syslog : le format par défaut de Fortinet, CSV pour une intégration facile avec des outils d'analyse, et CEF (Common Event Format) pour une compatibilité avec les solutions SIEM comme ArcSight.</p>
</div>

### Intégration avec des systèmes de monitoring tiers

FortiGate peut s'intégrer à divers systèmes de monitoring tiers :

#### Solutions SIEM (Security Information and Event Management)

* **Splunk** : Utilisez le Fortinet App for Splunk pour une intégration optimale
* **IBM QRadar** : Configurez un récepteur Syslog et des règles de corrélation
* **ArcSight** : Utilisez le format CEF pour une intégration native
* **ELK Stack** : Configurez Logstash pour parser les journaux FortiGate

#### Systèmes de monitoring réseau

* **Nagios/Icinga** : Utilisez SNMP pour surveiller l'état et les performances
* **PRTG** : Configurez des capteurs SNMP pour les métriques FortiGate
* **Zabbix** : Utilisez les templates FortiGate prédéfinis
* **SolarWinds** : Intégrez via SNMP et Syslog

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Monitoring centralisé</h4>
<p>Pour les environnements avec plusieurs appareils FortiGate, un système de monitoring centralisé est essentiel. Utilisez FortiManager et FortiAnalyzer pour une solution native Fortinet, ou intégrez avec votre système de monitoring existant via SNMP et Syslog pour une vue unifiée de votre infrastructure.</p>
</div>

<h2 id="alerting" style="color:#0D274D;">8.7 Alertes et notifications</h2>

Les alertes et notifications permettent d'être informé rapidement des événements importants ou critiques, facilitant une réponse rapide aux problèmes.

### Types d'alertes disponibles

FortiGate peut générer plusieurs types d'alertes :

* **Alertes système** : Problèmes matériels, utilisation élevée des ressources, etc.
* **Alertes de sécurité** : Détection de menaces, tentatives d'intrusion, etc.
* **Alertes VPN** : Problèmes de tunnels VPN
* **Alertes HA** : Basculements, problèmes de synchronisation, etc.
* **Alertes de conformité** : Violations de politiques de sécurité
* **Alertes de performance** : Goulots d'étranglement, latence élevée, etc.

### Configuration des alertes par email

Pour configurer les alertes par email via l'interface web :

1. Configurez d'abord le serveur SMTP :
   * Accédez à **System > Settings**
   * Dans la section **Email Service**, configurez les paramètres SMTP
   * Testez la configuration en envoyant un email de test

2. Configurez ensuite les alertes :
   * Accédez à **Log & Report > Alert E-mail**
   * Activez **Enable Alert E-mail**
   * Configurez les destinataires des alertes
   * Sélectionnez les événements qui déclencheront des alertes
   * Définissez la fréquence des alertes
   * Cliquez sur **Apply** pour enregistrer la configuration

Exemple de configuration CLI pour les alertes par email :

```
config system email-server
    set server "smtp.example.com"
    set port 587
    set security starttls
    set auth enable
    set username "alertuser"
    set password "AlertPassword123"
    set reply-to "fortialerts@example.com"
end

config alertemail setting
    set username "FortiGate Admin"
    set email-from "fortialerts@example.com"
    set email-to "admin@example.com"
    set alert-interval 5
    set critical-interval 1
    set emergency-interval 0
    set severity-level information
end
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Filtrage des alertes</h4>
<p>Configurez judicieusement le niveau de sévérité et les types d'événements qui déclenchent des alertes. Trop d'alertes peuvent conduire à une "fatigue d'alerte" où les notifications importantes sont ignorées parmi les nombreuses alertes mineures.</p>
</div>

### Alertes SNMP

Les traps SNMP permettent d'envoyer des alertes à un système de gestion SNMP :

1. Accédez à **System > SNMP**
2. Configurez une communauté SNMP (v1/v2c) ou un utilisateur (v3)
3. Dans la section **SNMP Traps**, configurez :
   * **Trap Status** : Activez les traps
   * **Trap Server IP** : Adresse IP du serveur de traps
   * **Trap Server Port** : Port du serveur (généralement 162)
   * **Trap Events** : Événements qui déclencheront des traps
4. Cliquez sur **Apply** pour enregistrer la configuration

### Alertes Syslog

Les événements critiques peuvent être envoyés à un serveur Syslog avec une priorité élevée :

1. Configurez un serveur Syslog comme décrit précédemment
2. Utilisez des filtres pour envoyer les événements critiques avec une priorité élevée
3. Configurez votre serveur Syslog pour traiter ces messages prioritaires de manière appropriée

### Automatisation des réponses aux alertes

FortiGate permet d'automatiser certaines réponses aux alertes via la fonctionnalité d'automatisation :

1. Accédez à **Security Fabric > Automation**
2. Cliquez sur **Create New**
3. Configurez le déclencheur (trigger) :
   * **Name** : Nom de l'automatisation
   * **Trigger** : Événement déclencheur (utilisation CPU élevée, détection de menace, etc.)
   * **Threshold** : Seuil de déclenchement si applicable
4. Configurez les actions à exécuter :
   * **Email** : Envoyer un email
   * **CLI Script** : Exécuter un script CLI
   * **Webhook** : Appeler un webhook externe
   * **Alert** : Générer une alerte dans l'interface
   * **Disable Interface/Quarantine** : Désactiver une interface ou mettre en quarantaine
5. Cliquez sur **OK** pour enregistrer l'automatisation

Exemple de configuration CLI pour une automatisation :

```
config system automation-action
    edit "high-cpu-email"
        set action-type email
        set email-to "admin@example.com"
        set email-subject "FortiGate High CPU Alert"
        set email-body "CPU usage has exceeded threshold on %device_name%."
    next
end

config system automation-trigger
    edit "high-cpu"
        set trigger-type event-based
        set event-type high-cpu
        set threshold 90
        config actions
            edit 1
                set action-id "high-cpu-email"
            next
        end
    next
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Automatisation avancée</h4>
<p>Pour une automatisation plus avancée, combinez les webhooks FortiGate avec des outils comme Zapier, Microsoft Flow, ou des scripts personnalisés. Cela permet d'intégrer les alertes FortiGate à vos systèmes existants comme les plateformes de ticketing, les outils de collaboration, ou les systèmes de notification d'astreinte.</p>
</div>

---

<h1 id="cli" style="color:#E23237;">9. Commandes CLI FortiGate</h1>

<h2 id="cli-basics" style="color:#0D274D;">9.1 Introduction à l'interface en ligne de commande</h2>

L'interface en ligne de commande (CLI) de FortiGate offre un contrôle plus précis et des fonctionnalités avancées qui ne sont pas toujours disponibles dans l'interface web. Cette section présente les bases de l'utilisation de la CLI FortiGate.

### Accès à la CLI

Il existe plusieurs méthodes pour accéder à la CLI FortiGate :

* **Console série** : Connexion directe via le port console de l'appareil
* **SSH** : Accès à distance sécurisé via le protocole SSH
* **Telnet** : Accès à distance non sécurisé (déconseillé, désactivé par défaut)
* **Interface web** : Accès via la console CLI intégrée dans l'interface web

#### Accès via SSH

Pour se connecter via SSH :

1. Assurez-vous que l'accès SSH est activé sur l'interface de gestion
2. Utilisez un client SSH comme PuTTY, OpenSSH ou SecureCRT
3. Connectez-vous à l'adresse IP de l'interface de gestion
4. Authentifiez-vous avec vos identifiants administrateur

```
ssh admin@192.168.1.99
```

#### Accès via la console CLI dans l'interface web

Pour accéder à la CLI depuis l'interface web :

1. Connectez-vous à l'interface web
2. Cliquez sur l'icône de terminal dans le coin supérieur droit
3. Une fenêtre de console CLI s'ouvre dans l'interface web

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Avantages de la CLI</h4>
<p>La CLI offre plusieurs avantages par rapport à l'interface web : accès à des fonctionnalités avancées, possibilité d'automatisation via des scripts, configuration plus rapide pour les administrateurs expérimentés, et accès même lorsque l'interface web n'est pas disponible.</p>
</div>

### Structure de la CLI

La CLI FortiGate est organisée hiérarchiquement :

* **Mode global** : Niveau supérieur, indiqué par le prompt `#`
* **Mode de configuration** : Pour modifier la configuration, indiqué par le prompt `(config)#`
* **Sous-modes de configuration** : Pour configurer des sections spécifiques

Exemple de navigation dans la hiérarchie :

```
# config system interface       // Entre dans le mode de configuration des interfaces
(config-system)# edit port1     // Entre dans la configuration de l'interface port1
(config-system-interface)# set ip 192.168.1.1 255.255.255.0  // Configure l'adresse IP
(config-system-interface)# end  // Revient au mode global
#
```

### Commandes de base

Voici quelques commandes de base essentielles :

* `?` : Affiche l'aide contextuelle
* `get` : Affiche les informations de configuration
* `show` : Affiche la configuration complète
* `config` : Entre dans un mode de configuration
* `edit` : Modifie un élément spécifique
* `set` : Définit une valeur
* `unset` : Supprime une valeur
* `end` : Quitte le mode de configuration actuel et applique les changements
* `abort` : Quitte le mode de configuration sans appliquer les changements
* `exit` : Quitte le niveau actuel ou se déconnecte

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Utilisation de l'aide contextuelle</h4>
<p>Utilisez abondamment la commande "?" pour découvrir les options disponibles à chaque niveau. L'aide contextuelle affiche les commandes disponibles, leur syntaxe et souvent une brève description de leur fonction.</p>
</div>

### Syntaxe des commandes

La syntaxe générale des commandes FortiGate est la suivante :

```
command [object] [action] [parameters]
```

Exemples :

```
# get system status                   // Affiche l'état du système
# config firewall policy              // Entre dans la configuration des politiques de pare-feu
# set srcintf "port1"                 // Définit l'interface source
# show firewall policy 1              // Affiche la configuration de la politique 1
```

### Modes d'affichage

FortiGate propose différents modes d'affichage pour les commandes `show` et `get` :

* **Standard** : Affichage par défaut
* **Verbose** : Affichage détaillé avec toutes les options
* **Filtered** : Affichage filtré selon des critères spécifiques

Exemples :

```
# show system interface               // Affichage standard
# show full-configuration             // Affichage complet de la configuration
# show | grep port1                   // Filtrage avec grep
```

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Attention aux modifications</h4>
<p>Contrairement à certains autres équipements réseau, les modifications dans la CLI FortiGate sont appliquées immédiatement lorsque vous quittez un mode de configuration avec "end". Il n'y a pas de concept de "configuration candidate" ou de "commit". Soyez donc prudent lors des modifications, surtout dans un environnement de production.</p>
</div>

<h2 id="system-commands" style="color:#0D274D;">9.2 Commandes système</h2>

Les commandes système permettent de configurer et de surveiller les paramètres fondamentaux du FortiGate. Cette section présente les commandes système les plus utiles.

### Informations système

Pour afficher les informations de base sur le système :

```
# get system status
```

Cette commande affiche des informations comme :
* Version du firmware
* Mode de fonctionnement
* Modèle de l'appareil
* Numéro de série
* Temps de fonctionnement
* État des licences

Pour afficher les informations sur les ressources système :

```
# get system performance status
```

Cette commande affiche :
* Utilisation du CPU
* Utilisation de la mémoire
* Température (sur les modèles équipés de capteurs)
* Statistiques de sessions
* Débit

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Surveillance régulière</h4>
<p>Exécutez régulièrement "get system performance status" pour surveiller l'état de santé de votre FortiGate. Une augmentation soudaine de l'utilisation du CPU ou de la mémoire peut indiquer un problème à investiguer.</p>
</div>

### Configuration des paramètres système

#### Configuration du nom d'hôte et de l'emplacement

```
# config system global
    set hostname "DC1-FGT-Primary"
    set location "Datacenter 1, Rack 3"
end
```

#### Configuration de la date et de l'heure

```
# config system time
    set timezone 28    // Correspond à GMT+1 (Paris)
    set daylight-saving-time enable
end

# execute date 2023-05-15
# execute time 14:30:00
```

Pour configurer NTP (Network Time Protocol) :

```
# config system ntp
    set status enable
    set server-mode enable
    config servers
        edit 1
            set server "0.pool.ntp.org"
        next
        edit 2
            set server "1.pool.ntp.org"
        next
    end
end
```

#### Configuration des administrateurs

Pour créer un nouvel administrateur :

```
# config system admin
    edit "nouvel-admin"
        set password "Mot_de_passe_sécurisé"
        set accprofile "super_admin"
        set vdom "root"
        set ssh-public-key1 "ssh-rsa AAAAB3NzaC1yc2E..."
    next
end
```

Pour configurer l'authentification à deux facteurs :

```
# config system admin
    edit "admin"
        set two-factor fortitoken
        set fortitoken "FTK0123456789"
    next
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Sécurisation des accès administrateurs</h4>
<p>Pour renforcer la sécurité, configurez des profils d'accès restreints pour les administrateurs selon le principe du moindre privilège, activez l'authentification à deux facteurs, et utilisez des clés SSH plutôt que des mots de passe lorsque c'est possible.</p>
</div>

### Gestion des firmwares

Pour vérifier les firmwares disponibles :

```
# diagnose fdsm updlist
```

Pour mettre à jour le firmware :

```
# execute restore image tftp firmware.out 192.168.1.100
```

Pour revenir à un firmware précédent :

```
# execute factoryreset
```

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Précautions pour les mises à jour</h4>
<p>Avant toute mise à jour de firmware, sauvegardez la configuration, vérifiez la compatibilité de la nouvelle version avec vos fonctionnalités, et prévoyez une fenêtre de maintenance. La commande factoryreset réinitialise l'appareil aux paramètres d'usine, donc utilisez-la avec précaution.</p>
</div>

### Sauvegarde et restauration de la configuration

Pour sauvegarder la configuration :

```
# execute backup config tftp backup.conf 192.168.1.100
# execute backup config usb backup.conf
```

Pour restaurer une configuration :

```
# execute restore config tftp backup.conf 192.168.1.100
# execute restore config usb backup.conf
```

### Redémarrage et arrêt

Pour redémarrer le FortiGate :

```
# execute reboot
```

Pour arrêter le FortiGate :

```
# execute shutdown
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Confirmation des commandes critiques</h4>
<p>Les commandes critiques comme reboot, shutdown ou factoryreset demandent une confirmation avant exécution. Assurez-vous de comprendre l'impact de ces commandes avant de les confirmer, surtout dans un environnement de production.</p>
</div>

<h2 id="network-commands" style="color:#0D274D;">9.3 Commandes réseau</h2>

Les commandes réseau permettent de configurer et de surveiller les interfaces, le routage et les services réseau du FortiGate. Cette section présente les commandes réseau les plus utiles.

### Configuration des interfaces

Pour afficher les interfaces réseau :

```
# get system interface
# diagnose hardware deviceinfo nic port1
```

Pour configurer une interface :

```
# config system interface
    edit "port1"
        set mode static
        set ip 192.168.1.1 255.255.255.0
        set allowaccess ping https ssh
        set description "WAN Interface"
        set alias "Internet"
        set role wan
    next
end
```

Pour configurer une interface VLAN :

```
# config system interface
    edit "VLAN100"
        set vdom "root"
        set ip 10.100.0.1 255.255.255.0
        set allowaccess ping
        set description "VLAN 100"
        set vlanid 100
        set interface "port2"
    next
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Sécurisation des interfaces</h4>
<p>Limitez les services d'accès administratif (allowaccess) au strict nécessaire pour chaque interface. Par exemple, n'activez SSH et HTTPS que sur les interfaces de gestion, et jamais sur les interfaces WAN sauf si absolument nécessaire.</p>
</div>

### Configuration du routage

Pour afficher la table de routage :

```
# get router info routing-table all
```

Pour configurer une route statique :

```
# config router static
    edit 1
        set dst 0.0.0.0 0.0.0.0
        set gateway 192.168.1.254
        set device "port1"
        set distance 10
        set priority 0
    next
end
```

Pour configurer OSPF :

```
# config router ospf
    set router-id 10.0.0.1
    config area
        edit 0.0.0.0
        next
    end
    config network
        edit 1
            set prefix 10.0.0.0 255.255.255.0
            set area 0.0.0.0
        next
    end
end
```

Pour configurer BGP :

```
# config router bgp
    set as 65001
    set router-id 10.0.0.1
    config neighbor
        edit "10.0.0.2"
            set remote-as 65002
        next
    end
    config network
        edit 1
            set prefix 192.168.0.0 255.255.0.0
        next
    end
end
```

### Configuration DHCP

Pour configurer un serveur DHCP :

```
# config system dhcp server
    edit 1
        set interface "port2"
        set ip-mode range
        set default-gateway 192.168.2.1
        set netmask 255.255.255.0
        set dns-service default
        config ip-range
            edit 1
                set start-ip 192.168.2.100
                set end-ip 192.168.2.200
            next
        end
        config reserved-address
            edit 1
                set ip 192.168.2.50
                set mac 00:11:22:33:44:55
                set description "Imprimante"
            next
        end
    next
end
```

Pour configurer un relais DHCP :

```
# config system dhcp server
    edit 1
        set interface "port2"
        set relay-service enable
        set relay-ip 10.0.0.100
    next
end
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Réservations DHCP</h4>
<p>Utilisez les réservations d'adresses DHCP pour les appareils qui nécessitent une adresse IP fixe mais qui sont configurés pour obtenir leur adresse via DHCP. Cela centralise la gestion des adresses IP et évite les conflits d'adresses.</p>
</div>

### Outils de diagnostic réseau

FortiGate propose plusieurs outils de diagnostic réseau via la CLI :

#### Ping

```
# execute ping 8.8.8.8
# execute ping-options source 192.168.1.1
# execute ping-options count 10
# execute ping-options size 1500
# execute ping 8.8.8.8
```

#### Traceroute

```
# execute traceroute 8.8.8.8
```

#### Capture de paquets

```
# diagnose sniffer packet port1 "host 8.8.8.8" 4 0 a
```

Les paramètres sont :
* `port1` : Interface à surveiller
* `"host 8.8.8.8"` : Filtre de capture (syntaxe tcpdump)
* `4` : Niveau de verbosité (0-4)
* `0` : Nombre de paquets à capturer (0 = illimité)
* `a` : Affichage ASCII des données

Pour arrêter la capture, appuyez sur Ctrl+C.

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Filtres de capture avancés</h4>
<p>Maîtrisez la syntaxe des filtres tcpdump pour des captures de paquets ciblées. Par exemple, "host 192.168.1.10 and port 80" capture uniquement le trafic HTTP vers/depuis 192.168.1.10, ou "tcp[tcpflags] & (tcp-syn|tcp-fin) != 0" capture uniquement les paquets SYN et FIN.</p>
</div>

### Diagnostic des sessions

Pour afficher les sessions actives :

```
# diagnose sys session list
```

Pour filtrer les sessions :

```
# diagnose sys session filter src 192.168.1.10
# diagnose sys session filter dst 8.8.8.8
# diagnose sys session filter proto 6    // TCP
# diagnose sys session filter port 80
# diagnose sys session list
```

Pour effacer les sessions :

```
# diagnose sys session clear
```

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Impact sur les connexions</h4>
<p>La commande "diagnose sys session clear" termine toutes les sessions actives, ce qui peut interrompre les communications en cours. Utilisez-la avec précaution, de préférence pendant une fenêtre de maintenance.</p>
</div>

<h2 id="firewall-commands" style="color:#0D274D;">9.4 Commandes de pare-feu</h2>

Les commandes de pare-feu permettent de configurer et de surveiller les politiques de sécurité, les objets et les fonctionnalités UTM du FortiGate. Cette section présente les commandes de pare-feu les plus utiles.

### Configuration des politiques de pare-feu

Pour afficher les politiques de pare-feu :

```
# show firewall policy
# diagnose firewall policy list
```

Pour créer une politique de pare-feu :

```
# config firewall policy
    edit 1
        set name "LAN to WAN"
        set srcintf "port2"
        set dstintf "port1"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
        set nat enable
    next
end
```

Pour configurer une politique avec des profils de sécurité :

```
# config firewall policy
    edit 2
        set name "Secure Web Access"
        set srcintf "port2"
        set dstintf "port1"
        set srcaddr "Internal_Network"
        set dstaddr "all"
        set action accept
        set schedule "business-hours"
        set service "HTTP" "HTTPS"
        set utm-status enable
        set av-profile "default"
        set webfilter-profile "default"
        set ips-sensor "default"
        set application-list "default"
        set ssl-ssh-profile "certificate-inspection"
        set logtraffic all
        set nat enable
    next
end
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Organisation des politiques</h4>
<p>Organisez vos politiques de manière logique, avec les politiques les plus spécifiques en haut et les plus générales en bas. Utilisez des noms descriptifs et des commentaires pour documenter l'objectif de chaque politique.</p>
</div>

### Configuration des objets

#### Objets d'adresse

```
# config firewall address
    edit "Internal_Network"
        set subnet 192.168.2.0 255.255.255.0
        set comment "LAN network"
    next
    edit "Web_Servers"
        set type iprange
        set start-ip 10.0.0.10
        set end-ip 10.0.0.20
        set comment "Web server farm"
    next
end
```

#### Groupes d'adresses

```
# config firewall addrgrp
    edit "Internal_Resources"
        set member "Internal_Network" "Web_Servers"
        set comment "All internal resources"
    next
end
```

#### Objets de service

```
# config firewall service custom
    edit "Custom_Web"
        set tcp-portrange 8080-8090
        set comment "Custom web services"
    next
end
```

#### Groupes de services

```
# config firewall service group
    edit "Web_Services"
        set member "HTTP" "HTTPS" "Custom_Web"
        set comment "All web services"
    next
end
```

### Configuration des profils de sécurité

#### Profil antivirus

```
# config antivirus profile
    edit "custom-av"
        set comment "Custom antivirus profile"
        config http
            set av-scan enable
            set outbreak-prevention enable
        end
        config ftp
            set av-scan enable
            set outbreak-prevention enable
        end
        config imap
            set av-scan enable
            set outbreak-prevention enable
        end
        config pop3
            set av-scan enable
            set outbreak-prevention enable
        end
        config smtp
            set av-scan enable
            set outbreak-prevention enable
        end
    next
end
```

#### Profil de filtrage web

```
# config webfilter profile
    edit "custom-webfilter"
        set comment "Custom web filter profile"
        config ftgd-wf
            set options https-scan
            config filters
                edit 1
                    set category 26    // Malware
                    set action block
                next
                edit 2
                    set category 61    // Phishing
                    set action block
                next
                edit 3
                    set category 2     // Drug Abuse
                    set action block
                next
            end
        end
    next
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Profils personnalisés</h4>
<p>Créez des profils de sécurité personnalisés adaptés à vos besoins spécifiques plutôt que d'utiliser les profils par défaut. Cela vous permet d'ajuster précisément les paramètres de sécurité pour différents types de trafic et d'utilisateurs.</p>
</div>

### Diagnostic et dépannage du pare-feu

#### Vérification de la correspondance des politiques

Pour vérifier quelle politique s'applique à un trafic spécifique :

```
# diagnose firewall iprope lookup 192.168.2.10 8.8.8.8 1 53 17 0
```

Les paramètres sont :
* `192.168.2.10` : Adresse IP source
* `8.8.8.8` : Adresse IP destination
* `1` : ID de l'interface entrante
* `53` : Port destination
* `17` : Protocole (17 = UDP)
* `0` : ID de l'interface sortante (0 = auto)

#### Débogage des politiques

```
# diagnose debug reset
# diagnose debug flow filter addr 192.168.2.10
# diagnose debug flow show function-name enable
# diagnose debug flow trace start 100
# diagnose debug enable
```

Pour arrêter le débogage :

```
# diagnose debug disable
```

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Impact du débogage</h4>
<p>Le débogage peut avoir un impact significatif sur les performances, surtout dans un environnement à haut débit. Utilisez-le avec parcimonie, avec des filtres précis, et désactivez-le dès que vous avez obtenu les informations nécessaires.</p>
</div>

<h2 id="vpn-commands" style="color:#0D274D;">9.5 Commandes VPN</h2>

Les commandes VPN permettent de configurer et de surveiller les tunnels VPN IPsec et SSL du FortiGate. Cette section présente les commandes VPN les plus utiles.

### Configuration VPN IPsec

#### Configuration d'un VPN IPsec site-à-site

```
# config vpn ipsec phase1-interface
    edit "Site_B_VPN"
        set interface "port1"
        set ike-version 2
        set peertype any
        set proposal aes256-sha256
        set dhgrp 14
        set remote-gw 203.0.113.2
        set psksecret "SecurePreSharedKey123!"
    next
end

# config vpn ipsec phase2-interface
    edit "Site_B_VPN_P2"
        set phase1name "Site_B_VPN"
        set proposal aes256-sha256
        set dhgrp 14
        set src-addr-type subnet
        set dst-addr-type subnet
        set src-subnet 192.168.1.0 255.255.255.0
        set dst-subnet 192.168.2.0 255.255.255.0
    next
end
```

#### Configuration d'un VPN IPsec dial-up (accès distant)

```
# config vpn ipsec phase1-interface
    edit "Dialup_VPN"
        set type dynamic
        set interface "port1"
        set mode aggressive
        set ike-version 2
        set peertype any
        set proposal aes256-sha256
        set dhgrp 14
        set psksecret "SecurePreSharedKey123!"
        set dpd on-idle
        set xauthtype auto
        set authusrgrp "VPN_Users"
    next
end

# config vpn ipsec phase2-interface
    edit "Dialup_VPN_P2"
        set phase1name "Dialup_VPN"
        set proposal aes256-sha256
        set dhgrp 14
        set src-addr-type subnet
        set dst-addr-type subnet
        set src-subnet 0.0.0.0 0.0.0.0
        set dst-subnet 192.168.1.0 255.255.255.0
    next
end
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Sélection des algorithmes</h4>
<p>Choisissez des algorithmes de chiffrement et d'intégrité forts pour vos VPNs. AES-256 pour le chiffrement, SHA-256 ou supérieur pour l'intégrité, et des groupes DH 14 ou supérieurs pour l'échange de clés offrent un bon équilibre entre sécurité et performances.</p>
</div>

### Configuration VPN SSL

#### Configuration du portail SSL VPN

```
# config vpn ssl settings
    set servercert "Fortinet_Factory"
    set tunnel-ip-pools "SSLVPN_TUNNEL_ADDR1"
    set tunnel-ipv6-pools "SSLVPN_TUNNEL_IPv6_ADDR1"
    set dns-server1 192.168.1.1
    set dns-server2 8.8.8.8
    set port 443
    set source-interface "port1"
    set default-portal "full-access"
end

# config vpn ssl web portal
    edit "full-access"
        set tunnel-mode enable
        set web-mode enable
        set ip-pools "SSLVPN_TUNNEL_ADDR1"
        set split-tunneling disable
        set ipv6-tunnel-mode disable
        set ipv6-pools "SSLVPN_TUNNEL_IPv6_ADDR1"
        set ipv6-split-tunneling disable
        set ipv6-dns-server1 ::
        set ipv6-dns-server2 ::
        set ipv6-wins-server1 ::
        set ipv6-wins-server2 ::
        set dns-suffix ""
        set idle-timeout 0
        set idle-timeout-warn-type banner
        set idle-timeout-warning 60
        set user-bookmark disable
        set user-group-bookmark disable
        set web-portal disable
        set keep-alive enable
        set save-password disable
        set display-connection-tools enable
        set display-history enable
        set display-status enable
        set heading "SSL-VPN Portal"
        set redir-url ""
        set theme blue
        set custom-lang ""
        set host-check none
        set host-check-interval 0
        set host-check-policy ""
    next
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Portails personnalisés</h4>
<p>Créez des portails SSL VPN personnalisés pour différents groupes d'utilisateurs avec des niveaux d'accès et des fonctionnalités adaptés à leurs besoins. Par exemple, un portail pour les administrateurs avec un accès complet, et un portail pour les utilisateurs standard avec un accès limité.</p>
</div>

### Diagnostic et dépannage VPN

#### Vérification de l'état des tunnels IPsec

```
# diagnose vpn ike gateway list
# diagnose vpn tunnel list
```

#### Vérification de l'état SSL VPN

```
# diagnose vpn ssl list
```

#### Débogage VPN IPsec

```
# diagnose debug reset
# diagnose debug application ike -1
# diagnose debug enable
```

Pour arrêter le débogage :

```
# diagnose debug disable
```

#### Effacement des SA IPsec

Pour forcer une renégociation des tunnels IPsec :

```
# diagnose vpn tunnel flush name Site_B_VPN
```

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Interruption des tunnels</h4>
<p>La commande "diagnose vpn tunnel flush" interrompt les tunnels VPN actifs, ce qui peut perturber les communications en cours. Utilisez-la avec précaution, de préférence pendant une fenêtre de maintenance.</p>
</div>

<h2 id="scripting" style="color:#0D274D;">9.6 Scripting et automatisation</h2>

FortiGate permet d'automatiser des tâches via des scripts CLI et des fonctionnalités d'automatisation. Cette section présente les bases du scripting et de l'automatisation sur FortiGate.

### Scripts CLI

Les scripts CLI permettent d'exécuter une série de commandes FortiGate de manière automatisée.

#### Création d'un script CLI

```
# config system cli-script
    edit "backup-config"
        set script "
config global
execute backup config ftp backup_\$(date +'%Y-%m-%d').conf 192.168.1.100 username password
end
"
    next
end
```

#### Exécution d'un script CLI

```
# execute cli-script name backup-config
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Variables dans les scripts</h4>
<p>Vous pouvez utiliser des variables shell dans vos scripts CLI en utilisant la syntaxe $(commande). Par exemple, $(date +'%Y-%m-%d') insère la date actuelle au format YYYY-MM-DD.</p>
</div>

### Automatisation

La fonctionnalité d'automatisation permet de déclencher des actions en réponse à des événements spécifiques.

#### Configuration d'une automatisation

```
# config system automation-action
    edit "high-cpu-email"
        set action-type email
        set email-to "admin@example.com"
        set email-subject "FortiGate High CPU Alert"
        set email-body "CPU usage has exceeded threshold on %device_name%."
    next
end

# config system automation-trigger
    edit "high-cpu"
        set trigger-type event-based
        set event-type high-cpu
        set threshold 90
        config actions
            edit 1
                set action-id "high-cpu-email"
            next
        end
    next
end
```

#### Types de déclencheurs disponibles

* **event-based** : Basé sur des événements système
* **scheduled** : Basé sur une planification
* **reboot** : Déclenché au redémarrage
* **config-change** : Déclenché lors d'un changement de configuration
* **security-rating-summary** : Basé sur l'évaluation de sécurité

#### Types d'actions disponibles

* **email** : Envoi d'un email
* **alert** : Génération d'une alerte dans l'interface
* **cli-script** : Exécution d'un script CLI
* **webhook** : Appel d'un webhook externe
* **azure-function** : Appel d'une fonction Azure
* **google-cloud-function** : Appel d'une fonction Google Cloud
* **aws-lambda** : Appel d'une fonction AWS Lambda
* **disable-interface** : Désactivation d'une interface
* **quarantine** : Mise en quarantaine d'un hôte

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Automatisation avancée</h4>
<p>Combinez les scripts CLI et les automatisations pour créer des solutions puissantes. Par exemple, créez un script qui génère un rapport personnalisé, puis configurez une automatisation pour exécuter ce script chaque semaine et envoyer le rapport par email.</p>
</div>

### Exemples de scripts utiles

#### Sauvegarde automatique de la configuration

```
config system cli-script
    edit "daily-backup"
        set script "
config global
execute backup config ftp FortiGate_\$(hostname)_\$(date +'%Y-%m-%d').conf 192.168.1.100 backup P@ssw0rd
end
"
    next
end

config system automation-trigger
    edit "daily-backup-trigger"
        set trigger-type scheduled
        set schedule daily
        set hour 23
        set minute 0
        config actions
            edit 1
                set action-id "daily-backup-script"
            next
        end
    next
end

config system automation-action
    edit "daily-backup-script"
        set action-type cli-script
        set script "daily-backup"
    next
end
```

#### Notification de changement de configuration

```
config system automation-action
    edit "config-change-email"
        set action-type email
        set email-to "admin@example.com"
        set email-subject "FortiGate Configuration Changed"
        set email-body "Configuration has been changed on %device_name% by %admin_user% at %time_str%."
    next
end

config system automation-trigger
    edit "config-change-trigger"
        set trigger-type config-change
        config actions
            edit 1
                set action-id "config-change-email"
            next
        end
    next
end
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Documentation des scripts</h4>
<p>Documentez soigneusement vos scripts et automatisations, en incluant leur objectif, leur fonctionnement, et les conditions dans lesquelles ils sont déclenchés. Cela facilitera la maintenance et le dépannage, surtout pour les autres administrateurs qui pourraient ne pas être familiers avec votre travail.</p>
</div>

---

<h1 id="annexes" style="color:#E23237;">10. Annexes</h1>

<h2 id="ports-services" style="color:#0D274D;">10.1 Tableau des ports et services Fortinet</h2>

Cette section présente un tableau complet des ports et services utilisés par les produits Fortinet, ce qui est essentiel pour la configuration correcte des pare-feu et la résolution des problèmes de connectivité.

### Ports utilisés par FortiGate

| Port | Protocole | Service | Description | Direction |
|------|-----------|---------|-------------|-----------|
| 22 | TCP | SSH | Accès en ligne de commande sécurisé | Entrant |
| 23 | TCP | Telnet | Accès en ligne de commande non sécurisé (désactivé par défaut) | Entrant |
| 80 | TCP | HTTP | Interface web (redirection vers HTTPS) | Entrant |
| 443 | TCP | HTTPS | Interface web sécurisée | Entrant |
| 161 | UDP | SNMP | Monitoring via SNMP | Entrant |
| 162 | UDP | SNMP Trap | Notifications SNMP | Sortant |
| 514 | UDP/TCP | Syslog | Envoi de journaux vers serveur Syslog | Sortant |
| 500 | UDP | IKE | Négociation VPN IPsec | Entrant/Sortant |
| 4500 | UDP | IPsec NAT-T | VPN IPsec à travers NAT | Entrant/Sortant |
| 1812 | UDP | RADIUS Auth | Authentification RADIUS | Sortant |
| 1813 | UDP | RADIUS Accounting | Accounting RADIUS | Sortant |
| 389 | TCP | LDAP | Authentification LDAP | Sortant |
| 636 | TCP | LDAPS | Authentification LDAP sécurisée | Sortant |
| 53 | UDP/TCP | DNS | Résolution de noms | Sortant |
| 8080 | TCP | Proxy explicite | Service de proxy web explicite | Entrant |
| 541 | TCP/UDP | FortiManager | Communication avec FortiManager | Sortant |
| 514 | UDP | FortiAnalyzer | Envoi de journaux vers FortiAnalyzer (ancien) | Sortant |
| 25 | TCP | SMTP | Envoi d'alertes par email | Sortant |

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Ports personnalisables</h4>
<p>La plupart des ports mentionnés ci-dessus peuvent être modifiés dans la configuration. Par exemple, vous pouvez configurer l'interface web HTTPS pour utiliser un port autre que 443, ou le service SSH pour utiliser un port autre que 22.</p>
</div>

### Ports utilisés pour la communication entre produits Fortinet

| Port | Protocole | Service | Description |
|------|-----------|---------|-------------|
| 541 | TCP/UDP | FortiGate ↔ FortiManager | Communication de gestion |
| 514 | UDP | FortiGate → FortiAnalyzer | Envoi de journaux (ancien) |
| 8888-8899 | TCP | FortiGate → FortiSandbox | Soumission de fichiers pour analyse |
| 443 | TCP | FortiClient ↔ FortiGate | Communication EMS et portail captif |
| 8013 | TCP | FortiAuthenticator ↔ FortiGate | Communication pour authentification |
| 1813 | UDP | FortiAuthenticator → FortiGate | RADIUS Accounting |
| 5246 | TCP | FortiAP → FortiGate | Communication de contrôle CAPWAP |
| 5247 | UDP | FortiAP → FortiGate | Communication de données CAPWAP |
| 443 | TCP | FortiSwitch → FortiGate | FortiLink management |

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Sécurisation des communications</h4>
<p>Pour sécuriser les communications entre les produits Fortinet, configurez des règles de pare-feu strictes autorisant uniquement les ports nécessaires entre les adresses IP spécifiques des appareils. Évitez d'utiliser des règles trop permissives comme "any/any".</p>
</div>

### Ports des services courants filtrés par FortiGate

| Port | Protocole | Service | Description |
|------|-----------|---------|-------------|
| 20-21 | TCP | FTP | Transfert de fichiers |
| 22 | TCP | SSH/SFTP | Shell sécurisé et transfert de fichiers sécurisé |
| 23 | TCP | Telnet | Terminal non sécurisé |
| 25 | TCP | SMTP | Envoi d'emails |
| 53 | UDP/TCP | DNS | Résolution de noms |
| 80 | TCP | HTTP | Web non sécurisé |
| 110 | TCP | POP3 | Réception d'emails |
| 143 | TCP | IMAP | Accès aux emails |
| 443 | TCP | HTTPS | Web sécurisé |
| 445 | TCP | SMB | Partage de fichiers Windows |
| 993 | TCP | IMAPS | Accès aux emails sécurisé |
| 995 | TCP | POP3S | Réception d'emails sécurisée |
| 1433 | TCP | MS SQL | Base de données Microsoft SQL Server |
| 1521 | TCP | Oracle | Base de données Oracle |
| 3306 | TCP | MySQL | Base de données MySQL |
| 3389 | TCP | RDP | Bureau à distance Windows |
| 5060-5061 | UDP/TCP | SIP | Téléphonie IP (signalisation) |
| 5432 | TCP | PostgreSQL | Base de données PostgreSQL |
| 8080 | TCP | HTTP Alternate | Web alternatif (souvent proxy) |

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Services sensibles</h4>
<p>Certains services comme Telnet (port 23), FTP (ports 20-21), HTTP (port 80), ou SMTP/POP3/IMAP non sécurisés transmettent les données en clair. Privilégiez leurs équivalents sécurisés (SSH, SFTP, HTTPS, SMTPS, POP3S, IMAPS) lorsque c'est possible.</p>
</div>

<h2 id="glossaire" style="color:#0D274D;">10.2 Glossaire des termes Fortinet</h2>

Ce glossaire présente les termes et acronymes spécifiques à l'environnement Fortinet, facilitant la compréhension de la documentation et des interfaces.

### A-C

**ADVPN (Auto-Discovery VPN)** : Technologie Fortinet permettant la création dynamique de tunnels VPN directs entre sites distants.

**ATP (Advanced Threat Protection)** : Ensemble de technologies avancées pour la détection et la prévention des menaces sophistiquées.

**CAPWAP (Control and Provisioning of Wireless Access Points)** : Protocole utilisé pour la gestion des points d'accès sans fil FortiAP.

**CLI (Command Line Interface)** : Interface en ligne de commande pour la configuration et la gestion des appareils Fortinet.

**CSMA (Collaborative Security Mesh Architecture)** : Architecture de sécurité collaborative de Fortinet, permettant l'intégration et la coordination de différents produits de sécurité.

**CSF (Cybersecurity Framework)** : Cadre de cybersécurité développé par Fortinet pour aider les organisations à évaluer et améliorer leur posture de sécurité.

### D-F

**DLP (Data Loss Prevention)** : Fonctionnalité permettant de prévenir la fuite de données sensibles.

**DTLS (Datagram Transport Layer Security)** : Protocole de sécurité utilisé dans certaines implémentations VPN de Fortinet.

**EMS (Endpoint Management Server)** : Serveur de gestion des terminaux FortiClient.

**FAP (FortiAP)** : Point d'accès sans fil de Fortinet.

**FAZ (FortiAnalyzer)** : Solution de gestion des journaux et de reporting de Fortinet.

**FDN (FortiGuard Distribution Network)** : Réseau de distribution des mises à jour FortiGuard.

**FDS (FortiGuard Distribution Server)** : Serveur de distribution des mises à jour FortiGuard.

**FGT (FortiGate)** : Appliance de sécurité réseau principale de Fortinet.

**FMG (FortiManager)** : Solution de gestion centralisée des appareils Fortinet.

**FNDN (Fortinet Developer Network)** : Réseau de développeurs Fortinet, fournissant des ressources pour l'intégration et l'automatisation.

**FortiASIC** : Circuits intégrés spécifiques à l'application développés par Fortinet pour accélérer les fonctions de sécurité.

**FortiGuard** : Service de renseignements sur les menaces de Fortinet, fournissant des mises à jour de sécurité et des signatures.

**FortiOS** : Système d'exploitation des appareils FortiGate.

**FortiSandbox** : Solution d'analyse avancée des menaces inconnues.

**FSSO (Fortinet Single Sign-On)** : Solution d'authentification unique de Fortinet.

**FSW (FortiSwitch)** : Commutateur réseau géré par FortiGate via FortiLink.

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Abréviations dans la CLI</h4>
<p>Dans la CLI FortiGate, de nombreuses commandes utilisent des abréviations des termes ci-dessus. Par exemple, "diag sys ha status" pour "diagnose system high-availability status" ou "get router info routing-table all" pour afficher la table de routage complète.</p>
</div>

### G-L

**HA (High Availability)** : Haute disponibilité, fonctionnalité permettant la redondance des appareils FortiGate.

**IPS (Intrusion Prevention System)** : Système de prévention d'intrusion intégré à FortiGate.

**IPsec (Internet Protocol Security)** : Protocole de sécurité utilisé pour les VPNs.

**ISFW (Internal Segmentation Firewall)** : Pare-feu de segmentation interne, concept de déploiement FortiGate pour la segmentation du réseau interne.

**LDAP (Lightweight Directory Access Protocol)** : Protocole d'accès aux annuaires, utilisé pour l'authentification.

**LENC (Light Encrypted Non-Commercial)** : Version limitée de FortiOS pour certains marchés.

### M-R

**NAC (Network Access Control)** : Contrôle d'accès réseau, fonctionnalité de sécurité pour contrôler l'accès des appareils au réseau.

**NGFW (Next-Generation Firewall)** : Pare-feu de nouvelle génération, catégorie d'appareils dont fait partie FortiGate.

**NSE (Network Security Expert)** : Programme de certification Fortinet.

**OCVPN (One-Click VPN)** : Fonctionnalité de configuration simplifiée de VPN dans FortiOS.

**RADIUS (Remote Authentication Dial-In User Service)** : Protocole d'authentification, d'autorisation et de comptabilité.

**RMA (Return Merchandise Authorization)** : Autorisation de retour de marchandise, processus de remplacement d'un appareil défectueux.

### S-Z

**SD-WAN (Software-Defined Wide Area Network)** : Réseau étendu défini par logiciel, fonctionnalité de FortiGate pour optimiser les connexions WAN.

**Security Fabric** : Architecture de sécurité intégrée de Fortinet, permettant la communication et la coordination entre différents produits Fortinet.

**SIEM (Security Information and Event Management)** : Gestion des informations et des événements de sécurité, fonctionnalité de FortiSIEM.

**SPU (Security Processing Unit)** : Unité de traitement de sécurité, processeur spécialisé dans les appareils Fortinet.

**SSL VPN (Secure Sockets Layer Virtual Private Network)** : VPN basé sur SSL/TLS, fonctionnalité de FortiGate.

**UTM (Unified Threat Management)** : Gestion unifiée des menaces, approche de sécurité intégrant plusieurs fonctionnalités de protection.

**VDOM (Virtual Domain)** : Domaine virtuel, fonctionnalité de virtualisation dans FortiGate permettant de créer plusieurs instances virtuelles sur un seul appareil physique.

**VIP (Virtual IP)** : IP virtuelle, utilisée pour le NAT de destination dans FortiGate.

**WAF (Web Application Firewall)** : Pare-feu d'applications web, fonctionnalité de protection des applications web.

**ZTP (Zero Touch Provisioning)** : Provisionnement sans intervention, fonctionnalité permettant le déploiement automatisé des appareils Fortinet.

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Ressources d'apprentissage</h4>
<p>Pour approfondir votre connaissance de la terminologie Fortinet, consultez les ressources de formation NSE (Network Security Expert) disponibles sur le site de Fortinet. Le programme NSE propose plusieurs niveaux de certification, du débutant à l'expert.</p>
</div>

<h2 id="modeles-config" style="color:#0D274D;">10.3 Modèles de configurations typiques</h2>

Cette section présente des modèles de configurations FortiGate pour des scénarios courants, que vous pouvez adapter à vos besoins spécifiques.

### Configuration de base pour un petit bureau

Ce modèle convient à un petit bureau avec une connexion Internet unique et un réseau local simple.

```
# Configuration des interfaces
config system interface
    edit "wan1"
        set mode static
        set ip 203.0.113.2 255.255.255.0
        set allowaccess ping
        set description "WAN"
        set role wan
    next
    edit "internal"
        set mode static
        set ip 192.168.1.1 255.255.255.0
        set allowaccess ping https ssh
        set description "LAN"
        set role lan
    next
end

# Configuration du serveur DHCP
config system dhcp server
    edit 1
        set interface "internal"
        set default-gateway 192.168.1.1
        set netmask 255.255.255.0
        set dns-service default
        config ip-range
            edit 1
                set start-ip 192.168.1.100
                set end-ip 192.168.1.200
            next
        end
    next
end

# Configuration du routage par défaut
config router static
    edit 1
        set gateway 203.0.113.1
        set device "wan1"
    next
end

# Politiques de pare-feu de base
config firewall policy
    edit 1
        set name "LAN to WAN"
        set srcintf "internal"
        set dstintf "wan1"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set nat enable
        set logtraffic all
    next
    edit 2
        set name "WAN to LAN - Deny"
        set srcintf "wan1"
        set dstintf "internal"
        set srcaddr "all"
        set dstaddr "all"
        set action deny
        set schedule "always"
        set service "ALL"
        set logtraffic all
    next
end
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Sécurité de base</h4>
<p>Même pour une configuration de base, activez au minimum l'antivirus et le filtrage web pour le trafic sortant. Ajoutez "set utm-status enable", "set av-profile default" et "set webfilter-profile default" à la politique "LAN to WAN".</p>
</div>

### Configuration pour un bureau avec DMZ

Ce modèle ajoute une zone démilitarisée (DMZ) pour héberger des serveurs accessibles depuis Internet.

```
# Configuration des interfaces
config system interface
    edit "wan1"
        set mode static
        set ip 203.0.113.2 255.255.255.0
        set allowaccess ping
        set description "WAN"
        set role wan
    next
    edit "internal"
        set mode static
        set ip 192.168.1.1 255.255.255.0
        set allowaccess ping https ssh
        set description "LAN"
        set role lan
    next
    edit "dmz"
        set mode static
        set ip 192.168.2.1 255.255.255.0
        set allowaccess ping
        set description "DMZ"
        set role dmz
    next
end

# Configuration des VIPs pour les serveurs DMZ
config firewall vip
    edit "WebServer_VIP"
        set extip 203.0.113.2
        set mappedip 192.168.2.10
        set portforward enable
        set extport 80
        set mappedport 80
    next
    edit "MailServer_VIP"
        set extip 203.0.113.2
        set mappedip 192.168.2.20
        set portforward enable
        set extport 25
        set mappedport 25
    next
end

# Politiques de pare-feu
config firewall policy
    edit 1
        set name "LAN to WAN"
        set srcintf "internal"
        set dstintf "wan1"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set nat enable
        set utm-status enable
        set av-profile "default"
        set webfilter-profile "default"
        set ips-sensor "default"
        set logtraffic all
    next
    edit 2
        set name "WAN to WebServer"
        set srcintf "wan1"
        set dstintf "dmz"
        set srcaddr "all"
        set dstaddr "WebServer_VIP"
        set action accept
        set schedule "always"
        set service "HTTP"
        set utm-status enable
        set av-profile "default"
        set webfilter-profile "default"
        set ips-sensor "default"
        set logtraffic all
    next
    edit 3
        set name "WAN to MailServer"
        set srcintf "wan1"
        set dstintf "dmz"
        set srcaddr "all"
        set dstaddr "MailServer_VIP"
        set action accept
        set schedule "always"
        set service "SMTP"
        set utm-status enable
        set av-profile "default"
        set ips-sensor "default"
        set logtraffic all
    next
    edit 4
        set name "LAN to DMZ"
        set srcintf "internal"
        set dstintf "dmz"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
    next
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Sécurisation de la DMZ</h4>
<p>Pour une DMZ sécurisée, appliquez le principe du moindre privilège : n'autorisez que les services nécessaires entre les zones, utilisez des profils de sécurité UTM pour tout le trafic entrant, et considérez l'utilisation de l'inspection SSL pour le trafic HTTPS.</p>
</div>

### Configuration VPN IPsec site-à-site

Ce modèle établit un tunnel VPN IPsec entre deux sites.

```
# Site A
config vpn ipsec phase1-interface
    edit "SiteB_VPN"
        set interface "wan1"
        set ike-version 2
        set peertype any
        set proposal aes256-sha256
        set dhgrp 14
        set remote-gw 198.51.100.2
        set psksecret "SecurePreSharedKey123!"
    next
end

config vpn ipsec phase2-interface
    edit "SiteB_VPN_P2"
        set phase1name "SiteB_VPN"
        set proposal aes256-sha256
        set dhgrp 14
        set src-addr-type subnet
        set dst-addr-type subnet
        set src-subnet 192.168.1.0 255.255.255.0
        set dst-subnet 192.168.2.0 255.255.255.0
    next
end

config firewall policy
    edit 10
        set name "Local to Remote"
        set srcintf "internal"
        set dstintf "SiteB_VPN"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
    next
    edit 11
        set name "Remote to Local"
        set srcintf "SiteB_VPN"
        set dstintf "internal"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set logtraffic all
    next
end

# Site B (configuration similaire avec adresses inversées)
config vpn ipsec phase1-interface
    edit "SiteA_VPN"
        set interface "wan1"
        set ike-version 2
        set peertype any
        set proposal aes256-sha256
        set dhgrp 14
        set remote-gw 203.0.113.2
        set psksecret "SecurePreSharedKey123!"
    next
end

config vpn ipsec phase2-interface
    edit "SiteA_VPN_P2"
        set phase1name "SiteA_VPN"
        set proposal aes256-sha256
        set dhgrp 14
        set src-addr-type subnet
        set dst-addr-type subnet
        set src-subnet 192.168.2.0 255.255.255.0
        set dst-subnet 192.168.1.0 255.255.255.0
    next
end

# Politiques similaires à celles du Site A
```

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Sécurité des clés pré-partagées</h4>
<p>Dans un environnement de production, utilisez des clés pré-partagées complexes (au moins 32 caractères avec un mélange de lettres, chiffres et symboles) ou, mieux encore, l'authentification par certificat pour une sécurité renforcée.</p>
</div>

### Configuration SSL VPN pour accès distant

Ce modèle configure un accès VPN SSL pour les utilisateurs distants.

```
# Configuration des utilisateurs
config user local
    edit "vpnuser1"
        set type password
        set passwd "SecurePassword123!"
    next
end

config user group
    edit "SSL_VPN_Users"
        set member "vpnuser1"
    next
end

# Configuration du portail SSL VPN
config vpn ssl web portal
    edit "Full_Access"
        set tunnel-mode enable
        set web-mode enable
        set ip-pools "SSLVPN_TUNNEL_ADDR1"
        set split-tunneling enable
        config split-tunneling-routing-address
            edit 1
                set name "Internal_Network"
            next
        end
    next
end

# Configuration des paramètres SSL VPN
config vpn ssl settings
    set servercert "Fortinet_Factory"
    set tunnel-ip-pools "SSLVPN_TUNNEL_ADDR1"
    set tunnel-ipv6-pools "SSLVPN_TUNNEL_IPv6_ADDR1"
    set dns-server1 192.168.1.1
    set dns-server2 8.8.8.8
    set port 443
    set source-interface "wan1"
    set default-portal "Full_Access"
end

# Configuration de l'adresse IP pour le split tunneling
config firewall address
    edit "Internal_Network"
        set subnet 192.168.1.0 255.255.255.0
    next
end

# Configuration du pool d'adresses IP pour les clients SSL VPN
config firewall ippool
    edit "SSLVPN_TUNNEL_ADDR1"
        set startip 192.168.10.1
        set endip 192.168.10.100
    next
end

# Politique de pare-feu pour l'accès SSL VPN
config firewall policy
    edit 20
        set name "SSL VPN Access"
        set srcintf "ssl.root"
        set dstintf "internal"
        set srcaddr "all"
        set dstaddr "Internal_Network"
        set action accept
        set schedule "always"
        set service "ALL"
        set groups "SSL_VPN_Users"
        set utm-status enable
        set av-profile "default"
        set webfilter-profile "default"
        set ips-sensor "default"
        set logtraffic all
    next
end
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Authentification renforcée</h4>
<p>Pour renforcer la sécurité de l'accès VPN, configurez l'authentification à deux facteurs avec FortiToken ou un service RADIUS/LDAP externe. Ajoutez également des restrictions d'accès basées sur les groupes d'utilisateurs et les horaires.</p>
</div>

### Configuration SD-WAN avec deux liens Internet

Ce modèle configure SD-WAN pour équilibrer le trafic entre deux connexions Internet.

```
# Configuration des interfaces WAN
config system interface
    edit "wan1"
        set mode static
        set ip 203.0.113.2 255.255.255.0
        set allowaccess ping
        set description "Primary WAN"
        set role wan
    next
    edit "wan2"
        set mode static
        set ip 198.51.100.2 255.255.255.0
        set allowaccess ping
        set description "Secondary WAN"
        set role wan
    next
end

# Configuration du routage par défaut pour chaque WAN
config router static
    edit 1
        set gateway 203.0.113.1
        set device "wan1"
        set distance 10
    next
    edit 2
        set gateway 198.51.100.1
        set device "wan2"
        set distance 20
    next
end

# Configuration SD-WAN
config system sdwan
    set status enable
    config zone
        edit "virtual-wan-link"
        next
    end
    config members
        edit 1
            set interface "wan1"
            set gateway 203.0.113.1
            set priority 1
        next
        edit 2
            set interface "wan2"
            set gateway 198.51.100.1
            set priority 2
        next
    end
    config health-check
        edit "Internet_Check"
            set server "8.8.8.8"
            set protocol ping
            set interval 1000
            set failtime 5
            set recoverytime 5
            set members 1 2
        next
    end
    config service
        edit 1
            set name "Web_Traffic"
            set mode load-balance
            set src "all"
            set dst "all"
            set protocol 6
            set port 80 443
            set health-check "Internet_Check"
            set priority-members 1 2
        next
        edit 2
            set name "Other_Traffic"
            set mode priority
            set src "all"
            set dst "all"
            set health-check "Internet_Check"
            set priority-members 1 2
        next
    end
end

# Politique de pare-feu pour SD-WAN
config firewall policy
    edit 1
        set name "LAN to SD-WAN"
        set srcintf "internal"
        set dstintf "virtual-wan-link"
        set srcaddr "all"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ALL"
        set nat enable
        set utm-status enable
        set av-profile "default"
        set webfilter-profile "default"
        set ips-sensor "default"
        set logtraffic all
    next
end
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Optimisation SD-WAN</h4>
<p>Pour une configuration SD-WAN optimale, définissez des règles de service basées sur les applications ou les types de trafic. Par exemple, dirigez le trafic VoIP et les applications critiques via le lien le plus fiable, et équilibrez le trafic web et moins critique entre tous les liens disponibles.</p>
</div>

<h2 id="depannage" style="color:#0D274D;">10.4 Guide de dépannage</h2>

Cette section présente des méthodologies et des commandes pour diagnostiquer et résoudre les problèmes courants sur FortiGate.

### Méthodologie générale de dépannage

1. **Identifier le problème** : Définissez clairement le problème et les symptômes
2. **Collecter des informations** : Rassemblez les journaux, les résultats de commandes de diagnostic, et les informations sur l'environnement
3. **Analyser les données** : Examinez les informations collectées pour identifier des modèles ou des anomalies
4. **Formuler des hypothèses** : Proposez des explications possibles du problème
5. **Tester les hypothèses** : Vérifiez chaque hypothèse de manière systématique
6. **Implémenter la solution** : Appliquez la solution identifiée
7. **Vérifier les résultats** : Confirmez que le problème est résolu
8. **Documenter** : Documentez le problème, la solution, et les leçons apprises

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Approche systématique</h4>
<p>Adoptez une approche systématique pour le dépannage, en commençant par les couches inférieures (connectivité physique, interfaces) et en remontant vers les couches supérieures (routage, politiques, services). Isolez chaque composant pour identifier précisément la source du problème.</p>
</div>

### Problèmes de connectivité réseau

#### Vérification des interfaces

```
# Afficher l'état des interfaces
# get system interface physical
# diagnose hardware deviceinfo nic port1

# Vérifier les statistiques d'interface
# diagnose netlink interface list port1
```

#### Vérification du routage

```
# Afficher la table de routage
# get router info routing-table all

# Vérifier le routage pour une destination spécifique
# diagnose firewall proute lookup 8.8.8.8
```

#### Tests de connectivité

```
# Ping depuis FortiGate
# execute ping 8.8.8.8

# Traceroute depuis FortiGate
# execute traceroute 8.8.8.8

# Capture de paquets
# diagnose sniffer packet port1 "host 8.8.8.8" 4 0 a
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Isolation des problèmes</h4>
<p>Pour isoler les problèmes de connectivité, testez chaque segment du chemin réseau. Par exemple, vérifiez d'abord si FortiGate peut atteindre sa passerelle par défaut, puis des hôtes sur Internet, puis le trafic spécifique qui pose problème.</p>
</div>

### Problèmes de politiques de pare-feu

#### Vérification des politiques

```
# Afficher toutes les politiques
# show firewall policy

# Vérifier quelle politique s'applique à un trafic spécifique
# diagnose firewall iprope lookup 192.168.1.10 8.8.8.8 1 53 17 0
```

#### Débogage du flux de trafic

```
# Activer le débogage du flux
# diagnose debug reset
# diagnose debug flow filter addr 192.168.1.10
# diagnose debug flow trace start 100
# diagnose debug enable

# Désactiver le débogage
# diagnose debug disable
```

#### Vérification des sessions

```
# Afficher les sessions actives
# diagnose sys session list

# Filtrer les sessions
# diagnose sys session filter src 192.168.1.10
# diagnose sys session filter dst 8.8.8.8
# diagnose sys session list
```

<div style="background-color:#FFF1F0; border-left:4px solid #FF4D4F; padding:15px; margin:15px 0;">
<h4>⚠️ Impact du débogage</h4>
<p>Le débogage du flux peut avoir un impact significatif sur les performances, surtout dans un environnement à haut débit. Utilisez des filtres précis, limitez la durée du débogage, et désactivez-le dès que possible.</p>
</div>

### Problèmes VPN

#### Vérification de l'état des tunnels IPsec

```
# Afficher l'état des tunnels
# diagnose vpn ike gateway list
# diagnose vpn tunnel list

# Vérifier les SAs IKE
# diagnose vpn ike gateway list name Site_B_VPN
```

#### Débogage VPN IPsec

```
# Activer le débogage IKE
# diagnose debug reset
# diagnose debug application ike -1
# diagnose debug enable

# Désactiver le débogage
# diagnose debug disable
```

#### Vérification SSL VPN

```
# Afficher les sessions SSL VPN
# diagnose vpn ssl list

# Vérifier la configuration SSL VPN
# get vpn ssl settings
# get vpn ssl monitor
```

### Problèmes de performances

#### Vérification de l'utilisation des ressources

```
# Afficher l'utilisation CPU et mémoire
# get system performance status

# Afficher les processus consommant le plus de ressources
# diagnose sys top
```

#### Vérification des sessions et connexions

```
# Afficher les statistiques de sessions
# diagnose sys session stat

# Afficher les connexions par protocole
# diagnose firewall stat 0
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Surveillance continue</h4>
<p>Pour les problèmes de performance intermittents, configurez une surveillance continue avec des outils comme SNMP ou syslog, ou utilisez FortiAnalyzer pour collecter et analyser les données de performance sur une période prolongée.</p>
</div>

### Problèmes d'authentification

#### Vérification des utilisateurs et groupes

```
# Afficher les utilisateurs locaux
# show user local

# Afficher les groupes d'utilisateurs
# show user group

# Vérifier les serveurs d'authentification
# show user radius
# show user ldap
```

#### Débogage de l'authentification

```
# Activer le débogage de l'authentification
# diagnose debug reset
# diagnose debug application fnbamd -1
# diagnose debug enable

# Désactiver le débogage
# diagnose debug disable
```

### Problèmes de services UTM

#### Vérification des profils UTM

```
# Afficher les profils antivirus
# show antivirus profile

# Afficher les profils de filtrage web
# show webfilter profile

# Afficher les profils IPS
# show ips sensor
```

#### Débogage des services UTM

```
# Activer le débogage antivirus
# diagnose debug reset
# diagnose debug application scanunit -1
# diagnose debug enable

# Activer le débogage IPS
# diagnose debug reset
# diagnose debug application ipsmonitor -1
# diagnose debug enable

# Désactiver le débogage
# diagnose debug disable
```

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Journalisation ciblée</h4>
<p>Pour diagnostiquer les problèmes UTM, activez temporairement une journalisation détaillée pour le service concerné. Par exemple, pour le filtrage web, configurez "set log-all-url enable" dans le profil webfilter pour enregistrer toutes les URLs visitées.</p>
</div>

### Ressources de support

#### Support Fortinet

* **FortiCare** : Service de support officiel de Fortinet
* **Base de connaissances Fortinet** : Articles techniques et guides de dépannage
* **Forums Fortinet** : Communauté d'utilisateurs et d'experts Fortinet
* **Documentation produit** : Manuels d'administration, guides de référence CLI, etc.

#### Commandes pour collecter des informations de support

```
# Générer un rapport de diagnostic complet
# execute tac report

# Sauvegarder la configuration
# execute backup config ftp backup.conf 192.168.1.100 username password

# Afficher les informations système
# get system status
# diagnose sys top
# diagnose debug crashlog read
```

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Préparation pour le support</h4>
<p>Avant de contacter le support Fortinet, rassemblez toutes les informations pertinentes : description précise du problème, étapes pour le reproduire, configuration concernée, journaux pertinents, et rapport de diagnostic TAC. Cela accélérera considérablement la résolution du problème.</p>
</div>

<h2 id="liens-docs" style="color:#0D274D;">10.5 Liens vers la documentation officielle</h2>

Cette section fournit des liens vers les ressources officielles Fortinet pour approfondir vos connaissances et rester à jour avec les dernières informations.

### Documentation produit

* **Administration Guides** : [https://docs.fortinet.com/product/fortigate/](https://docs.fortinet.com/product/fortigate/)
* **Cookbook** : [https://docs.fortinet.com/document/fortigate/7.4.0/cookbook/](https://docs.fortinet.com/document/fortigate/7.4.0/cookbook/)
* **Best Practices** : [https://docs.fortinet.com/document/fortigate/7.4.0/best-practices/](https://docs.fortinet.com/document/fortigate/7.4.0/best-practices/)
* **Hardware Guides** : [https://docs.fortinet.com/product/fortigate/hardware](https://docs.fortinet.com/product/fortigate/hardware)
* **CLI Reference** : [https://docs.fortinet.com/document/fortigate/7.4.0/cli-reference/](https://docs.fortinet.com/document/fortigate/7.4.0/cli-reference/)

### Ressources de formation

* **NSE Training Institute** : [https://training.fortinet.com/](https://training.fortinet.com/)
* **Fortinet Certification Program** : [https://www.fortinet.com/training-certification](https://www.fortinet.com/training-certification)
* **Fortinet Security Academy** : [https://www.fortinet.com/training/security-academy-program](https://www.fortinet.com/training/security-academy-program)

### Support et communauté

* **FortiCare Support** : [https://support.fortinet.com/](https://support.fortinet.com/)
* **Fortinet Knowledge Base** : [https://kb.fortinet.com/](https://kb.fortinet.com/)
* **Fortinet Community** : [https://community.fortinet.com/](https://community.fortinet.com/)
* **Fortinet Blog** : [https://www.fortinet.com/blog](https://www.fortinet.com/blog)
* **Fortinet Security Research** : [https://www.fortinet.com/fortiguard/labs](https://www.fortinet.com/fortiguard/labs)

### Ressources pour développeurs

* **Fortinet Developer Network (FNDN)** : [https://fndn.fortinet.net/](https://fndn.fortinet.net/)
* **FortiOS REST API Reference** : [https://docs.fortinet.com/document/fortigate/7.4.0/fortios-rest-api-reference](https://docs.fortinet.com/document/fortigate/7.4.0/fortios-rest-api-reference)
* **FortiOS 7.4 JSON API Reference** : [https://docs.fortinet.com/document/fortigate/7.4.0/json-api-reference/](https://docs.fortinet.com/document/fortigate/7.4.0/json-api-reference/)
* **Ansible Modules** : [https://galaxy.ansible.com/fortinet/fortios](https://galaxy.ansible.com/fortinet/fortios)
* **Terraform Modules** : [https://registry.terraform.io/providers/fortinetdev/fortios/latest/docs](https://registry.terraform.io/providers/fortinetdev/fortios/latest/docs)

<div style="background-color:#F6FFED; border-left:4px solid #52C41A; padding:15px; margin:15px 0;">
<h4>🏆 Ressources recommandées</h4>
<p>Pour les administrateurs FortiGate, nous recommandons particulièrement le Cookbook et les Best Practices. Ces documents contiennent des exemples concrets et des recommandations basées sur l'expérience de terrain, qui complètent parfaitement les guides d'administration plus théoriques.</p>
</div>

### Mises à jour et bulletins de sécurité

* **FortiGuard Security Subscriptions** : [https://www.fortinet.com/support/support-services/fortiguard-security-subscriptions](https://www.fortinet.com/support/support-services/fortiguard-security-subscriptions)
* **FortiGuard Labs Threat Intelligence** : [https://www.fortinet.com/fortiguard/labs/threat-intelligence](https://www.fortinet.com/fortiguard/labs/threat-intelligence)
* **Security Advisories** : [https://www.fortiguard.com/psirt](https://www.fortiguard.com/psirt)
* **FortiOS Release Notes** : [https://docs.fortinet.com/product/fortigate/7.4.0](https://docs.fortinet.com/product/fortigate/7.4.0)

### Ressources vidéo

* **Fortinet YouTube Channel** : [https://www.youtube.com/user/fortinettv](https://www.youtube.com/user/fortinettv)
* **FortiGate Tutorials** : [https://video.fortinet.com/products/fortigate](https://video.fortinet.com/products/fortigate)
* **NSE Training Videos** : [https://video.fortinet.com/training/nse](https://video.fortinet.com/training/nse)

<div style="background-color:#E6F7FF; border-left:4px solid #1890FF; padding:15px; margin:15px 0;">
<h4>📝 Documentation hors ligne</h4>
<p>Pour les environnements sans accès Internet ou pour une référence rapide, téléchargez les versions PDF de la documentation depuis le site de documentation Fortinet. Ces documents peuvent être particulièrement utiles lors des déploiements sur site ou des interventions d'urgence.</p>
</div>

---

<div style="text-align:center; margin-top:50px; margin-bottom:50px;">
<p style="font-size:14px; color:#666;">© 2025 - Manuel FortiGate Complet</p>
<p style="font-size:14px; color:#666;">Auteur : Lejeune Geoffrey</p>
<p style="font-size:14px; color:#666;">Tous droits réservés</p>
</div>
