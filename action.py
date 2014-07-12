# -*- coding: utf-8 -*-
class Action:
    # name should be a fully descriptive reference in present tense, while d_event should be an Event with the description of the thing actually happening in past tense
    #for instance name would be "grab the Sword of Penetration"
    #while d_event is an Event with "#sub grabbed the sword and tilted it until it broke free from the cleft, then hefted it above #pos head to watch it shine in the sun. #sub tied the hilt to #pos belt and stepped down determinedly."
    #p_success is probability of success
    #sform is state which holds/allows this action
    def __init__(self, name, success_event, failure_event, p_success, sfrom):
        self.name = name
        self.d_event = d_event
        self.p_success = p_success
        self.edges = []
        
    def add_edge(self,edge):
        self.edges.append(edge)
        
    def perform(self):
        import random
        if random.random() < p_success:
            success_event.trigger()
            for edge in edges:
                edge.update()
        else:
            failure_event.trigger()
            
        
    