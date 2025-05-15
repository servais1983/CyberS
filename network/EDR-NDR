# 🛡️ Stratégie de Détection avec EDR & NDR

## 🎯 Objectif

Utiliser les capacités complémentaires de l’EDR (sur les endpoints) et du NDR (sur le réseau) pour maximiser la couverture de détection, réduire les angles morts et accélérer la réponse aux incidents.

---

## 1. 🔍 Vue d’Ensemble

| Composant | Fonction principale | Cible | Exemple de détection |
|-----------|---------------------|-------|-----------------------|
| **EDR**   | Surveillance des endpoints (PC, serveurs) | Processus, fichiers, registres, mémoire | `powershell.exe` exécuté par `winword.exe` |
| **NDR**   | Surveillance du trafic réseau | Paquets, flux, protocoles | Exfiltration de données via DNS tunneling |

---

## 2. 🧠 Détection avec l’EDR

### 2.1. Cas d’usage typiques

- Exécution de commandes suspectes (`cmd`, `powershell`, `wmic`)
- Création de fichiers exécutables dans des chemins temporaires
- Persistence via clés de registre
- Attaques en mémoire (living-off-the-land)
- Utilisation anormale d’outils légitimes (LOLbins)

### 2.2. Méthodes de détection

- **Règles comportementales** (e.g., MITRE T1059 – Command and Scripting Interpreter)
- **Machine Learning** pour détecter les attaques sans signature
- **IOC matching** (hashs, chemins, certificats, etc.)

---

## 3. 🌐 Détection avec le NDR

### 3.1. Cas d’usage typiques

- Détection de beaconing vers un C2
- Transfert anormal de fichiers (exfiltration)
- Détection de protocole interdit ou tunelling (DNS, ICMP)
- Activité réseau interne anormale (lateral movement, scan)

### 3.2. Méthodes de détection

- **Deep Packet Inspection (DPI)** & analyse des flux (NetFlow, PCAP)
- **Profiling comportemental** par IP/port/service
- **Détection statistique** : volume de données, fréquences inhabituelles
- **Détection SSL/TLS anormale** : JA3/JA3S fingerprinting

---

## 4. 🔄 Corrélation EDR & NDR

| Exemple d’attaque              | Indicateur EDR                    | Indicateur NDR                         |
|-------------------------------|-----------------------------------|----------------------------------------|
| Emotet                        | Création de fichiers DLL suspect | Connexion C2 par HTTP sur port 8080   |
| Lateral movement via SMB      | Exécution de `psexec`            | Augmentation soudaine du trafic SMB   |
| Data exfiltration             | Zippage de gros volumes de données | Transfert DNS > seuil normal         |

- Intégration dans SIEM ou XDR pour **corrélation inter-capteurs**
- Enrichissement mutuel : une alerte NDR alimente une chasse sur EDR

---

## 5. ⚙️ Bonnes pratiques

- Déployer EDR sur tous les endpoints critiques (serveurs, postes VIP)
- Activer TLS inspection ou JA3 fingerprinting côté NDR
- Maintenir des règles de détection MITRE alignées sur les tactiques/techniques
- Évaluer la **couverture ATT&CK** pour EDR et NDR
- Automatiser la réponse (containment EDR, alerte réseau)

---

## 6. 📚 Références

- [MITRE ATT&CK for Enterprise](https://attack.mitre.org/)
- [NIST 800-94: Guide to IDS/IPS](https://csrc.nist.gov/publications/detail/sp/800-94/final)
- [SANS: EDR vs NDR - Better Together](https://www.sans.org/)
- [Elastic EDR Detection Rules](https://github.com/elastic/detection-rules)

---

## ✅ Résumé

L’approche combinée EDR + NDR permet :

- Une **détection multi-couche** : endpoint & réseau
- Une meilleure **visibilité latérale et externe**
- Une **réduction du temps de réponse (MTTR)** grâce à la complémentarité
