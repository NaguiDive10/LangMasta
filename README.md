## LangMasta
Débloque tes compétences linguistes


# LangMasta - Application d'Apprentissage de Langue avec IA
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

### Description

LangMasta est une application interactive développée avec Streamlit qui aide les utilisateurs à apprendre du vocabulaire à travers un quiz de traduction et un système de synthèse vocale. L'application utilise gTTS (Google Text-to-Speech) pour la prononciation et un fichier CSV pour stocker les mots et leurs traductions.

### Fonctionnalités

📖 Quiz de vocabulaire : Testez vos connaissances en traduisant des mots affichés.

🔊 Synthèse vocale : Écoutez la prononciation des mots dans la langue de votre choix.

🎯 Système de score : Suivez votre progression en temps réel.

🎉 Animations interactives : Ballons à la fin du quiz pour encourager l'apprentissage.

📊 Affichage de la progression : Barre de progression dynamique.

🔄 Option de redémarrage : Recommencez le quiz autant de fois que vous le souhaitez.

### Technologies Utilisées

Python

Streamlit (interface utilisateur interactive)

Pandas (gestion des fichiers CSV)

gTTS (génération de synthèse vocale)


### Prérequis

Avant d'exécuter l'application, assurez-vous d'avoir installé les dépendances suivantes :

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
pip install streamlit pandas gtts
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

### Installation et Exécution

Clonez le dépôt ou copiez les fichiers du projet.

Assurez-vous d'avoir un fichier CSV contenant le vocabulaire avec deux colonnes : Word (mot à traduire) et Translation (traduction correcte).

Exécutez l'application avec la commande suivante :

xxxxxxxxxxxxxxxxxxxxxxxx
streamlit run app.py
xxxxxxxxxxxxxxxxxxxxxxxx


### Utilisation

- Lancez l'application.

- Sélectionnez la langue de synthèse vocale.

- Lisez le mot affiché et entrez sa traduction.

- Cliquez sur Valider pour vérifier votre réponse.

- Utilisez le bouton 🎧 Écouter la prononciation pour entendre le mot.

Progressez dans le quiz et visez le score parfait !


### Améliorations Futures

- Ajout de plusieurs niveaux de difficulté.

- Intégration d'une base de données pour stocker l'historique des scores.

- Extension à d'autres langues et nouveaux types d'exercices.

### Auteur

NaguiDiv - Développeur de LangMasta


### Licence @credit

Ce projet est Open-source.
