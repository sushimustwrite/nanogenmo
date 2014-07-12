#TODO:ALL THE THINGS
#well, the rest of the things

class Character:

    def __init__(self, name, pronouns, catchphrase, location, items=None, #TODO):
        self.name = name
        self.catchphrase = catchphrase
        self.pronouns = #TODO
        self.location = location #how would this change location
        if self.items is None:
            self.items = []
        else:
            self.items = items
