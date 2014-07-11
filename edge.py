# -*- coding: utf-8 -*-
class Edge:
    on = False
    #whether the edge "sticks", what action it comes from, what state it goes to
    def __init__(self,permanent=False,sfrom,sto):
        self.permanent = permanent
        self.sfrom = sfrom
        self.sto = sto
        
    def is_on(self):
        if self.on and not self.permanent and not self.sfrom.is_on():
            self.on = False
        return self.on
        
    def update(self):
        self.on=true
        