# 🔬 Guide Complet – Outils d’Analyse & Investigation Forensic

## 🎯 Objectif

Fournir une vue structurée des **outils essentiels d’analyse forensique numérique** (poste, réseau, cloud, RAM, disques), pour les équipes de **réponse à incident**, **Blue Team**, **SOC**, ou **DFIR**.

---

## 🧠 1. Qu’est-ce que la Forensique numérique ?

La **forensique numérique** (ou forensic informatique) désigne l’ensemble des techniques utilisées pour **acquérir, préserver, analyser et présenter** des **preuves numériques** après un incident de sécurité ou une infraction.

---

## 💾 2. Outils Forensic Disque & Fichiers

| Outil         | Fonction                             | OS     |
|---------------|--------------------------------------|--------|
| **Autopsy**   | GUI forensique complète (files, timeline, meta) | Windows/Linux |
| **The Sleuth Kit (TSK)** | Analyse de FS, lignes de commande | Linux |
| **FTK Imager**| Création d’images disque, preview    | Windows |
| **Magnet AXIOM** | Suite pro forensique complète     | Windows |
| **dd / dc3dd** | Clonage bas niveau (raw image)      | Linux  |
| **X-Ways Forensics** | Analyse disque et RAM (pro)    | Windows |

---

## 🧠 3. Outils Forensic Mémoire (RAM)

| Outil          | Fonction                                | OS     |
|----------------|-----------------------------------------|--------|
| **Volatility3**| Analyse mémoire (processus, DLL, network) | Linux/Win |
| **Rekall**     | Analyse mémoire rapide & scriptable     | Linux  |
| **DumpIt**     | Capture de mémoire Windows              | Windows |
| **LiME**       | Module Linux pour dump mémoire          | Linux  |
| **Belkasoft RAM Capturer** | Simple et léger pour RAM     | Windows |

---

## 🌐 4. Outils Forensic Réseau

| Outil        | Fonction                             |
|--------------|--------------------------------------|
| **Wireshark**| Capture et analyse de paquets (PCAP) |
| **NetworkMiner** | Reconstruction de sessions & fichiers |
| **tcpdump**  | Capture CLI des paquets              |
| **Arkime (ex-Moloch)** | Analyse à grande échelle de PCAP |
| **Suricata/Zeek** | IDS/NSM avec logs exploitables en forensic |

---

## 📦 5. Suites Forensiques Complètes

| Nom             | Description                                 |
|------------------|---------------------------------------------|
| **CAINE**        | Distribution Linux forensique bootable     |
| **SANS SIFT**    | Distribution DFIR officielle du SANS       |
| **Kali + Forensics** | Outils forensic préinstallés          |
| **Tsurugi Linux**| Alternative CAINE orientée investigation   |
| **Cyborg Linux** | OS pentest & forensic hybride              |

---

## 📁 6. Analyse des artefacts Windows

| Artefact             | Outil recommandé                       |
|----------------------|----------------------------------------|
| Registre Windows     | Registry Explorer, RECmd               |
| Jump Lists           | JLECmd                                 |
| Prefetch             | PECmd                                  |
| Event logs (EVTX)    | EventLog Explorer, EVTXtract, Chainsaw |
| MFT/USN              | MFTECmd, AnalyzeMFT                    |
| LNK files            | LECmd                                  |
| Timeline complète    | Plaso (log2timeline)                   |

➡️ Pour la suite complète de commande, voir [Eric Zimmerman's tools](https://ericzimmerman.github.io/)

---

## 🧩 7. Analyse artefacts Linux

| Élément                | Outils ou commandes                     |
|------------------------|-----------------------------------------|
| Logs systèmes          | `journalctl`, `/var/log/`, `ausearch`   |
| Users/Shell history    | `.bash_history`, `last`, `who`, `w`     |
| Processus              | `ps aux`, `lsof`, `netstat`, `ss`       |
| Cron/at jobs           | `crontab -l`, `/etc/cron*`              |
| Liste des paquets      | `dpkg -l`, `rpm -qa`                    |
| Forensic scriptable    | `log2timeline`, `timesketch`, `Loki`    |

---

## 🧰 8. Outils spécialisés & complémentaires

| Type                | Outil                        | Fonction                             |
|---------------------|------------------------------|--------------------------------------|
| Antivirus statique  | VirusTotal, HybridAnalysis   | Analyse de fichiers suspects         |
| Timeline            | Plaso, Timesketch             | Reconstitution temporelle            |
| Analyse rapide      | KAPE, Loki                    | Collecte & scan rapide de postes     |
| Hashing & file info | Hashdeep, md5sum/sha256sum    | Intégrité & identification           |
| Analyse de malware  | Cuckoo Sandbox, CAPEv2        | Analyse dynamique                    |

---

## 🔏 9. Gestion des preuves

### 🧪 Bonnes pratiques

- Toujours travailler sur une **copie de l’image disque** (jamais l’original)
- Utiliser **hash MD5/SHA256** avant et après acquisition
- Documenter l’acquisition : heure, outil, hôte, opérateur
- Stocker les preuves dans un stockage chiffré et horodaté

```bash
# Exemple de hash
sha256sum disk.dd

🔐 10. Bonnes pratiques générales
✅ À FAIRE :

Travailler avec un kit USB forensic bootable

Documenter chaque action (chaîne de traçabilité)

Conserver tous les artefacts (même non analysés)

Automatiser la collecte si possible (KAPE, GRR, Velociraptor)

❌ À ÉVITER :

Monter un disque suspect sur le système actif

Écrire sur les preuves

Oublier la synchronisation de l’heure

📚 11. Ressources & formations
🎓 SANS FOR508 – Advanced IR & Threat Hunting

📘 DFIR Training

🔧 Eric Zimmerman's Tools

📖 Digital Forensics Cheat Sheet (DFIR)

📦 Plaso + Timesketch
