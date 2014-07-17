# -*- coding: utf-8 -*-
class Event:
    
    def __init__(self,location,description,update_fun):
        self.location = location
        self.description = description
        self.update_fun = update_fun
        
    def trigger(self):
        import utility
        print description
        update_fun(location)

class SingleCharacterEvent(Event):
    
    def __init__(self,character,location,description,update_fun):
        self.character = character
        self.location = location
        self.description = description
        self.update_fun = update_fun

    def trigger(self):
        import printutils
        import utility
        print printutils.return_single(self.description,self.character)
        update_fun(self.character,self.location)
        date = utility.date()
        self.character.add_history(date,self)
        
class DoubleCharacterEvent(Event):
    
    def __init__(self,character1,character2,location,description,update_fun):
        self.character1 = character1
        self.character2 = character2
        self.location = location
        self.description = description
        self.update_fun = update_fun
        
    def trigger(self):
        import printutils
        import utility
        print printutils.return_double(description,character1,character2)
        update_fun(character1,character2,location)
        date  = utility.date()
        self.character.add_history(date,self)