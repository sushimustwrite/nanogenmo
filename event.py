# -*- coding: utf-8 -*-
class Event:
    
    def __init__(self,character,location,description,update_fun):
        self.character = character
        self.location = location
        self.description = description
        self.update_fun = update_fun

    def trigger(self):
        import printutils
        printutils.print(description,character)
        update_fun(character,location)