# -*- coding: utf-8 -*-
def return_single(string,pronouns):
    string = string.replace('#sub',pronouns['subject'])
    string = string.replace('#spos',pronouns['subj_possess'])
    string = string.replace('#opos',pronouns['obj_possess'])
    string = string.replace('#obj',pronouns['object'])
    string = string.replace('#ref',pronouns['reflex'])
    return string
    
def return_double(string, pronouns1, pronouns2):
    string = string.replace('#sub1',pronouns1['subject'])
    string = string.replace('#sub2',pronouns2['subject'])
    string = string.replace('#spos1',pronouns1['subj_possess'])
    string = string.replace('#spos2',pronouns2['subj_possess'])
    string = string.replace('#opos1',pronouns1['obj_possess'])
    string = string.replace('#opos2',pronouns2['obj_possess'])
    string = string.replace('#obj1',pronouns1['object'])
    string = string.replace('#obj2',pronouns2['object'])
    string = string.replace('#ref1',pronouns1['reflex'])
    string = string.replace('#ref2',pronouns2['reflex'])
    return string
