# Manuel Très Complet d'Autopsy

## Introduction : Autopsy, la Plateforme Open Source de Criminalistique Numérique

Dans le monde complexe de la criminalistique numérique (digital forensics), l'analyse des preuves électroniques est une tâche exigeante qui requiert des outils puissants et fiables. **Autopsy** se distingue comme la principale plateforme open source de criminalistique numérique, offrant une interface graphique intuitive pour The Sleuth Kit et d'autres outils forensiques. Conçu pour être rapide, facile à utiliser et capable d'analyser tous types de supports numériques, Autopsy est devenu un choix privilégié pour les enquêteurs, les analystes de sécurité et les professionnels de la récupération de données.

### Qu'est-ce qu'Autopsy ?

Autopsy est une plateforme d'analyse forensique numérique qui permet aux enquêteurs d'examiner efficacement les disques durs et les smartphones. Il fournit une interface conviviale pour des fonctionnalités avancées telles que :

*   **Analyse de fichiers et de systèmes de fichiers** : Permet d'explorer la structure des disques, d'identifier les fichiers supprimés, et de récupérer des données.
*   **Recherche de mots-clés** : Facilite la recherche rapide de termes spécifiques à travers l'ensemble des données.
*   **Extraction d'artefacts** : Identifie et extrait automatiquement des informations pertinentes comme l'historique de navigation web, les e-mails, les chats, les documents, et les images.
*   **Timeline Analysis** : Crée une chronologie des événements pour aider à reconstituer les activités de l'utilisateur.
*   **Hashing et filtrage** : Utilise des bases de données de hachage pour identifier les fichiers connus (bons ou mauvais) et filtrer le bruit.
*   **Support de plugins** : Sa modularité permet d'étendre ses capacités via des modules tiers pour des analyses spécialisées.

### Pourquoi Autopsy est-il Essentiel en Criminalistique Numérique ?

Autopsy est un outil indispensable pour plusieurs raisons :

*   **Open Source et Gratuit** : Il est accessible à tous, des étudiants aux professionnels, sans coût de licence.
*   **Complet et Puissant** : Il intègre une large gamme de fonctionnalités que l'on retrouve dans des outils commerciaux coûteux.
*   **Facilité d'Utilisation** : Son interface graphique simplifie des tâches forensiques complexes, le rendant accessible même aux débutants.
*   **Large Compatibilité** : Il peut analyser des images disque créées par d'autres outils (comme FTK Imager) et prend en charge une multitude de systèmes de fichiers.
*   **Communauté Active** : Bénéficie d'une communauté de développeurs et d'utilisateurs qui contribuent à son amélioration continue et offrent un support.

Ce manuel vous guidera à travers l'installation, la configuration et l'utilisation approfondie d'Autopsy, avec un accent particulier sur les étapes pratiques et les captures d'écran pour vous aider à maîtriser cet outil essentiel de la criminalistique numérique.



    *   **Installation Complète** : Laissez l'option par défaut pour une installation complète, qui inclut tous les composants nécessaires.

    *   **Finalisation** : Une fois l'installation terminée, cliquez sur `Finish` (Terminer).

    ![Installation de FTK Imager terminée](/home/ubuntu/upload/search_images/zIk9I3g8kLak.jpeg)
    *Figure 3: Écran de fin d'installation de FTK Imager.* 

### 3. Lancement de FTK Imager

Après l'installation, vous pouvez lancer FTK Imager depuis le menu Démarrer de Windows ou via le raccourci créé sur le bureau. Il est recommandé de l'exécuter en tant qu'administrateur pour s'assurer qu'il dispose des permissions nécessaires pour accéder aux disques et à la mémoire.

    ![Lancement de FTK Imager](/home/ubuntu/upload/search_images/nh1zFNy3X8Db.png)
    *Figure 4: Interface principale de FTK Imager après le lancement.* 

Vous êtes maintenant prêt à utiliser FTK Imager pour vos tâches d'acquisition et de prévisualisation de preuves numériques.




## Installation d'Autopsy : Un Guide Étape par Étape

L'installation d'Autopsy est un processus relativement simple, mais il est important de suivre les étapes pour s'assurer que tous les composants nécessaires sont correctement configurés. Autopsy est une application Java, et sur Windows, elle est généralement fournie avec un installeur MSI qui gère les dépendances.

### 1. Téléchargement d'Autopsy

Autopsy est disponible gratuitement sur le site officiel de The Sleuth Kit (qui est le moteur sous-jacent d'Autopsy).

1.  **Accédez au Site Officiel** : Ouvrez votre navigateur web et naviguez vers la page de téléchargement d'Autopsy : [https://www.autopsy.com/download/](https://www.autopsy.com/download/)

2.  **Téléchargez la Dernière Version** : Sur la page de téléchargement, vous trouverez des liens pour différentes versions et systèmes d'exploitation. Pour Windows, téléchargez le fichier `.msi` (Microsoft Installer) de la dernière version stable.

    ![Page de téléchargement d'Autopsy](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556604_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL3lvdURIUXBnT3l6OQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MDRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMM2x2ZFVSSVVYQm5UM2w2T1EucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=eWTdb1zKllXrDmv5BQe90QZrN64ZlrVzyW3EwwJcB29av991XPTl7lIoACUwvaO1BYHsWAFMdLMMatNARMcosRrI6lXbnL4Zyn9gPLENwXul51uV0GDTl2BR8mzA7av0VHkQ~uu-on9GoLKMe85AvcjIVn0GVovwLz5JTyqEXtJefoftjz-vX2eL1sAm~Waxk3~AWdG4EOv8E4orRnrD7FTlfOSc5-6SyDOD-IO4~rHexG87VStDUnXGcBvz7PW2qiGvc7mLZpt3Wb~0sSEbDRCZabrc4PWiEcD6j18bqWO8H1dEU8tY1tqUFU5-c1ib5a1sMi-4Li9GqNLzIS5t4A__)
    *Figure 1: Page de téléchargement d'Autopsy sur le site officiel.* 

### 2. Installation d'Autopsy

Une fois le fichier d'installation téléchargé, vous pouvez procéder à l'installation.

1.  **Exécutez l'Installeur** : Localisez le fichier `.msi` téléchargé et double-cliquez dessus pour lancer l'assistant d'installation.

2.  **Assistant d'Installation** :
    *   **Écran de Bienvenue** : Cliquez sur `Next` (Suivant) sur l'écran de bienvenue de l'assistant d'installation.

    *   **Contrat de Licence** : Lisez et acceptez le contrat de licence utilisateur final (EULA). Sélectionnez `I accept the terms in the License Agreement` et cliquez sur `Next`.

    *   **Type d'Installation** : Choisissez le type d'installation. Pour la plupart des utilisateurs, `Complete` (Complet) est recommandé pour installer tous les composants nécessaires. Cliquez sur `Next`.

    *   **Dossier de Destination** : Choisissez le dossier où Autopsy sera installé. Le chemin par défaut est généralement approprié. Cliquez sur `Next`.

    *   **Prêt à Installer** : L'assistant est maintenant prêt à installer le programme. Cliquez sur `Install` (Installer) pour commencer le processus.

    ![Assistant d'installation d'Autopsy](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556606_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0FQejVaYmpOcFpwSQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MDZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMEZRZWpWYVltcE9jRnB3U1EucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=LhhRXRxxgXRCd2WIiQzSrf~iD41X-uQky8tHc5wK68c2YWu3EU3FMrkr~SU02um4V1jJLlqooAO0zAs~0dm9K49MC-g0JdhWLGCzfp4Cns8aBo765xoA2tkb~L3-d-KSpEwmGu-j-9YvxEb6cMttDAOkKBfT9ZeLWLWi4yIZTEy1cX8IJfem2vOi2GMM7LhY--suCrMUJrZgj8HLB5JzYAezfgfo8WEiRhd7tjffY9d0j3r-cr6Q-mlWkJIW13yctGtH060zc7mym-aqjsx5eox3ASoQ8i-De741A3k7R5cf02tpHkmeWB1bv1tr7dUFTGF3~aajllCpbDBJMbBcsQ__)
    *Figure 2: Assistant d'installation d'Autopsy, montrant l'étape de confirmation avant l'installation.* 

    *   **Progression de l'Installation** : L'installation peut prendre quelques minutes. Une barre de progression s'affichera.

    *   **Finalisation** : Une fois l'installation terminée, cliquez sur `Finish` (Terminer).

### 3. Lancement d'Autopsy

Après l'installation, vous pouvez lancer Autopsy depuis le menu Démarrer de Windows ou via le raccourci créé sur le bureau. La première fois que vous lancez Autopsy, il peut prendre un peu de temps pour initialiser ses composants.

    ![Écran de bienvenue d'Autopsy](/home/ubuntu/upload/search_images/JMxOMMqenUSP.png)
    *Figure 3: Écran de bienvenue d'Autopsy, offrant les options de création ou d'ouverture de cas.* 

Vous êtes maintenant prêt à créer votre premier cas et à commencer votre analyse forensique avec Autopsy.




## Création d'un Nouveau Cas et Ajout de Sources de Données dans Autopsy

Pour commencer toute investigation forensique avec Autopsy, la première étape consiste à créer un nouveau cas. Un cas dans Autopsy est un conteneur logique qui organise toutes les données, les analyses et les résultats liés à une enquête spécifique. Une fois le cas créé, vous pouvez y ajouter les sources de données (images disque, disques physiques, dossiers logiques, etc.) que vous souhaitez analyser.

### 1. Création d'un Nouveau Cas

1.  **Lancer Autopsy** : Ouvrez Autopsy. Vous serez accueilli par l'écran de bienvenue.

2.  **Sélectionner 'Create New Case'** : Sur l'écran de bienvenue, cliquez sur le bouton `Create New Case` (Créer un nouveau cas).

    ![Écran de bienvenue d'Autopsy - Créer un nouveau cas](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556606_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0pNeE9NTXFlblVTUA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MDZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMHBOZUU5TlRYRmxibFZUVUEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=tlBKHFudElJbwfJYYsGCNSB3OmDdjnDIbxL-TuzhoJZe7JOgs3zg7PFGX5XZLStzmA5kyntkUtN4zBwSyY1aCB5tN3Xe6GYVP2OPZ7IXCVTjA892uwf1X3-CjXYRwXF2fyOWUPFU72Pzo3mlqTJoNqahT5c~~4lFtrD2Xs-KxaVi7c~NobF3WT3ettC6Yd3xjiCvNOUG8UfP3FmHuIz0zmyKcEyGBvN3BuMDrUoVxO7LONhS7qnLrfd7OcnQKgr9sRCosQqqO1qQ1f~h2ohLEHTlwLmppROxoMhmpJzpKFVY6V17S81nwM~5OfF76l-Wov-1rxQ3DVhvDVKbWgtlQw__)
    *Figure 4: L'écran de bienvenue d'Autopsy, avec l'option 'Create New Case' mise en évidence.* 

3.  **Informations sur le Cas** : L'assistant de création de cas s'ouvrira. Remplissez les informations suivantes :
    *   **Case Name** (Nom du cas) : Un nom unique pour votre enquête (par exemple, `Enquete_Fraude_2024`).
    *   **Base Directory** (Répertoire de base) : Le chemin où les fichiers du cas Autopsy seront stockés. Il est recommandé de choisir un emplacement avec suffisamment d'espace disque et sur un disque différent de celui que vous analysez.
    *   **Case Type** (Type de cas) : Choisissez `Single-user` (Utilisateur unique) si vous travaillez seul sur le cas, ou `Multi-user` (Multi-utilisateur) si plusieurs enquêteurs doivent collaborer sur le même cas (nécessite une configuration de base de données).

    Cliquez sur `Next` (Suivant).

    ![Informations sur le nouveau cas](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556607_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL3hKZEZTRVZmQnFLag.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MDdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMM2hLWkVaVFJWWm1RbkZMYWcucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=PBVWnAtrn6bbBBP4B7sHpXgRgflk8i4vIXS~fudVjIL7ZT57ZwKqWnbFR9IftbNy7JfIUOwDc78ErtPvKnYk~Kg~4cJTRVALJnpvA-yXSgRO3MNqbwoYUSyuvi7lTRS9ZuQRDjwJfNJXPeK9BMcop2RRoyJzDXPujghw--dAkJk0bcGBtklX~qM4bWxGnNO3ixrayUFYkDql1w2rX~7nN9GRsfu~SNZnF8n9v84tC8P~MH~e5Mtdxsnra0tcyYDEfqfgV5qpCgk9nCn0lz~ou9p-SgKWsv7tlbJEEBuqkxVJTGUtGrfZgNjX76OEu~UY-FyyypQc7UrlX83LKyD2-A__)
    *Figure 5: Remplir les informations de base pour le nouveau cas dans Autopsy.* 

4.  **Informations Optionnelles** : Sur l'écran suivant, vous pouvez ajouter des informations optionnelles :
    *   **Case Number** (Numéro de cas) : Un identifiant unique pour le cas, souvent utilisé dans les organisations.
    *   **Examiner Name** (Nom de l'examinateur) : Votre nom ou l'identifiant de l'enquêteur.
    *   **Phone Number** (Numéro de téléphone) : Votre numéro de contact.
    *   **Email Address** (Adresse e-mail) : Votre adresse e-mail.

    Ces informations sont utiles pour la documentation et les rapports. Cliquez sur `Finish` (Terminer).

    ![Informations optionnelles sur le cas](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556607_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL1JpRXM3MjRtUG9SSw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MDdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMUpwUlhNM01qUnRVRzlTU3cucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=KYVdoKrkWsZewoNzWO3YwlExUZBZQsdQjp9sGrqoBeJeZwvbu91pmxk62sN-DnEfOIM3jYKHiEt1h2x6WFazqsRDjEupvMIivmFlRElR0uIqjOTf5~3jD-CjcdzwGidM9PkAGQxH78xmQEZkawvfruvGhjumxmL6JQBzWftKwqMUtiW86iJxIh3o0pkSnbjy3IaRHk2TJJMVTaOrUxxF5Tgp5s98SEwGQ~Qut1z42ItifjIAZUoKSo-194vDW4aGRLCbz-iMMUcBpOV~Rig8M8ub4W-7TS8w-bMJlMP81sxy0yyVXiKvwUiY9hncEERXRWSd58BKDrJatsiW6Vwtkw__)
    *Figure 6: Ajouter des informations optionnelles pour le cas, telles que le numéro de cas et les détails de l'examinateur.* 

Autopsy va maintenant créer la structure du cas et ouvrir l'interface principale, prête à recevoir les sources de données.

### 2. Ajout de Sources de Données

Une fois le cas créé, Autopsy vous invite automatiquement à ajouter une source de données. C'est ici que vous allez importer les preuves numériques à analyser.

1.  **Sélectionner 'Add Data Source'** : Si la fenêtre d'ajout de source de données ne s'ouvre pas automatiquement, vous pouvez la lancer en cliquant sur `Add Data Source` dans la barre d'outils ou via `File` > `Add Data Source`.

    ![Ajouter une source de données](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556608_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzLzFDMU03dzlBb1A3RA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MDhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMekZETVUwM2R6bEJiMUEzUkEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=BJC-SK65XTRyhxdg86b-hgAQ8VnFhmYRhH1VIovjllWlcZ04BjaNvOzLNq~S5Mz9WOEkTJpsnXA~equlqyMqTW01MAPXyCQb-xBc7xHun4yhuZ8UZbuJtLiIvpCUTcGfPooDZ2a7mK~Kwe9kr7~nZkUfmba7P6HMh9eeIntdS7RZ~L-UXgRycLrvpUYR~ZoRvg7fKAtXQXtCXO~NMCQFxXW9ueAT4o3tIMJZIwk1hvKrBH8tka0CUGIvlF~Iv20eBoKBGY-cNVfcHW9oSUs-Pr5zWfiy9vzFk6nJ-3BN4Es0aZF8vTTmvH~mtNC~YNdOcZMo8E2cJC6tO93s5RR8ZA__)
    *Figure 7: L'option 'Add Data Source' dans la barre d'outils d'Autopsy.* 

2.  **Choisir le Type de Source de Données** : Autopsy prend en charge plusieurs types de sources de données :
    *   **Disk Image** (Image Disque) : C'est le type le plus courant. Il s'agit d'une copie bit-à-bit d'un disque dur, d'une clé USB, etc. (par exemple, des fichiers `.E01`, `.DD`, `.RAW`).
    *   **Local Disk** (Disque Local) : Permet d'analyser un disque physique directement connecté à la machine sur laquelle Autopsy est exécuté (à utiliser avec prudence pour ne pas altérer les preuves).
    *   **Logical Files** (Fichiers Logiques) : Permet d'ajouter des fichiers ou des dossiers spécifiques pour analyse, sans créer une image complète du disque.
    *   **Virtual Machine** (Machine Virtuelle) : Pour analyser des disques virtuels (par exemple, `.vmdk`, `.vhd`).

    Sélectionnez le type de source de données que vous souhaitez ajouter et cliquez sur `Next`.

    ![Choisir le type de source de données](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556608_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL2sweGZ0bDlQV3oxUg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MDhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMnN3ZUdaMGJEbFFWM294VWcucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=B5LXoyb74z929sPQ1Yn88ytPqvqxBG7Oga4JQVEYzFI2gpEIKYnvNaiuu0xQYurYNiF-jeI00toZUSDU5U9-Mgfl9kPSenBEVNqhxlI-rhCWACyd4JVm3h19Y7Uja4~8MFF-5phHy5axBZS~535hq2Y9KC8gorp9DV7TbSe~MaVnwgjOmgoDYjZBdySJyYDCXJ8M7tG5o1srimYTt39pim~6S2Xf7Cw51Nbrs06NE6F6JSHdbbED-94S6Dq0CL5RV8bxe~~ArKqyPaFDQLEESuRPvCqZIxWnp~vTzAHh8bg-woMBleBe5mngzlJD0wAfc-YPMPnAIMk9yXvJ4KXARg__)
    *Figure 8: Sélection du type de source de données à ajouter pour l'analyse.* 

3.  **Spécifier la Source de Données** : Selon le type choisi, vous devrez fournir des informations supplémentaires :
    *   **Pour une Image Disque** : Naviguez jusqu'au fichier de l'image disque (si l'image est fragmentée en plusieurs fichiers, sélectionnez le premier). Autopsy détectera automatiquement les autres parties.
    *   **Pour un Disque Local** : Sélectionnez le disque physique dans la liste.
    *   **Pour des Fichiers Logiques** : Naviguez et sélectionnez le dossier ou les fichiers à ajouter.

    Cliquez sur `Next`.

    ![Spécifier le chemin de la source de données](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556609_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0MwV0o4YlgxQWZhSA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MDlfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMME13VjBvNFlsZ3hRV1poU0EucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=vZAC27ut3sJ7ReS6FG~Bd2sppq554U6Hwi2VhveFDe3D845lWHqf1M7cO9bK1XnIALnwJRwgpaptnEuHF~ycAvKD7qv83R6ZWd2AJLjxbvI0QKOqELWcxlD4VFvA2YPktrm6PfHerrp8D3wEXfgbG18~IoBEMzRMsJkJMcxgFq0IKb-I94zicoqPlcmw4jR18Mzcr2HZpBHc18kwFT3tYSTkwMD23Qx9wmY3SB5krJvsOV2Zr4giAs885pEGL0LWS9ACdnPBhYC87o1zSAHa4ewXpUYH5HcLPFw6oRCWXziZd9HTnOLTDDN2~ih8AbhfuqpMoOpAsUJOzzucgQ8zKw__)
    *Figure 9: Spécification du chemin de l'image disque à ajouter.* 

4.  **Configuration des Modules d'Ingestion** : C'est une étape cruciale où vous choisissez les modules d'analyse qu'Autopsy exécutera sur la source de données. Ces modules effectuent diverses tâches, telles que :
    *   **Recent Activity** : Analyse l'historique de navigation web, les fichiers récents, etc.
    *   **Hash Lookup** : Vérifie les hachages des fichiers par rapport à des bases de données connues (NSRL, bases de données personnalisées) pour identifier les fichiers malveillants ou connus.
    *   **Keyword Search** : Effectue une recherche de mots-clés sur l'ensemble de la source de données.
    *   **Exif Parser** : Extrait les métadonnées des images.
    *   **File Type Identification** : Identifie les types de fichiers.
    *   **Extension Mismatch Detector** : Détecte les fichiers dont l'extension ne correspond pas au type réel.
    *   **Email Parser** : Analyse les fichiers d'e-mails.
    *   **Android Analyzer** : Pour l'analyse de données Android.

    Sélectionnez les modules pertinents pour votre enquête. Vous pouvez également configurer des options spécifiques pour chaque module. Cliquez sur `Next`.

    ![Configuration des modules d'ingestion](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556609_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzLzNHb1JxQUNYOW5NSw.jpg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MDlfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMek5IYjFKeFFVTllPVzVOU3cuanBnIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=PRkvBkVhnYYCHhBAu2bsP26vIe2NDPtEz6t3SUiaEDBqvDkZkP1Dx55qW9QO0fdjXmtbtBjRY7opM6y7nHwWm6QfvNIYwxrgXBS8MTqdFALEe4c6OQdnJYP8BwzLDOLx4zbXaPtQgfz5x6PjOyOLd9cmHI6qWV9R86k3ug75MoJXuu3opvwLyeElTYAKGvKtkfHtCDwGyzOyXEKO4APaPCGU1FpNAma3pO-H1anvjChY26Uolfw4EFvDLPNcqEp0bV31V5rs0-Y-6kLrHKRofmud7NC1QjJQcPnmi2QWIanUClbzj0-Nr231bC45wj4aPz7TLyqy4cou~WraLkupdg__)
    *Figure 10: Sélection et configuration des modules d'ingestion pour l'analyse des données.* 

5.  **Résumé et Démarrage de l'Ingestion** : Un résumé des informations du cas et des modules d'ingestion sélectionnés s'affichera. Vérifiez que tout est correct, puis cliquez sur `Finish` (Terminer) pour démarrer le processus d'ingestion et d'analyse.

Autopsy commencera alors à traiter la source de données, ce qui peut prendre un temps considérable en fonction de la taille de la source et du nombre de modules d'ingestion activés. Vous pouvez suivre la progression dans le panneau inférieur droit de l'interface d'Autopsy. Une fois l'ingestion terminée, vous pourrez commencer l'exploration et l'analyse des données.



## L'Interface d'Autopsy : Une Vue Détaillée

L'interface utilisateur d'Autopsy est conçue pour être intuitive, organisée en plusieurs panneaux qui facilitent la navigation et l'analyse des preuves numériques. Comprendre la disposition de ces panneaux est essentiel pour utiliser efficacement l'outil.

### 1. Vue d'Ensemble de l'Interface Principale

Après avoir créé un cas et ajouté une source de données, l'interface principale d'Autopsy se présente généralement comme suit :

    ![Interface principale d'Autopsy](/home/ubuntu/upload/search_images/wWmwPZEecvZz.png)
    *Figure 4: Vue d'ensemble de l'interface principale d'Autopsy, avec ses principaux panneaux.* 

Les principaux panneaux sont :

*   **Tree Viewer (Arborescence des Preuves)** : Situé sur le côté gauche, ce panneau affiche une vue hiérarchique des sources de données ajoutées, des types de fichiers, des artefacts extraits, et des résultats d'analyse.
*   **Result Viewer (Afficheur de Résultats)** : Situé dans la partie supérieure droite, ce panneau affiche les résultats détaillés des sélections faites dans le Tree Viewer. Il peut présenter les données sous forme de tableau, de vignettes ou de résumé.
*   **Content Viewer (Afficheur de Contenu)** : Situé dans la partie inférieure droite, ce panneau affiche le contenu brut ou interprété de l'élément sélectionné dans le Result Viewer. Il peut s'agir de texte, d'images, de vidéos, ou de données hexadécimales.
*   **Status Area (Zone de Statut)** : Située en bas de l'interface, elle affiche la progression des tâches en cours (ingestion, recherche, etc.) et les messages du système.

### 2. Le Tree Viewer (Arborescence des Preuves)

Le Tree Viewer est votre point de départ pour naviguer à travers les données. Il est organisé en plusieurs catégories :

*   **Data Sources** : Liste les images disque, disques locaux ou dossiers logiques que vous avez ajoutés au cas.
*   **Views** : Permet de filtrer les fichiers par type (images, vidéos, documents, etc.), par taille, ou de voir les fichiers supprimés.
*   **Results** : Contient les résultats des modules d'ingestion et d'analyse, organisés par type d'artefact (par exemple, historique web, e-mails, mots-clés, hachages).
*   **Tags** : Affiche les éléments que vous avez marqués avec des tags personnalisés.
*   **Reports** : Contient les rapports générés.

    ![Tree Viewer d'Autopsy](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556609_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzLzRDTzJXdHRzd0c4aA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MDlfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMelJEVHpKWGRIUnpkMGM0YUEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=IwvhUJ975uEAf59Lr18yakpH5eAP7dkn~Ws3nWGgyFI7bAknWEiVJojPvNnvV04gpn7jQwQcxpIgdnafzP2ckPWpOUigPRhnftS6rl2Gt-olAin~P88mIila~s-MLTN4waRoONFkkyrbBGceNzwepp5FU-qhQcjDXwXaAknKzEZk7JQwHNDAUSNub5-nVhzgXIgrW9Rpbb8Q7ez-TPHjjvhSB-R3~VmuXNRWDSuI8oG4fm60Vo8rnj7i0iFRSNlb4NAlWhBnBDzUz1F1~BvIf4wTTQRr02ayYaKRou-fF0BjU8zdTqPNH5w-TeRCb~mXKNc9DWipLWMniuy3zO-fdQ__)
    *Figure 5: Le Tree Viewer, montrant l'organisation hiérarchique des données et des résultats d'analyse.* 

### 3. Le Result Viewer (Afficheur de Résultats)

Lorsque vous sélectionnez un élément dans le Tree Viewer, les résultats correspondants sont affichés dans le Result Viewer. Ce panneau dispose de plusieurs onglets pour différentes vues :

*   **Table** : Affiche les résultats sous forme de tableau, avec des colonnes pour le nom du fichier, le chemin, la date de modification, la taille, etc. Vous pouvez trier et filtrer les colonnes.
*   **Thumbnail** : Pour les fichiers image, cette vue affiche des vignettes des images, ce qui est très utile pour une revue rapide.
*   **Summary** : Fournit un résumé des informations pour l'élément sélectionné.

    ![Result Viewer d'Autopsy - Vue Tableau et Vignettes](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556610_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL3FQNkNVeDB1Q1dsOA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTBfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMM0ZRTmtOVmVEQjFRMWRzT0EucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=vflWLJYwHCmqbNC244cxfW3PmTAg2i64ZbJHtSafADL78lbHtqbrltDeoc4F0JFXqrRljUYsZ26oe03Bk51AFMKIjAlWBZBvH4ISL0jhJkh79XUQped49ItwH8p5Q~jM8AfIIzyriC8hVEUtl2kVYJHW2sWsV-qrCqAo-KCv28Vs0n04gi1g2AIX7Gws6Gc3WNFsok7hm6kHbgAlyua5oHHjV0hB8mRRFA-tM2ehROhw21rj5Oq2ggfOxRKbIk5WJeCzMjAie5e3l5~BnDvXIkilPl1AWi1aOPWMnpuS21BF6ob3Z7TbiSmgdnP5sXeUJ6X2QhqVHo7gcyz4xyDe6A__)
    *Figure 6: Le Result Viewer, affichant les résultats sous forme de tableau et de vignettes pour les images.* 

### 4. Le Content Viewer (Afficheur de Contenu)

Le Content Viewer affiche le contenu de l'élément sélectionné dans le Result Viewer. Il s'adapte au type de fichier :

*   **Text** : Pour les fichiers texte, affiche le contenu lisible.
*   **Hex** : Affiche le contenu du fichier en format hexadécimal, utile pour l'analyse de bas niveau.
*   **Image** : Affiche l'image sélectionnée.
*   **Video** : Permet de lire les fichiers vidéo.
*   **Browser** : Pour les fichiers HTML ou les pages web, affiche le contenu comme un navigateur.

    ![Content Viewer d'Autopsy - Vue Hexadécimale](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556610_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0tieVhpbDhic3prSw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTBfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMHRpZVZocGJEaGljM3ByU3cucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=dqDRAsfqXR0FfApOKdDkMVf~W~0S-V2rSNf~sXnffQA6SfrKEiX0jLgIbeHufEP38zO0JC3uYMbY7YH-zEPkSxRHEOFOjeBfI7eHSqhdWWks04KQOfGmYJ4dlLW7fe5eIgbbCfv1lxOfwRhucq7hnq0ShdsWWFf8hnXOki3cS2E6QY3HfDWOoPq1He7m0YU9Bwtytuxrh-j5DJpvnB76PyB1AZe-axQWxx7onVUSRHBHAZgbyokVsjM1PcN~XeZimtmra5pjU8a87Cn3thvutUEG4res9ZfgdUG4AEqtpcn72HaWKQmzB0zThKz5Htk1~3kbL6kLTyyMFL-M8YpHSw__)
    *Figure 7: Le Content Viewer, affichant le contenu d'un fichier en format hexadécimal.* 

La maîtrise de ces panneaux et de leurs interactions est fondamentale pour naviguer efficacement dans les preuves numériques et extraire les informations pertinentes pour votre enquête.



## Exploration du Système de Fichiers et Récupération de Fichiers Supprimés

L'une des fonctionnalités les plus puissantes d'Autopsy est sa capacité à explorer en profondeur le système de fichiers d'une source de données, y compris la récupération de fichiers supprimés. Cette capacité est cruciale pour découvrir des preuves cachées ou des activités suspectes.

### 1. Exploration du Système de Fichiers

Dans le **Tree Viewer** (panneau de gauche), sous la section `Data Sources`, vous trouverez la source de données que vous avez ajoutée. En la développant, vous verrez la structure du système de fichiers (par exemple, `NTFS`, `FAT32`, `Ext4`).

1.  **Naviguer dans les Dossiers** : Cliquez sur les dossiers pour les développer et explorer leur contenu. Le **Result Viewer** affichera les fichiers et sous-dossiers du répertoire sélectionné.

2.  **Filtrer par Type de Fichier** : Sous la section `Views` dans le Tree Viewer, vous pouvez filtrer les fichiers par type (par exemple, `Images`, `Videos`, `Documents`, `Executables`). Cela est particulièrement utile pour cibler des types de preuves spécifiques.

    ![Exploration du système de fichiers dans Autopsy](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556611_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0JiOTQ2YXNpUE43TA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMEppT1RRMllYTnBVRTQzVEEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=OR1GiICwc2ggTJjheT2Cj34Tjh6WRKaKK4BNH8ixzYbS-93k85VDA4cu~X2~S4Xm3-tBHtwHQ2-s9ykMXMgCeWqQ6wQe8C~e3yiKqGiAvHPh9C8t7R81atNwy5f3RzRXXBfv2w~CwsepBwJnvdEfUl4tI3Z54GdXWroGONZ55Ys8CVYQgDDssZL-mdLTrufB2vG4wLrlt-OrizTcBlKFGvNQ0-bbJZSMv3BmDVCLSX0W5nQ3giAXfOVjh40OI6zmc95qW5Z65yF~V7yqQmCaTxtksHfCvLFJW4k-hRbo1SCIznr7UhEEC3cDACYSPuH9Dq9o6FzSminEJHMiEWngXg__)
    *Figure 8: Exploration de la structure du système de fichiers dans Autopsy, montrant les dossiers et les fichiers.* 

### 2. Identification et Récupération de Fichiers Supprimés

Autopsy est capable de détecter et de lister les fichiers qui ont été supprimés mais dont les données n'ont pas encore été écrasées. Ces fichiers sont souvent une mine d'informations pour les enquêteurs.

1.  **Accéder aux Fichiers Supprimés** : Dans le **Tree Viewer**, sous la section `Views`, cliquez sur `Deleted Files` (Fichiers supprimés). Le **Result Viewer** affichera une liste de tous les fichiers supprimés détectés.

    ![Vue des fichiers supprimés dans Autopsy](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556611_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzLzJONXFSRk1kS0hjVg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMekpPTlhGU1JrMWtTMGhqVmcucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=iAg~UHDEiL6q5fE4ZFYaZGUD6Sio0DDSf7UVYcol5o7JRa8x7CkJmS-DVB6sDSl8-SHV0utXydCavvTGiWRBRxohx4uSm5NICBYFp7kCJkokrx5q2b3afyzc5uIk68~AvumUZuGIuHU-6rDA4CrdV4E6yBZc5lE8HkmoEZWxc4fmw8xg1U0txtnzK3Jo4~~X36caKDp~l~cSNZbSQlm7rcWYLdLvlV2ustUvDJ61dZxYx6NjlaBi9MDdshWw4URX2MXTAigCsFkygNE6bMgTHUDHlwG87w5Rejfhz7tB6Dox~pHGmgLPfI88YKFRGhcyVQyUF6igrVNSKDOL7Wfy1Q__)
    *Figure 9: Liste des fichiers supprimés détectés par Autopsy.* 

2.  **Prévisualiser les Fichiers Supprimés** : Sélectionnez un fichier supprimé dans le Result Viewer. Le **Content Viewer** tentera d'afficher son contenu. Pour les fichiers texte ou les images, vous pourrez souvent voir une partie ou la totalité du contenu.

3.  **Récupérer (Exporter) les Fichiers Supprimés** : Pour récupérer un fichier supprimé, cliquez avec le bouton droit de la souris sur le fichier dans le Result Viewer et sélectionnez `Extract File` (Extraire le fichier). Choisissez un dossier de destination sur votre système d'analyse (pas sur la source de données originale) pour enregistrer le fichier récupéré.

    ![Extraction d'un fichier supprimé dans Autopsy](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556612_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL2IwRzFCZXpNbGRuSA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTJfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMkl3UnpGQ1pYcE5iR1J1U0EucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=Zxf1iSzmasWgCh9QOkxbL6ylSj36ZrVfTsIumR-OLjIuZALzvFRasZPwBMNDLM3H9vFbn4QkmiRivpbKYGxiRkDVToDYua5O~-El-vyGqsydjMdPAOof9w35OC8ZDl9s~4pQ6hLHZCYGnk5pupd3sflMf-KOi4kY-LbHvr4o37EkT-pKOh-DsIOLuQ72LO1y0jbzn4SWDp7stcs1jxK3~GGbTkYSwm6Z01PQlxf1NquOXuwtlmTC1SJoGoE7E60swGIpCQwMVX9L37VCognjAXoFDLfU3qqWnN~46RaOqdolS3mXsn2j1tzbdzbLpOM5XsjtOuilGNDE2pgk3N2iDA__)
    *Figure 10: Extraction d'un fichier supprimé vers un emplacement sécurisé.* 

Il est important de noter que la récupération d'un fichier supprimé n'est pas toujours garantie. Si le système d'exploitation a réutilisé l'espace disque où se trouvait le fichier, une récupération complète peut être impossible. Cependant, Autopsy fait un excellent travail pour récupérer ce qui est récupérable, y compris des fragments de fichiers.



## Analyse des Artefacts : Historique Web, E-mails et Recherche de Mots-clés

Autopsy excelle dans l'extraction et l'analyse d'artefacts numériques cruciaux, tels que l'historique de navigation web, les communications par e-mail et la recherche de mots-clés. Ces fonctionnalités sont essentielles pour reconstituer les activités de l'utilisateur et identifier des informations pertinentes pour l'enquête.

### 1. Analyse de l'Historique Web

L'historique de navigation web est une source d'information inestimable pour comprendre les activités en ligne d'un utilisateur. Autopsy analyse automatiquement les navigateurs web courants (Chrome, Firefox, Edge, Internet Explorer) et extrait les données pertinentes.

1.  **Accéder à l'Historique Web** : Dans le **Tree Viewer**, sous la section `Results` > `Extracted Content` > `Web History` (ou `Web Artifacts`), vous trouverez les entrées d'historique de navigation.

2.  **Explorer les Résultats** : Le **Result Viewer** affichera une liste des URL visitées, avec des informations telles que la date et l'heure de la visite, le titre de la page, et le navigateur utilisé. Vous pouvez trier ces colonnes pour organiser les données.

3.  **Prévisualiser le Contenu** : Sélectionnez une entrée dans le Result Viewer. Le **Content Viewer** tentera d'afficher la page web telle qu'elle était au moment de la visite (si les données sont disponibles dans le cache ou l'image).

    ![Analyse de l'historique web dans Autopsy](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556612_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL2IwUGM3bVBabGRLcw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTJfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMkl3VUdNM2JWQmFiR1JMY3cucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=SxEMyKCHcZuo48ELh89MbKDNpQqwFh9lbP16Zpm9KDhJMinTfp9p~pf5ksHRI-sY90dU3QzYlPL9gjGwqO6NCf1xGzPV~hyySOMq8ejc1QO~nJtYyPGoB87~tEbJHfJe-su5AcaHT4nYdhYpb6nFFe4dmvvSX1949-3Nq5WtdJJIwcWDvO~EV5wujJG9odC-Zx-I85Pd24wCL-GBde9umKKzWGyZHJMeBbLJHLyfV7Qo7we1TG73qTBj6U~9Y3qhUkFs5t~BTdPzMoh5NXP4QGhOpJs6poNdace2139KA~Kq4Aoa0xyd13ENNGerIrEtpStdFLej7XqsIEgPIAH5rQ__)
    *Figure 11: Vue de l'historique web extrait par Autopsy, montrant les URL visitées et les détails associés.* 

### 2. Analyse des E-mails

Autopsy peut analyser les fichiers d'e-mails (comme les fichiers `.pst` de Microsoft Outlook ou les fichiers `.mbox` de Thunderbird) et extraire les messages, les pièces jointes et les métadonnées.

1.  **Accéder aux E-mails** : Dans le **Tree Viewer**, sous la section `Results` > `Extracted Content` > `E-mail Messages` (si le module d'analyse d'e-mails a été activé), vous trouverez les e-mails extraits.

2.  **Explorer les Messages** : Le **Result Viewer** affichera une liste des e-mails, avec des informations telles que l'expéditeur, le destinataire, l'objet, la date et l'heure. Vous pouvez filtrer et trier les messages.

3.  **Prévisualiser le Contenu** : Sélectionnez un e-mail dans le Result Viewer. Le **Content Viewer** affichera le corps du message et les pièces jointes.

    ![Analyse des e-mails dans Autopsy](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556612_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL3psVHl3ZVE3ekZFcg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTJfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMM3BzVkhsM1pWRTNla1pGY2cucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=CrF-0ujgKM3c~35wj6oVgtVoINSYr1nRgdeY7nSNP8LA6VYMi5jjvzupJDC-ZZN5hWoYb5Y8mEkFg3Q9LoWUs4OGiiRUM0XH9WtPLcn9E714eB7o8PvPahFl0CHB0ex~y3Iv~SB9KMTpqME76tHbR896IIJT~XuO5yq51omnmv0K6ghuag6K-zjqNq4~54XQoGe0Cwdib1t~X5t9aHOAg5QHKkVVeMxIGdunchmmupulyoWEZWNZgLLIGh8NCB8M1RakbGjXS5sPmn~bZxEEQs4wnTztvZOp9YW~KlXVyABKtv-BFhlDwv5vQUNtYyXrUYwBDEd8c4WQ~34FrVXkSA__)
    *Figure 12: Affichage des messages e-mail extraits, avec les détails de l'expéditeur, du destinataire et de l'objet.* 

### 3. Recherche de Mots-clés

La recherche de mots-clés est une fonctionnalité puissante pour trouver rapidement des informations spécifiques à travers l'ensemble de la source de données. Autopsy peut effectuer des recherches simples ou des recherches basées sur des expressions régulières.

1.  **Lancer une Recherche de Mots-clés** : Dans la barre d'outils supérieure, cliquez sur l'icône `Keyword Search` (Recherche de mots-clés) ou allez dans `Tools` > `Keyword Search`.

2.  **Configurer la Recherche** :
    *   **Keyword List** (Liste de mots-clés) : Vous pouvez utiliser des listes de mots-clés prédéfinies ou créer les vôtres. Chaque mot-clé sera recherché.
    *   **Keywords** (Mots-clés) : Entrez les mots-clés ou les expressions régulières que vous souhaitez rechercher.
    *   **Search Options** (Options de recherche) : Vous pouvez spécifier si la recherche doit être sensible à la casse, si elle doit inclure les fichiers supprimés, etc.

3.  **Lancer la Recherche** : Cliquez sur `Search` (Rechercher) pour démarrer la recherche. Autopsy parcourra la source de données et affichera les correspondances.

    ![Fenêtre de recherche de mots-clés dans Autopsy](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556613_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL2ZKREd5T01aT3lyWQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTNfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMlpLUkVkNVQwMWFUM2x5V1EucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=UZM2bLmlGiYyW9V9fATUbqCNkb18~Jl6~THOWjdZZ4n~uTR48ZLyPxQsG5OpgulQ3WStijCZQhLk0JSs24GLt2R-Wklo4dl1Q1jXjyT9dPIPai7z1HYJSb2hBgyiR-QLmpzWcRZNg7ykxxb-x858yEEitrbhQpGKoZUMjV6j~38uILOWLuphR5WY-sb8apo7DzR8HhAeWN2qbzfoL2FeW0zsK-uAW7DRJTjTj4xf8JuzVcyfl2HNQnaqAY3WVM2r8NjLvXwL2kzBjFU7yzTjN3QcpZkBL2x1Gd~beXyCfjwVREelUxNdMEQLrhZK4w8rOfXEbLiTkLthYF78VolNig__)
    *Figure 13: Configuration d'une recherche de mots-clés dans Autopsy.* 

4.  **Explorer les Résultats** : Les résultats de la recherche de mots-clés seront affichés dans le **Result Viewer**, indiquant le fichier où le mot-clé a été trouvé, le contexte et d'autres détails. Vous pouvez naviguer directement vers le fichier en question.

    ![Résultats de la recherche de mots-clés](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556613_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL01pUHRTTjNNajAwRg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTNfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMDFwVUhSVFRqTk5hakF3UmcucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=jbYQno3IL5t8Uh99nV7LVTKBXkEfi-cAL1VVdUv4gdCzMyK~UmFORXKzuAN0d-WOxVQxQSFKvQlccb6muxCvN7WWRv7sKi-K4R2xVexlbvJ9nQOfbmxXAdJCok4rMneisr9-ven4cRKKfxucUaECplR7Q1ksHeTCzzk2RTGMVgCKB4qCs66HE7NybqxU3v~eRM-fwCOxsuiabb3Pzy4LR06JKkLUM3PdtgP7F~O~RtqMCVgPE7Gh~1yrKlojiMeZNbbxy47aipyxkuRS~GS-eUqYz1K3EV8wxgxO8T~RCvhvnFZ9NO7BfGLXYokIIFQnkEPw0hzSFdQPFzdcVR5iKg__)
    *Figure 14: Résultats d'une recherche de mots-clés, montrant les correspondances trouvées dans les fichiers.* 

Ces outils d'analyse d'artefacts sont fondamentaux pour extraire des informations exploitables et construire une chronologie des événements dans une enquête forensique.



## Analyse de la Chronologie (Timeline Analysis)

L'analyse de la chronologie est une fonctionnalité extrêmement puissante d'Autopsy qui permet aux enquêteurs de visualiser les événements d'une source de données dans un ordre chronologique. Cela aide à reconstituer les activités de l'utilisateur, à identifier les anomalies et à comprendre la séquence des événements.

### 1. Accéder à la Chronologie

1.  **Lancer Autopsy** : Assurez-vous que votre cas est ouvert et que l'ingestion des données est terminée.

2.  **Sélectionner 'Timeline'** : Dans le menu supérieur, cliquez sur `Tools` (Outils), puis sélectionnez `Timeline` (Chronologie).

    ![Menu Outils - Chronologie](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556613_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL24wamRoZlN0TDdtSg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTNfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMjR3YW1Sb1psTjBURGR0U2cucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=hKddTx98HPJpz9xYhwodNUedH8YF~G6WcEgtdWGwPI6Eir8rDji4pq4xiyFb-FZ4gog-Rq5qvZ9Pox7GCGiwyDYadrycqk7LNxBd7cnDcLOUbEwWdU~-Zq~p6Qk~v38uonfFJVRwuh4OcuxQ4W1ImF7tRelXjN0TZHEeoqc1qYUzo9lqb6GCx3nzhSju~vbusZr3f3lPt0PIl4oiwt9uaf-YHB4Dk8HA7-dbmTJTLwrNXDq3vriDlJ7L~l33ZrCiHqc4-fBjQvOhkMfOTEZum95~fxfrFV3BtVJ7mkKLRoZgQN0jJQevDLCWI~MKqdueMAV8EKPVpggBGaVUjneEqA__)
    *Figure 15: Accès à la fonction 'Timeline' via le menu 'Tools'.* 

### 2. Comprendre l'Interface de la Chronologie

La fenêtre de la chronologie présente une vue graphique des événements, organisée par date et heure. Elle est divisée en plusieurs sections :

*   **Barre de Temps** : Affiche une vue d'ensemble des événements sur une période donnée, souvent représentée par des barres colorées indiquant la densité des événements.
*   **Détails des Événements** : Liste les événements individuels avec des informations telles que la date, l'heure, le type d'événement (création de fichier, modification, accès, etc.), et le fichier ou l'artefact associé.
*   **Filtres** : Permet de filtrer les événements par date, type, source, ou mots-clés pour affiner l'analyse.

    ![Interface de la chronologie d'Autopsy](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556613_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL1FpN1ZQQmxHek41Wg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTNfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMUZwTjFaUVFteEhlazQxV2cucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=EfRVeYwft9~JNqMCa0KTxLG34pySk-DnpWFTXGU0RqEZkj5oWKdBBqd6KXJ9QH~B3r4E5xKkU7W5JdRIvYYhp8WLW29BmSF6hHkKO~zUvZA1lKndCPLN2KEMVN2wFrEiE7jg5lVL-aIGupTBaqH6vzujhmp1QLnL5MTamFTdD6gyTlawB3U0WlDgS9xf-GZ-IfVP9aaS9-WroNz4nGrUyQfUu-5da~7VTTGmCceeW6aHa~dMpmFU8NjRNT1l0HMQGOs~IIn9YxeKGhaZT6HzTV~iBvaAvVgurBuFfwGohFlNJOQVauvoPzXDqpnJpxmB~dZD2R-iqruTHY7HLQGT-Q__)
    *Figure 16: Vue d'ensemble de l'interface de la chronologie d'Autopsy, montrant la barre de temps et les détails des événements.* 

### 3. Utilisation des Filtres et de la Navigation

Pour une analyse efficace de la chronologie, il est crucial d'utiliser les filtres et les options de navigation :

1.  **Zoomer et Dézoomer** : Utilisez les contrôles de zoom pour ajuster la période affichée dans la barre de temps. Vous pouvez zoomer sur des jours, des heures ou même des minutes spécifiques.

2.  **Filtrer par Type d'Événement** : Le panneau de gauche vous permet de filtrer les événements par type (par exemple, 'File System Events', 'Web Activity', 'Email Activity'). Cela aide à se concentrer sur des catégories d'activités spécifiques.

3.  **Recherche de Mots-clés dans la Chronologie** : Vous pouvez effectuer des recherches de mots-clés directement dans la chronologie pour trouver des événements spécifiques liés à des termes d'intérêt.

4.  **Exporter la Chronologie** : Une fois que vous avez identifié une séquence d'événements pertinente, vous pouvez exporter la chronologie sous différents formats (CSV, HTML) pour une analyse ou un rapport ultérieur.

    ![Filtres et navigation dans la chronologie](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556614_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL3dnck9vM2xuWXhTRQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMM2RuY2s5dk0yeHVXWGhUUlEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=WkhuR3VkVo4HgzDspY9nRStHheejJM~EdhuD98DT15g7Z3CS5BV~fYldzmJEazy38P85Yu8-cxfQryoBZ-dUW9ZQSEhvUovpPPTjCLOc-Z8AzumU2YVKp-2mJzwvBgqqJe3nROVWubKwXP~wV7Whlbz55EpfO4C-dWUd1oh2tK1KJ4GItgKJ7mjN6CyYgURAs4wpL9oa0U6sOijqoDiysO6O7UfUiESyjlSYJqfnWiwndujQI75YClsN6UF5guT8Z~2mPDJkb0c2OG0fHT599wERSVHpj6QXAZa3YFrNp2Qzi6XQ77jG8qJgNcykZZDSHCYOdslt3MYC3OGI9PtlLQ__)
    *Figure 17: Utilisation des filtres pour affiner l'affichage des événements dans la chronologie.* 

L'analyse de la chronologie est un outil puissant pour les enquêteurs, car elle permet de visualiser les activités de l'utilisateur de manière dynamique et de détecter des schémas ou des anomalies qui pourraient être difficiles à repérer autrement.



## Recherche de Hachages et Filtrage

La recherche de hachages (hash lookup) est une fonctionnalité fondamentale en criminalistique numérique. Elle permet d'identifier rapidement les fichiers connus (bons ou mauvais) en comparant leurs valeurs de hachage (MD5, SHA1) à des bases de données de hachages préexistantes. Cela aide à réduire le volume de données à analyser et à se concentrer sur les fichiers potentiellement pertinents.

### 1. Comprendre les Bases de Données de Hachages

Autopsy utilise des bases de données de hachages pour classer les fichiers :

*   **Known Good Hashes (Bons Hachages Connus)** : Contiennent les hachages de fichiers système légitimes, d'applications courantes, etc. Ces fichiers peuvent être ignorés lors de l'analyse.
*   **Known Bad Hashes (Mauvais Hachages Connus)** : Contiennent les hachages de malwares, d'outils de piratage, de fichiers illégaux, etc. Ces fichiers sont d'un intérêt particulier pour l'enquête.
*   **Notable Hashes (Hachages Notables)** : Des hachages personnalisés que vous pouvez créer pour marquer des fichiers spécifiques à votre enquête.

### 2. Configuration du Module de Recherche de Hachages

Lors de l'ajout d'une source de données, vous avez la possibilité d'activer et de configurer le module `Hash Lookup`.

1.  **Accéder aux Options d'Ingestion** : Lors de l'étape de configuration des modules d'ingestion (voir section 


2.2 Ajout de Sources de Données), assurez-vous que le module `Hash Lookup` est coché.

2.  **Gérer les Bases de Données de Hachages** : Vous pouvez gérer les bases de données de hachages via `Tools` > `Options` > `Hash Databases`. Ici, vous pouvez ajouter de nouvelles bases de données (par exemple, la NSRL - National Software Reference Library), les activer ou les désactiver.

    ![Configuration des bases de données de hachages](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556614_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL01CRDdMMzVCOUNiRQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMDFDUkRkTU16VkNPVU5pUlEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=Q9GQq2tslgfkegV8j3tmZ29GiOALRiuwOXm0apm8yt48suRNCN~0YIgXgM9QEmOhm8~CuZDvHNbS1bjEDZQYkYUeKlIcBfW2Djf7eoMazsKLoBgR-GqAfP1wn3Vf6hze0xbkkieqIZemXp7vWcb9hh7XxllXnCA0mUPQrVmRGP4LQ8dwuynE7ZoqHG25ClHNMDsMdMk05mbjL-W-fPTeFPiaImGwnEScjgGC6bHEN~JyIFT0IJFgsqfORz9m~QPGtZiBOY-c5IGpZ1c~hznH8jmwx5QCaV2o~COMitfNmTJM3RJ0DEWLna-NeUnFHUoaz-w6F4ocWupnmd2jhh7VmA__)
    *Figure 18: Gestion des bases de données de hachages dans les options d'Autopsy.* 

### 3. Analyse et Filtrage par Hachages

Une fois le module `Hash Lookup` activé et les bases de données configurées, Autopsy calculera automatiquement les hachages de tous les fichiers lors de l'ingestion et les comparera aux bases de données.

1.  **Voir les Résultats des Hachages** : Dans le **Tree Viewer**, sous la section `Results` > `Hashset Hits`, vous trouverez les fichiers qui ont correspondu à une entrée dans l'une de vos bases de données de hachages.

    *   **Known Bad Files** : Fichiers identifiés comme malveillants ou illégaux.
    *   **Known Good Files** : Fichiers système ou d'applications légitimes.
    *   **Notable Files** : Fichiers que vous avez marqués comme notables.

    ![Résultats des correspondances de hachages](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556614_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL1F5SlRhUnF2bExqOQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMUY1U2xSaFVuRjJiRXhxT1EucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=f0hUuMfgc0Z-cYd0MR27jacF~aBD~E9sO~WuzzKmH0oFm3fNJWA3yvFUMsd7ZkqfEIRFMtpLblZgJ50amMrOQ8ntjzg5HJENnYfzmhFZzod7BS0aE~1M0k89GYbIgrS1gSoavFs22yQOXppDMTUPO9I-Q-VUxMy0glQsR7UJQhqaPOOy4WwF4nEOES~eIBB3cIvQMyCVUbBGAI5M5ELuYHx9vKSZkV29ifuxULiY7YSQvH1cr4Qk4lJE3JH4qqq2Zv36OG~YhUUAfWjUBlKyQF1pe1zgp77qEU2~zLwUDB3u7BeTTZ6M2vL-HbKNP~faALPDVIiwooahWfA7q7NN6g__)
    *Figure 19: Affichage des fichiers identifiés par les bases de données de hachages.* 

2.  **Filtrage des Résultats** : La recherche de hachages permet de filtrer rapidement les fichiers non pertinents (connus comme bons) et de se concentrer sur les fichiers suspects ou inconnus. Vous pouvez utiliser les options de filtrage dans le Result Viewer pour n'afficher que les fichiers 


qui correspondent à certains critères (par exemple, `Known Bad` ou `Notable`).

La recherche de hachages est un gain de temps considérable et une méthode fiable pour identifier rapidement les fichiers d'intérêt ou à ignorer, rendant l'analyse forensique plus efficace.



## Fonctionnalités de Rapports dans Autopsy

La phase finale de toute investigation forensique est la génération d'un rapport. Autopsy offre des fonctionnalités robustes pour créer des rapports personnalisables qui résument les découvertes clés de votre analyse. Ces rapports sont essentiels pour documenter l'enquête, présenter les preuves aux parties prenantes et soutenir les conclusions forensiques.

### 1. Génération d'un Rapport

1.  **Accéder à la Fonctionnalité de Rapport** : Une fois votre analyse terminée et les artefacts pertinents identifiés, vous pouvez générer un rapport en allant dans le menu supérieur `Tools` (Outils) > `Generate Report` (Générer un rapport).

    ![Menu Outils - Générer un rapport](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556615_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0tES2l1ZlZKRkFJTg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTVfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMHRFUzJsMVpsWktSa0ZKVGcucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=pjGnOZY2Cezx1aE~NyzAlMya-KauG~pyQW4vxTJKoQVyn2s-qk0SwrI41k0q2Iir9elDBRUNzVnDsfACynijBgXkWCqx~NiijaXvmHJx100VxgLEOdbO-rMkGKmEw0PTdxFr63HoA2Y7LpPKHKgwSxzDEWAq5gYSlYoCKLw56~hbmm7J-ylbxsvYo9Xkv7fc8tjyXKx2Wzpj5C7vCpvJVdiiygGrZXuOqWhoNK8Izc3zdT-bMRzHBBurPPON8m2MOX0qFU1A-gr4mlhWMP-QkrIHUXqUPf~fXVUlCM3ikdoo90J4sr5rCJsemIzxiX4MnoabQTh84daBkf75OJskHA__)
    *Figure 20: Accès à la fonction de génération de rapport via le menu 'Tools'.* 

2.  **Sélectionner les Modules de Rapport** : Autopsy propose différents formats de rapport. Vous pouvez sélectionner un ou plusieurs modules de rapport en fonction de vos besoins :
    *   **HTML Report** : Un rapport interactif en HTML, facile à naviguer et à partager.
    *   **Excel Report** : Un rapport au format CSV ou XLSX, utile pour l'analyse de données tabulaires.
    *   **KML Report** : Pour les données géospatiales, exporte les informations de localisation au format KML pour Google Earth.
    *   **Body File** : Crée un fichier de corps (body file) au format mactime, utile pour l'analyse chronologique externe.
    *   **JSON Report** : Un rapport au format JSON, idéal pour l'intégration avec d'autres outils ou scripts.

    Cochez les formats de rapport souhaités et cliquez sur `Next`.

    ![Sélection des modules de rapport](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556615_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL3VqOExFTHZpS2Q5Rw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTVfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMM1ZxT0V4RlRIWnBTMlE1UncucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=nH3jTZsAbfluqhdnHqIaaZ~RbpgQM1ZzkoRgipC~EG3avrL~yCaplqATHxIiKHUjwBx2SGQ6iC8934BuqHp9bbHqBnds3~DP1wzPEo1zGwdrezadr3LHrmOxY5Ae73JpFZBz9ZOHRiEx~n-t~MRd6DRL7mrLy~-ElceTu2f4nuE0ddZ8PXEGNoT7RNgYRmJJtRZnRJOb1-tFwIyNP48q2EJPqvuRgL7HPssDb20lT1F4zkAXFFchOtPgVvJxyKnkYBD3NsZs9CX4YojQhCmf8qaf4P8Huxee6tNj2XZaqI2B27o4xRqG1Pp13WerGJrc62Gei-f0ThbnNftQ~AtCVA__)
    *Figure 21: Sélection des formats de rapport à générer dans Autopsy.* 

3.  **Configurer les Données du Rapport** : À cette étape, vous pouvez choisir quelles données inclure dans votre rapport. Vous avez généralement deux options :
    *   **All Results** (Tous les résultats) : Inclut tous les artefacts et les résultats d'analyse découverts par Autopsy.
    *   **Tagged Results** (Résultats marqués) : Inclut uniquement les éléments que vous avez spécifiquement marqués (tagués) comme importants pendant votre analyse. C'est souvent l'option préférée pour créer des rapports ciblés et concis.

    Si vous choisissez `Tagged Results`, vous pouvez ensuite sélectionner les types de tags que vous souhaitez inclure.

    ![Configuration des données du rapport](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556615_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0U3Nk0yUjFHUFF2Tg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTVfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMFUzTmsweVVqRkhVRkYyVGcucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=ACMxs8GRtuLZBEA8zFD6MA42TYKZDj9IdStkvD60pbrdKRfQ-1yKnLagqbN3plJe1neb96hmFIS8v7PJ0qD2CNygBCr5f4Fz0vaJaS6UfVatmoztK0nIsy6-0~GQCUQwS20pS2cdjwZcEitrQtWS6bhJOo7SsIiqPq5ND-JGrh7d8H2GjzufX5Eg0M86lJhO~mRxa10MNFUqyx2NFto1a5W6--NeWpGCmSp65vveNsEoC86G5AYY99SuCClYNyGW1yUK5vDNiSxxqHg1y~0ejm6MkkvIzCa4wiLn4XALmlmsZDaCLqpNtTyS~DOFidgrjqD8Zk9~pUA6jEg8m8SvpQ__)
    *Figure 22: Configuration des données à inclure dans le rapport (tous les résultats ou seulement les résultats marqués).* 

4.  **Générer le Rapport** : Cliquez sur `Finish` (Terminer) pour lancer la génération du rapport. Le temps nécessaire dépendra de la quantité de données à inclure et du format choisi.

    ![Progression de la génération du rapport](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556616_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL1F6S084R3pCTjl5WA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMUY2UzA4NFIzcENUamw1V0EucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=CaLFZ2-qAyqj8Whsf5MJskaYFexFf9R13f7OZlQud2PoM5Gr9TsoJi3iL45VDGRpEskIJif3ITom5rbXl1PzC5NE-D0SKtl-6-5FxEFiVeUu5d9p8McGCeZ9lIDLwJcN2fmaXZGNgdjyfWH7HuHIYyEZZYqoMmwn0gYfSpGagk2cKOig9SDc2wsD2dwFsbYhqwnztxVS~Bj67c9fYzJcKUpl9bcyJ9mn8UapxBmeAdTSOyWj2h7ylMka2Dn5BC8V6D4rRJVZjRz4izZ7H5061gohuUXLUynOEkgphL5rZn33RKl6YZKTxFr~7osa0P~ZKr1vSkjOMPwmrfa3j2zvQA__)
    *Figure 23: Progression de la génération du rapport dans Autopsy.* 

### 2. Examen et Utilisation des Rapports

Une fois le rapport généré, Autopsy vous fournira un lien vers le dossier où les fichiers du rapport sont enregistrés. Vous pouvez alors ouvrir et examiner le rapport.

*   **Rapport HTML** : Le rapport HTML est interactif et permet de naviguer facilement entre les différentes sections (historique web, e-mails, fichiers supprimés, etc.). Il est idéal pour la présentation des résultats.

    ![Exemple de rapport HTML généré par Autopsy](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/bq8xHr7EU2CfSlf3pSwi7K-images_1749847556616_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzLzhabmI4ZnVLRjZFRw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L2JxOHhIcjdFVTJDZlNsZjNwU3dpN0staW1hZ2VzXzE3NDk4NDc1NTY2MTZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMemhhYm1JNFpuVkxSalpGUncucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=m6sG7cCM7Nq5fTz~3qyohlmM~Zj6iRD~RJGsqr9K7q9BTv~fby13lvIKax~hXtOsFxJ0oNAUIC2EmygYjOw-Mxs9klqn2~dgsKZrrClstFxBd5fzh0gZLfOK8D-3AlBcHGW5E~iMOth-w9rVDUs9Qb8F-Mrm7WtNHquFGnLzMNpYpNWtt4alJSr6wtA6ky333ooBTeSTpAQL6vRV-dD6~jnoCfqlblz~XIQeBrGYZ008KEsVvDxRRJBNrBg-qXnEGk-KF3R09AE9Z9lKfO-aq9DrKQOGlHEBnvjih4koa0Jo4trvSCLhn~gEvv9KmNVSaIh51VCP8Ca4fmzAcW8c~Q__)
    *Figure 24: Exemple d'un rapport HTML généré par Autopsy, montrant la navigation et les informations résumées.* 

*   **Autres Formats** : Les rapports Excel peuvent être utilisés pour des analyses statistiques ou des tris personnalisés, tandis que les fichiers KML sont parfaits pour visualiser les données géospatiales.

La capacité à générer des rapports clairs et complets est une compétence essentielle en criminalistique numérique, et Autopsy simplifie grandement ce processus, permettant aux enquêteurs de communiquer efficacement leurs découvertes.

