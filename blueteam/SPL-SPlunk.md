# SPLUNK SPL COMMANDS - BLUE TEAM & FIDR (V2 AMELIOREE)

## Sommaire

1. [Commandes de base](#commandes-de-base)
2. [Recherches temporelles](#recherches-temporelles)
3. [Filtres et conditions](#filtres-et-conditions)
4. [Statistiques et agregations](#statistiques-et-agregations)
5. [Visualisation](#visualisation)
6. [Requetes investigation](#requetes-investigation)
7. [Recherches sur les logs Windows](#recherches-sur-les-logs-windows)
8. [Cas d'usage FIDR](#cas-dusage-fidr)
9. [Detection MITRE ATTCK](#detection-mitre-attck)
10. [Dashboards recommandes](#dashboards-recommandes)
11. [Templates de Dashboards Splunk](#templates-de-dashboards-splunk)

...

## Templates de Dashboards Splunk

### 🎯 Dashboard : Surveillances Authentification (Windows Logon)

* **Panel 1** : `Tentatives echouees`

```spl
index=windows EventCode=4625 | timechart span=1h count by user
```

* **Panel 2** : `Tentatives reussies`

```spl
index=windows EventCode=4624 | timechart span=1h count by user
```

* **Panel 3** : `Type de Logon suspects`

```spl
index=windows EventCode=4624 LogonType!=2 AND LogonType!=10 | stats count by LogonType
```

### 🧠 Dashboard : Activite PowerShell

* **Panel 1** : `Commandes PowerShell encodees`

```spl
index=sysmon EventCode=1 | where like(CommandLine, "%EncodedCommand%") | timechart span=1h count
```

* **Panel 2** : `Scripts Invoke suspects`

```spl
index=sysmon EventCode=1 | search CommandLine="*Invoke*" | stats count by CommandLine
```

### 🌍 Dashboard : Activite reseau externe

* **Panel 1** : `Connexions sortantes par destination`

```spl
index=firewall OR index=sysmon EventCode=3 | stats count by dest_ip
```

* **Panel 2** : `Taux de DNS long ou anormal`

```spl
index=dns_logs | eval qlen=len(query) | where qlen > 50 | timechart span=1h count
```

### 🛡️ Dashboard : Securite des Comptes

* **Panel 1** : `Creation de comptes`

```spl
index=windows EventCode=4720 | timechart span=1h count by user
```

* **Panel 2** : `Ajout aux groupes admin`

```spl
index=windows EventCode=4728 OR EventCode=4732 | stats count by user, GroupName
```

### 📦 Dashboard : Exfiltration/DLP

* **Panel 1** : `Telechargements de gros fichiers compresses`

```spl
index=proxy_logs uri="*.zip" OR uri="*.rar" OR uri="*.7z" | stats count by src_ip, uri
```

* **Panel 2** : `Transferts DNS suspects`

```spl
index=dns_logs | where like(query, "%_%") OR len(query)>50 | timechart span=30m count by query
```

---
