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
    root_goal = None

#TODO: Add relationships (with other characters, etc)
#TODO: Add random reflect method (lets them talk motivation) and a random character/action method
    
    
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
            pronouns = printutils.neutral
        self.location = location
        self.attributes = attributes
        if goals is None:
            self.goals = []
        else:
            self.goals = goals
            root_goal = goal[0]
        anti_goals = []
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
        mygoal = remember(goal)
        if mygoal is None:
            self.learn(goal)
        mygoal = remember(goal)
        if mygoal not in goals:
            goals.add(mygoal)
    
    def add_anti_goal(self,goal):
        mygoal = remember(goal)
        if mygoal is None:
            self.learn(goal)
        mygoal = remember(goal)
        if mygoal not in anti_goals:
            anti_goals.add(mygoal)
            
    def add_terminal_goal(self,goal):
        self.add_goal(goal)
        self.root_goal = goal
            
    def remove_goal(self,goal):
        goal = remember(goal)
        if goal in self.goals:
            self.goals.remove(goal)
            
    #find my own version of this object, 
    def remember(self,obj):
	    myobj=None
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
    def learn(self,obj,attributes=None):
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
        if attributes is not None:
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
        #check all goals to see which have been satisfied
        continue = True
        for goal in goals:
            action = goal.get_required_action()
            if action is not None:
                action.perform()
                continue=False
                break
        if continue:
            for goal in anti_goals:
                action = goal.get_required_off_action()
                if action is not None:
                    action.perform()
                    continue=False
                    break
        #if any goal has its non-action prerequisites satisfied, perform the required action(s)
            
        #if any goal has all its prerequisites satisfied EXCEPT for being in the right location, move toward that location
        #find a goal with no inputs identified--pick at random, and search the current location for someone to ask about it
        #if no person to ask exists, go somewhere else at random!
        
        printutils.new_paragraph()
        
        
    
    #give another character some info (which does not have to be the same type as was asked about)
	#returns a boolean whether or not any information was given
    #after the first time add "Did I mention" "Did you know" "I can't remember if I said" things like that to some of the dialogues
    def tell(self,character,obj):
        if random.rand()>0.8:
            self.refuse()
            return false
        myobj = remember(obj)
        if myobj is None:
            printutils.formatdialog(self.pronouns,"I'm afraid I don't know anything about that","said")
            return false
		
        if type(myobj) is Location:
            #TODO: say its catchphrase and attributes and up to five times either: a character who is there, a route that goes there, 
            printutils.print_single("Ah, yes, I've been there. #catchphrase")
            for i in range(random.randInt(1,5)):
                #pass
                
                #TODO: learn the asker the relevant info, add knowledge item to character's knowledge
                return true
        if type(myobj) is Item:
            #TODO: say its catchphrase and attributes and up to five times either: where it is/who has it, what it does, or what it can accomplish (one state it can be used to get to)
            for i in range(random.randInt(1,5)):
                pass
                #TODO: learn the asker the relevant info
        if type(myobj) is Character:
            #TODO: say its catchphrase and attributes and up to five times either: their current location, their current goal, an item they have, a bit of history
            for i in range(random.randInt(1,5)):
                printutils.formatdialog(self.pronouns,
                pass
                #TODO: learn the asker the relevant info
        if type(myobj) is State:
            if myobj.character.name != character.name:
                printutils.formatdialog(self.pronouns,"I'm afraid you won't be able to do that at all!","explained")
            else:
                pass
                #TODO: learn the asker all inputs to this state (yes i realize a person won't always know everything about how to achieve something, but we're going to assume they do to simiplify algorithms

				
        
	
    def refuse(self):
        refusals = ["Sorry mate, I have to get going", "No way, I can't tell you that", "That's a secret", "I'd love to tell you, but oh look, my house is on fire", "I'd tell you but I'd have to kill you", "Oh look, time for my daily ritual sacrifice", "I'm afraid you're not paying me nearly enough to know that. Nor are you attractive enough", "No way. I know people like you can't keep a secret", "You want the truth? You can't handle the truth", "Nope, sorry", "Not on your life", "If the king can't know, then you can't either", "Crossed my heart and hoped to die if I ever told. I also shook my bottom because I got 'em", "I don't think I could live with myself if you knew","Sure, I'll tell you...nope, changed my mind","I swore to the gods above to never tell"] #and so on #TODO Add more of these refusals
        excuse = random.choice(refusals)
        printutils.formatdialog(self.pronouns,excuse,"replied")

    
    #TODO name him/herself and give a random event from his/her history
    def introduce(self):
        greeting = random.choice(["Greetings, traveler", "Yo", "Hello, friend", "Oy, fancy meeting you here", "Sup", "Bonjour", "Hola", "Duuuuuude", "HODOR", "Lfhaifsodif", "My oh my, lovely to meet you", "How YOU doin'", "Fancy a cuppa", "Who are you", "Top of the morning to you,", "Privet", "Zdorovat'sya", "Hallo", "Zvat'", "Oklikat'", "Hey", "Ahoy", "Aey", "V chem delo?", "How's it going?", "Hey sexy", "Well, look who's here", "Do I know you?", "Hey Jamie. It is Jamie, right?", "Genya! I haven't seen you in forever", "Oh, sorry. I thought you were someone else", "Can I bum a cig off you?", "Hey pal, do you have a few bucks?", "Have I see you somewhere before?", "Howdy", "What's a nice person like you doing in a place like this?", "What are you doing here?", "Good day to you", "Nice to meet you", "Salutations"])
        introduction = random.choice(["I am #name. #catchphrase", "You may call me #name. #catchphrase", "You're probably wondering who I am. I am #name. #catchphrase", "#catchphrase. I am #name", "#name's the name. #catchphrase", "Good to meetcha. I'm #name", "You don't know me? Oh right, you don't. I'm #name","I'm #name. As I like to say, #catchphrase"])
        introduction = introduction.replace("#name", self.name)
        introduction = introduction.replace("#catchphrase", self.catchphrase)
		printutils.formatdialog(self.pronouns,introduction,"said")
    
    #TODO say a random exclamation
    def exclaim(self):
        if self.mood_goodbad > -1:
            exclamation = random.choice(["Willickers!", "Wahoo!", "W00t!", "Bless your heart!", "Oh my god!", "Oh my goodness!", "Oooh.", "Cheers!", "Praise Helix!", "Yay!", "Woohoo!", "Golly gee!", "Wheeee~!", "Shiny!", "All glory to the Hypnotoad!", "Neato!", "Yesssss!!!", "Excellent!", "Great!"])
        else:
            exclamation = random.choice(["Fuck this!", "Shit!", "Nooooooooooooooo!", "Fuck this shit!", "Motherfucker!", "Crap!", "Oh dear!", "Aaaaaah!", "Zounds!", "God's blood!", "Fie!", "Tut", "Pooh!", "Merde!", "That sucks!", "Oh shit balls!", "Holy fish", "Damnit!", "Asscakes", "Uhoh!", "Derp!", "Balls!", "Oh no!", "Oy vey!"]) #add more of these too
        printutils.formatdialog(self.pronouns,exclamation,"exclaimed")
		
    def go(self):
        self.location.move_along(self,route)
        
    #TODO do something related to mood. come up with more emotes.
    #TODO if mood_goodbad is high, medium, low--set emote equal to something appropriate to mood
    def emote(self):
        if self.mood_goodbad > 1 and self.mood_energy > 1: #happy and with energy
            emote = random.choice(["A large grin filled #name's face", "#name's laugh filled the area", "#name smiled", "#name grinned", "#name bounced in place", "#name drummed to the beat of a familiar song", "#name did some vigorious jazz hands"])
        elif self.mood_goodbad < -1 and self.mood_energy < -1: # unhappy and low energy
            emote = random.choice(["#name kicked a rock several feet ahead", "#name sighed deeply and stared at the ground", "#name frowned", "A grimace appeared on #name's face", "#name turned away", "name stared into the distance"])
        elif self.mood_goodbad < 2 and self.mood_energy > 1: # unhappy and high energy
            emote = random.choice(["#name was busy finger drumming", "#name rocked from side to side", "#name adjusted #spos shirt", "#name looked around nervously", "#name tapped a tune with a stick", "#name shifted weight from one foot to the other", ])
        else: # happy but low energy
            emote = random.choice(["#name looked ahead", "#name stared", "#name blinked", "#name swayed from side to side", "#name pushed back a lock of hair", "A forced grin appeared on #name's face", "#name managed a smile", "#name leaned back", ])
        emote = emote.replace("#name", self.name)
        emote = emote.replace("#pos", self.pronouns) #TODO: Add lots more of these

    def goodbye(self):
        farewell = random.choice(["Here's to you, kid", "Au revoir", "May Helix be with you", "Stay thirsty, my friend", "Live long and prosper", "May your genitals never be cursed off by an evil item", "Don't let the boogeyman get you", "Say hi to your mom for me", "Fare thee well", "Adieu", "So long and thanks for all the fish", "So long and may you die before you pass a kidney stone", "Zod be with you", "May Avandre bring you luck", "Baty blesses you", "I hope you get the bastard", "Y'all come back, ya hear", "Go face your next challenge", "See you around", "Stay alive", "Good night and good luck", "Peace", "Peace out", "Peach out", "God bless", "May your life be long and interesting", "Why don't you come up and see me sometime?"])
        printutils.formatdialog(self.name,farewell,"said")
    
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
            
        if success and item.name not in keys(self.items) and (len(self.items) < capacity or 'Bag of Holding' in keys(self.items)):
            printutils.print_single("#sub took the "+item.name+" from "+character.name+".")
            self.items[item.name]=item
            self.knowledge['items'][item.name]=item
            if len(self.items)>capacity:
                bag = self.items['Bag of Holding']
                moveitem = self.least_useful_item()
                if moveitem==item:
                    printutils.print_single("#sub couldn't find a way to carry or wear it, so #sub put it in #spos Bag of Holding.",self.pronouns)
                else:
                    printutils.print_single("#sub couldn't find a way to carry or wear it, so #sub put the "+moveitem.name+" in #spos Bag of Holding to make some space.",self.pronouns)
                bag.add_subitem(moveitem)
                self.items.remove(moveitem)
        else if success and item.name not in keys(items):
            self.leave(self.least_useful_item())
        
    def catch_thief(self):
        warning = random.choice(["You'll pay if you do that again", "Hope you like the pokey", "You get a warning this time. Don't make me warn you again", "I'll let you go this time, but you better not be here when my big brother gets here", "STOP THIEF!", "Joke's on you. That one's a fake", "If I ever see your face again, I'm gonna give you an icepick lobotomy","Drop it and put your hands up"]) #TODO: Add more of these
        printutils.formatdialog(self.pronouns,warning,"growled")
    
    def offer(self,character,item):
        blahblah = random.choice(["I think you should have this #item","Take this #item. It could be useful","Well, I guess you can have this #item, then","It's dangerous to go alone! Take this #item","Hmm, you seem pretty okay, I guess. I have this old #item if you want it","Take this #item and get! I've got work to do","You could probably use this #item better than I can","If I let you have this #item, will you get out of my hair?","You must really want this #item. Fine, take it"])
        blahblah.replace("#item",item.name)
        printutils.formatdialog(self.pronouns,blahblah,"offered")
        offered_item[character.name] = item

    def offering(self,character,item):
        return offered_item[character.name] is item
        
    #TODO: decide which item is no longer necessary, or won't be needed soonest, or just a random item
    def least_useful_item(self):
        items = []
        tovisit = [self.root_goal]
    
        for state in tovisit: #looking at one particular state
            if type(state) is Item_State and state.item in self.items:
                if state.item in items:
                    items.remove(state.item)
                items.append(state.item)
            for v in state.input.values: #v is some list of edges
                for e in v: #now e is some particular edge
                    if e.sfrom not in tovisit:
                        tovisit.append(e.sfrom)
        if len(items)>0:
            return items[0]
        else:
            #TODO: it would be smarter to search FORWARD from current state in this situation
            return random.choice(self.items)
        #starting with terminal goal, do a BFS of inputs, adding items to a list as their states appear. 
        #if their states appear more again, delete them and move them to the end of the list
        #when the BFS finishes, the first item on this list should be the one that is least likely to be needed soon
        
    def pick_up(self,item):
        success = (item in self.location.items)
        if success and item.name not in keys(self.items) and (len(self.items) < capacity or 'Bag of Holding' in keys(self.items)):
            printutils.print_single("#sub grabbed the "+item.name+".")
            self.items[item.name]=item
            self.knowledge['items'][item.name]=item
            if len(items)>capacity:
                bag = items['Bag of Holding']
                moveitem = self.least_useful_item()
                if moveitem==item:
                    printutils.print_single("#sub couldn't find a way to carry or wear it, so #sub put it in #spos Bag of Holding.",self.pronouns)
                else:
                    printutils.print_single("#sub couldn't find a way to carry or wear it, so #sub put the "+moveitem.name+" in #spos Bag of Holding to make some space.",self.pronouns)
                bag.add_subitem(moveitem)
                items.remove(moveitem)
        else if success and item.name not in keys(self.items):
            self.leave(least_useful_item())
        if success: 
            items[item.name]=item
            self.location.delete_item(item)
        
    def leave(self,item):
        printutils.print_single("#sub tossed the "+item.name+" aside.",self.pronouns)
        if item.name in keys(self.items):
            self.items.remove(item)
            self.location.add_item(item)
            item.location = self.location
            item.owner = None
            self.learn(item,['location', 'owner', 'subitems'])
            
    def use(self,item):
        if item.name in keys(items):
            item.use()
            
    #obj is a State, Item, Location, or Character
    def ask(self,character,obj):
		#TODO: phrase information request sensibly
		#Do you know anything about ...?
        queries = random.choice(["Do you know anything about #thing?", "What do you know about #thing?", "What can you tell me about #thing?", "I beg you. Can you tell me about #thing?", "I don't mean to bother you, but would you please tell me about #thing?", "What would it take to convince you to tell me about #thing?", "Excuse me, do you know a thing or two about #thing?", "Could I bribe you to tell me about #thing?", "May I inquire about #thing?"]) #TODO Add more of these
        queries.replace("#thing", obj.name)
        printutils.formatdialog(self.pronouns, queries, "asked")
		character.tell(self,obj)
        
        
