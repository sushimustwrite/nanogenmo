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

masculine = {'subject':'he','object':'him','subj_possess':'his','obj_possess':'his','reflex':'himself'}
feminine = {'subject':'she','object':'her','subj_possess':'her','obj_possess':'hers','reflex':'herself'}
neuter = {'subject':'it','object':'it','subj_possess':'its','obj_possess':'its', 'reflex':'itself'}
neutral = {'subject':'ze','object':'hir','subj_possess':'hir','obj_possess':'hirs','reflex':'hirself'}
first_singular = {'subject':'I','object':'me','subj_possess':'my','obj_possess':'mine','reflex':'myself'}
first_plural = {'subject':'we','object':'us','subj_possess':'our','obj_possess':'ours','reflex':'ourselves'}
second_singular = {'subject':'you','object':'you','subj_possess':'your','obj_possess':'yours','reflex':'yourself'}
second_plural = {'subject':'you','object':'you','subj_possess':'your','obj_possess':'yours','reflex':'yourselves'}
third_plural = {'subject':'they','object':'them','subj_possess':'their','obj_possess':'theirs','reflex':'themselves'}