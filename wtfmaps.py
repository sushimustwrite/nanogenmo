#what is happening
#TODO: Stuff everywhere

class Location(object):
   

    def __init__(self, name, attributes, catchphrase=None)
        self.attributes = attributes
        self.catchphrase = catchphrase
        self.name = name
        self.characters_present = []
        self.adjacent_routes = []
        self.items = []
        self.sublocations = []
        self.entrances = [] 
        

    def items_in_location(self):
        # see if items are in location???
        itemlist = self.items
        #TODO: stuff here
        return itemlist 

    def delete_item(self, item):
        items.remove(item)


    def characters_in_location(character):
        #should i assume no characters in location besides Protag?
        characters_present.append(character)
        
    def delete_character(character):
        #see if character is in location
        #if yes, delete character
        characters_present.remove(character)


    def nearby_routes(route):
        adjacent_routes.append(route)
        
        
        #return nearby_routes
        

    def add_sublocation(self, location, entrance=False):
        if location is not in self.sublocations:
            self.sublocations.append(location)

        if entrance:
            self.entrances.append(location)
        

# wtf is happening i don't even
class Sublocation(Location):
    def __init__(self, name, attributes, catchphrase, parent):
        self.parent = parent
        super(Sublocation, self).__init__(name, attributes, catchphrase)
        
    
class Entrance(Sublocation):
    pass
