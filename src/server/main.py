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



agents = {
    "agentBlue": {
        "team":0,
        "x": 5,
        "y": 10,
        "led": [0,0,255]
        },
    "agentRed": {
        "team": 1,
        "x": 10, 
        "y": 5,
        "led": [255,0,0]
    }
}

for agentId, attributes in agents.items():
    for attributeKey, attributeValue, in attributes.items():
        referee.rulePlayer(agentId, attributeKey, attributeValue)
referee.update()