# use this file to define the 3 mech type - starting with over all definitions 

class MechType():
    def __init__(self, name):
        
        self.name = name

class Tank(MechType):
    def __init__(self, name, y, radius):
        super().__init__(x,y, radius)
        self.x = x
        self.y = y
        
        self.name = name
        self.max_hp = max_hp
        self.attack = attack 
        self.speed = speed

class Gunner():
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        self.x = x
        self.y = y
        
        self.name = name
        self.max_hp = max_hp
        self.attack = attack 
        self.speed = speed

class Bomber():
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        self.x = x
        self.y = y
        
        self.name = name
        self.max_hp = max_hp
        self.attack = attack 
        self.speed = speed