# 🔍 Gobuster – Outil de Bruteforce pour la Découverte de Contenus Web

## 📌 Présentation

**Gobuster** est un outil en ligne de commande, écrit en Go, qui permet de réaliser des attaques de **bruteforce** pour découvrir des **chemins cachés** sur des serveurs web, des **fichiers**, des **sous-domaines**, ou des **buckets S3**.

Il est couramment utilisé par les pentesteurs et les professionnels de la cybersécurité pendant la phase de **reconnaissance** d'un audit.

---

## 🛠️ Fonctionnalités principales

- 🔹 Bruteforce de **répertoires et fichiers** (`dir`)
- 🔹 Bruteforce de **sous-domaines** (`dns`)
- 🔹 Bruteforce de **buckets S3** (`s3`)
- 🔹 Découverte via **Virtual Hosts** (`vhost`)
- 🔹 Rapide grâce au multithreading

---

## 💻 Installation

### 🔧 Sous Kali Linux ou Debian :

```bash
sudo apt install gobuster
📦 Depuis la source (nécessite Go) :

go install github.com/OJ/gobuster/v3@latest
🧪 Commandes courantes
📁 Découverte de répertoires :

gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt
Options utiles :
Option	Description
-u	URL cible
-w	Wordlist utilisée
-x	Extensions à tester (ex: php, html, txt)
-t	Nombre de threads (par défaut : 10)
-o	Fichier de sortie
-k	Ignorer les erreurs de certificat SSL
--wildcard	Gérer les réponses wildcard (pour DNS)

🌐 Découverte de sous-domaines :

gobuster dns -d target.com -w subdomains.txt
🪣 Bruteforce de buckets S3 :

gobuster s3 -w wordlist.txt
🧾 Exemple complet :

gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/big.txt -x php,txt -t 30 -o resultats.txt
🛑 Avertissement légal
Comme pour tout outil de sécurité, n'utilisez jamais Gobuster sans une autorisation explicite. Toute utilisation non autorisée peut être illégale.

📚 Ressources
🔗 GitHub officiel

📘 Wordlists recommandées : /usr/share/wordlists/ (Kali)

🧰 Alternative : Dirb
