# 🎯 Tactiques de Persistance des APT

<div align="center">
  <img src="../../assets/logos/apt-persistence-logo.png" alt="APT Persistence Logo" width="200"/>
  <br>
  <p><em>Guide complet des tactiques de persistance utilisées par les APT</em></p>
</div>

## 🧠 Présentation

Les tactiques de persistance permettent aux APT de maintenir leur accès à long terme dans une infrastructure compromise. Ce guide détaille les méthodes les plus courantes et les contre-mesures associées.

---

## 🔍 Tactiques Principales

### Méthodes de Persistance Système
| Méthode | Description | Fréquence |
|---------|-------------|-----------|
| **Registry Run Keys** | Clés de démarrage | ⭐⭐⭐⭐⭐ |
| **Scheduled Tasks** | Tâches planifiées | ⭐⭐⭐⭐⭐ |
| **Services** | Services Windows | ⭐⭐⭐⭐⭐ |
| **WMI** | Windows Management Instrumentation | ⭐⭐⭐⭐ |

### Méthodes de Persistance Application
| Méthode | Description | Impact |
|---------|-------------|--------|
| **Browser Extensions** | Extensions malveillantes | ⭐⭐⭐⭐ |
| **Office Macros** | Macros persistantes | ⭐⭐⭐⭐⭐ |
| **Startup Items** | Éléments de démarrage | ⭐⭐⭐⭐ |
| **COM Objects** | Objets COM malveillants | ⭐⭐⭐⭐ |

---

## 🛠️ Outils et Techniques

### Outils de Persistance
- **PowerSploit**
- **Empire**
- **Cobalt Strike**
- **Metasploit**

### Techniques Avancées
- **Rootkits**
- **Bootkits**
- **Firmware Malware**
- **Custom Backdoors**

---

## 📊 Indicateurs de Compromission

### Signes de Persistance Système
- ✅ Modifications du registre
- ✅ Tâches planifiées suspectes
- ✅ Services inconnus
- ✅ Processus persistants

### Signes de Persistance Application
- ✅ Extensions suspectes
- ✅ Macros inhabituelles
- ✅ Fichiers de démarrage
- ✅ Objets COM modifiés

---

## 🎯 Contre-Mesures

### Protection Système
- Monitoring du registre
- Gestion des services
- Contrôle des tâches
- Analyse WMI

### Protection Application
- Contrôle des extensions
- Gestion des macros
- Surveillance des démarrages
- Audit des objets COM

---

## 📈 Détection

### Surveillance
- Analyse des logs
- Détection d'anomalies
- Monitoring des modifications
- Analyse comportementale

### Réponse
- Suppression des persistance
- Investigation
- Remédiation
- Documentation

---

## 🛡️ Recommandations

### Prévention
- ✅ Politiques de sécurité
- ✅ Contrôle d'accès
- ✅ Monitoring continu
- ✅ Tests de sécurité

### Réponse
- ✅ Plan d'incident
- ✅ Équipe de réponse
- ✅ Outils de détection
- ✅ Procédures de récupération

---

## 📚 Références

- [MITRE ATT&CK - Persistence](https://attack.mitre.org/tactics/TA0003/)
- [CIS Controls](https://www.cisecurity.org/controls/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [Microsoft Security Blog](https://www.microsoft.com/security/blog/)

---

> ⚠️ Ce document est fourni à des fins d'information et de sensibilisation. La mise en œuvre des mesures de sécurité doit être adaptée à votre environnement spécifique.

## 📅 Mise à Jour
- Dernière mise à jour : [Date]
- Version : 1.0
- Statut : Actif 