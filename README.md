# 🛡️ Système de Détection de Fraude avec Blockchain

## 📖 Description du Projet

Le projet **« Système de Détection de Fraude avec Blockchain »** est une application complète permettant d'analyser des transactions financières, de détecter automatiquement les comportements suspects, et d'enregistrer les résultats de manière sécurisée et immuable dans une blockchain.

Ce système combine l'analyse de données avec la technologie blockchain pour garantir :
- 🔍 **Détection intelligente** des transactions frauduleuses
- 🔒 **Sécurité** grâce à la blockchain (immuabilité et traçabilité)
- 📊 **Visualisation** via un dashboard interactif
- ⚡ **Performance** avec une interface moderne et rapide

---

## ✨ Fonctionnalités Principales

### 🔍 Détection de Fraude
- Analyse automatique des transactions financières
- Identification des transactions suspectes selon un seuil configurable
- Règles de détection basées sur le montant des transactions (> 1000$)

### ⛓️ Blockchain Sécurisée
- Création de blocs contenant les transactions suspectes
- Hachage cryptographique SHA-256 pour l'intégrité des données
- Vérification de la validité de la chaîne de blocs
- Lien cryptographique entre les blocs (chaînage)

### 📊 Dashboard Interactif
- Interface graphique moderne (CustomTkinter)
- Statistiques en temps réel (total, moyenne, maximum)
- Graphiques et visualisations (histogrammes, camemberts, scatter plots)
- Navigation entre différentes vues (Données, Statistiques, Blockchain)

### 💾 Gestion des Données
- Chargement de données depuis fichier CSV
- Export des résultats (CSV ou Excel)
- Tableau interactif avec toutes les transactions

---

## 🛠️ Technologies Utilisées

| Technologie | Description |
|------------|-------------|
| **Python 3.10+** | Langage de programmation principal |
| **CustomTkinter** | Interface graphique moderne |
| **Pandas** | Manipulation et analyse des données |
| **Matplotlib** | Visualisation et graphiques |
| **Hashlib** | Cryptographie (SHA-256) pour la blockchain |
| **Git & GitHub** | Versionning et collaboration |

---

## 📁 Structure du Projet

```
fraud-blockchain/
│
├── data/
│   └── transactions.csv          # Données des transactions (30 transactions)
│
├── src/
│   ├── data_loader.py            # Module de chargement des données
│   ├── fraud_detector.py         # Module de détection de fraude
│   ├── blockchain.py             # Module blockchain (Block + Blockchain)
│   └── main.py                   # Point d'entrée principal (CLI)
│
├── gui.py                        # Interface graphique simple
├── gui_advanced.py               # Dashboard complet avec graphiques
├── requirements.txt              # Dépendances Python
├── .gitignore                    # Fichiers à ignorer par Git
├── LICENSE                       # Licence MIT
└── README.md                     # Documentation du projet
```

---

## 🚀 Installation et Exécution

### Prérequis
- Python 3.10 ou supérieur
- Git
- pip (gestionnaire de paquets Python)

### Étape 1 : Cloner le dépôt

Ouvrez un terminal et exécutez :
```bash
git clone https://github.com/Amejoud/fraud-blockchain.git
cd fraud-blockchain
```

### Étape 2 : Installer les dépendances

Installez toutes les bibliothèques nécessaires :
```bash
pip install -r requirements.txt
```

Cela installera automatiquement :
- pandas (analyse de données)
- customtkinter (interface graphique)
- matplotlib (graphiques)
- numpy (calculs numériques)

### Étape 3 : Lancer l'application

Choisissez l'interface que vous souhaitez utiliser :

#### Option 1 : Dashboard Avancé (Recommandé) ⭐
```bash
python gui_advanced.py
```
Ouvre une interface complète avec graphiques, statistiques et navigation.

#### Option 2 : Interface Simple
```bash
python gui.py
```
Interface basique avec tableau et boutons.

#### Option 3 : Ligne de Commande
```bash
python src/main.py
```
Exécution rapide sans interface graphique.

---

## 💻 Utilisation du Dashboard

### Étape 1 : Charger les Données
1. Cliquez sur le bouton **« Tableau de Bord »** dans le menu latéral
2. Cliquez sur **« Charger Donnees »**
3. Les 30 transactions seront importées automatiquement
4. Les statistiques s'affichent (Total, Montant, Moyenne, etc.)

### Étape 2 : Détecter les Fraudes
1. Cliquez sur **« Detecter Fraudes »**
2. Le système analyse toutes les transactions
3. Les transactions > 1000$ sont marquées comme **SUSPECTES**
4. Un message affiche le nombre de fraudes détectées

### Étape 3 : Créer la Blockchain
1. Cliquez sur **« Creer Blockchain »**
2. Les transactions suspectes sont enregistrées dans un bloc
3. Un hash SHA-256 est généré
4. La validité de la blockchain est vérifiée

### Étape 4 : Consulter les Statistiques
1. Cliquez sur **« Statistiques »** dans le menu latéral
2. Visualisez les graphiques :
   - Distribution des montants
   - Top 10 des transactions
   - Répartition statistique
   - Transactions vs ID

### Étape 5 : Exporter les Données
1. Cliquez sur **« Exporter »** dans le menu latéral
2. Choisissez l'emplacement
3. Sélectionnez le format (CSV ou Excel)
4. Les données sont sauvegardées

---

## 📊 Résultats Attendus

Après exécution complète du système :

| Métrique | Valeur |
|----------|--------|
| **Total Transactions** | 30 |
| **Montant Total** | $34,605 |
| **Montant Moyen** | $1,153.50 |
| **Transaction Maximale** | $5,000 |
| **Transactions Normales** | 19 |
| **Transactions Suspectes** | 11 |
| **Blocs Créés** | 2 (genesis + 1) |
| **Validation Blockchain** | ✅ VALIDE |

---

## 🔐 Sécurité Blockchain

Le système utilise les mécanismes de sécurité suivants :

- **SHA-256** : Algorithme de hachage cryptographique robuste
- **Chaînage** : Chaque bloc contient le hash du bloc précédent
- **Immuabilité** : Impossible de modifier un bloc sans casser la chaîne
- **Validation** : Vérification automatique de l'intégrité à chaque ajout
- **Timestamp** : Horodatage de chaque bloc pour la traçabilité

---

##  Cas d'Usage

Ce projet peut être utilisé dans plusieurs domaines :

- 🏦 **Secteur bancaire** : Détection de transactions frauduleuses
- 🛒 **E-commerce** : Surveillance des paiements suspects
- 💳 **Cartes de crédit** : Analyse en temps réel des transactions
- 📊 **Audit financier** : Traçabilité complète des opérations
- 🏢 **Entreprises** : Contrôle interne des flux financiers

---

## 📸 Captures d'Écran

### Dashboard Principal
<img width="1370" height="811" alt="image" src="https://github.com/user-attachments/assets/b1477039-3263-41f2-be20-f775e77a9aaf" />

### Statistiques et Graphiques
<img width="1370" height="796" alt="image" src="https://github.com/user-attachments/assets/2837bc62-0696-41e6-b530-645ea5747cfb" />


### Informations Blockchain
<img width="1197" height="480" alt="image" src="https://github.com/user-attachments/assets/4b463bc2-df7b-430d-95f6-64cb5563c184" />


---

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer au projet :

1. **Fork** le projet
2. Créez une branche : `git checkout -b feature/NouvelleFonctionnalite`
3. Committez vos changements : `git commit -m 'Ajout nouvelle fonctionnalité'`
4. Push vers la branche : `git push origin feature/NouvelleFonctionnalite`
5. Ouvrez une **Pull Request**

---

##  Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

La licence MIT permet :
- ✅ Utilisation commerciale
- ✅ Modification
- ✅ Distribution
- ✅ Utilisation privée

---
---


---

## 🎯 Comment utiliser ce README :

### Étape 1 : Ouvrir le fichier
Dans VS Code, ouvrez le fichier `README.md`

### Étape 2 : Tout sélectionner
Appuyez sur **Ctrl + A** pour tout sélectionner

### Étape 3 : Supprimer
Appuyez sur **Suppr** ou **Delete**

### Étape 4 : Coller le nouveau contenu
Copiez le code ci-dessus et collez-le dans le fichier

### Étape 5 : Sauvegarder
Appuyez sur **Ctrl + S**

### Étape 6 : Mettre à jour GitHub
Dans le terminal :
```bash
git add .
git commit -m "Mise a jour complete du README avec guide d'installation"
git push origin main
```

---

