# -*- coding: utf-8 -*-
import re

def multiple_replacer(*key_values):
    replace_dict = dict(key_values)
    replacement_function = lambda match: replace_dict[match.group(0)]
    pattern = re.compile("|".join([re.escape(k) for k, v in key_values]), re.M)
    return lambda string: pattern.sub(replacement_function, string)
    
def multiple_replace(string, *key_values):
    return multiple_replacer(*key_values)(string)
    
def return_single(string,pronouns):
    replacements = ("#sub",pronouns['subject']), ("#spos", pronouns['subj_possess']), ("#opos", pronouns['obj_possess']), ("#obj",pronouns['object']), ("#ref", pronouns['reflex'])
    return multiple_replace(string, *replacements).title()+" "
	
def print_single(string,pronouns):
	print return_single(string,pronouns)+
    
def return_double(string, pronouns1, pronouns2):
    replacements = ("#sub1",pronouns1['subject']), ("#spos1", pronouns1['subj_possess']), ("#opos1", pronouns1['obj_possess']), ("#obj1",pronouns1['object']), ("#ref1", pronouns1['reflex']), ("#sub2",pronouns2['subject']), ("#spos2", pronouns2['subj_possess']), ("#opos2", pronouns2['obj_possess']), ("#obj2",pronouns2['object']), ("#ref2", pronouns2['reflex'])
    return multiple_replace(string, *replacements).title()+" "
    
def print_double(string, pronouns1, pronouns2):
    print return_double(string, pronouns1, pronouns2)
	
def formatdialog(pronouns,dialog,verb):
    if dialog[-1]=="!":
        print "\n\t\"{0}\" {1} {2}.\n".format(dialog,pronouns['subject'],verb)
    else:
        print "\n\t\"{0},\" {1} {2}.\n".format(dialog,pronouns['subject'],verb)

masculine = {'subject':'he','object':'him','subj_possess':'his','obj_possess':'his','reflex':'himself'}
feminine = {'subject':'she','object':'her','subj_possess':'her','obj_possess':'hers','reflex':'herself'}
neuter = {'subject':'it','object':'it','subj_possess':'its','obj_possess':'its', 'reflex':'itself'}
neutral = {'subject':'ze','object':'hir','subj_possess':'hir','obj_possess':'hirs','reflex':'hirself'}
first_singular = {'subject':'I','object':'me','subj_possess':'my','obj_possess':'mine','reflex':'myself'}
first_plural = {'subject':'we','object':'us','subj_possess':'our','obj_possess':'ours','reflex':'ourselves'}
second_singular = {'subject':'you','object':'you','subj_possess':'your','obj_possess':'yours','reflex':'yourself'}
second_plural = {'subject':'you','object':'you','subj_possess':'your','obj_possess':'yours','reflex':'yourselves'}
third_plural = {'subject':'they','object':'them','subj_possess':'their','obj_possess':'theirs','reflex':'themselves'}