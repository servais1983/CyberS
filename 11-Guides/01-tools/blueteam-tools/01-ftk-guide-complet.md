# Manuel Très Complet de FTK Imager

## Introduction : FTK Imager, l'Outil Indispensable de la Criminalistique Numérique

Dans le domaine de la criminalistique numérique (forensics), l'acquisition de données est une étape fondamentale et critique. Pour qu'une preuve numérique soit recevable et fiable, elle doit être collectée de manière intègre, sans altération et en respectant des procédures strictes. C'est dans ce contexte que **FTK Imager** se positionne comme un outil gratuit et puissant, largement reconnu et utilisé par les enquêteurs, les analystes forensiques et les professionnels de la cybersécurité.

### Qu'est-ce que FTK Imager ?

FTK Imager est un utilitaire logiciel développé par AccessData (désormais Exterro) qui permet de créer des images forensiques bit-à-bit de disques durs, de clés USB, de la mémoire vive (RAM), de dossiers spécifiques ou même de fichiers individuels. Une image forensique est une copie exacte et fidèle d'un support de stockage, incluant non seulement les fichiers visibles, mais aussi les données supprimées, les espaces non alloués et les métadonnées, le tout sans altérer la source originale.

### Pourquoi FTK Imager est-il Essentiel en Criminalistique Numérique ?

FTK Imager est un pilier de la boîte à outils forensique pour plusieurs raisons :

*   **Intégrité des Preuves** : L'outil garantit que l'acquisition des données est réalisée de manière 



## Installation de FTK Imager : Un Guide Détaillé

L'installation de FTK Imager est un processus simple et direct, mais il est important de suivre les étapes pour s'assurer que l'outil est correctement configuré et prêt à l'emploi. FTK Imager est un logiciel Windows, donc ces instructions sont spécifiques à cet environnement.

### 1. Téléchargement de FTK Imager

FTK Imager est disponible gratuitement sur le site officiel d'Exterro (anciennement AccessData).

1.  **Accédez au Site Officiel d'Exterro** : Ouvrez votre navigateur web et naviguez vers la page de téléchargement de FTK Imager : [https://www.exterro.com/ftk-imager](https://www.exterro.com/ftk-imager)

2.  **Enregistrez-vous ou Connectez-vous** : Exterro exige généralement une inscription gratuite pour télécharger ses outils. Remplissez le formulaire avec vos informations (nom, adresse e-mail professionnelle, organisation, etc.) ou connectez-vous si vous avez déjà un compte.

3.  **Téléchargez la Dernière Version** : Une fois le formulaire soumis, vous devriez être redirigé vers la page de téléchargement. Cliquez sur le lien pour télécharger la dernière version de FTK Imager (généralement un fichier `.exe`).

    ![Page de téléchargement de FTK Imager](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143614_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzLzJXaEozdTlwQ3hoQg.jpg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MTRfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMekpYYUVvemRUbHdRM2hvUWcuanBnIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=fUTl6~oZSWAhJKZ2GEUCSQTLQf4yC547HrG6sZGO5HWzfdM8BMZA5rSHM0YeEe6F59SKOLztYyoNhxGxvKEoqq8zO8pYpg4ot6NkWfWs7HOyxNY1pCDSkwrPGDDeaqGMIwAaT0NlWlHtFwqV~7NZ9FOpnwcPgaS3~h-43HFcLODziyUvH085oru42adsoVpVx3dciYD1YHFG5OxuprxO~nKjizt8UOGnJI7UD-SedHYbfUQXh0UW7UW2X-2Hd04yNMkoeQvfLRtv9xLOD5zojpTLrbijHk4KFg~WO717ZF2b6R5gftdQVvo9IDdL-HYNPHsbPbZ3924TrohzG0hTRw__)
    *Figure 1: Page de téléchargement de FTK Imager sur le site d'Exterro.* 

### 2. Installation de FTK Imager

Une fois le fichier d'installation téléchargé, vous pouvez procéder à l'installation.

1.  **Exécutez l'Installeur** : Localisez le fichier `.exe` téléchargé (par exemple, `FTKImager_X.X.X.exe`) et double-cliquez dessus pour lancer l'assistant d'installation.

2.  **Assistant d'Installation** :
    *   **Écran de Bienvenue** : Cliquez sur `Next` (Suivant) sur l'écran de bienvenue de l'assistant d'installation.

    *   **Contrat de Licence** : Lisez attentivement le contrat de licence utilisateur final (EULA). Si vous acceptez les termes, sélectionnez `I accept the terms in the License Agreement` et cliquez sur `Next`.

    *   **Dossier de Destination** : Choisissez le dossier où FTK Imager sera installé. Le chemin par défaut est généralement recommandé, sauf si vous avez une raison spécifique de le modifier. Cliquez sur `Next`.

    *   **Prêt à Installer** : L'assistant est maintenant prêt à installer le programme. Cliquez sur `Install` (Installer) pour commencer le processus.

    ![Assistant d'installation de FTK Imager](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143615_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0VnMGQyN0lsa0plTw.jpg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MTVfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMFZuTUdReU4wbHNhMHBsVHcuanBnIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=GepunI019XJyT3IzYbica3UOODvHQgv4YgxjjPblFPrthUjMUbXIensWjioo3CDb0v0-QxGWMNtlmoA7mJczxmHE8nXECysmR6PXqM68hz3oTEPpmeX5LPxb3YXohZoyHi51zVm3~S8zSENqnOkveOoEFjd3AC9H8YwPEXgdD1XJzG8shcQihFP9uynU2nHyH6g9-WdfrxVLSPbP115~9YJd4djGbSPqZhDPzf6A8ayiUNn11Fw~SDIbLkBlq6awgAkgAnQfGHEdNPNLKX4CzvhJqbGfwIs0gwlQWiLlCxP9juRUkhxRrrYe7qgOIhXq3C2oxBjk2CoKiyzoW85iNQ__)
    *Figure 2: Assistant d'installation de FTK Imager, montrant l'étape 



## Création d'une Image Disque avec FTK Imager

La fonction principale de FTK Imager est de créer des images forensiques de divers supports de stockage. Ce processus est crucial pour préserver l'intégrité des preuves numériques. Nous allons détailler la création d'une image d'un disque physique, qui est l'un des scénarios les plus courants.

### 1. Lancement de la Création d'Image Disque

1.  **Ouvrez FTK Imager** : Lancez l'application FTK Imager. Vous verrez l'interface principale.

2.  **Sélectionnez 'Create Disk Image'** : Dans le menu supérieur, cliquez sur `File` (Fichier), puis sélectionnez `Create Disk Image` (Créer une image disque).

    ![Menu Fichier - Créer une image disque](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143616_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0dscWxoOERoRmFTeQ.jpeg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MTZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMGRzY1d4b09FUm9SbUZUZVEuanBlZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NzIyNTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=v~toLq7sakq6O7uT9KwdAWlGNGsILn~u4~TPgWXfFNgFarJjnRie~ns~Dcpg4mHJ7-FWgFOE8w9gnmh1wZgCDaHR8Y2SDJ-zP0qbk2VjMQ0p0JMUJp-e7RUrSVbP4jbWlE57syjYNU6f90aighmyNeXLRrMsAnJ8Clcdoku5u7zAHbplvJSV7-V~~yMuJZXzp-q4ShVC5yr0d6gkz7tPo4-~Ci67~VHm5kCI9PraduYVx8vkr4VCIQES6OQaUjVogS3qy4jO~nZYpYiaR5HFO~Kvo8qqQXLVNMP5upVnlkc7zbl7gM4Jp601oq94CXN5w2y2sGfHyhT3ErcZmAHTCw__)
    *Figure 3: Accès à la fonction 'Create Disk Image' via le menu 'File'.* 

### 2. Choix du Type de Source

Une fenêtre 



## Montage d'une Image Disque avec FTK Imager

Une fois que vous avez créé une image forensique, il est souvent nécessaire de la "monter" pour pouvoir l'explorer comme un disque dur normal, sans altérer l'original. FTK Imager permet de monter des images en mode lecture seule, garantissant ainsi l'intégrité des preuves.

### 1. Lancement du Montage d'Image

1.  **Ouvrez FTK Imager** : Lancez l'application FTK Imager.

2.  **Sélectionnez 'Image Mounting'** : Dans le menu supérieur, cliquez sur `File` (Fichier), puis sélectionnez `Image Mounting` (Montage d'image).

    ![Menu Fichier - Montage d'image](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143617_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL2luYTczWDJDOXhrUg.jpeg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MTdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMmx1WVRjeldESkRPWGhyVWcuanBlZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NzIyNTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=VEPIkkayn-ZOAlIw9qXW7lkn8gV2e35kyWCdfc~Bi~h8Wwq3RTLiiLU6h3TRegAokr8LHsKolFkbs67JbMwK5Bg4BgCboKxleT68i7pMjaKYz0fsTtZcYmgL4KPbiM36lZGzRgv1Al9-9Se8lG-2ndAdGBDRncat3eI28tdVbp6ZquB6UpuhzUwJRrLOky7YajDTAPEOIlOkDsEcRJO5CnEVwg6qXHHqMXsZHGrjGX7FzDpJsTZVz6r~zmo4h7fvbzIP4dv7eGPSsrS3jAz3xPb4Nt9wr-0lg1ReqxQrHKkQu4JM-R~5k1CbfTlA3UG63t-SlmtwYUvPwdzQVPy9PQ__)
    *Figure 7: Accès à la fonction 'Image Mounting' via le menu 'File'.* 

### 2. Configuration du Montage

Une fenêtre 'Image Mounting' s'ouvrira, vous permettant de configurer les options de montage.

1.  **Chemin de l'Image** : Cliquez sur le bouton `Add Image` (Ajouter une image) et naviguez jusqu'à l'emplacement de votre fichier d'image forensique (par exemple, un fichier `.E01`, `.DD`, ou `.AFF`). Sélectionnez le fichier et cliquez sur `Open`.

2.  **Type de Montage** :
    *   **Physical Drive** : Monte l'image comme un disque physique. Cela permet d'accéder à toutes les partitions et à l'espace non alloué, comme si le disque original était connecté.
    *   **Logical Drive** : Monte uniquement les partitions logiques de l'image, comme des lettres de lecteur (par exemple, `D:`, `E:`). C'est utile si vous voulez simplement explorer les fichiers et dossiers visibles.

3.  **Mode de Montage** :
    *   **Read-Only (Recommandé)** : C'est le mode par défaut et le plus sûr. Il garantit que l'image ne sera pas modifiée pendant l'exploration, préservant ainsi l'intégrité des preuves.
    *   **Writable (À utiliser avec prudence)** : Permet d'écrire sur l'image montée. À n'utiliser que dans des environnements de test contrôlés et jamais avec des preuves originales, car cela altérerait l'image.

4.  **Lettre de Lecteur** : Choisissez une lettre de lecteur disponible pour le montage de l'image (par exemple, `Z:`).

5.  **Cliquez sur 'Mount'** : Une fois les options configurées, cliquez sur le bouton `Mount` (Monter) pour démarrer le processus de montage.

    ![Fenêtre de configuration du montage d'image](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143617_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0ZpbDV1N3EwZlpwNQ.jpg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MTdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMFpwYkRWMU4zRXdabHB3TlEuanBnIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=AVeHRCzbRsP5nwj64-PFBvXD29DkFRDrJ7p1SWrBQGZsA1bJ5ZbgXWeEPLKia2VwCLcyPPabakiI-f1Pbe7ScHDmC88PqSmfZRUVRu4lJA7FDN0m-0wYu3-q8smdfFDDYYPGXGlsuXgt9OrDDF6Xer9qPEo4g-Vfr813YOfbxBu8AKR0J4jUPCombY-j4BlkbJImntRavO5pIG3Xies4dVjB2ut2EhouBpVjJU3o03P5xB75ElapxQWpy1oENOw-K35xCEEpjmbni3bWrDNwbgDRxEXgX7vYiAXBiEyMyNm-q-~cz2JdHwCRRC8dGuzFJUG4k9lY~fMEOhkfpDwrTw__)
    *Figure 8: Configuration des options de montage d'une image disque dans FTK Imager.* 

### 3. Exploration de l'Image Montée

Une fois l'image montée avec succès, elle apparaîtra comme un nouveau lecteur dans l'Explorateur de fichiers de Windows. Vous pouvez alors l'explorer, copier des fichiers, et effectuer des analyses comme vous le feriez avec un disque dur physique, mais en toute sécurité en mode lecture seule.

    ![Image montée dans l'Explorateur Windows](/home/ubuntu/upload/search_images/2kLMR9fBuERo.jpg)
    *Figure 9: L'image disque montée apparaît comme un nouveau lecteur dans l'Explorateur de fichiers de Windows.* 

### 4. Démontage de l'Image

Lorsque vous avez terminé votre analyse, il est important de démonter l'image pour libérer les ressources et s'assurer qu'aucune modification accidentelle ne puisse survenir.

1.  **Retournez à la fenêtre 'Image Mounting'** : Dans FTK Imager, allez dans `File` > `Image Mounting`.

2.  **Sélectionnez l'Image à Démonter** : Dans la liste des images montées, sélectionnez celle que vous souhaitez démonter.

3.  **Cliquez sur 'Dismount'** : Cliquez sur le bouton `Dismount` (Démonter). L'image sera alors retirée du système.

    ![Démontage d'une image disque](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143618_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0ROUFRZbG1wMUx3Qg.jpg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMFJPVUZSWmJHMXdNVXgzUWcuanBnIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=PsJdpMj4zaQgT~LDM0540NltOj0h2YY01z4qn3IdsROERAmnhni1VHgYWLgmFJ-tV9kcm5J5V4hg6t8JXRido5TuV9PdcbfuQx4~N1elChQ1hb731vsq2fQ3QvO-4aVzOlrp8DgJtlwXcwC8tbu4eTkAFD2cDbgjAsSoJtdQ6AlSEfepFqpWGvrt0Mu9ImypRQtRiRCIrSBxFZmSOJF2GoUuOucQvY3KNVfDRmgI0FMJHL5lCQaAlE~Lutjvhxmbc1sP7Of4~RGFl0pHnfzIRPQNrMZdEsuCwF4cojAhs63WePdi1jB8arU4upFyoZuPFlrGHp1b3WC45hSxeEb71A__)
    *Figure 10: Démontage d'une image disque après l'analyse.* 

Le montage d'images est une fonctionnalité puissante de FTK Imager qui facilite l'analyse forensique en permettant une exploration non destructive des preuves numériques.



## Capture de la Mémoire Vive (RAM) avec FTK Imager

La capture de la mémoire vive (RAM) est une étape essentielle en criminalistique numérique, notamment pour l'analyse des artefacts volatils (processus en cours, connexions réseau actives, clés de chiffrement, mots de passe en clair, etc.) qui disparaissent à l'extinction de l'ordinateur. FTK Imager offre une fonctionnalité simple pour réaliser cette capture.

### 1. Lancement de la Capture de Mémoire

1.  **Ouvrez FTK Imager** : Lancez l'application FTK Imager.

2.  **Sélectionnez 'Capture Memory'** : Dans le menu supérieur, cliquez sur `File` (Fichier), puis sélectionnez `Capture Memory` (Capturer la mémoire).

    ![Menu Fichier - Capturer la mémoire](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143618_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL3Y0ZjRKblNQQXMxag.jpeg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MThfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMM1kwWmpSS2JsTlFRWE14YWcuanBlZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NzIyNTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=hYRJIKVwPAGvDTGPCwfUG4FkB81-7IN71LwO1NeL8F7WjgxIIG33p~QcVSs2RIl-NngN6l2WPqFp5woQsr1qxrcLrRrgdpnUDUs8jdsiNjxmF-1FcU94UdioeuclL3aFCEzq1pUmgPRH8dm9EN3cijrZcqAvHLXAFPVaQxEbu2WMGDD26R2xLV5PS1kfUPE1eaArHGjKK39AGbeoWsEQQtZVUFxjETQoam1DHgwKjbfVMLx0krzeC2pgis-2EYHNszM8wCtnKUfFRoKrlzfhzpsebTTxERSYrDJrxTXGvNVFC4dygCR5rnh8mnWnONftJpUqJTfBtCInbsecVakPbQ__)
    *Figure 11: Accès à la fonction 'Capture Memory' via le menu 'File'.* 

### 2. Configuration de la Capture de Mémoire

Une fenêtre 'Memory Capture' s'ouvrira, vous permettant de spécifier l'emplacement et le nom du fichier de sortie.

1.  **Chemin de Destination** : Cliquez sur le bouton `Browse` (Parcourir) et choisissez un emplacement pour enregistrer le fichier de vidage de la mémoire. Il est recommandé de l'enregistrer sur un support externe ou un emplacement sécurisé pour ne pas altérer le système cible.

2.  **Nom du Fichier** : Donnez un nom significatif au fichier de vidage de la mémoire (par exemple, `RAM_dump_DATE_TIME.mem`). L'extension `.mem` est couramment utilisée.

3.  **Inclure le Fichier d'Échange (Pagefile.sys)** : Vous avez l'option d'inclure le fichier d'échange (`pagefile.sys`) dans la capture. Le fichier d'échange est utilisé par Windows pour stocker temporairement des données de la RAM sur le disque dur lorsque la mémoire physique est pleine. L'inclure peut fournir des informations supplémentaires, mais augmentera la taille du fichier de sortie.

4.  **Créer un fichier AD1 avec le fichier d'échange et les fichiers protégés** : Cette option permet de créer un fichier d'image forensique au format AD1 qui inclura le fichier d'échange et les fichiers protégés (comme le SAM, SYSTEM, SECURITY hives du registre). C'est une option très utile pour une analyse complète.

5.  **Cliquez sur 'Capture Memory'** : Une fois les options configurées, cliquez sur le bouton `Capture Memory` pour démarrer le processus. La durée de la capture dépendra de la quantité de RAM et de la vitesse du disque de destination.

    ![Fenêtre de configuration de la capture de mémoire](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143619_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL25tVmNBSjY5QTdWeg.jpg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MTlfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMjV0Vm1OQlNqWTVRVGRXZWcuanBnIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=lIZ4QBROgmWMLUMJmMzwoNZraOj17olz39uweIZA5ZrKqNEzcjQ4A1AQxaZINxn2SvaY3FpsJvYGfJVIJzbHULPUEJAV68O2bWII69~5cNFmMDbeWXc1n7~~EubiCHdz9GWTJMN9UCLNrRQFgYtBtMYdUqUAgvP2tcDOPn-SGsCLVsFb8pze-IleLFvr18L6uRQT96ja3N0K3lAWQpMtBRKp5HdjhUrvtei1ZWs3Lk7ulyOq37OXBwq0YNBJ-IUQsZEDo7dOAltMLHAoARwUTiIyg4AlsGQg2qIEZ9AW4DenEOdAAX~cHq3O9FJgC3LnLTaP4mk4bjbKjwsExUl2Ow__)
    *Figure 12: Configuration des options de capture de mémoire dans FTK Imager.* 

### 3. Progression et Fin de la Capture

FTK Imager affichera une barre de progression pendant la capture. Une fois terminée, un message de confirmation apparaîtra.

    ![Progression de la capture de mémoire](/home/ubuntu/upload/search_images/d69i61kwrjzc.jpg)
    *Figure 13: Progression de la capture de mémoire vive.* 

Le fichier de vidage de la mémoire (`.mem` ou `.ad1`) pourra ensuite être analysé avec des outils spécialisés comme Volatility Framework pour extraire des informations précieuses.



## Obtention de Fichiers Protégés avec FTK Imager

Certains fichiers sur un système d'exploitation, comme le registre Windows (SAM, SYSTEM, SECURITY) ou les fichiers de mots de passe (NTDS.dit sur les contrôleurs de domaine), sont souvent verrouillés ou protégés par le système d'exploitation en cours d'exécution. FTK Imager offre une fonctionnalité pour contourner ces protections et acquérir ces fichiers essentiels pour l'analyse forensique.

### 1. Lancement de l'Obtention de Fichiers Protégés

1.  **Ouvrez FTK Imager** : Lancez l'application FTK Imager.

2.  **Sélectionnez 'Obtain Protected Files'** : Dans le menu supérieur, cliquez sur `File` (Fichier), puis sélectionnez `Obtain Protected Files` (Obtenir les fichiers protégés).

    ![Menu Fichier - Obtenir les fichiers protégés](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143619_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL2hpNW1BYU9wd3Fjdw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MTlfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMmhwTlcxQllVOXdkM0ZqZHcucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=kVdT86gKM7h0wGPNH79qvLXImPPEHokL6HP~V2ukIQdXEnGIfMyQt2AKU3jCtkaEyiHPmJQp-WTncCqHMjDsOOqfbsQGoIe3xfr-Zx3dmXF3yByLTYxSo~ksuDYSajpYBuP6edap9pEXu1YTfd0dmATe3oGJwWWi7veFKwCsLV-K9t9wlORxnH~Jpi6BL3AisB02Pxa3bpw95dfNJMgYtDj7vY08IlQ6XB7TTxPIe6Zd1v47HTzWqpFYKRt8XY0Eb5QqbCyVElBM2iypz-pFwUAUkmWFyeKxqPZHT-xceKgnWOiJSttio093tvAXlC68x-Qyq1Ulaa7TbQLoLFf-dw__)
    *Figure 14: Accès à la fonction 'Obtain Protected Files' via le menu 'File'.* 

### 2. Configuration de l'Obtention de Fichiers Protégés

Une fenêtre 'Obtain Protected Files' s'ouvrira, vous permettant de choisir les types de fichiers à acquérir et l'emplacement de destination.

1.  **Sélectionnez les Fichiers à Obtenir** : FTK Imager vous présentera une liste de fichiers protégés courants que vous pouvez acquérir. Les options typiques incluent :
    *   **Password Hashes (SAM/SYSTEM/SECURITY)** : Pour extraire les hachages de mots de passe du registre Windows.
    *   **NTDS.dit (Active Directory Database)** : Pour les contrôleurs de domaine, ce fichier contient les informations d'identification des utilisateurs du domaine.
    *   **Other Protected Files** : D'autres fichiers système qui pourraient être verrouillés.

    Cochez les cases correspondant aux fichiers que vous souhaitez acquérir.

2.  **Chemin de Destination** : Cliquez sur le bouton `Browse` (Parcourir) et choisissez un dossier de destination pour enregistrer les fichiers extraits. Il est recommandé de les enregistrer sur un support externe ou un emplacement sécurisé.

3.  **Cliquez sur 'OK'** : Une fois les options configurées, cliquez sur `OK` pour démarrer le processus d'extraction.

    ![Fenêtre d'obtention des fichiers protégés](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143620_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL1dZVTc1ZFlWc1pNUQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MjBfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMWRaVlRjMVpGbFdjMXBOVVEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=EUURhj0RLapzdT80zD8pJAplZemL5kcNVvcPRW39sIRoOr8L0kEztofDOZqAASNqAEwIZfUlqYoFB6nTrbgboo350gLxZc53ryebii3LpbbJgEkEKdNBDDaa9o3685AI04eCG6HT~5u5cDhisfoPWjPLmm2Vxqh3UG72yXye-cOIB3n-CUqsMnAII3RYTZxv~uV4BCPxlN-B0hI6tizNsFhSr1-QkF3TBFsf5yJJUItbge6tX7WM8s43ZNCZAHJk5w700F78aPoPQ6X2xSl8Y9di77zUmfYjmI0K091gzGq6ggt~f1AfovmbEIWM~IZlWuiegvgkYf~xzfIC-RmxDw__)
    *Figure 15: Configuration des options pour obtenir les fichiers protégés dans FTK Imager.* 

### 3. Progression et Fin de l'Extraction

FTK Imager affichera une barre de progression pendant l'extraction. Une fois terminée, un message de confirmation apparaîtra.

    ![Progression de l'extraction des fichiers protégés](/home/ubuntu/upload/search_images/VOBCt9YPDXmg.png)
    *Figure 16: Progression de l'extraction des fichiers protégés.* 

Ces fichiers extraits sont cruciaux pour des analyses ultérieures, notamment pour le craquage de mots de passe (avec des outils comme Hashcat ou John the Ripper) ou pour l'analyse des informations d'identification du domaine.



## Exportation de Fichiers et Dossiers avec FTK Imager

Après avoir acquis une image forensique ou monté une image, vous aurez souvent besoin d'exporter des fichiers ou des dossiers spécifiques pour une analyse plus approfondie ou pour les présenter comme preuves. FTK Imager permet d'exporter des éléments individuels ou des répertoires entiers tout en préservant leurs métadonnées.

### 1. Navigation et Sélection des Éléments

1.  **Chargez l'Image ou le Disque** : Assurez-vous que l'image forensique est chargée dans FTK Imager (soit en l'ajoutant comme élément de preuve, soit en la montant).

2.  **Explorez l'Arborescence** : Dans le panneau de gauche (Evidence Tree), naviguez à travers l'arborescence du système de fichiers pour localiser les fichiers ou dossiers que vous souhaitez exporter.

3.  **Sélectionnez les Éléments** : Cliquez sur les fichiers ou dossiers que vous voulez exporter. Vous pouvez sélectionner plusieurs éléments en utilisant les touches `Ctrl` ou `Shift`.

    ![Exploration de l'arborescence et sélection de fichiers](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143620_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0N2OFhESHlFOWFXQQ.jpeg?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MjBfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMME4yT0ZoRVNIbEZPV0ZYUVEuanBlZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NzIyNTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=B83dCN177eNKXAhf0v57OpNNNdUJeJLCl-yLi2tYqPPOW2BGi8gbOQVRx9W0aOjQjuI09td30G7cgN2nkr3CnMYG5e1lvyw9FM6RyH-tSC4t759~wxAclGq-OTeOu915TC1jH~igDGPO4GVC9StUQhRMZDADWUCNNcdzaigaV1q95lehEDE77~bRh3AjFqqZuagduX5BUtztA9MUelb9Od17np~mK3fIPeStFMJun2NSMxEvmPO2lQhgxWa-aLAGaP7h~vlBIBJQqkqEan45Sojy76wemXN~zuLUPAOxh-9qo~BA6pv9ZR0npynFo~QEGSxEeUQmp0FZOxg7dKhlcw__)
    *Figure 17: Navigation dans l'arborescence des preuves et sélection des fichiers à exporter.* 

### 2. Lancement de l'Exportation

1.  **Cliquez Droit ou Utilisez le Menu Fichier** : Une fois les éléments sélectionnés, vous avez deux options :
    *   **Clic Droit** : Cliquez avec le bouton droit de la souris sur la sélection et choisissez `Export Files` (Exporter les fichiers).
    *   **Menu Fichier** : Allez dans `File` (Fichier) > `Export Files`.

    ![Menu Fichier - Export Files](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143620_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL1N3dmNraXJPQ1YxeA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MjBfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMU4zZG1OcmFYSlBRMVl4ZUEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=beR7SXOCSRPhMQ7cykERM2vdjwY8b6h~-jQsN-r~nMTlFor7nwHxPNTTs035016BoCfR0kQ39MrMb4DoAOm7PHNYYZka4aTeQYa7IUlXCRKSxqUEbi9PIcWkdwqJ1YXnKnZxeJ17ty4RWGmaNm-OpuINKtOatQXhk3bX06rG1XjGNUuF1NfmLBaLmnpbSmR3~Qg7tOELO20-eS2F6o52zLhA7yr~yVI1n65nyfvMavZif6e5PMNO502pfspHjvrFv5W0XsPrQNdr2mtTd5zx9FYXZGp6TfjcMCUSRdMV0O-ZWLDS~mweSdLPMo88h5yCSgt8SZA6KSI2W0jw4gvYkA__)
    *Figure 18: Accès à la fonction d'exportation de fichiers via le menu contextuel ou le menu 'File'.* 

### 3. Configuration de l'Exportation

Une fenêtre de dialogue s'ouvrira, vous demandant de spécifier l'emplacement de destination.

1.  **Choisissez le Dossier de Destination** : Cliquez sur `Browse` (Parcourir) et sélectionnez le dossier où vous souhaitez enregistrer les fichiers exportés. Il est recommandé de choisir un emplacement sécurisé et organisé pour vos preuves.

2.  **Cliquez sur 'OK'** : Une fois le dossier de destination choisi, cliquez sur `OK` pour lancer l'exportation.

    ![Fenêtre de sélection du dossier de destination pour l'exportation](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143621_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0pPbTFWQjI2NU5TeQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MjFfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMHBQYlRGV1FqSTJOVTVUZVEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=SgpQ22vn-tq9TxnMXQWUHXA9WgktYcAIblsuIuYFVya89Bv-a3RVX9BaGQdeiiCeVpsk6~p4HUeoOGrlzor1EphQDc-L-HLjSRyL3TGMCA47v2R2b2oqDfFcU2OUPjQRNE2v3hq8OIwvbPtrAbjyzrZ~MkbWvuMas-lKkEt5lzr0NH4gfK2zhE91aHofRDYDN88couEanrR5PkyOfHeYk~rvCNmntDupUrKM1Q5iJu8XzzzRFep4XyycIUal9KLF2UKsVd79Rew2qNqVq2C903CVkHWSBE5wiaaZRVP2LvCwBbEGDj63nipZHLzQlCebpZiGY9IOLu2dui7f-9B2mA__)
    *Figure 19: Sélection du dossier de destination pour les fichiers exportés.* 

### 4. Progression et Fin de l'Exportation

FTK Imager affichera une barre de progression pendant l'exportation. Une fois terminée, un message de confirmation apparaîtra.

    ![Progression de l'exportation des fichiers](/home/ubuntu/upload/search_images/hX8S8ijWKRjq.png)
    *Figure 20: Progression de l'exportation des fichiers et dossiers.* 

Les fichiers et dossiers exportés conserveront leurs noms d'origine et, dans la mesure du possible, leurs métadonnées. Cette fonctionnalité est essentielle pour isoler des éléments spécifiques d'une preuve numérique pour une analyse ciblée ou pour les partager avec d'autres outils ou parties prenantes.



## Vérification d'une Image Disque avec FTK Imager

La vérification de l'intégrité d'une image forensique est une étape cruciale pour s'assurer que l'image est une copie exacte et non altérée de la source originale. FTK Imager permet de comparer les valeurs de hachage (MD5 et SHA1) de l'image avec celles calculées à partir de la source, garantissant ainsi la fidélité de la copie.

### 1. Lancement de la Vérification

1.  **Ouvrez FTK Imager** : Lancez l'application FTK Imager.

2.  **Ajoutez l'Élément de Preuve** : Si l'image n'est pas déjà chargée, allez dans `File` (Fichier) > `Add Evidence Item` (Ajouter un élément de preuve) et sélectionnez votre fichier d'image forensique.

3.  **Sélectionnez l'Image à Vérifier** : Dans le panneau de gauche (Evidence Tree), sélectionnez l'image disque que vous souhaitez vérifier.

4.  **Sélectionnez 'Verify Drive/Image'** : Dans le menu supérieur, cliquez sur `File` (Fichier), puis sélectionnez `Verify Drive/Image` (Vérifier le lecteur/l'image).

    ![Menu Fichier - Vérifier le lecteur/l'image](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143622_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL1FMQVVobnNUMDBMWg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MjJfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMUZNUVZWb2JuTlVNREJNV2cucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=MrGYjHQxgLL4uqKzH9hl9LLWunmYhCsAmDz~tiwOs3J3NypWwgWQvPbpY8ch~OsbFT7Fwxt~rvyqmRm7nPhE0scMRcqw09W1d3mBhrFfXGgVw6mQ0mojsCR93D-9-yoQHpf6d4S08OoEU9jBtQQIEgunnsvkpB1LJM4vxAcaw8iUftgQ7~T6CALVfu~rfugYK-qtA3yMvM0rr~HoNB7TOy9gncjFxXCLZyxFgguecLG3ZWLOuDk~DopPJG9yO5YzXOnYNOj-fi4xPnEII0TrQvqNHIq4qsqLeNJpG3jo4CeO7rHFZqeWvJ-jf49RPos1LY9Ul5UujSugCbHGmjmsSg__)
    *Figure 21: Accès à la fonction 'Verify Drive/Image' via le menu 'File'.* 

### 2. Processus de Vérification

FTK Imager va alors calculer les valeurs de hachage (MD5 et SHA1) de l'image et les comparer avec les valeurs de hachage qui ont été enregistrées lors de la création de l'image (si elles ont été incluses).

    ![Progression de la vérification de l'image](/home/ubuntu/upload/search_images/ciTJIOykiXzC.png)
    *Figure 22: Progression de la vérification de l'intégrité de l'image disque.* 

### 3. Résultats de la Vérification

Une fois le processus terminé, une fenêtre 'Drive/Image Verify Results' s'affichera, présentant les résultats de la comparaison des hachages.

*   **MD5 Hash** : Affiche le hachage MD5 calculé et le compare avec le hachage stocké. Le statut doit être `Match` (Correspondance).
*   **SHA1 Hash** : Affiche le hachage SHA1 calculé et le compare avec le hachage stocké. Le statut doit également être `Match`.
*   **Bad Blocks List** : Indique si des blocs défectueux ont été trouvés dans l'image. Idéalement, cette liste devrait être vide.

    ![Résultats de la vérification de l'image](https://private-us-east-1.manuscdn.com/sessionFile/qGmLfo3bbhr8fQu0zeox2w/sandbox/RuiGvlS9W95QMuBrU79OSu-images_1749845143622_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0lnWHhkdHFBazgySQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvcUdtTGZvM2JiaHI4ZlF1MHplb3gydy9zYW5kYm94L1J1aUd2bFM5Vzk1UU11QnJVNzlPU3UtaW1hZ2VzXzE3NDk4NDUxNDM2MjJfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMGxuV0hoa2RIRkJhemd5U1EucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzY3MjI1NjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=qEcP0c1juwe9qik-PwKV9jnNYl~Ft3SFaLP8IMiI59zke53A9PWUoshfrI-22RIAvJEfRVRL0sHAtYOgerA1hE-EXX6JtgIOoCVkw4Ex3IAfvuFFmjiKygN96EzejmUDVSsa4ZWGWaH~~XbnGmmiD4IL9R2USh8Pd~S9W4zl0xo~TnacU8x5MGZrtRkBvEPWiT2xJBdWjvhe2DRJ2t~xZBs2gDLn5mK8DTx970WaD3jt5tvF7bdtesyLitsGsehHPqDj~IudY6VxBwKiM40WOh5I7ruO8Gdeeh25yt-~EZx4Zg33tLRXXyXMW5cdNUwhMBrsA1YQUAxgjb-gv8PpHA__)
    *Figure 23: Résultats de la vérification de l'image, confirmant l'intégrité des données.* 

Si les hachages correspondent et qu'aucun bloc défectueux n'est signalé, cela confirme que l'image forensique est une copie bit-à-bit exacte de la source originale et que son intégrité a été préservée. Cette étape est fondamentale pour la recevabilité des preuves numériques en justice.



## Conclusion : FTK Imager, Votre Allié en Criminalistique Numérique

FTK Imager est bien plus qu'un simple outil de copie de données ; c'est une pierre angulaire de la criminalistique numérique. Sa capacité à créer des images forensiques bit-à-bit, à monter ces images en toute sécurité, à capturer la mémoire vive et à extraire des fichiers protégés en fait un utilitaire indispensable pour tout professionnel de la sécurité ou de l'investigation.

En maîtrisant FTK Imager, vous vous assurez que vos acquisitions de preuves numériques sont réalisées avec la plus grande intégrité, garantissant leur recevabilité et leur fiabilité dans le cadre d'une enquête ou d'une procédure judiciaire. C'est un outil qui, par sa simplicité d'utilisation et sa robustesse, permet de se concentrer sur l'analyse des données plutôt que sur les défis techniques de l'acquisition.

Nous espérons que ce manuel détaillé vous aura fourni les connaissances nécessaires pour utiliser FTK Imager de manière efficace et professionnelle. N'oubliez jamais l'importance de la chaîne de conservation des preuves et de l'intégrité des données dans toutes vos opérations forensiques.

