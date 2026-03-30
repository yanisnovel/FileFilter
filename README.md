# 📂 FileFilter

**FileFilter** est un script d'automatisation développé en **Python** pour organiser intelligemment les dossiers encombrés (comme le dossier `Téléchargements`). Il trie automatiquement les fichiers dans des sous-dossiers thématiques en fonction de leurs extensions.

---

## ✨ Fonctionnalités

* **Tri Intelligent :** Identifie et classe les fichiers (Images, Documents, Vidéos, Archives, etc.).
* **Gestion Automatique :** Crée les dossiers de destination s'ils n'existent pas encore.
* **Multi-plateforme :** Utilise `os.path` pour garantir la compatibilité entre Windows, macOS et Linux.
* **Sécurité :** Ne traite que les fichiers à la racine du dossier cible pour éviter de modifier des structures de dossiers existantes.

## 🛠️ Technologies & Bibliothèques

* **Langage :** Python 3.x
* **Module `os` :** Navigation dans le système de fichiers et gestion des chemins.
* **Module `shutil` :** Manipulation et déplacement sécurisé des fichiers.

## 🚀 Installation & Utilisation

1. **Cloner le projet**
   ```bash
   git clone [https://github.com/ton-pseudo/FileFilter.git](https://github.com/ton-pseudo/FileFilter.git)
   cd FileFilter
