class Board:
    

    def __init__(self):
        
    
        self.__points__ = [ [] for _ in range(24) ]

        
        self.__bar__ = { "player1": [], "player2": [] }

    
        self.__home__ = { "player1": [], "player2": [] }

        
        self._setup_initial_position()

    def _setup_initial_position(self):
       
        self.__points__[0]   = ["player1"] * 2
        self.__points__[11]  = ["player1"] * 5
        self.__points__[16]  = ["player1"] * 3
        self.__points__[18]  = ["player1"] * 5

        self.__points__[23]  = ["player2"] * 2
        self.__points__[12]  = ["player2"] * 5
        self.__points__[7]   = ["player2"] * 3
        self.__points__[5]   = ["player2"] * 5
