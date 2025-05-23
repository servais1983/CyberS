
# SPLUNK SPL COMMANDS - BLUE TEAM & FIDR (V2 AMELIOREE)

## Sommaire
1. [Commandes de base](#commandes-de-base)
2. [Recherches temporelles](#recherches-temporelles)
3. [Filtres et conditions](#filtres-et-conditions)
4. [Statistiques et agregations](#statistiques-et-agregations)
5. [Visualisation](#visualisation)
6. [Requetes investigation](#requetes-investigation)
7. [Recherches sur les logs windows](#recherches-sur-les-logs-windows)
8. [Cas dusage fidr](#cas-dusage-fidr)
9. [Detection mitre attck](#detection-mitre-attck)
10. [Dashboards recommandes](#dashboards-recommandes)
11. [Templates de dashboards splunk](#templates-de-dashboards-splunk)

## Commandes de base
```spl
index=<nom_index>
sourcetype=<nom_sourcetype>
source=<chemin_source>
host=<nom_hote>
```

## Recherches temporelles
```spl
index=win_logs earliest=-24h latest=now
index=firewall earliest=-7d@d latest=@d
```
```spl
timechart span=1h count by host
```

## Filtres et conditions
```spl
index=firewall action=blocked
index=windows (EventCode=4625 OR EventCode=4624)
index=sysmon (EventCode=1 OR EventCode=3) AND Image="cmd.exe"
| rename source_ip as src_ip dest_ip as dst_ip
```

## Statistiques et agregations
```spl
stats count by src_ip
stats dc(user) by src_ip
stats avg(response_time) by uri_path
```

## Visualisation
```spl
timechart span=1h count by EventCode
chart count over dest_ip by action
```

## Requetes investigation
```spl
index=windows EventCode=4624 LogonType=10 | stats count by user, src_ip
index=windows EventCode=4625 | stats count by user, src_ip | where count > 10
index=sysmon EventCode=1 | where match(Image, "(?i)\\powershell.exe") AND like(CommandLine, "%Invoke%")
index=dns_logs | stats count by query | where like(query, "%_%") OR len(query) > 50
index=fs_logs path="*confidential*" | stats count by user, file | where count > 5
```

## Recherches sur les logs windows
```spl
index=windows EventCode=4720
index=windows EventCode=4726
index=windows EventCode=4728 OR EventCode=4732
index=windows EventCode=1102
```

## Cas dusage fidr
```spl
index=proxy_logs uri="*.zip" OR uri="*.rar" OR uri="*.7z" | stats count by src_ip, uri
index=sysmon EventCode=3 DestinationPort=445 | stats count by src_ip, dest_ip
index=sysmon EventCode=1 | where like(CommandLine, "%EncodedCommand%")
index=windows EventCode=4698 | stats count by TaskName, user
index=proxy_logs | timechart span=1m count by src_ip | streamstats avg(count) as avg | where count == avg
```

## Detection mitre attck
```spl
# T1059 - Execution de commande
index=sysmon EventCode=1 | where match(Image, ".*cmd.exe|powershell.exe|wmic.exe")

# T1078 - Compte Compromis
index=windows EventCode=4624 | stats dc(src_ip) by user | where 'dc(src_ip)' > 5

# T1566 - Phishing (fichiers joints)
index=email_logs attachment="*.doc" OR attachment="*.xls" OR attachment="*.exe" | stats count by sender, subject

# T1021 - Remote Services (RDP/WinRM)
index=windows EventCode=4624 LogonType IN (10, 3) | stats count by user, src_ip
```

## Dashboards recommandes
- Tentatives de connexion (4624/4625)
- Utilisation de PowerShell encodé
- Flux réseau anormal ou suspect
- Créations de comptes ou changements dans les groupes
- Téléchargement de fichiers compressés

## Templates de dashboards splunk

### 🎯 Dashboard : Surveillances authentification (windows logon)
```spl
index=windows EventCode=4625 | timechart span=1h count by user
index=windows EventCode=4624 | timechart span=1h count by user
index=windows EventCode=4624 LogonType!=2 AND LogonType!=10 | stats count by LogonType
```

### 🧠 Dashboard : Activite powershell
```spl
index=sysmon EventCode=1 | where like(CommandLine, "%EncodedCommand%") | timechart span=1h count
index=sysmon EventCode=1 | search CommandLine="*Invoke*" | stats count by CommandLine
```

### 🌍 Dashboard : Activite reseau externe
```spl
index=firewall OR index=sysmon EventCode=3 | stats count by dest_ip
index=dns_logs | eval qlen=len(query) | where qlen > 50 | timechart span=1h count
```

### 🛡️ Dashboard : Securite des comptes
```spl
index=windows EventCode=4720 | timechart span=1h count by user
index=windows EventCode=4728 OR EventCode=4732 | stats count by user, GroupName
```

### 📦 Dashboard : Exfiltration/dlp
```spl
index=proxy_logs uri="*.zip" OR uri="*.rar" OR uri="*.7z" | stats count by src_ip, uri
index=dns_logs | where like(query, "%_%") OR len(query)>50 | timechart span=30m count by query
```

---
