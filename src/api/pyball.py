import j2l.pytactx.agent as pytactx

class IPyFootballer:
    def __init__(self) -> None:
        ...
    def update(self) -> None :
        """
        Fetch the last values of robot sensors from server
        And send buffered requests in one shot to limit bandwidth.
        To be call in the main loop at least every 10 msecs.
        """
        ...
    def move(self,dx:int,dy:int) -> None:
        """
        Request a relative moves on the grid around the previous agent position 
        according to the specified dx, dy values.
        The request will be send the next update() call
        """
        ...
    def shoot(self, targetX:int, targetY:int, magnitude:float):
        """
        The purpose of this function is to shoot a ball at a position x,y 
        and with a specified magnitude. 
        According to the games rules, random factors may be applied to the ball trajectory
        """
        ...
    def getBallOwner (self) -> str:
        """
        To have the name of the ball owner
        """
        ...
    
    def getBallPosition (self) -> tuple[int,int]:
        ...
    def getPlayerPostition (self) -> tuple[int,int]:
        ...
 
class PytactXFootballer (IPyFootballer):
    def __init__(self, playerId:str, arena:str, server:str, port:int, username:str, password:str) -> None:
        self.__agent=pytactx.Agent(playerId, arena, username, password, server, port)
        ...

    def update(self) -> None :
        self.__agent.update()
    def move(self,dx:int,dy:int) -> None:
        self.__agent.move(dx,dy)
    def shoot(self, targetX:int, targetY:int, magnitude:float):

        ...
    def getBallOwner (self) -> str:
        return ""
  
    def getBallPosition (self) -> tuple[int,int]:
        return (self.__agent.x, self.__agent.y) #todo
    
    def getPlayerPostition (self) -> tuple[int,int]:
        return (self.__agent.x, self.__agent.y)
        
