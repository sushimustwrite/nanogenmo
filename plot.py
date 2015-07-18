# -*- coding: utf-8 -*-

major_characters = []
items = []

#this is a list of random encounters (Events) for the protagonist
p_rand_encounters = []
#this is a list of random encounters (Events) for the antagonist
a_rand_encounters = []

#add stuff to the plot here
#=======

#add stuff to the plot here

#CHARACTERS
#dict key is the character's name
#leave items=none for all, we'll make a note of who has items later
major_characters["Protagovitch"] = character.Character("Protagovitch", "male", "(That's #obj!)", "not very tall and not very handsome, but with a heart of gold", location=None, items=None)
protagonist = major_characters["Protagovitch"]
major_characters["Antagovitch"] = character.Character("Antagovitch", "male", "catchphrase", "tall and attractive with a hunger for power", location=None, items=None)
antagonist = major_characters["Antagovitch"]
major_characters["Protagslova"] = character.Character("Protagslova", "female", "A vos souhaits", "wavy red hair, piercing blue eyes, and a smile that melts hearts",  location=None, items=None)
major_characters["Dolga"] = character.Character("Dolga", "neutral", "That's an awfully long name. That's an awfully long dragon.", "shiny red and breathe", location=None, items="scale")
major_character["Demon"] = character.Character("Demon", "neutral", "", "carries a bright red pitchfork and is unusually cute for a demon", location=None, items=None)
major_character["Rodent of Unusual Size"] = character.Character("Rodent of Unusual Size", "neuter", "", "", location=None, items=None)
major_character["Mom"] = character.Character("Mom", "female", "Would you like a cuppa?", "", location=None, items=None)
major_character["Donovitch"] = character.Character("Donovitch", "male", "It's dangerous to go alone! Take this.", "", location=None, items=None)
major_character["Snezana"] = character.Character("Snezana", "female", "", "jet black hair, big blue eyes", location=None, items=None)
major_character["Baba Yaga"] = character.Character("Baba Yaga", "female", "", "", location=None, items=None)
major_character["Hammerhead Shark"] = character.Character("Hammerhead Shark", "neuter", "You look like a nail.", "", location=None, items=None)
major_character["Crab King"] = character.Character("Crab King", "male", "Crabhammer!!!", "the largest of the crabs", location=None, items=None)
major_character["Firebird"] = character.Character("Firebird", "female", "born of ash", "red fiery wings and a long beak that can peck through anything", location=None, items=None)
major_character["Shtativ the Three-Legged Ghost"] = character.Character("Shtativ the Three-Legged Ghost", "male", "Are you scared yet?", "perfectly ordinary except for a third leg and that whole ghost thing", location=None, items=None)
major_character["Pesoky the Sandworm"] = character.Character("Pesoky the Sandworm", "neuter", "", "", location=None, items=None)
major_character["Vila the Vila"] = character.Character("Vila the Vila", "female", "", "", location=None, items=None)
major_character["Pauk the Giant Spider"] = character.Character("Pauk the Giant Spider", "neuter", "The stench and the dread.", "big hairy spider with eight long legs", location=None, items=None)
major_character["Psoglav"] = character.Character("Psoglav", "male", "", "", location=None, items=None)
major_character["Hag of Odinokorod"] = character.Character("Hag of Odinokorod", "female", "", "", location=None, items=None)
major_character["King Odinovski the First"] = character.Character("King Odinovski the First", "male", "", "", location=None, items=None)
major_character["King Dvaski the Second"] = character.Character("King Dvaski the Second", "male", "Hope you like it hot.", "", location=None, items=None)
major_character["Queen Triski the Third"] = character.Character("Queen Triski the Third", "female", "Ditto.", "", location=None, items=None)
major_character["King Chetyrski the Fourth"] = character.Character("King Chetyrski the Fourth", "male", "", "", location=None, items=None)
major_character["Quing Pyatski the Fifth"] = character.Character("Quing Pyatski the Fifth", "neutral", "", "", location=None, items=None)
major_character["Queen Shestski the Sixth"] = character.Character("Queen Shestski the Sixth", "female", "Up on Cloud Nine", "", location=None, items=None)
major_character["Centaurskaya"] = character.Character("Centaurskaya", "female", "Mars is bright tonight.", "", location=None, items=None)
major_character["Karzelek the Dwarf"] = character.Character("Karzelek the Dwarf", "male", "Where's Snezana?", "", location=None, items=None)
major_character["Ziz"] = character.Character("Ziz", "neutral", "", "", location=None, items=None)
major_character["Troll"] = character.Character("Troll", "male", "", "", location=None, items=None)
major_character["Goat King"] = character.Character("Goat King", "male", "", "", location=None, items=None)
major_character["Werewolf"] = character.Character("Werewolf", "male", "", "", location=None, items=None)
major_character["Vucagorod"] = character.Character("Vucagorod", "male", "", "", location=None, items=None)
major_character["Gamayun the Bird"] = character.Character("Gamayun the Bird", "female", "Wings and breasts, just like chicken", "half-bird, half-woman with all the best features of both", location=None, items=None)

#STATE GRAPH
states = {
    


    }

#LOCATIONS
#name, attributes, state, catchphrase?, sublocations?
doma_village = [
    
    ]
protag_house = [

    ]
doma_meadow = [

    ]
oblako = [

    ]
zapovednik = [

    ]
prizrak = [

    ]
barbistan = [

    ]
castle_zamok = [

    ]
glubok = [

    ]
magorod = [

    ]
odinokorod = [

    ]
shrifta = [

    ]
locations = [
    Location("Doma Village", "A peaceful little hamlet near the river Drugoy. Known for hay and goats.", states['Doma Village'], "Everybody's somebody in Doma Village! Even the goats!", doma_village),
    Location("Doma Meadow", "A series of rolling hills, often covered in wildflowers, surrounding a strange mound of boulders.", states['Doma Meadow'], "It's more interesting to look at from a distance than it is to visit.", doma_meadow),
    Location("Oblako", "A village of tiny bamboo houses backed up to a dark and mysterious wilderness. Famed for its sex dungeon.", states['Oblako'], "What happens in Oblako stays in Oblako.", oblako),
    Location("Zapovednik Forest", "Very dark. Very mysterious.", states['Zapovednik Forest'], "No one goes in there, because no one wants to ruin the mystery.", zapovednik),
    Location("Prizrak Forest", "A thousand miles long, with trees upwards of 100 feet tall.", states['Prizrak Forest'], "Some say it's haunted.", prizrak),
    Location("The Distant Kingdom of Barrrrbistan", "It overflows with money and thieves.", states['Barbistan'], "It arrrren't for landlubbers!", barbistan),
    Location("Castle Zamok", "Within its walls are the seven castles of the seven emperors of Zamok, each more evil than the others. Those who have passed beyond its walls and returned say that everything there is impossible.", states['Zamok Castle'], "All hail the Emperors of Zamok!", castle_zamok),
    Location("Glubok Sea", "The Zhidky River flows into it, and beyond it lies only the Edge of the World. Below its surface lie other mysteries entirely.", states['Glubok Sea'], "Who knows what lies beneath its waves?", glubok),
    ]
locations.extend(doma_village)
locations.extend(protag_house)
locations.extend(doma_meadow)
locations.extend(oblako)
locations.extend(zapovednik)
locations.extend(prizrak)
locations.extend(barbistan)
locations.extend(castle_zamok)
locations.extend(glubok)
locations.extend(magorod)
locations.extend(odinokorod)
locations.extend(shrifta)