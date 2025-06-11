

<h1 align="center">Tycoon 2FA : le kit de phishing-as-a-service qui contourne la MFA</h1>

<p align="center">
  <a href="#points-forts"><img src="https://img.shields.io/badge/Active_depuis-Août 2023-red?style=for-the-badge&logo=launchpad" alt="Active since 2023"></a>
  <a href="#evasion--stealth"><img src="https://img.shields.io/badge/Dernière_màj-Avril 2025-orange?style=for-the-badge&logo=javascript" alt="April 2025 update"></a>
  <a href="#stats--tendances"><img src="https://img.shields.io/badge/Type-PhaaS-AitM-critical?style=for-the-badge&logo=cloudflare" alt="PhaaS / AitM"></a>
</p>

---

## ✨ Points forts
| | Fonctionnalité | Détails |
| --- | --- | --- |
| 🛰️ | **Adversary-in-the-Middle (AitM)** | Intercepte le trafic entre l’utilisateur et la page Microsoft 365 ou Gmail pour voler les cookies de session et contourner la MFA :contentReference[oaicite:0]{index=0} |
| 🧩 | **Modèle PhaaS low-cost** | Pages de phishing prêtes à l’emploi vendues sur Telegram : 120 $ pour 10 jours, jusqu’à 320 $ selon le TLD :contentReference[oaicite:1]{index=1} |
| ⚙️ | **Écosystème en expansion** | >1 100 domaines recensés entre oct. 2023 et fév. 2024 ; popularité croissante auprès d’IABs :contentReference[oaicite:2]{index=2} |

---

## 🔗 Chaîne d’attaque (6 étapes)

| Étape | Ce qui se passe |
| --- | --- |
| 0️⃣ | Lien ou QR code dans l’e-mail / PDF malveillant |
| 1️⃣ | Passage par un **Cloudflare Turnstile** ou CAPTCHA custom pour filtrer les bots |
| 2️⃣ | Redirection JS invisible vers une page intermédiaire |
| 3️⃣ | Nouvelle redirection vers page de phishing finale |
| 4️⃣ | Faux formulaire Microsoft / Google, code HTML obfusqué |
| 5️⃣ | Cookies de session capturés → accès sans MFA :contentReference[oaicite:3]{index=3} |

---

## 🕵️‍♂️ Évasion & Stealth
| Technique | Description |
| --- | --- |
| 🖼️ CAPTCHA HTML5 canvas | Blocage des scanners automatisés :contentReference[oaicite:4]{index=4} |
| 🫥 **Caractères Unicode invisibles** | Encodage binaire “0/1” dans le JS pour gêner l’analyse statique :contentReference[oaicite:5]{index=5} |
| 🕷️ Anti-debug / anti-DevTools | Redirection vers site légitime si inspection détectée :contentReference[oaicite:6]{index=6} |
| 🙈 Obfuscation & clipboard jamming | Code auto-généré + impossibilité de copier le texte :contentReference[oaicite:7]{index=7} |

---

## 📈 Stats & Tendances

| Indicateur (e-mail) | Valeur / tendance |
| --- | --- |
| Attaques d’identifiants liées au PhaaS (2024) | **≈ 30 %** |
| Projection 2025 | **≈ 50 %** des attaques de credentials utiliseront un kit PhaaS :contentReference[oaicite:8]{index=8} |

---

## 🛡️ Bonnes pratiques de défense
1. **Passer au FIDO2** / passkeys pour éliminer les cookies de session réutilisables.  
2. Activer la revocation agressive des cookies sur tout changement de contexte (IP, UA).  
3. Surveillez les domaines “lookalike” ; bloquez ceux signalés dans les IOCs Tycoon.  
4. Combinez filtrage d’URL, sandbox *et* détection comportementale (anti-AitM).  
5. Entraînez les utilisateurs : lures bonus/paye, faux voicemail, QR codes sont les plus courants :contentReference[oaicite:9]{index=9}  

---

## 📚 Ressources

- 🔎 **Proofpoint :** « Unmasking Tycoon 2FA » (mai 2024)  
- 🕳️ **Dark Reading :** « Tycoon 2FA bypasses Microsoft & Google MFA » (mars 2024)  
- 🐍 **Trustwave SpiderLabs :** « New evasion techniques 2025 » (avr. 2025)  
- 🛑 **Barracuda Threat Spotlight :** « Tycoon 2FA updated to evade inspection » (janv. 2025)  

> *Tycoon 2FA illustre l’évolution fulgurante du phishing-as-a-service : accessible, modulaire, et capable de neutraliser la MFA classique. Restez vigilants !*
