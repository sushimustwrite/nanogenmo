# -*- coding: utf-8 -*-
def print_single(string,character):
    string.replace('#sub',character.pronouns['subject'])
    string.replace('#spos',character.pronouns['subj_possess'])
    string.replace('#opos',character.pronouns['obj_possess'])
    string.replace('#obj',character.pronouns['object'])
    string.replace('#ref',character.pronouns['reflex'])
    print string
    
def print_double(string, character1, character2):
    string.replace('#sub1',character1.pronouns['subject'])
    string.replace('#sub2',character2.pronouns['subject'])
    string.replace('#spos1',character1.pronouns['subj_possess'])
    string.replace('#spos2',character2.pronouns['subj_possess'])
    string.replace('#opos1',character1.pronouns['obj_possess'])
    string.replace('#opos2',character2.pronouns['obj_possess'])
    string.replace('#obj1',character1.pronouns['object'])
    string.replace('#obj2',character2.pronouns['object'])
    string.replace('#ref1',character1.pronouns['reflex'])
    string.replace('#ref2',character2.pronouns['reflex'])