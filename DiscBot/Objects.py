import random

class Player:
    """
    A class that represents a plyer in the game of Assasin

    === Attributes ===
    - name: The discord name of this player
    - _killtoken: The 5 digit randomly generated number that will kill this player
               if typed into the chat
    - contract: A contract that must be completed in order to get paid. 
    - isAlive: The current state of this player.

    """
    name: str 
    _killtoken: int
    contract: list
    status: bool 

    def __init__(self, name: str) -> None:
        ''' Initialize this player object '''
        self.name = name
        self._killtoken = generateToken()
        self.contract = list()
        self.status = True

    def __str__(self) -> str:
        if self.status is True:
            return "Name: {}\nStatus: Alive\nKill token: {}\n".format(self.name, self._killtoken)
        return "Name: {}\nStatus: Dead\nKill token: {}".format(self.name, self._killtoken)
    
    def getToken(self)-> int:
        return int(self._killtoken)

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
    '''TODO'''
    assassins: list()

    def __init__(self) -> None:
        self.assassins = list()

    def kill(self, id:int) -> str:
        for i in range(len(self.assassins)):
            killed = False
            if id == self.assassins[i]._killtoken:
                self.assassins[i].status = False
                killed = True
                return ("{} has been assasinated\n".format(self.assassins[i].name))
        if not killed:
            return ("Invalid Kill Token")
    
    def __str__(self) -> str:
        ''' Returns the string representaion of the game'''
        str_rep = ''
        for assassin in self.assassins:
            str_rep += '{}\n'.format(str(assassin))
        return str_rep

    def add(self, assassin: Player) -> None:
        ''' Adds <assassin> to the game'''
        self.assassins.append(assassin)

    def getPlayer(self, id:int) -> str:
        ''' returns the player with the <id>'''
        for player in self.assassins:
            if player._killtoken == id:
                return player.name             

if __name__ == "__main__":
    newGame = Game()
    names = ['Jaivir', 'Simrat', 'Juan', 'Akksayen']
    [newGame.add(Player(name)) for name in names]
    print(newGame)
    tooken = newGame.assassins[3].getToken()
    msg = newGame.kill(tooken)
    print(msg)
    print(newGame)
