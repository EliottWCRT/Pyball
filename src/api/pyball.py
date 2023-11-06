import j2l.pytactx.agent as pytactx

class IPyFootballer:
    def __init__(self) -> None:
        self
    def update(self) -> None :
        """
        Fetch the last values of robot sensors from server
        And send buffered requests in one shot to limit bandwidth.
        To be call in the main loop at least every 10 msecs.
        """


agent.update()
print(agent.game)
while True:
    agent.lookAt((agent.dir+1)%4)
    agent.update()





"""
yEnnemi, xEnnemi = 0,0
class State:
    def __init__(self, agent):
        self.__agent = <agent

    def enter(self):
        pass
    def execute(self):
        pass
    def exit(self):
        pass

class StateMachine:
    def __init__(self, agent):
        self.agent = agent
        self.current_state = None

    def set_state(self, new_state):
        if self.current_state:
            self.current_state.exit()
        self.current_state = new_state
        self.current_state.enter()

    def update(self):
        if self.current_state:
            self.current_state.execute()

class ScanState(State):
    def enter(self):
        pass

    def execute(self):
        if self.agent.distance>0:
            self.agent.current_state(AttackState(self.agent))

            return
        
        x=random.randint (0,39) 
        y=random.randint (0,29)
        agent.deplacerVers(x,y)
        agent.changerCouleur(0,255,0)

    def exit(self):
        pass
class AttackState(State):
    def enter(self):
        pass

    def execute(self):
        pass
        global xEnnemi
        global yEnnemi
        if agent.distance==0  and agent.x==xEnnemi and agent.y==yEnnemi:
            self.agent.current_state(ScanState(self.agent))
            agent.changerCouleur(255,0,0)

    def exit(self):
        pass"""








































while True:
	agent.update()
	agent.lookAt((agent.dir + 1) % 4)