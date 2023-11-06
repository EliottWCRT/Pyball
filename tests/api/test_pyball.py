from ...src.api.pyball import PytactXFootballer



import os
from dotenv import load_dotenv

load_dotenv()

ARENA= os.getenv("ARENA")
SERVER= os.getenv("SERVER")
PORT= os.getenv("PORT")
USERNAME= os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


def createAgent(playerId:str) -> PytactXFootballer :
   return PytactXFootballer(playerId, "pyball", 1883, "demo","demo","mqtt.jusdeliens.com")
    


def test_instanciation():
    # Agent test is register as blue team on the server 
    playerBlue = createAgent ("agentBlue")
    x,y = playerBlue.getPlayerPostition()
    assert x >=18
    assert 4<=y<=12

    # Agent test is register as red team on the server 
    playerRed = createAgent ("agentRed")
    x,y = playerRed.getPlayerPostition()
    assert x <=18
    assert 4>=y>=12

def test_move():
    # Agent blue is moving 
    playerBlue = createAgent ("agentBlue")
    x,y = playerBlue.getPlayerPostition()
    playerBlue.move(+1,+1)
    playerBlue.update()
    xafter,yafter = playerBlue.getPlayerPostition()
    assert xafter == x+1
    assert yafter == y+1
    
    # Agent blue is moving 
    playerRed = createAgent ("agentRed")
    x,y = playerRed.getPlayerPostition()
    playerRed.move(-1,+-1)
    playerRed.update()
    xafter,yafter = playerRed.getPlayerPostition()
    assert xafter == x-1
    assert yafter == y-1

def test_getBallOwner():
    playerBlue = createAgent ("agentBlue")
    while playerBlue.getPlayerPostition() !=playerBlue.getBallPosition():
        xPlayer,yPlayer = playerBlue.getPlayerPostition()
        xBall,yBall = playerBlue.getBallPosition()
        playerBlue.move(dx=xBall-xPlayer, 
                        dy=yBall-yPlayer)
        playerBlue.update()
    assert playerBlue.getBallOwner() == "agentBlue"

def test_shoot():
    playerBlue = createAgent ("agentBlue")
    while  playerBlue.getBallOwner() != "agentBlue":
        xPlayer,yPlayer = playerBlue.getPlayerPostition()
        xBall,yBall = playerBlue.getBallPosition()
        playerBlue.move(dx=xBall-xPlayer, 
                        dy=yBall-yPlayer)
        playerBlue.update()
    playerBlue.shoot(xPlayer+3, yPlayer, 0.1)
    playerBlue.update()
    xBall,yBall = playerBlue.getBallPosition()
    xPlayer,yPlayer = playerBlue.getPlayerPostition()
    assert xBall > xPlayer and yBall == yPlayer