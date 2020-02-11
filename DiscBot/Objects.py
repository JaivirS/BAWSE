import random
from typing import Union

GAME_MODE = {1: "Team vs Team", 2: "Last Man Standing", 3: "Elite"}

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
    _contract: None
    status: bool 

    def __init__(self, name: str) -> None:
        ''' Initialize this player object '''
        self.name = name
        self._killtoken = generateToken()
        self._contract = None
        self.isAlive = True

    def __str__(self) -> str:
        if self.isAlive is True:
            return "Name: {}\nStatus: Alive\n".format(self.name)
        return "Name: {}\nStatus: Dead\n".format(self.name)
    
    def info(self):
        '''Returns all the info of this player'''
        return "Name: {}\nKill Token: {}\nHere is your contract\n{}".format(self.name, self._killtoken, self._contract)

    def getToken(self)-> int:
        return int(self._killtoken)
    
    def getContract(self) -> None:
        '''Returns the string representation of all the contracts'''
        return str(self._contract)
    
    def assign(self, c) -> None:
        ''''''
        self._contract = c
    
    def update(self) -> None:
        self._contract._update()

def generateToken() -> int:
    ''' returns a random 5 digit number'''
    return random.randint(10000, 99999)


class Contract:
    ''' A contract for an assasin to complete
    
    === Attributes ===
    - target: The target for the assasin that the contract is assigned tol 
    - assignedTo: The assasin who is assigned this contract 
    - completed: The current state of this contract 


    === Representation Invariants === 
    - completed must always be a boolean value 

    '''
    target: Player
    assignedTo: Player
    completed: bool


    def __init__(self, mar: Player, tar:Player) -> None:
        ''' Initialize a Conctract '''
        self.assignedTo = mar 
        self.target = tar
        self.completed = False
    
    def __str__(self) -> str:
        ''' returns the string representation of this contract'''
        return "Assassin: {} Target: {}\n".format(self.assignedTo.name, self.target.name)

    def claim(self, code:int) -> None:
        ''' Claim this contract by confirming if <code> is == to <self.assignedTo>.<_killtoken>'''
        if code == self.assignedTo._killtoken:
            self.completed = True 
    
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
    - _dead: A list of all the dead players

    === Representation Invariants === 
    - _isRunning must only be a boolean value
    '''
    assassins: list()
    contracts: list()
    _isRunning: bool
    _dead: list()
 

    def __init__(self) -> None:
        self.assassins = list()
        self.contracts = list()
        self._isRunning = False
        self._dead = list()

    def __str__(self) -> str:
        ''' Returns the string representaion of the game'''
        str_rep = ''
        for assassin in self.assassins:
            str_rep += '{}\n'.format(str(assassin))
        for assassin in self._dead:
            str_rep += '{}\n'.format(str(assassin))
        return str_rep
    
    def kill(self, id:int, assassin_name: str) -> str:
        for i in range(len(self.assassins)):
            killed = False
            if id == self.assassins[i]._killtoken:
                if self.assassins[i].isAlive is True:
                    self.assassins[i].isAlive = False
                    name = self.assassins[i].name
                    killed = True
                    self._on_death(id, assassin_name)
                    if len(self.assassins) == 1:
                        return ("Congratulations {}, You have won the game".format(assassin_name))
                    else:
                        return ("Contract confirmed, {} has been assasinated\n".format(name))
                else:
                    return ('{} is already dead!'.format(self.assassins[i].name))
        if not killed:
            return ("Invalid Kill Token")

    def _on_death(self, dead_id: int, hitman_name:str) -> None:
        '''Removes the dead player in the game and assigns a new contract'''
        killed_player = self._on_death_helper(dead_id)
        hitman = self._on_death_helper(hitman_name)

        killed_player._contract.assignedTo = hitman
        hitman.assign(killed_player._contract)
        self._dead.append(self.assassins.pop(self.assassins.index(killed_player)))
        
    def _on_death_helper(self, obj: Union[int,str])-> Player:
        ''' A helper method for _on_death'''
        if isinstance(obj, int):
            for i in range(len(self.assassins)):
                if self.assassins[i].name == self.getPlayerId(obj):
                    return self.assassins[i]
        else:
            for i in range(len(self.assassins)):
                if self.assassins[i].name == self.getPlayer(obj):
                    return self.assassins[i]

    def _correct_kill(self, name:str, id:int) -> bool:
        '''Returns True is the player with <name> has killed their target'''
        a1, a2 = self._on_death_helper(name), self._on_death_helper(id)

        return a1._contract.target.name == a2.name

    def addPlayer(self, assassin: Player) -> None:
        ''' Adds <assassin> to the game'''
        self.assassins.append(assassin)

    def getPlayer(self, name:str) -> str:
        ''' returns the player with the <name>'''
        for i in range(len(self.assassins)):
            if self.assassins[i].name == name:
                return self.assassins[i].name

    def _getPlayer(self, name:str) -> str:
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

    
    def _get_a_contract(self, name:str) -> str:
        '''Cheat method to get the contract object for the player with <name>'''
        for a in self.assassins:
            if a.name == name:
                return a.getContract()  

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
    
    def distribute_contracts(self) -> None:
        ''' assigns all contracts to all the players in the game'''
        
        random.shuffle(self.assassins)
        i = 1
        
        for player in self.assassins:
            if i < len(self.assassins):
                c = Contract(player, self.assassins[i])
                player.assign(c)
                i +=1
            else:
                i = 0
                c = Contract(player, self.assassins[i])
                player.assign(c)