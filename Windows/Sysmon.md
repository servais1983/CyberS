# 🛡️ Sysmon (System Monitor)

## 📘 Introduction

**Sysmon** est un utilitaire du kit Sysinternals de Microsoft, conçu pour surveiller et enregistrer en profondeur les activités du système Windows. Il fournit des journaux détaillés des événements système pour aider à la détection des comportements malveillants et l’analyse post-incident.

---

## 🧪 Fonctionnalités principales

| Fonction                     | Description                                          |
| ---------------------------- | ---------------------------------------------------- |
| 👣 Suivi des processus       | Log des créations et fermetures de processus         |
| 🔗 Traçabilité réseau        | Journalisation des connexions réseau sortantes       |
| 🧬 Intégrité des fichiers    | Hachage des fichiers exécutés (MD5, SHA1, SHA256)    |
| 📁 Activité sur les fichiers | Surveillance des accès et modifications              |
| 🔑 Chargement de DLL         | Enregistrement des bibliothèques dynamiques chargées |
| 🕵️ Détection d’anomalies    | Suivi de patterns suspects dans les logs             |

---

## ⚙️ Fonctionnement

Sysmon fonctionne comme un **service système Windows** qui capture des événements et les consigne dans le **journal des événements Windows**, sous :

```
Applications and Services Logs > Microsoft > Windows > Sysmon > Operational
```

Il utilise une **configuration XML** pour déterminer quelles données surveiller et comment les filtrer.

---

## 📝 Événements courants

| ID Événement | Description                      |
| ------------ | -------------------------------- |
| 1            | Création d’un processus          |
| 3            | Connexion réseau                 |
| 6            | Chargement d’une DLL             |
| 7            | Création de fichiers             |
| 10           | Détection d'accès à un processus |
| 11           | Création d’objet de registre     |
| 15           | Création d’un fichier modifié    |

---

## 🧰 Exemple de configuration

Exemple de ligne de commande d’installation :

```bash
sysmon.exe -accepteula -i config.xml
```

Extrait de configuration XML :

```xml
<Sysmon schemaversion="4.50">
  <EventFiltering>
    <ProcessCreate onmatch="include">
      <Image condition="end with">powershell.exe</Image>
    </ProcessCreate>
  </EventFiltering>
</Sysmon>
```

---

## 🔍 Cas d’utilisation

* 🛡️ Détection des attaques par scripts (PowerShell, WMI, etc.)
* 📊 Analyse comportementale d’un malware
* 📁 Traçabilité des accès fichiers sensibles
* 🔍 Corrélation avec des outils comme **SIEM** (Splunk, Elastic, Sentinel)

---

## ✅ Avantages

* 🔎 Très détaillé et précis
* 🧩 Facilement configurable via XML
* 🛠️ Intégrable dans des solutions de détection avancées

## ⚠️ Inconvénients

* 📈 Génère beaucoup de données (journalisation intensive)
* 🧠 Requiert une bonne connaissance pour une configuration efficace

---

## 🚀 Bonnes pratiques

* Utiliser une configuration XML personnalisée adaptée à l’environnement
* Intégrer les logs dans une solution SIEM pour corrélation
* Mettre à jour régulièrement Sysmon et ses règles

---

## 📚 Références

* [Sysmon sur Microsoft Docs](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
* [GitHub - Configurations Sysmon](https://github.com/SwiftOnSecurity/sysmon-config)
* [Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/)

---

> 📝 **Remarque** : Sysmon ne remplace pas un antivirus ou EDR, mais constitue un excellent **complément de surveillance proactive** dans un environnement Windows.
