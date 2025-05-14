# 📬 Analyse d’une en-tête de mail sous Linux

L’analyse de l’entête d’un email permet de :
- Identifier l’adresse IP et le serveur d’envoi
- Vérifier l’authenticité de l’expéditeur
- Détecter des techniques de spoofing ou phishing

---

## 📂 1. Obtenir l’en-tête complet d’un email

Depuis un webmail ou un client (Thunderbird, Outlook) :
- **Gmail** : Plus (⋮) → "Afficher l’original"
- **Outlook** : Fichier → Propriétés → En-têtes Internet
- **Thunderbird** : `Ctrl + U` ou `Affichage > Code source du message`

📝 Copie-colle l’en-tête dans un fichier texte sur Linux, par exemple : `header.txt`

---

## 🧪 2. Lire le fichier sous Linux

```bash
cat header.txt | less
Ou ouvrir avec un éditeur :


nano header.txt
🔍 3. Éléments clés à analyser
Champ	Utilité
From:	Adresse déclarée de l’expéditeur (peut être spoofée)
Return-Path:	Adresse de retour réelle
Received:	Liste des serveurs par lesquels le mail est passé
Received-SPF:	Résultat de la vérification SPF (authentification IP)
Authentication-Results:	Résultats DKIM, SPF, DMARC
Message-ID:	Identifiant unique (souvent utilisé pour retracer)
Date:	Date/heure d’envoi (peut être falsifiée)
Subject:	Sujet de l’email

🧭 4. Suivre le chemin du mail (Received:)
Les lignes Received: sont en ordre inverse :

La dernière = point d’origine

La première = réception finale (votre serveur)

🔎 Exemple :

vbnet

Received: from mail.fake.com (unknown [203.0.113.5])
        by mx.votresite.fr (Postfix) with ESMTP id 123456789;
        Thu, 14 May 2025 10:01:00 +0200 (CEST)
Tu peux extraire toutes les IP :


grep "Received:" header.txt | grep -Eo '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
🛡️ 5. Vérifier SPF, DKIM et DMARC
Exemple dans le header :

pgsql

Authentication-Results: spf=fail smtp.mailfrom=fake.com;
                        dkim=fail header.d=fake.com;
                        dmarc=fail action=none header.from=fake.com;
➡️ Interprétation :

SPF fail : le serveur d’envoi n’est pas autorisé pour ce domaine

DKIM fail : signature non valide ou absente

DMARC fail : politique du domaine non respectée

🌍 6. Géolocaliser l’IP d’envoi (facultatif)

whois 203.0.113.5
geoiplookup 203.0.113.5
🧠 7. Outils en ligne utiles
🔎 MXToolbox Header Analyzer

🔍 Google Admin Toolbox Messageheader

🧪 Mailheader.org

✅ Astuces
L’en-tête peut révéler des domaines frauduleux (ex : micr0soft.com)

Regarde les décalages horaires ou Date: incorrecte

En forensic, compare les Message-ID dans des spams similaires

📘 Références
RFC 5322 – Format d’un email

Email header cheat sheet

SPF/DKIM/DMARC specs – https://dmarc.org/
