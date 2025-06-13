# 🛡️ Unprotect Project – *Scan* Service

> Analyse instantanément vos exécutables Windows et identifiez les techniques d'évasion qu'ils renferment.

> ℹ️ **Note :** Ce service est un outil d'analyse statique qui utilise des règles prédéfinies et des patterns de détection pour identifier les techniques d'évasion. Bien qu'il soit automatisé, il ne s'agit pas d'un service basé sur l'intelligence artificielle.

---

## 🔍 Aperçu
- **Unprotect Scan**, c'est un uploader (≤ 20 MiB) qui dissèque votre binaire PE et lui associe les techniques d'évasion répertoriées par le projet open-source **Unprotect**.  
- Les rapports sont publics par défaut ; cochez la case *Do not show the scan report on the boards* pour rester discret. 🔒

---

## 🚀 Guide ultra-rapide
1. Rendez-vous sur **[unprotect.it/scan](https://unprotect.it/scan/)**.  
2. Glissez-déposez `sample.exe`, `malware.dll` ou un ZIP. 📦  
3. (Optionnel) Cochez la case confidentialité ci-dessus.  
4. Cliquez **Scan** et récupérez l'URL permanente vers votre rapport.  

> 🗨️ *Astuce :* gardez le hash SHA-256 à portée de main pour retrouver votre analyse plus tard.

---

## 📑 Ce que contient le rapport

| Section | Infos délivrées | Exemple |
|---------|-----------------|---------|
| **Matching Techniques** | Liste des techniques + ID + règle | `INT3 Instruction Scanning` (U0105) |
| **Meta-data** | Hashes, compile-time, archi, signature PEiD | `loader.exe` (x86-64, 29 mai 2025) |
| **Imports & APIs** | APIs marquantes (ex. `VirtualAlloc`) | Même échantillon |

---

## ✨ Techniques mises en lumière

| 🏷️ Catégorie | 💡 Technique | Résumé éclair |
|--------------|-------------|--------------|
| Anti-Debugging | **INT3 Instruction Scanning** | Repère les breakpoints `0xCC` pour détecter un débogueur. |
| Obfuscation d'API | **API hashing** | Remplace les noms d'API par des hashes. |
| Sandbox Evasion | **API Hammering** | Inonde la sandbox d'appels bénins pour retarder l'analyse. |
| Anti-Monitoring | **EnumProcess scanning** | Cherche `ollydbg.exe`, `wireshark.exe`, etc. |

---

## 🛠️ Accès programmatique (API)

```bash
# Extrait simplifié
curl -F "file=@sample.exe" \
     -H "Authorization: Bearer <TOKEN>" \
     https://unprotect.it/api/scan
# ➜ JSON : report_url, techniques[], hashes…
```

---

## 📅 Mise à jour
- Dernière mise à jour : [Date]
- Version : 1.0
- Statut : Actif 