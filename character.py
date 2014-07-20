# -*- coding: utf-8 -*-
import printutils, random

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
		mood_goodbad = random.
			
			
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
        if goal in self.goals:
            self.goals.remove(goal)
            
    #find my own version of this object, 
    def remember(self,obj):
		myobj=obj
        if type(obj) is Location:
            myobj=self.knowledge['locations'].get(obj.name)
        else if type(obj) is Item:
            myobj=self.knowledge['items'].get(obj.name)
        else if type(obj) is Character:
            myobj=self.knowledge['characters'].get(obj.name)
        else if type(obj) is State:
            myobj=self.knowledge['states'].get(obj.name)
        return myobj
        
    #add specified attributes to local version
    def learn(self,obj,attributes):
        myobj = self.remember(obj)
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
                value = self.remember(value)
			else if type(value) is list:
				newlist = []
				for item in list:
					newitem = self.remember(item)
					newlist.append(newitem)
				value = newlist
			else if type(value) is dict:
				newdict = {}
				for (key,item) in items(value):
					newdict[key] = self.remember(item)
				value = newdict
			setattr(myobj,attr,value)

            
    def experience(self,date,event):
        if date not in keys(history):
            history[date] = event
            
    #TODO: infer what to do to get to goal HARD
    def doSomething(self):
        pass
    
    #give another character some info (which does not have to be the same type as was asked about)
	#returns a boolean whether or not any information was given
    def tell(self,character,obj):
		if random.rand()>0.8:
			self.refuse()
			return false
		myobj = remember(obj)
		if myobj is None:
			printutils.formatdialog(self.pronouns,"I'm afraid I don't know anything about that","said")
			return false
		
		if myobj is Location:
			#TODO: say its catchphrase and attributes and up to five times either: a character who is there, a route that goes there, 
			for i in range(random.randInt(1,5)):
				pass
				#TODO: learn the asker the relevant info
			return true
		if myobj is Item:
			#TODO: say its catchphrase and attributes and up to five times either: where it is, what it is does, or what it can accomplish (one state it can be used to get to)
			for i in range(random.randInt(1,5)):
				pass
				#TODO: learn the asker the relevant info
		if myobj is Character:
			#TODO: say its catchphrase and attributes and up to five times either: their current location, their current goal, an item they have, a bit of history
			for i in range(random.randInt(1,5)):
				pass
				#TODO: learn the asker the relevant info
		if myobj is State:
			if myobj.character.name != character.name:
				printutils.formatdialog(self.pronouns,"I'm afraid you won't be able to do that at all!","explained")
			#TODO: say up to five times: an input to this state
			for i in range(random.randInt(1,5)):
				pass
				#TODO: learn the asker the relevant info
				
        
	#TODO: different ways of refusing to talk to someone. these should work even if they've been talking a bit
	def refuse():
		refusals = ["Sorry mate, I have to get going"] #and so on
		excuse = random.choose(refusals)
		printutils.formatdialog(self.pronouns,excuse,"replied")
    
    #TODO name him/herself and give a random event from his/her history
    def introduce(self):
        introduction = random.choose(["Hello, I am #name. #catchphrase", "Greetings, traveler. You may call me #name. #catchphrase", "You're probably wondering who I am. I am #name. #catchphrase"])
        introduction = introduction.replace("#name", self.name)
        introduction = introduction.replace("#catchphrase", self.catchphrase)
		printutils.formatdialog(self.pronouns,introduction,"said")
    
    #TODO say a random exclamation
    def exclaim(self):
        if self.mood_goodbad > -1:
            exclamation = random.choose(["Willickers!", "Wahoo!", "W00t!", "Bless your heart.", "Oh my god.", "Oh my goodness.", "Oooh.", "Cheers!"])
        else:
            exclamation = random.choose(["Fuck this!", "Shit!", "Nooooooooooooooo.", "Fuck this shit.", "Motherfucker.", "Crap.", "Oh dear.", "Aaaaaah!", "Zounds!", "God's blood!", "Fie!", "Tut.", "Pooh!", "Merde."])
		printutils.formatdialog(self.pronouns,introduction,"exclaimed")
		
    def go(self):
        self.location.move_along(self,route)
        
    #TODO do something related to mood. come up with more emotes.
    #TODO if mood_goodbad is high, medium, low--set emote equal to something appropriate to mood
    def emote(self):
    if self.mood_goodbad > 1:
        emote = random.choose(["A large grin filled #name's face.", "#name's laugh filled the area.", "#name smiled.", "#name grinned."])
    elif self.mood_goodbad < -1:
        emote = random.choose(["#name kicked a rock several feet ahead.", "#name sighed deeply and stared at the ground.", "#name frowned.", "A grimace appeared on #name's face.", "#name ])
    else:
        emote = random.choose(["#name looked ahead.",  "#name stared."])
    emote = emote.replace("#name", self.name)
    
    #TODO output some text about this action
    #TODO put things in bag of holding?
    def take(self,character,item):
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
            
    #obj is a State, Item, Location, or Character
    def ask(self,character,obj):
		#TODO: phrase information request sensibly
		#Do you know anything about ...?
		character.tell(self,obj)
        
        
