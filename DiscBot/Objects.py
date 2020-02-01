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

    def __str__(self) -> str:
        return "Name: {}\nKill token: {}".format(self.name, self._killtoken)
    
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

class Game:
    ''''''
    assassins: list()

    def __init__(self) -> None:
        self.assassins = list()

    def kill(self, id:int) -> str:
        for man in self.assassins:
            if id == man._killToken:
                m = self.assassins.pop(self.assassins.index(man))
                del(m)
            return "{} has been assasinated".format(man.name)
        return "Invalid Kill Token"
    
    def __str__(self) -> str:
        ''' Returns the string representaion of the game'''
        return str(self.assassins)

    def add(self, assassin: Player) -> None:
        ''' Adds <assassin> to the game'''
        self.assassins.append(assassin)