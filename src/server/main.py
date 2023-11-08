import j2l.pytactx.agent as pytactx
import os
from dotenv import load_dotenv

load_dotenv()

REFEREE= os.getenv("REFEREE")
ARENA= os.getenv("ARENA")
SERVER= os.getenv("SERVER")
PORT= int(os.getenv("PORT"))
USERNAME= os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Création de l'arbitre
referee = pytactx.Agent(REFEREE, ARENA,  USERNAME, PASSWORD, SERVER, PORT)
referee.moveTowards(18, 0)




def resetStadium():
    agents = {
    "DefenseurB": {
        "team":0,
        "x": 7,
        "y": 7,
        "color": (0,0,255)
        },
    "AttaquantB1": {
        "team":0,
        "x": 15,
        "y": 4,
        "color": (0,0,255)
        },
    "AttaquantB2": {
        "team":0,
        "x": 15,
        "y": 10,
        "color": (0,0,255)
        },
    "DefenseurR": {
        "team": 1,
        "x": 28, 
        "y": 7,
        "color": (255,0,0)
    },
    "AttaquantR1": {
        "team": 1,
        "x": 20, 
        "y": 10,
        "color": (255,0,0)
    },
    "AttaquantR2": {
        "team": 1,
        "x": 20, 
        "y": 4,
        "color": (255,0,0)
    }
}

    for agentId, attributes in agents.items():
        for attributeKey, attributeValue, in attributes.items():
            referee.rulePlayer(agentId, attributeKey, attributeValue)
    referee.update()


#1. Initialiser les règles du jeu : Tir 
# Regle pour gérer la balle profile indice 4 : collision =False (Pouvoir marcher dessus), invincible =True, hitCollision =0dmg, ammoIni =0, spawnArea(balle au milieu equipe 2), 
# Regle pour gérer les joueurs profile indice 0 : invincible =True, hitCollision =0dmg, infiniteAmmo, spawnArea(sur toute la carte), range max 
# Regle pour gérer l'affichage de l'arène : gridsColumns, grids Rows

#2. Initialisition de l'arbitre, des teams et des agents : 

#3 Fermer les portes de l'arène 

#4 Boucle principale du jeu
#4.2 : Joueur a la balle il peut tirer ou bien se deplacer
# Tirer:Appliquer une force d'acceleration sur l'agent ball et mettre a false le Ownership de la ball du joueur 
# Se deplacer avec la balle: Mettre a jour la position de l'agent Ball et mettre la position du Owner
#4.2 : Le joueur n'a pas la balle: se deplacer indépandament de la balle, ou bien il peut intercepter la balle
# intercepter la balle: a une distance de une case de la balle et si une condition random est vrai 1/5, transferer le Ownership de la balle au joueur intercepteur

# 4.2 : Si la balle arrive dans un but d'une équipe
    # Rajoute +1 au score de l'équipe opposée
    # Replacer les joueurs et la balle a leurs états initiaux en prennant un certain temps

# 4.2 : Si le temps du jeu est écoulé 
# Le jeu est mis en pause pendant 30 secondes 




