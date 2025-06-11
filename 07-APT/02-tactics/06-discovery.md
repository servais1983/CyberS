# 🎯 Tactiques de Découverte des APT

<div align="center">
  <img src="../../assets/logos/apt-discovery-logo.png" alt="APT Discovery Logo" width="200"/>
  <br>
  <p><em>Guide complet des tactiques de découverte utilisées par les APT</em></p>
</div>

## 🧠 Présentation

Les tactiques de découverte permettent aux APT de collecter des informations sur l'environnement compromis pour planifier leurs actions futures. Ce guide détaille les méthodes les plus courantes et les contre-mesures associées.

---

## 🔍 Tactiques Principales

### Découverte Système
| Méthode | Description | Fréquence |
|---------|-------------|-----------|
| **System Information** | Informations système | ⭐⭐⭐⭐⭐ |
| **Process Discovery** | Découverte des processus | ⭐⭐⭐⭐⭐ |
| **Service Discovery** | Découverte des services | ⭐⭐⭐⭐⭐ |
| **Software Discovery** | Découverte des logiciels | ⭐⭐⭐⭐ |

### Découverte Réseau
| Méthode | Description | Impact |
|---------|-------------|--------|
| **Network Scanning** | Scan réseau | ⭐⭐⭐⭐⭐ |
| **Remote System Discovery** | Découverte des systèmes distants | ⭐⭐⭐⭐⭐ |
| **Domain Trust Discovery** | Découverte des relations de confiance | ⭐⭐⭐⭐⭐ |
| **Network Share Discovery** | Découverte des partages | ⭐⭐⭐⭐ |

---

## 🛠️ Outils et Techniques

### Outils de Découverte
- **PowerShell**
- **Net Commands**
- **WMI**
- **Custom Scripts**

### Techniques Avancées
- **Active Directory Enumeration**
- **Network Mapping**
- **Service Enumeration**
- **Vulnerability Scanning**

---

## 📊 Indicateurs de Compromission

### Signes de Découverte Système
- ✅ Commandes système suspectes
- ✅ Énumération des processus
- ✅ Énumération des services
- ✅ Scan de logiciels

### Signes de Découverte Réseau
- ✅ Scan réseau
- ✅ Énumération AD
- ✅ Découverte de partages
- ✅ Énumération de confiance

---

## 🎯 Contre-Mesures

### Protection Système
- Monitoring des commandes
- Contrôle d'accès
- Journalisation
- Détection d'anomalies

### Protection Réseau
- Segmentation réseau
- Monitoring des scans
- Contrôle des accès
- Détection des énumérations

---

## 📈 Détection

### Surveillance
- Analyse des logs
- Détection d'anomalies
- Monitoring des commandes
- Analyse comportementale

### Réponse
- Investigation
- Remédiation
- Documentation
- Mise à jour des contrôles

---

## 🛡️ Recommandations

### Prévention
- ✅ Contrôle d'accès strict
- ✅ Monitoring continu
- ✅ Politiques de sécurité
- ✅ Tests de sécurité

### Réponse
- ✅ Plan d'incident
- ✅ Équipe de réponse
- ✅ Outils de détection
- ✅ Procédures de récupération

---

## 📚 Références

- [MITRE ATT&CK - Discovery](https://attack.mitre.org/tactics/TA0007/)
- [CIS Controls](https://www.cisecurity.org/controls/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [Microsoft Security Blog](https://www.microsoft.com/security/blog/)

---

> ⚠️ Ce document est fourni à des fins d'information et de sensibilisation. La mise en œuvre des mesures de sécurité doit être adaptée à votre environnement spécifique.

## 📅 Mise à Jour
- Dernière mise à jour : [Date]
- Version : 1.0
- Statut : Actif 