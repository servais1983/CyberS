# 💽 Disk Analysis

## 📋 Overview

Disk analysis involves examining storage devices to recover data, analyze file systems, and reconstruct user activities. This is often the most comprehensive part of digital forensics.

## 🗄️ File System Analysis

### Supported File Systems
- **NTFS** - Windows file system
- **FAT32/exFAT** - Portable device file systems
- **HFS+/APFS** - macOS file systems
- **ext2/ext3/ext4** - Linux file systems
- **UFS** - Unix file systems

### Key Artifacts
- **File allocation tables** - File location mapping
- **Directory entries** - File and folder structure
- **Metadata** - File timestamps and attributes
- **Journal entries** - File system transactions

## 🕰️ Timestamp Analysis

### NTFS Timestamps
- **Created** - File creation time
- **Modified** - Last write time
- **Accessed** - Last access time
- **MFT Modified** - Master File Table change

### Timestamp Interpretation
- **User activity** - File interaction patterns
- **System events** - Automated processes
- **Timeline reconstruction** - Event sequencing
- **Anti-forensics detection** - Timestamp manipulation

## 🗑️ Deleted File Recovery

### Recovery Techniques
- **Unallocated space** - Scanning free disk space
- **File carving** - Signature-based recovery
- **Journal analysis** - Transaction log examination
- **Shadow copies** - System restore points

### Carving Methods
- **Header/footer** - File signature identification
- **Entropy analysis** - Data pattern recognition
- **Cluster analysis** - Disk allocation patterns
- **Fragment reconstruction** - Partial file assembly

## 🗂️ Registry Analysis (Windows)

### Registry Hives
- **SYSTEM** - System configuration
- **SOFTWARE** - Installed applications
- **SECURITY** - Security policies
- **SAM** - User account database
- **NTUSER.DAT** - User-specific settings

### Key Forensic Locations
- **Run keys** - Program autostart
- **MRU lists** - Most recently used items
- **USB history** - Connected devices
- **Network information** - WiFi and network configs

## 🔍 Artifact Analysis

### Browser Artifacts
- **History** - Visited websites
- **Cache** - Temporary files
- **Cookies** - Session data
- **Downloads** - File download history
- **Bookmarks** - Saved websites

### Application Artifacts
- **Recent documents** - File access history
- **Temporary files** - Application cache
- **Configuration files** - User preferences
- **Log files** - Application events

## 🗺️ Location Data

### GPS and Location Services
- **EXIF data** - Photo location information
- **Location history** - Movement tracking
- **WiFi networks** - Connection history
- **Cell tower data** - Mobile location tracking

### Mapping and Navigation
- **Route history** - Navigation patterns
- **Search history** - Location searches
- **Cached maps** - Downloaded map data
- **POI data** - Points of interest

## 🔒 Encryption and Security

### Encrypted Storage
- **BitLocker** - Windows disk encryption
- **FileVault** - macOS disk encryption
- **LUKS** - Linux disk encryption
- **TrueCrypt/VeraCrypt** - Third-party encryption

### Recovery Strategies
- **Key escrow** - Backup encryption keys
- **Memory analysis** - In-memory key recovery
- **Brute force** - Password cracking
- **Dictionary attacks** - Common password lists

## 🛠️ Analysis Tools

### Commercial Tools
- **EnCase** - Comprehensive forensic suite
- **FTK** - Forensic Toolkit
- **X-Ways Forensics** - Advanced disk editor
- **Magnet AXIOM** - Digital investigation platform

### Open Source Tools
- **Autopsy** - Digital forensics platform
- **The Sleuth Kit** - Command-line tools
- **PhotoRec** - File carving utility
- **TestDisk** - Data recovery software

## 📈 Analysis Workflow

### 1. **Image Verification**
- Hash comparison
- Image integrity check
- Write protection validation

### 2. **File System Examination**
- Partition analysis
- File system identification
- Structure validation

### 3. **Artifact Extraction**
- Automated parsing
- Manual examination
- Custom scripts

### 4. **Timeline Creation**
- Event correlation
- Activity reconstruction
- Pattern identification

### 5. **Reporting**
- Findings summary
- Evidence documentation
- Expert opinions

---

*Disk analysis requires systematic methodology and attention to detail*
