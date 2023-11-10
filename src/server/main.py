import copy
import time
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


stadiumWidth= 37
stadiumHeight= 17

def timestampToStr(sec):
   sec = sec % (24 * 3600)
   hour = sec // 3600
   sec %= 3600
   min = sec // 60
   sec %= 60
   return "%02d:%02d:%02d" % (hour, min, sec) 

def resetStadium():
    """1. Initialiser les règles du jeu"""
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

        },
        "ball": {
            "playerId": "",
            "profile": 11,
            "team": 3,
            "x":18, 
            "y": 7,    
        }
    }


    
    # Regle pour gérer la balle profile indice 4 : collision =False (Pouvoir marcher dessus), invincible =True, hitCollision =0dmg, ammoIni =0, spawnArea(balle au milieu equipe 2) 
    colisionBallRule = referee.game["collision"]
    colisionBallRule[11] = False
    referee.ruleArena("collision", colisionBallRule)
    

    invicibleRule = referee.game["invincible"]
    invicibleRule[11] = True
    invicibleRule[0] = True
    referee.ruleArena("invincible", invicibleRule)
    
    hitCollision = referee.game["hitCollision"]
    hitCollision[11] = 0
    hitCollision[0] = 0
    referee.ruleArena("hitCollision", hitCollision)


    ammoIni = referee.game["ammoIni"]
    ammoIni[11] = 100
    referee.ruleArena("ammoIni", ammoIni)

    # Regle pour gérer les joueurs profile indice 0 : invincible =True, hitCollision =0dmg, infiniteAmmo, spawnArea(sur toute la carte), range max 
    

    infiniteAmmo = referee.game["infiniteAmmo"]
    infiniteAmmo[0] = True
    referee.ruleArena("infiniteAmmo", infiniteAmmo)

    rangePlayers = referee.game["range"]
    rangePlayers [0] = 0
    referee.ruleArena("range", rangePlayers)

    referee.ruleArena("gridRows", stadiumHeight)
    referee.ruleArena("gridColumns", stadiumWidth)


    # Regle pour gérer l'affichage de l'arène : gridsColumns, grids Rows
    #2. Initialisition de l'arbitre, des teams et des agents : 

    for agentId, attributes in agents.items():
        for attributeKey, attributeValue, in attributes.items():
            referee.rulePlayer(agentId, attributeKey, attributeValue)
    referee.update()
    #3 Fermer les portes de l'arène 

resetStadium()


players= {}
oldPlayers= {}
scoreEquipeB=0
scoreEquipeR=0
gameOver=False
timeLimit=1*60
gameStartTime=referee.game["t"]
#4 Boucle principale du jeu

while gameOver==False:
    referee.update()
    while "ball" not in referee.range:
        referee.update()
        referee.ruleArena("info", "Initilisation de la balle ⚽️")

    players=copy.deepcopy(referee.range)
    ball=players["ball"] 
    xBall, yBall = ball["x"],ball["y"]
    # 4.2 : Si le temps du jeu est écoulé 
    elapsedTime=(referee.game["t"]-gameStartTime)/1000
    gameOver=elapsedTime>=timeLimit
    referee.ruleArena("info", f" Equipe bleu🔵 {scoreEquipeB} - {scoreEquipeR} 🔴Equipe Rouge  ⏳{timestampToStr(elapsedTime)}")

    
    # 4.2 : Si la balle arrive dans un but d'une équipe
    if 0<=xBall<1 and -1<=yBall-stadiumHeight//2<=+1:
        ...
    # Rajoute +1 au score de l'équipe opposée
        print("équipe rouge a marqué un but")
        scoreEquipeB+=1
    # Replacer les joueurs et la balle a leurs états initiaux en prennant un certain temps
        resetStadium()

    if stadiumWidth-1<=xBall<stadiumWidth and -1<=yBall-stadiumHeight//2<=+1:
        ...
        print("équipe bleu a marqué un but")
        scoreEquipeR+=1
        resetStadium()

# Afficher le commentaire selon le score quand le jeu est terminé
if scoreEquipeB>scoreEquipeR:
    referee.ruleArena("info", "🏆 l'équipe Bleu a gagné")
elif scoreEquipeR>scoreEquipeB:
    referee.ruleArena("info", "🏆 l'équipe Rouge a gagné")
else:
    referee.ruleArena("info", "🏆 égalité")
referee.ruleArena("pause", True)
time.sleep(1)
referee.update()



    
        



#4.2 : Joueur a la balle il peut tirer ou bien se deplacer
# Tirer:Appliquer une force d'acceleration sur l'agent ball et mettre a false le sur Ownership de la ball du joueur 
# Se deplacer avec la balle: Mettre a jour la position de l'agent Ball et mettre la position du Owner
#4.2 : Le joueur n'a pas la balle: se deplacer indépandament de la balle, ou bien il peut intercepter la balle
# intercepter la balle: a une distance de une case de la balle et si une condition random est vrai 1/5, transferer le Ownership de la balle au joueur intercepteur


# Le jeu est mis en pause pendant 30 secondes 

