# -*- coding: utf-8 -*-
#what is happening
#TODO: Stuff everywhere

class Location:
   

    def __init__(self, name, attributes, catchphrase=None)
        self.attributes = attributes
        self.catchphrase = catchphrase
        self.name = name
        self.characters_present = []
        self.adjacent_routes = []
        self.items = []
        self.sublocations = []

    def delete_item(self, item):
        if item in items:
            items.remove(item)
        
    def add_item(self, item):
        if not item in items:
            items.append(item)

    #TODO: set the corresponding State for this character in this location
    def arrive_character(character):
        characters_present.append(character)
        
    def delete_character(character):
        #see if character is in location
        #if yes, delete character
        characters_present.remove(character)


    def nearby_routes(route):
        adjacent_routes.append(route)
        
        
        #return nearby_routes
        

    def add_sublocation(self, location):
        if location is not in self.sublocations:
            self.sublocations.append(location)
            
    #TODO: move a character from one place to another, possibly with random encounters along the way
    def move_along(character,location)
        pass
        

# wtf is happening i don't even
class Sublocation(Location):
    def __init__(self, name, attributes, catchphrase, parent):
        self.parent = parent
        super(Sublocation, self).__init__(name, attributes, catchphrase)
        

class Entrance(Sublocation):
    pass
