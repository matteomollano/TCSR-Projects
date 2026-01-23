class Ship():
    
    # constructor
    def __init__(self):
        self.symbol = ""
        self.target = False
      
    # getter and setter methods  
    def getSymbol(self):
        return self.symbol
    
    def setSymbol(self, symbol):
        self.symbol = symbol
    
    def getTarget(self):
        return self.target
    
    def setTarget(self, target):
        self.target = target
    
    # toString method
    def __str__(self):
        return self.getSymbol()