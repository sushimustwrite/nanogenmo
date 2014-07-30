# -*- coding: utf-8 -*-
class State:
    triggered = False
    def __init__(self,name,namepast,character, event_arrival=None):
        #name should be statable as a goal to be achieved, such as "make the princess marry me" or "get the Sword of Penetration"
        self.name = name
        #namepast should be statable as a goal achieved/fact about the world which can follow a form of "to be", such as "married to the princess" or "carrying the Sword of Penetration"
        self.namepast = namepast
        #character which can achieve this state (exactly one character can achieve a state, so we add multiple states to the big graph if more than one character could potentially achieve it: one for each character, and if it is mutually exclusive, we negate it for any other characters at that time
        self.character = character
        #event that triggers the first time this state is reached
        self.event_arrival = event_arrival
        #positive actions are those that can be taken when this state is on
        self.postiveactions = []
        #negative actions are those that can be taken when this state is off
        self.negativeactions = []
        #inputs are lists of edges
        self.inputs = {}
        #same
        self.negatedinputs = {}
        #whether the arrival event has triggered
    
    def add_action(self, actionobject, negative=False):
        if negative:
            negativeactions.append(actionobject)
        else:
            positiveactions.append(actionobject)
            
    #every input has a name that is purely for programmer use, to make it easier to plug the edges into the right place.
    #input edges should be added in the order their corresponding actions should be taken
    def add_input(self, name, edgeobject, negated=False)
        if negated:
            if not self.negatedinputs.has_key(name):
                self.negatedinputs[name]=[]
            self.negatedinputs[name].append(edgeobject)
        else:
            if not self.inputs.has_key(name):
                self.inputs[name]=[]
            self.inputs[name].append(edgeobject)
    
    #check if any of the inputs is satisfied and none of the negated inputs are satisfied
    def is_on(self):
        for conj in self.inputs.values():
            on = True
            for edge in conj:
                on = on and edge.is_on()
            if on:
                break
        if not on:
            return False
        cancel = self.is_canceled()
        if cancel:
            return False
        if not triggered:
            triggered = True
            event_arrival.trigger()
        return True
        
    def get_action_for(self, edge):
        for action in positiveactions:
            for x in action.edges:
                if edge is x:
                    return action
                    
    def get_negative_action_for(self, edge):
        for action in negativeactions:
            for x in action.edges:
                if edge is x:
                    return action
        
    def get_required_action(self):
        if self.is_on():
            return None
        for conj in self.inputs.values():
            on = True
            action_to_take = None
            for edge in conj:
                on = on and (edge.is_on() or edge.sfrom.is_on())
                if action_to_take is None and not edge.is_on():
                    action_to_take = get_action_for(edge)
            if on: #we should not be here unless there is an action to be taken
                return action_to_take
        return None
    
    def get_required_off_action(self):
        if not self.is_on():
            return None
        for conj in self.negativeinputs.values():
            on = True
            action_to_take = None
            for edge in conj:
                on = on and (edge.is_on() or edge.sfrom.is_on())
                if action_to_take is None and not edge.is_on():
                    action_to_take = get_negative_action_for(edge)
            if on: #we should not be here unless there is an action to be taken
                return action_to_take
        return None
    
    def is_canceled(self):
        for conj in self.negatedinputs.values():
            cancel = True
            for edge in conj:
                cancel = cancel and edge.is_on()
            if cancel:
                break
        return cancel

class Location_State(State):
    def __init__(self, character, location, event_arrival=None):
        super(Location_State,self).__init__("get to "+location.name,"in "+location.name,character,event_arrival=None)
        self.location = location
        
    def is_on(self):
        return character in location.characters_present and super(Location_State,self).is_on()
        
class Sticky_State(State):
    def __init__(self, name, namepast, character, event_arrival=None):
        super(Location_State,self).__init__(name,namepast,character,event_arrival)
    
    def is_on(self):
        return self.triggered or super(Sticky_State,self).is_on()
        
class Item_State(State):
    def __init__(self, character, item, event_arrival=None):
        super(Item_State,self).__init__("get the "+item.name,"carrying the "+item.name,character,event_arrival)
        self.item = item
        
    def is_on(self):
        return item in character.items and super(Location_State,self).is_on()
        
    