class  Band():
    instances = []
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
         
    def play_solos(self):
       solos = []
       for member in self.members:
           solos.append(member.play_solo())
       return solos
   
class Musician():
    def __str__(self):
        return "My name is " + str(self.name) + " and I play " + str(self.instrument)      
    def __repr__(self):
        if self.instrument == 'guitar':
            musician_type = 'Guitarist'
        elif self.instrument == 'bass':
            musician_type = 'Bassist'
        elif self.instrument == 'drums':
            musician_type = 'Drummer'
        rep = f"{musician_type} instance. Name = " + self.name
        return rep
    
    def get_instrument(self):
        return self.instrument
    
 
class Guitarist(Musician):
    
    def __init__(self, name='unkown'):
        self.name = name
        self.instrument = 'guitar'      
    
    def __repr__(self):
        return 'Guitarist instance. Name = ' + str(self.name)
    
    def play_solo(self):
        return "face melting guitar solo"
    
    
class Drummer(Musician):
    def __init__(self, name='unkown' ):
        self.name = name
        self.instrument = 'drums'          
        
    def __repr__(self):
        return 'Drummer instance. Name = ' + str(self.name)
    
    def play_solo(self):
        return "rattle boom crash"
    

class Bassist(Musician):
    def __init__(self, name='unkown' ):
        self.name = name
        self.instrument = 'bass'         
    
    def __repr__(self):
        return 'Bassist instance. Name = ' + str(self.name)
    
    def play_solo(self):
        return "bom bom buh bom"
     
    