# -*- coding: utf-8 -*-

class Item:
    

    def __init__(self, name, attributes, catchphrase=None, ability, location=None, owner=None, subitems=None):
        self.name = name
        self.attributes = attributes
        self.location = location
        self.owner = owner
        self.ability = ability #does this need its own method?
        
        
        if subitems is None:        
            self.subitems = []
        else:
            self.subitems = subitems

    def add_subitem(self, item): #say, to the bag of holding
        if item is not in self.subitems:
            self.subitems.append(item)

    def remove_subitem(self, item):
        if item is in self.subitems:
            self.subitems.remove(item)

    def get_location(self):
        if owner is None:
            return location
        else:
            return owner.location