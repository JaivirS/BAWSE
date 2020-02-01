import random

class Player:
    """
    A class that represents a plyer in the game of Assasin

    === Attributes ===
    - name: The discord name of this player
    - _killToken: The 5 digit randomly generated number that will kill this player
               if typed into the chat
    - contract: A contract that must be completed in order to get paid. 
    - isAlive: The current state of this player.

    """
    name: str 
    _killtoken: int
    contract: list
    isAlive: bool 

    def __init__(self, name: str) -> None:
        ''' Initialize this player object '''
        self.name = name
        self._killtoken = generateToken()
        self.contract = list()
    
def generateToken() -> int:
    ''' returns a random 5 digit number'''
    return random.randint(10000, 99999)


class Contract:
    ''' A contract for an assasin to complete
    
    === Attributes ===
    - target: The target for the assasin that the contract is assigned tol 
    -  assignedTo: The assasin who is assigned this contract 
    - completed: The current state of this contract 

    === Representation Invariants === 
    - completed must always be a boolean value 
    '''
    target: Player
    assignedTo: Player
    completed: bool

    def __init__(self, tar: Player, aTo: Player) -> None:
        ''' Initialize a Conctract '''
        self.target = tar
        self.assignedTo = aTo 
        self.completed = False


    
    