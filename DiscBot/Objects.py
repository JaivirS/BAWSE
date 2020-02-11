import random

class Player:
    """
    A class that represents a plyer in the game of Assasin

    === Attributes ===
    - name: The discord name of this player
    - _killtoken: The 5 digit randomly generated number that will kill this player
               if typed into the chat
    - contract: The contract to complete by this player. 
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
        self.contract = None
        self.isAlive = True

    def __str__(self) -> str:
        if self.isAlive is True:
            return "Name: {}\nStatus: Alive\nKill token: {}\n".format(self.name, self._killtoken)
        return "Name: {}\nStatus: Dead\nKill token: {}".format(self.name, self._killtoken)
    
    def getToken(self)-> int:
        return int(self._killtoken)
    
    def getContract(self) -> None:
        '''Returns the string representation of all the contracts'''
        return str(self.contract)
    
    def update(self) -> None:
        self.contract._update()

def generateToken() -> int:
    ''' returns a random 5 digit number'''
    return random.randint(10000, 99999)


class Contract:
    ''' A contract for an assasin to complete
    
    === Attributes ===
    - target: The target for the assasin that the contract is assigned tol 
    - assignedTo: The assasin who is assigned this contract 
    - completed: The current state of this contract 
    - reward : The reward for completing this contract

    === Representation Invariants === 
    - completed must always be a boolean value 
    - reward > -1
    '''
    target: Player
    assignedTo: Player
    completed: bool
    reward: int

    def __init__(self, tar: Player) -> None:
        ''' Initialize a Conctract '''
        self.target = tar
        self.assignedTo = None 
        self.completed = False
        self.reward = 100 
    
    def __str__(self) -> str:
        ''' returns the string representation of this contract'''
        return "Assassin: {} Target: {} Reward: {}\n".format(self.assignedTo.name, self.target.name, self.reward)

    def claim(self, code:int) -> None:
        ''' Claim this contract by confirming if <code> is == to <self.assignedTo>.<_killtoken>'''
        if code == self.assignedTo._killtoken:
            self.completed = True 

    def assign(self, assassin: Player) -> None:
        ''' assigns this contract to <assassin.'''
        self.assignedTo = assassin
        assassin.contract = (self)
    
    def _update(self) -> None:
        '''completes this contract'''
        self.completed = True

    def is_completed(self) -> bool:
        ''' check to see if this contract has been claimed'''
        return self.completed


class Game:
    '''A game of Assassin 
    === Attributes ===
    - assasins: A list of all the assassins in the game
    - contracts: A list of all the contracts in the game
    - _isRunning: Current state of the game 

    === Representation Invariants === 
    - _isRunning must only be a boolean value
    '''
    assassins: list()
    contracts: list()
    _isRunning: bool 

    def __init__(self) -> None:
        self.assassins = list()
        self.contracts = list()
        self._isRunning = False

    def __str__(self) -> str:
        ''' Returns the string representaion of the game'''
        str_rep = ''
        for assassin in self.assassins:
            str_rep += '{}\n'.format(str(assassin))
        return str_rep
    
    def kill(self, id:int) -> str:
        for i in range(len(self.assassins)):
            killed = False
            if id == self.assassins[i]._killtoken:
                if self.assassins[i].isAlive is True:
                    self.assassins[i].isAlive = False
                    killed = True
                    return ("Contract confirmed, {} has been assasinated\n".format(self.assassins[i].name))
                else:
                    return ('{} is already dead!'.format(self.assassins[i].name))
        if not killed:
            return ("Invalid Kill Token")

    def addPlayer(self, assassin: Player) -> None:
        ''' Adds <assassin> to the game'''
        self.assassins.append(assassin)

    def addContract(self, assassin: Player) -> None:
        ''' Creates a contract on <assasin>'''
        self.contracts.append(Contract(assassin))

    def getPlayer(self, name:str) -> str:
        ''' returns the player with the <name>'''
        for i in range(len(self.assassins)):
            if self.assassins[i].name == name:
                return self.assassins[i]
    
    def getPlayerId(self, idd:int) -> str:
        ''' returns the player with the <id>'''
        for i in range(len(self.assassins)):
            if self.assassins[i]._killtoken == idd:
                return self.assassins[i].name
    
    def getContracts(self) -> str:
        '''returns the string representation of all the contracts in the game'''
        string = ''
        for c in self.contracts:
            string += str(c) 

        return string  

    def runGame(self) -> None:
        '''Runs the game'''
        self._isRunning = True  

    def is_running(self) -> None:
        ''' Returns true if <self._isRunning> is True:'''
        return self._isRunning 

    def Endgame(self) -> None:
        ''' Ends this game'''
        self.assassins.clear()
        self.contracts.clear()
        self._isRunning = False

    def distribute_conracts(self) -> None:
        ''' assigns all contracts to all the players in the game'''
        # for c in self.contracts:
        #     t = [x for x in self.assassins if x != c.target]
        #     print('t =')
        #     for i in t:
        #         print(i)
        #     x = random.choice(t)
        #     c.assign(x)
        t = random.sample(self.assassins, len(self.assassins))
        i = len(self.assassins) -1
        j = 0
        while (i > 0 and j < len(self.assassins)):
            self.contracts[j].assign(t[i])
            i -= 1
            j += 1

    def update_contracts(self) -> None:
        '''re-assaign contracts when someone kills someone'''


if __name__ == "__main__":
    newGame = Game()
    names = ['Jaivir', 'Simrat', 'Juan', 'Akksayen']
    
    for n in names:
        temp = Player(n)
        newGame.addPlayer(temp)
        newGame.addContract(temp)    
    
    newGame.distribute_conracts()
    print(newGame)
    print(newGame.getContracts())
    print(newGame.assassins[1].getContract())
    tooken = newGame.assassins[3].getToken()
    msg = newGame.kill(tooken)
    print(msg)
    print(newGame)
