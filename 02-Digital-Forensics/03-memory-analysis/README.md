# 🧠 Memory Analysis

## 📋 Overview

Memory forensics involves analyzing RAM dumps to understand system state, detect malware, and investigate security incidents. Memory contains volatile data not available in disk analysis.

## 🔍 Why Memory Analysis?

### Volatile Evidence
- **Running processes** - Active malware and applications
- **Network connections** - Live communication channels
- **Encryption keys** - In-memory cryptographic material
- **Passwords** - Cached authentication data
- **Registry data** - Current system configuration
- **Command history** - Recent user commands

### Investigation Scenarios
- **Malware analysis** - Unknown or suspicious processes
- **Incident response** - Live system compromise
- **Password recovery** - Cached credentials
- **Network forensics** - Active connections
- **Rootkit detection** - Hidden processes and modules

## 🧑‍💻 Volatility Framework

### Core Concepts
- **Profiles** - OS-specific memory structures
- **Plugins** - Analysis modules
- **Address spaces** - Memory layout understanding
- **Objects** - Kernel data structures

### Essential Plugins
- **pslist** - List running processes
- **pstree** - Process hierarchy
- **psxview** - Cross-view process validation
- **netscan** - Network connections
- **malfind** - Malware indicators
- **handles** - Open handles
- **cmdline** - Process command lines
- **filescan** - Open files

## 🔍 Process Analysis

### Process Investigation
```bash
# Basic process listing
volatility -f memory.img --profile=Win7SP1x64 pslist

# Process tree view
volatility -f memory.img --profile=Win7SP1x64 pstree

# Process command lines
volatility -f memory.img --profile=Win7SP1x64 cmdline

# Process memory dump
volatility -f memory.img --profile=Win7SP1x64 procdump -p 1234 -D output/
```

### Suspicious Process Indicators
- **Unusual locations** - Processes in temp directories
- **Misspelled names** - svchost.exe vs svch0st.exe
- **Missing parent processes** - Orphaned processes
- **Unusual network activity** - Unexpected connections
- **Code injection** - Modified process memory

## 🌐 Network Analysis

### Connection Analysis
```bash
# Network connections
volatility -f memory.img --profile=Win7SP1x64 netscan

# Connection details
volatility -f memory.img --profile=Win7SP1x64 connections

# Socket information
volatility -f memory.img --profile=Win7SP1x64 sockets
```

### Network Artifacts
- **TCP connections** - Active network communications
- **UDP sockets** - Datagram communications
- **Raw sockets** - Low-level network access
- **Connection states** - ESTABLISHED, LISTEN, etc.
- **Process associations** - Which process owns connections

## 🦠 Malware Detection

### Malware Indicators
```bash
# Suspicious process characteristics
volatility -f memory.img --profile=Win7SP1x64 malfind

# Hidden/terminated processes
volatility -f memory.img --profile=Win7SP1x64 psxview

# Injected code
volatility -f memory.img --profile=Win7SP1x64 hollowfind

# API hooks
volatility -f memory.img --profile=Win7SP1x64 apihooks
```

### Advanced Techniques
- **YARA scanning** - Pattern matching
- **String analysis** - Suspicious strings
- **Import reconstruction** - API analysis
- **Shellcode detection** - Code injection

## 🔑 Credential Recovery

### Password Extraction
```bash
# LSA secrets
volatility -f memory.img --profile=Win7SP1x64 lsadump

# Cached credentials
volatility -f memory.img --profile=Win7SP1x64 cachedump

# Hash extraction
volatility -f memory.img --profile=Win7SP1x64 hashdump

# Mimikatz artifacts
volatility -f memory.img --profile=Win7SP1x64 mimikatz
```

### Key Recovery
- **Encryption keys** - BitLocker, TrueCrypt keys
- **SSH keys** - Private key material
- **SSL/TLS keys** - Communication keys
- **Application keys** - Software-specific keys

## 🗂️ Registry Analysis

### Registry in Memory
```bash
# Registry hives
volatility -f memory.img --profile=Win7SP1x64 hivelist

# Print registry key
volatility -f memory.img --profile=Win7SP1x64 printkey -K "Software\Microsoft\Windows\CurrentVersion\Run"

# Dump registry hive
volatility -f memory.img --profile=Win7SP1x64 dumpregistry -D output/
```

### Key Analysis Areas
- **Autostart locations** - Persistence mechanisms
- **USB devices** - Connected hardware
- **Network configurations** - System network settings
- **User activities** - Recent file access

## 🕰️ Timeline Analysis

### Timeline Creation
```bash
# Timeline generation
volatility -f memory.img --profile=Win7SP1x64 timeliner --output=body > timeline.body

# Parse timeline
mactime -d -b timeline.body > timeline.csv
```

### Timeline Benefits
- **Event correlation** - Related activity identification
- **Attack reconstruction** - Incident timeline
- **Evidence validation** - Cross-reference verification
- **Gap analysis** - Missing time periods

## 🔧 Alternative Tools

### Rekall Framework
- **Multi-platform** - Windows, Linux, macOS
- **Live analysis** - Direct memory analysis
- **Extended features** - Advanced analysis capabilities

### MemProcFS
- **Virtual file system** - Memory as file system
- **Real-time analysis** - Live memory examination
- **Plugin architecture** - Extensible functionality

### Other Tools
- **WinDbg** - Windows debugging tools
- **GDB** - GNU debugger for Linux
- **YARA** - Pattern matching engine
- **Bulk Extractor** - Feature extraction

## 📈 Analysis Workflow

### 1. **Memory Acquisition**
- Capture memory image
- Verify image integrity
- Identify OS profile

### 2. **Initial Analysis**
- Process listing
- Network connections
- System information

### 3. **Focused Investigation**
- Suspicious process analysis
- Malware detection
- Credential recovery

### 4. **Advanced Analysis**
- Code injection detection
- Rootkit analysis
- Custom plugin development

### 5. **Documentation**
- Analysis findings
- IOC extraction
- Report generation

---

*Memory analysis provides unique insights into system compromise and malware activity*
