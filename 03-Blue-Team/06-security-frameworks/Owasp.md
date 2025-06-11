# 🔐 Guide Complet – OWASP & Sécurité des Applications Web

## 📖 1. Qu’est-ce que l’OWASP ?

L’**OWASP** (Open Worldwide Application Security Project) est une organisation à but non lucratif qui fournit des **ressources open-source** pour améliorer la sécurité des logiciels, notamment :

- Bonnes pratiques de développement sécurisé
- Référentiels (OWASP Top 10, ASVS, Mobile Top 10, etc.)
- Outils de test et d’analyse
- Formations et événements

---

## 🔟 2. OWASP Top 10 (2021)

Le **OWASP Top 10** est une liste des **10 principales vulnérabilités applicatives** les plus critiques. Mise à jour régulièrement, elle guide les développeurs et pentesters.

| Rang | Vulnérabilité                        | Exemple concret                                  |
|------|--------------------------------------|--------------------------------------------------|
| A01  | Broken Access Control                | Lecture des données d’un autre utilisateur       |
| A02  | Cryptographic Failures               | Stockage MD5 de mots de passe                    |
| A03  | Injection                            | SQLi, XSS, LDAPi                                 |
| A04  | Insecure Design                      | Absence de logique de sécurité                   |
| A05  | Security Misconfiguration            | Stack trace visible, ports ouverts               |
| A06  | Vulnerable and Outdated Components   | Librairies non mises à jour                      |
| A07  | Identification and Authentication Failures | Auth sans expiration de session           |
| A08  | Software and Data Integrity Failures | MàJ non signées, dépendances non vérifiées       |
| A09  | Security Logging and Monitoring Failures | Aucune trace des attaques                    |
| A10  | Server-Side Request Forgery (SSRF)   | Requête interne vers une ressource non exposée   |

---

## 🧠 3. Bonnes pratiques de développement sécurisé

| Aspect                  | Recommandation                               |
|-------------------------|----------------------------------------------|
| 🔐 Authentification     | Hashing sécurisé (bcrypt/argon2), MFA        |
| 🧱 Contrôle d’accès     | Vérification côté serveur, pas dans le front |
| 🧼 Entrées utilisateur  | Sanitation, validation (ex: `express-validator`)|
| 🛡️ Headers HTTP        | `X-Frame-Options`, `Content-Security-Policy` |
| 🔒 Session             | Cookies HttpOnly, Secure, rotation régulière |
| 📦 Dépendances         | Scanner via `npm audit`, `pip-audit`, etc.   |

---

## 🔧 4. Outils de test et automatisation

### 🛠️ Outils OWASP recommandés

| Outil        | Fonction                                 |
|--------------|------------------------------------------|
| **ZAP**      | Proxy et scanner de vulnérabilités web   |
| **Amass**    | Enumération DNS / reconnaissance         |
| **Dependency-Check** | Analyse de CVE dans les dépendances |
| **DefectDojo** | Tracker de vulnérabilités DevSecOps     |

### 🔬 Outils externes compatibles

- **Burp Suite** (scanner semi-automatique)
- **Nikto** (scan vulnérabilités serveur)
- **Trivy**, **Grype** (images Docker)
- **Snyk**, **GitHub Advisory**, **SonarQube**

---

## 🧪 5. Intégration dans un pipeline DevSecOps

| Étape CI/CD      | Action sécurité                         |
|------------------|------------------------------------------|
| 🏗️ Build         | Scan dépendances (`OWASP DC`, Snyk)     |
| 🧪 Test           | Scan DAST (ZAP automation)              |
| 🚀 Déploiement    | Headers HTTP, CSP en prod               |
| 📊 Monitoring     | Journalisation + SIEM/EDR                |

➡️ Exemple : Intégration de ZAP dans GitLab CI

```yaml
zap_scan:
  image: owasp/zap2docker-stable
  script:
    - zap-baseline.py -t http://localhost:3000
🧾 6. OWASP Projects utiles
Projet	Description
ASVS (App Sec Verification Standard)	Grille d’audit complète des applis
MASVS	Sécurité des applis mobiles
SAMM	Maturité sécurité logiciel (benchmark)
Cheat Sheets Series	Recettes sécurité pour développeurs
Threat Dragon	Modélisation de menace

📋 7. Checklist OWASP de base
Item	État
🔐 Authentification sécurisée (pas de MD5/SHA1)	✅ / ❌
🧼 Validation des entrées côté serveur	✅ / ❌
🔒 Sessions sécurisées + cookies HttpOnly	✅ / ❌
🧱 Accès basés sur rôles	✅ / ❌
🔄 Mises à jour des dépendances	✅ / ❌
📊 Logs d’accès et erreurs activés	✅ / ❌
🚧 Scanner ZAP exécuté dans le pipeline CI	✅ / ❌

📚 8. Ressources et documentation
🔗 OWASP Top 10 (2021)

📘 OWASP ASVS

🧰 OWASP ZAP

📖 Cheat Sheet Series

🎓 OWASP Training & Labs

yaml


---
