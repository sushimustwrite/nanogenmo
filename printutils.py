# -*- coding: utf-8 -*-
import re
import sys

def multiple_replacer(*key_values):
    replace_dict = dict(key_values)
    replacement_function = lambda match: replace_dict[match.group(0)]
    pattern = re.compile("|".join([re.escape(k) for k, v in key_values]), re.M)
    return lambda string: pattern.sub(replacement_function, string)
    
def pluralize(string,repl):
    pattern1 = re.compile("([sz])"+repl)
    pattern2 = re.compile("([a-rt-y])"+repl)
    return pattern2.sub(r"\1s",pattern1.sub(r"\1es",string))
    
def article(string,repl,plural):
    pattern1 = re.compile(repl+" ([aeiou])", re.I)
    pattern2 = re.compile(repl+" ([b-df-hj-np-tv-z])", re.I)
    if plural:
        return pattern2.sub(r"\1",pattern1.sub(r"\1",string))
    else:
        return pattern2.sub(r"a \1",pattern1.sub(r"an \1",string))

def multiple_replace(string, *key_values):
    pattern = re.compile("[A-Za-z]")
    capitalizer = lambda match: match.group(0).capitalize()
    return pattern.sub(capitalizer,multiple_replacer(*key_values)(string),1)

def return_single(string,pronouns,sentence=True):
    replacements = ("#sub",pronouns['subject']), ("#spos", pronouns['subj_possess']), ("#opos", pronouns['obj_possess']), ("#obj",pronouns['object']), ("#ref", pronouns['reflex']), ("#tobe", pronouns['tobe'])
    string = multiple_replace(string, *replacements)
    if pronouns['plural']: 
        string = pluralize(string,"#plu")
    else:
        string = string.replace("#plu","")
    string = article(string,"#art",pronouns['plural'])
    if sentence:
        if string[-1] in ['.','!','?','"']:
            string += " "
        else:
            string += ". "
    return string
    
def print_single(string,pronouns,sentence=True):
    sys.stdout.write(return_single(string,pronouns,sentence))
    
def return_double(string, pronouns1, pronouns2, sentence=True):
    if pronouns1 is not pronouns2:
        replacements = ("#sub1",pronouns1['subject']), ("#spos1", pronouns1['subj_possess']), ("#opos1", pronouns1['obj_possess']), ("#obj1",pronouns1['object']), ("#ref1", pronouns1['reflex']), ("#tobe1", pronouns1['tobe']), ("#sub2",pronouns2['subject']), ("#spos2", pronouns2['subj_possess']), ("#opos2", pronouns2['obj_possess']), ("#obj2",pronouns2['object']), ("#ref2", pronouns2['reflex']), ("#tobe2", pronouns2['tobe'])
    else:
        if not pronouns1['plural']:
            replacements = ("#sub1","the former"), ("#spos1", "the former's"), ("#opos1", "the former's"), ("#obj1","the former"), ("#ref1", pronouns1['reflex']), ("#tobe1", "the former was"), ("#sub2","the latter"), ("#spos2", "the latter's"), ("#opos2", "the latter's"), ("#obj2","the latter"), ("#ref2", pronouns2['reflex']), ("#tobe2", "the latter is")
        else:
            replacements = ("#sub1","the former"), ("#spos1", "the former's"), ("#opos1", "the former's"), ("#obj1","the former"), ("#ref1", pronouns1['reflex']), ("#tobe1", "the former was"), ("#sub2","the latter"), ("#spos2", "the latter's"), ("#opos2", "the latter's"), ("#obj2","the latter"), ("#ref2", pronouns2['reflex']), ("#tobe2", "the latter are")
    string = multiple_replace(string, *replacements)
    if pronouns1['plural']:
        string=pluralize(string,"#plu1")
    else:
        string=string.replace("#plu1","")
    if pronouns2['plural']:
        string=pluralize(string,"#plu2")
    else:
        string=string.replace("#plu2","")
    string = article(string,"#art1",pronouns1['plural'])
    string = article(string,"#art2",pronouns2['plural'])
    if sentence:
        if string[-1] in ['.','!','?','"']:
            string += " "
        else:
            string += ". "
    return string
    
def print_double(string, pronouns1, pronouns2, sentence=True):
    sys.stdout.write(return_double(string, pronouns1, pronouns2, sentence))
    
def formatdialog(pronouns,dialog,verb=None):
    if verb is None:
        sys.stdout.write("\""+dialog+"\" ")
    else:
        if dialog[-1]=="!" or dialog[-1] == "?":
            sys.stdout.write("\"{0}\" {1} {2}. ".format(dialog,pronouns['subject'],verb))
        else:
            sys.stdout.write("\"{0},\" {1} {2}. ".format(dialog,pronouns['subject'],verb))
        
def new_paragraph():
    print "\n\t"

masculine = {'subject':'he','object':'him','subj_possess':'his','obj_possess':'his','reflex':'himself','tobe':'he\'s','plural':False}
feminine = {'subject':'she','object':'her','subj_possess':'her','obj_possess':'hers','reflex':'herself','tobe':'she\'s','plural':False}
neuter = {'subject':'it','object':'it','subj_possess':'its','obj_possess':'its', 'reflex':'itself','tobe':'it\'s','plural':False}
neutral = {'subject':'ze','object':'hir','subj_possess':'hir','obj_possess':'hirs','reflex':'hirself', 'tobe':'ze\'s','plural':False}
first_singular = {'subject':'I','object':'me','subj_possess':'my','obj_possess':'mine','reflex':'myself', 'tobe':'I\'m','plural':False}
first_plural = {'subject':'we','object':'us','subj_possess':'our','obj_possess':'ours','reflex':'ourselves', 'tobe':'we\'re','plural':True}
second_singular = {'subject':'you','object':'you','subj_possess':'your','obj_possess':'yours','reflex':'yourself', 'tobe':'you\'re','plural':True}
second_plural = {'subject':'you','object':'you','subj_possess':'your','obj_possess':'yours','reflex':'yourselves', 'tobe':'you\'re', 'plural':True}
third_plural = {'subject':'they','object':'them','subj_possess':'their','obj_possess':'theirs','reflex':'themselves', 'tobe':'they\'re', 'plural':True}

if __name__=="__main__":
    print_single("#sub couldn't find a way to carry or wear it, so #sub put it in #spos Bag of Holding.",masculine)
    print_single("#sub couldn't find a way to carry or wear it, so #sub put it in #spos Bag of Holding.",feminine)
    print_single("#sub couldn't find a way to carry or wear it, so #sub put it in #spos Bag of Holding.",neuter)
    print_single("#sub couldn't find a way to carry or wear it, so #sub put it in #spos Bag of Holding.",neutral)
    print_single("#sub couldn't find a way to carry or wear it, so #sub put it in #spos Bag of Holding.",first_singular)
    print_single("#sub couldn't find a way to carry or wear it, so #sub put it in #spos Bag of Holding.",first_plural)
    print_single("#sub couldn't find a way to carry or wear it, so #sub put it in #spos Bag of Holding.",second_singular)
    print_single("#sub couldn't find a way to carry or wear it, so #sub put it in #spos Bag of Holding.",third_plural)
    new_paragraph()
    formatdialog(masculine,return_single("You don't know #obj? Oh right, you don't. ",first_singular,False)+return_single("#tobe #art Bad-Ass Motherfucker#plu",first_singular, False)+"!","exclaimed")
    formatdialog(masculine,return_single("So, yeah, now you know #obj!",first_singular,False))
    new_paragraph()
    formatdialog(third_plural,return_single("You don't know #obj? Oh right, you don't. ",first_plural, False)+return_single("#tobe #art Bad-Ass Motherfucker#plu",first_plural, False),"said")
    formatdialog(third_plural,return_single("So, yeah, now you #obj!",first_plural,False))
    new_paragraph()
    print_double("#sub1 did it for #obj2 because #sub2 could not do #spos2 task for #ref2.", masculine, feminine)
    print_double("#sub1 did it for #obj2 because #sub2 could not do #spos2 task for #ref2.", feminine, third_plural)
    print_double("#sub1 did it for #obj2 because #sub2 could not do #spos2 task for #ref2.", feminine, feminine)
    new_paragraph()