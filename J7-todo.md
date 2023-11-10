# 💡 A comprendre et savoir expliquer dans une app desktop 
- [x] les données
- [x] les algorithmes
- [x] les machines
- [x] les protocoles réseaux

# ⚔️ Plan d'attaque de la conception du jeu
- [x] Comprendre les interactions entre les end points d'un jeu robotique réseau
- [x] Faire le diagramme de séquence de PytactX
- [x] Comprendre les données échangées entre les end points : dictionnaires, listes en python
- [x] Partir de l'API, définir tous les use cases des utilisateurs joueurs, rédiger le diagramme de séquence pour chaque use case, et choisir interface/méthodes correspondante en Python
- [x] Noyau du serveur pytactX : définir les responsabilités du jeu et les classes évènements et méthodes associées 
- [x] A partir de l'API, définir les données envoyées et reçues par le serveur du jeu et choisir les "routes" du controleur du serveur
- [x] A partir de la maquette, définir les données envoyées par le serveur et à recevoir par la view

# 📂 Arborescence projet Github
- votrejeu
    - doc
        - *.svg
    - src
        - api
            - j2l
            - votrejeu.py   -> *interface API de votre jeu côté client*
            - readme.md     -> *explique au joueur les actions possibles de l'api*
        - server
            - main.py       -> *logique backend implémentant les règles du jeu*
        - gui
            - ...
    - tests
        - api
            - test_votrejeu.py
        - server
            - test_main.py
        - gui
            - ...
    - readme.md             -> *inclus diagramme de conception du dossier doc*

# 💻 Dev de votre API en TDD
1. Définir l'interface de l'API du jeu pour respecter les US de l'utilisateur joueur
    - 1 méthode update() pour actualiser votre classe joueur et synchroniser son état et requêtes avec le server
    - 1 constructeur prennant en paramètre au minimum : playerId, arena, le serveur et son port, username et password
    ⚠️ Méthodes et attributs en anglais, avec la même convention de nommage (en snake case ou camel case) 

2. Créer fichier .env en mettant les credentials de votre arène
    ⚠️ ** RAJOUTER DANS GIT IGNORE CE .env POUR NE PAS COMMIT LES MOTS DE PASSE"
    - install dotenv
    ```bash
    pip install python-dotenv
    ```
    - créer votre fichier à la racine du dossier projet
    ```
    # environment variables defined inside a .env file
    ARENA=votrejeu
    SERVER=mqtt.jusdeliens.com
    PORT=1883
    USERNAME=demo
    PASSWORD=demo
    ```
    - charger votre env dans chaque fichier où vous avez besoin des credentials de l'arène
    ```python
    import os
    from dotenv import load_dotenv
    load_dotenv()
    ARENA = os.getenv('ARENA')
    SERVER = os.getenv('SERVER')
    PORT = os.getenv('PORT')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    ``` 

3. Ecrire les tests de l'interface dans le fichier "test_*" correspondant à chaque fichier * de l'API. 
    Dans ce fichier, 
    - importer pytest et le module à tester au début de chaque fichier de test
        ```
        import os
        import sys
        __workdir__ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        __j2ldir__ = os.path.join(__workdir__, "src", "api")
        sys.path.append(__workdir__)
        sys.path.append(__j2ldir__)

        from src.api.votrejeu import *
        import pytest
        ...
        ```
    - definir une fonction "test_{featureATester}" en listant les assert
        ```
        def test_instanciation():
            player = VotreJeu("agentTest", "")
            assert player.life == 100
        ```

3. Utiliser pytest pour générer une série de test unitaires dans le dossier tests
    - Installer pytest
    ```
    pip install pytest
    ```
    - Executer pytest
    ```
    pytest path/vers/votreFichierDeTest.py -v -s
    ```
4. Implémenter les méthodes de votre classe concrête de votre Jeu en TDD
    - reprendre d'abord les méthodes qui wrappent pytactX
    - implémenter ensuite les features plus originales qui ne sont pas implémentées dans PytactX

4. Commit une fois 1 test passé par feature.
    Mentionner la référence (e.g. "100% pass #10 feature") à la carte feature dans votre kanban
    Sous trello, installer le power-ups "Card Numbers by Reenhanced" pour voir les numéro de chaque carte

5. Pour les plus avancés, intégrer pytest en CI/CD à chaque commit (pre-commit)

# 💻 Dev de votre server

1. A partir du tutoriel tutos.jusdeliens.com  "Créer vos propres règles du jeu"
- Téléchargez le dernier zip pytactx 
- Créer votre main.py dans votre dossier server recopiez le sample de l'arbitre pour comprendre les règles du jeu  

2. Nommer votre arbitre dans votre .env (NE PAS LE COMMIT):
```
@arenaname  
```
**arenaname** à remplacer par le nom de l'arène
ex: @spythoon pour l'arène spythoon

3. Utiliser les méthodes **ruleArena** et **rulePlayer** en bac à sable pour tester le bon fonctionnement des modifications du serveur
    - Redemarrer l'arène
    ```python
    arbiter.ruleArena("reset", True)
    ```
    - Modifier le infinite ammo de tous les joueurs par défaut (profile = 0)
    ```python
    infiniteAmmoRule = arbiter.game["infiniteAmmo"]
    infiniteAmmoRule[0] = True #Modifie uniquement pour le 1er porfile (0)
    arbiter.ruleArena("infiniteAmmo", infiniteAmmoRule)
    arbiter.update()
    ```
    - Créer des joueurs dans différentes équipes à différentes positions sur la carte
    ```python
    agents = {
        "joueur1": {
            "team": 0,
            "x": 5,
            "y": 10
        },
        "joueur2": {
            "team": 1,
            "x": 15,
            "y": 10
        },
        "ball": {
            "playerId": "",
            "profile": 4,
            "x": 15,
            "y": 10
        }
    }
    for agentId, attributes in agents.items():
        for attributeKey, attributeValue in attributes.items():
            arbitre.rulePlayer(agentId, attributeKey, attributeValue)
    arbiter.update()
    ```

4. Développer en CDD la logique de votre server dans votre main.py
```python
#0. Reset de l'arène
#1. Initialiser les règles du jeu : changer graphiques, et logiques, profiles des joueurs ...
#2. Créer les agents avec le bon profile et les bons états
#3. Fermer l'arène pour interdire la venue de nouveaux agents non autorisés
#4. Dans votre boucle principale : tant que le jeu tourne
    #4.1. Récupérer les requêtes et infos des joueurs dans le range de l'arbitre
    #4.2. Si le range change (ex: nFire pour check si un agent à tiré), 
        # 4.3. mettre à jour les règles du jeu (ex: appliquer acceleration sur agent, ou changer état de la map)
    #4.5. Sauvegarder le nouveau range avant de reboucler
    #4.6. Gérer condition de fin de jeu : fin du délai réglementaire, morts des joueurs d'une équipe ...
```

# 🤔 Vos README.md
## A la racine du projet : pour l'administrateur
- **Titre** du jeu
- **Description** courte du jeu
- **🎯 Contexte & cahier des charges** : développé dans le cadre d'une formation, pour un formateur pour monter en compétence en Python ...
- **🎲 Règles** du jeu : maquette, déroulé d'une partie, conditions de victoire
- **🎮 Use cases**: 
    - pour l'administrateur : expliquer ce que peut/doit faire un administrateur qui souhaite lancer/administrer une arène de jeu avec des apprenants 
    - pour le joueur : renvoyer vers README API
- **🖧 Architecture matériel** (optionnel, peut être décrit avec le diagramme de séquence) : schéma overview présentant les machines et protocoles (serveurs, clients, broker) avec texte expliquant le choix des technologies 
- **📞 Diagramme de séquence**: expliquer le déroulé d'une partie, les principales étapes à faire dans l'ordre et qui/quoi/comment, les couches s'échangent quelles données pour qui/pour quoi
- **✅ Pré-requis** 
    - matériel et logiciel requis pour executer votre projet, pour l'administrateur 
    - pour les apprenants rediriger vers README API
- **⚙️ Installation** : step by step (commandes à executer par l'administrateur, paquets à installer ...)
- **🧪 Tests**: 
    - définition du plan de test ce qu'on attend quand on fait quoi 
    - step by step pour lancer les tests
- **🧑‍💻 Auteur**
- **⚖️ License**

## Dans le dossier API : pour les joueurs
- **Titre** du jeu
- **Description** courte du projet
- **🎲 Règles du jeu** : maquette, déroulé d'une partie, conditions de victoire
- **🎮 Use cases**: actions possibles du joueur via l'API
- **✅ Pré-requis** : matériel et logiciel requis pour executer votre projet
- **⚙️ Installation** : step by step (commandes à executer, paquets à installer ...)
- **🧑‍💻 Auteur**
- **⚖️ License**

