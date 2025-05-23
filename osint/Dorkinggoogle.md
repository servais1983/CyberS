🕵️‍♂️ Google Dorking — Techniques avancées de recherche
Le Google Dorking est une méthode d’OSINT qui consiste à utiliser des requêtes avancées dans les moteurs de recherche (principalement Google) pour accéder à des informations sensibles ou cachées mais publiquement disponibles.

⚠️ À utiliser uniquement à des fins légales et éthiques (test de sécurité, pentest autorisé, OSINT, etc.)

🔍 Opérateurs de recherche Google
Opérateur	Description	Exemple
site:	Recherche uniquement dans un domaine ou sous-domaine donné	site:example.com
inurl:	Recherche d'une chaîne dans l'URL	inurl:admin
intitle:	Recherche d'une chaîne dans le titre de la page	intitle:index of
filetype:	Recherche un type de fichier spécifique	filetype:pdf
ext:	Synonyme de filetype:	ext:sql
intext:	Recherche un mot-clé dans le corps de la page	intext:"confidential"
cache:	Affiche la version en cache d'une page	cache:example.com
related:	Trouve des sites similaires à un autre	related:example.com
allintext:	Tous les mots doivent apparaître dans le texte	allintext:login password
allinurl:	Tous les mots doivent apparaître dans l'URL	allinurl:admin login
allintitle:	Tous les mots doivent apparaître dans le titre	allintitle:admin panel
*	Joker (remplace un ou plusieurs mots)	"login * admin"
OR	OU logique	filetype:pdf OR filetype:xls
-	Exclusion	site:gov -site:nasa.gov

🛠️ Exemples de Dorks utiles
🔐 Trouver des pages d'administration
bash
Copier
Modifier
inurl:admin
intitle:"admin login"
site:example.com inurl:admin
🗃️ Fichiers exposés (PDF, DOC, XLS, etc.)
bash
Copier
Modifier
filetype:pdf confidential
filetype:xls password
intitle:"index of" "backup"
🔑 Informations sensibles
bash
Copier
Modifier
intext:"index of /" "passwd"
intitle:"index of /" "database"
filetype:env DB_PASSWORD
🧪 Recherches techniques (log, config, Git, .env…)
bash
Copier
Modifier
filetype:log site:example.com
filetype:env site:example.com
intitle:"index of /.git"
intitle:"index of" .bash_history
🧍‍♂️ Fuites de credentials
bash
Copier
Modifier
filetype:txt intext:"password"
intext:"username=*" intext:"password=*"
inurl:"/phpmyadmin" "Welcome to phpMyAdmin"
📂 Listes de fichiers accessibles
bash
Copier
Modifier
intitle:"index of" "parent directory"
intitle:"index of" site:gov filetype:xls
🛡️ Bonnes pratiques
✅ Pour tester légalement, ciblez vos propres domaines ou ceux sur lesquels vous avez une autorisation.
✅ Combinez les dorks avec d'autres outils (ex : Google, Shodan, Hunter.io, Spiderfoot)
🚫 N’exploitez pas des données sensibles trouvées sans autorisation.

📚 Ressources complémentaires
🔗 Google Hacking Database (GHDB)

🔎 Operators Doc Google

📖 Livre : Google Hacking for Penetration Testers – Johnny Long

