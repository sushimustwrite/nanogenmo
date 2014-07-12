#TODO: ALL THE THINGS
#but mostly conditions

class Item:
    

    def __init__(self, name, attributes, catchphrase=None, location, ability, subitems=None, owner=None):
        self.name = name
        self.attributes = attributes
        self.location = location
        self.ability = ability #does this need its own method?
                
        if subitems is None:        
            self.subitems = []
        else:
            self.subitems = subitems

        if owner is not None:
            self.owner = owner
            #self.location = Character.location #???

    def add_subitem(self, item): #say, to the bag of holding
        if item is not in self.subitems:
            self.subitems.append(item)
    #how can we tell whether an item is a subitem of anotehr item? example: the feather will never be a subitem of the dragon scale.
    #does this need its own class too? once you take an item out of the bag, then it's not a subitem anymore

    def remove_subitem(self, item):
        if item is in self.subitems:
            self.subitems.remove(item)
