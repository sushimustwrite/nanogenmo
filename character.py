# -*- coding: utf-8 -*-
#TODO:ALL THE THINGS
#well, the rest of the things

class Character:
    #range from -10 (sad) to 10 (happy)
    mood_goodbad = 0
    #range from -10 (depressed) to 10 (excited/agitated)
    mood_energy = 0
    #number of items I can hold
    capacity = 5
    hasBag = False
    offered_item = {}
    
    
    def __init__(self, name, gender, catchphrase, attributes, location=None, items=None, goals=None, history=None):
        import printutils
        self.name = name
        self.catchphrase = catchphrase
        if gender == 'male':
            pronouns = printutils.masculine
        else if gender == 'female':
            pronouns = printutil.feminine
        else if gender == 'neuter':
            pronouns = printutils.neuter
        else if gender == 'neutral':
            pronouns = neutral
        self.location = location #how would this change location
        self.attributes = attributes
        if goals is None:
            self.goals = []
        else:
            self.goals = goals
        if items is None:
            self.items = []
        else:
            self.items = items
        knowledge = {'items':{},'locations':{},'characters':{},'states':{}}
        if history is None:
            self.history = {}
        else:
            self.history = history
    def set_location(location):
        self.location = location
        
    def happify(self,bump=1):
        mood_goodbad+=bump
        if mood_goodbad > 10:
            mood_goodbad = 10
            
    def saddify(self,bump=1):
        mood_goodbad-=bump
        if mood_goodbad < -10:
            mood_goodbad = -10
            
    def excite(self,bump=1):
        mood_energy+=bump
        if mood_energy >10:
            mood_energy = 10
    
    def depress(self,bump=1):
        mood_energy-=bump
        if mood_energy <-10:
            mood_energy = -10
            
    def add_goal(self,goal):
        goal = remember(goal)
        if goal not in goals:
            goals.add(goal)
            
    def remove_goal(self,goal):
        goal = remember(goal)
        if goal in goals:
            goals.remove(goal)
            
    #find my own version of this object, 
    def remember(self,obj):
        if type(obj) is Location:
            myobj=knowledge['locations'].get(obj.name)
        else if type(obj) is Item:
            myobj=knowledge['items'].get(obj.name)
        else if type(obj) is Character:
            myobj=knowledge['characters'].get(obj.name)
        else if type(obj) is State:
            myobj=knowledge['states'].get(obj.name)
        return myobj
        
    #add specified attributes to local version
    def learn(self,obj,attributes):
        myobj = remember(obj)
        if myobj is None:
            if type(obj) is Location:
                knowledge['locations'][obj.name] = Location(obj.name,obj.attributes,obj.catchphrase)
                myobj = knowledge['locations'][obj.name]
            else if type(obj) is Item:
                knowledge['items'][obj.name] = Item(obj.name,obj.attributes,obj.catchphrase)
                myobj = knowledge['locations'][obj.name]
            else if type(obj) is Character:
                knowledge['characters'][obj.name] = Character(obj.name,obj.pronouns,obj.catchphrase,obj.attributes)
                myobj = knowledge['characters'][obj.name]
            else if type(obj) is State:
                knowledge['states'][obj.name] = State(obj.name,obj.namepast,obj.character)
                myobj = knowledge['states'][obj.name]
        
        for attr in attributes:
            value = getattr(obj,attr)
            #replace the referenced attribute by the one i remember: no catastrophic delivery of free information!
            if type(value) is Item or type(value) is Location or type(value) is State or type(value) is Character:
                value = remember(value)
            setattr(myobj,attr,value)

            
    def experience(self,date,event):
        if date not in keys(history):
            history[date] = event
            
    #TODO: infer what to do to get to goal HARD
    def doSomething(self):
        pass
    
    #TODO: give another character some info
    def tell(self,character,string):
        pass
    
    #TODO name him/herself and give a random event from his/her history
    def introduce(self):
        pass
    
    #TODO say a random exclamation
    def exclaim(self):
        
    def go(self):
        self.location.move_along(self,route)
        
    #TODO do something related to mood
    def emote(self):
        pass
    
    #TODO output some text about this action
    #TODO put things in bag of holding?
    def take(self,character,item):
        import random
        success=True
        if not character.offering(self,item):
            if random.rand()<0.4
                character.removeItem(item)
            else:
                character.catch_thief()
                success=False
            
        if success and item.name not in keys(items) and (len(items) < capacity or 'Bag of Holding' in keys(items)):
            items[item.name]=item
            if len(items)>capacity:
                #TODO: decide what goes in bag of holding
        else if success and item.name not in keys(items):
            #TODO: decide what item to drop
            pass
        
    #TODO: what do you do? this probably depends on the character so just put a default "stern warning" here and we'll modify it to something else for specific characters
    def catch_thief(self):
        pass
    
    def offer(self,character,item):
        offered_item[character.name] = item

    def offering(self,character,item)
        return offered_item[character.name] is item
        
    #TODO: decide which item is no longer necessary, or won't be needed soonest, or just a random item
    def least_useful_item(self):
        pass
        
    def pick_up(self,item):
        success = (item in self.location.items)
        if success and item.name not in keys(items) and (len(items) < capacity or 'Bag of Holding' in keys(items)):
            if len(items)>capacity:
                pass
                #TODO: decide what goes in bag of holding
        else if success and item.name not in keys(items):
            leave(least_useful_item())
        if success: 
            items[item.name]=item
            self.location.delete_item(item)
        
    def leave(self,item):
        if item.name in keys(items):
            items.remove(item)
            location.add_item(item)
            
    def use(self,item):
        if item.name in keys(items):
            item.use()
            
    #obj is a State, Item, or Character
    def ask(self,character,obj):
        import random
        #TODO: phrase information request sensibly
        if random.rand()<0.8:
            character.tell(self)
        else:
            pass
            #TODO You are not a nice man and I won't tell you!