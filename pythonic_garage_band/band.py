from collections import namedtuple


class  Band():
    pass
    
class Musician():
    pass     

class Guitarist:
    
    def __init__(self, name, ):
        self.name = name
        self.instrument = 'guitar'
          
    def __str__(self):
        return 'My name is ' + str(self.name) + ' and I play ' + str(self.instrument)
    
    def __repr__(self):
        return 'Guitarist instance. Name = ' + str(self.name)
    
class Drummer:
    def __init__(self, name, ):
        self.name = name
        self.instrument = 'drums'
          
    def __str__(self):
        return 'My name is ' + str(self.name) + ' and I play ' + str(self.instrument)
    
    def __repr__(self):
        return 'Drummer instance. Name = ' + str(self.name)

class Bassist:
    def __init__(self, name, ):
        self.name = name
        self.instrument = 'bass'
          
    def __str__(self):
        return 'My name is ' + str(self.name) + ' and I play ' + str(self.instrument)
    
    def __repr__(self):
        return 'Bassist instance. Name = ' + str(self.name) 
    