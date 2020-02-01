import random

class Player:
    """
    A class that represents a plyer in the game of Assasin

    === Attributes ===
    - name: The discord name of this player
    - _killToken: The 5 digit randomly generated number that will kill this player
               if typed into the chat
    - contract: The target assigned to this player.
    - isAlive: The current state of this player.

    """
    name: str 
    _killtoken: int
    contract: Contract
    isAlive: bool 

    def __init__(self, name: str) -> None:
        ''' Initialize this player object '''
        self.name = name
        self._killtoken = generateToken()
        self.contract = []
        self.isAlive = True 
    
def generateToken() -> int:
    ''' returns a random 5 digit number'''
    return random.randint(10000, 99999)

    
    