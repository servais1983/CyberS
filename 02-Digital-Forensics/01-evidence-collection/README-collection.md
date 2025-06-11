# 🗂️ Collection - Acquisition d'Artefacts Forensiques

<div align="center">

![Collection](https://img.shields.io/badge/Phase-Collection-blue?style=for-the-badge)
![Tools](https://img.shields.io/badge/Tools-12+-green?style=for-the-badge)

*Outils et techniques pour l'acquisition sécurisée d'artefacts forensiques*

</div>

---

## 📋 Contenu du Dossier

### 🔴 **Live Forensics**
- **KAPE** - Kroll Artifact Parser & Extractor
- **Velociraptor** - Endpoint visibility platform
- **GRR** - Google Rapid Response
- **CyLR** - Live Response Collection

### 💾 **Disk Imaging**
- **FTK Imager** - AccessData imaging tool
- **DD/DC3DD** - Linux disk cloning
- **Guymager** - Linux GUI imager
- **MSAB XRY** - Mobile forensics

### 🧠 **Memory Capture**
- **WinPmem** - Windows memory acquisition
- **LiME** - Linux Memory Extractor
- **OSForensics** - Memory imaging
- **Belkasoft RAM Capturer** - Live memory

### 🌐 **Network Capture**
- **Wireshark** - Network protocol analyzer
- **TCPDump** - Command-line packet analyzer
- **NetworkMiner** - Network forensic analysis
- **Netresec** - Network security monitoring

---

## 🎯 Principes de Collection

### ⚖️ **Ordre de Volatilité**
```
1. CPU registers, cache          # Plus volatil
2. RAM, swap space
3. Network connections
4. Running processes
5. File system
6. Logs, archives               # Moins volatil
```

### 🔒 **Chain of Custody**
- **Documentation** complète
- **Hachage** des preuves
- **Signatures** d'acquisition
- **Stockage** sécurisé

---

## 🚀 KAPE - Guide Complet

### 📥 **Installation**
```bash
# Télécharger KAPE depuis
# https://www.kroll.com/en/services/cyber-risk/investigate-and-respond/kroll-artifact-parser-extractor-kape

# Structure KAPE
KAPE/
├── kape.exe           # Executable principal
├── Targets/          # Définitions de collecte
├── Modules/          # Parsers d'analyse
└── Documentation/    # Guides et aide
```

### 🎯 **Targets Essentiels**
| Target | Description | Usage |
|--------|-------------|-------|
| !BasicCollection | Collection de base | Triage rapide |
| !SANS_Triage | Collection SANS | Investigation complète |
| !Malware | Artefacts malware | Analyse malware |
| !WebBrowsers | Navigateurs | Activité web |
| !FileExploration | Exploration fichiers | Activité utilisateur |

### ⚡ **Commandes KAPE**
```bash
# Collection basique
kape.exe --tsource C: --tdest C:\KAPE_Output --target !BasicCollection

# Collection avec parsing
kape.exe --tsource C: --tdest C:\KAPE_Output --target !BasicCollection --mdest C:\KAPE_Parsed --module !EZParser

# Collection spécifique
kape.exe --tsource C: --tdest C:\KAPE_Output --target EventLogs,RegistryHives

# Mode GUI
kape.exe --gui
```

---

## 🧠 Acquisition Mémoire

### 🪟 **Windows - WinPmem**
```bash
# Acquisition mémoire
winpmem.exe memory.raw

# Avec compression
winpmem.exe -c memory.aff4

# Information système
winpmem.exe -i
```

### 🐧 **Linux - LiME**
```bash
# Compilation LiME
make -C /lib/modules/$(uname -r)/build M=$(pwd) modules

# Acquisition
sudo insmod lime.ko "path=memory.dump format=raw"

# Via TCP
sudo insmod lime.ko "path=tcp:4444 format=raw"
```

---

## 💾 Imagerie Disque

### 🖥️ **FTK Imager**
```
1. File > Create Disk Image
2. Select Source (Physical Drive)
3. Choose Image Type (E01, DD, AFF)
4. Set Destination
5. Add Case Information
6. Start Imaging
```

### 🐧 **DD/DC3DD (Linux)**
```bash
# DD classique
sudo dd if=/dev/sda of=disk_image.dd bs=4M status=progress

# DC3DD avec hachage
sudo dc3dd if=/dev/sda of=disk_image.dd hash=sha256 log=acquisition.log

# Avec compression
sudo dd if=/dev/sda bs=4M | gzip > disk_image.dd.gz
```

---

## 🌐 Capture Réseau

### 📡 **Wireshark**
```bash
# Capture interface
wireshark -i eth0

# Capture en ligne de commande
tshark -i eth0 -w capture.pcap

# Avec filtre
tshark -i eth0 -f "host 192.168.1.1" -w filtered.pcap
```

### 🔍 **TCPDump**
```bash
# Capture basique
sudo tcpdump -i eth0 -w capture.pcap

# Avec filtre host
sudo tcpdump -i eth0 host 192.168.1.1 -w host_capture.pcap

# Affichage temps réel
sudo tcpdump -i eth0 -n -X
```

---

## 📋 Checklists de Collection

### ✅ **Pré-Collection**
- [ ] Documentation de la scène
- [ ] Photos de l'équipement
- [ ] Chain of custody initialisé
- [ ] Outils préparés et testés
- [ ] Stockage sécurisé disponible

### ✅ **Durante Collection**
- [ ] Ordre de volatilité respecté
- [ ] Hash des preuves calculé
- [ ] Logs d'acquisition conservés
- [ ] Timestamps documentés
- [ ] Copies de sauvegarde créées

### ✅ **Post-Collection**
- [ ] Intégrité vérifiée
- [ ] Documentation complétée
- [ ] Stockage sécurisé
- [ ] Copies de travail créées
- [ ] Chain of custody mise à jour

---

## 🛠️ Scripts Utiles

### 🐍 **Python - Acquisition Helper**
```python
import hashlib
import datetime

def calculate_hash(file_path):
    """Calculate SHA256 hash of file"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def log_acquisition(source, destination, hash_value):
    """Log acquisition details"""
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"{timestamp} - Source: {source} - Dest: {destination} - Hash: {hash_value}\n"
    
    with open("acquisition.log", "a") as log_file:
        log_file.write(log_entry)
```

---

## 📚 Ressources

- 🎓 **[KAPE Documentation](https://ericzimmerman.github.io/KapeDocs/)** - Guide officiel
- 📖 **[SANS DFIR](https://www.sans.org/posters/windows-forensic-analysis/)** - Windows forensics
- 🔧 **[Volatility Foundation](https://www.volatilityfoundation.org/)** - Memory analysis
- 📋 **[NIST SP 800-86](https://csrc.nist.gov/publications/detail/sp/800-86/final)** - Forensics guidelines

---

<div align="center">

*🔑 La qualité de la collection détermine la qualité de l'analyse !*

</div>