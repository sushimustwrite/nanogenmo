# dolga's randomized o's
# replace dolga with appropriate character dict

import random, string

def dolgo_replace(search_string):
    search_query = "Dolgo"
    for search_query in search_string:
        search_string = search_string.replace("Dolgo", "D"+"o"*random.randint(3,20)+"lgo ", 1)
    print search_string

dolgo_replace("Dolgo your mom Dolgo protagodolgo rawr Dolgo Dolgo Dolgo alalala") 
