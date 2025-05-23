
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
12. [Alertes splunk](#alertes-splunk)
13. [Matrice mitre complete](#matrice-mitre-complete)
14. [Export xml dashboards](#export-xml-dashboards)
15. [Playbooks SOAR (exemples)](#playbooks-soar-exemples)
16. [Bonnes pratiques blue team](#bonnes-pratiques-blue-team)

...

## Alertes splunk

### 🔔 Alerte : Commandes interactives suspectes
```spl
index=sysmon EventCode=1 | search CommandLine="*cmd.exe*" OR CommandLine="*powershell*"
```
Déclenchement : à la détection
Action : Envoi webhook vers SOAR ou Slack + log

## Matrice mitre complete

| Technique ID | Nom Tactique             | SPL détection                                                  |
|--------------|--------------------------|-----------------------------------------------------------------|
| T1059        | Command-line Interface   | `index=sysmon EventCode=1 Image=*cmd.exe* OR *powershell.exe*` |
| T1078        | Valid Accounts           | `index=windows EventCode=4624 | stats dc(src_ip) by user`       |
| T1566.001    | Spearphishing Attachment | `index=email_logs attachment="*.doc"`                           |
| T1021.001    | Remote Desktop Protocol  | `index=windows EventCode=4624 LogonType=10`                     |
| T1105        | Ingress Tool Transfer    | `index=proxy_logs uri="*.exe"`                                 |
| T1086        | PowerShell               | `index=sysmon EventCode=1 Image=*powershell.exe*`               |
| T1055        | Process Injection        | `index=sysmon EventCode=8`                                      |
| T1112        | Registry Permissions     | `index=sysmon EventCode=13`                                     |

## Export xml dashboards

### 🧾 Exemple XML Dashboard bruteforce
```xml
<dashboard>
  <label>Bruteforce Detection</label>
  <row>
    <panel>
      <title>Failed Logins by User</title>
      <chart>
        <searchString>index=windows EventCode=4625 | timechart span=1h count by user</searchString>
        <earliest>-24h</earliest>
        <latest>now</latest>
      </chart>
    </panel>
  </row>
</dashboard>
```

## Playbooks SOAR (exemples)

### 📘 Playbook : Brute Force AD
1. Détection alerte (4625 > 10)
2. Enrichir IP via VirusTotal
3. Bloquer via firewall (API)
4. Notifier analyste Slack

### 🧩 Playbook : Exfiltration suspecte
1. Requête proxy `*.zip/*.rar`
2. Requête DNS avec `len(query)>50`
3. Vérifier géo IP avec AbuseIPDB
4. Générer PDF rapport dans ticketing

### 📕 Playbook : Création de compte inattendue
1. Détection 4720 + contexte horaire
2. Vérifier groupe avec 4732
3. Ajouter marqueur sur compte (SIEM tag)
4. Journaliser dans base incidents

## Bonnes pratiques blue team

- Normaliser les noms de champs avec `| rename` pour requêtes génériques
- Prioriser les alertes avec `risk_score` ou `notable` tags
- Sauvegarder les dashboards/export XML dans un dépôt Git privé
- Ajouter `eventtypes` pour catégoriser les recherches récurrentes
- Utiliser `lookup` pour enrichir avec IP/Users externes (CTI, HR)
- Automatiser les tests de requêtes avec des macros programmées

---
