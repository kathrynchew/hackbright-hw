### TRANSLATOR EXERISE ###
deutsch_dict = {
    "bread": "Brot",
    "vegetable": "Gemuese",
    "chocolate": "Schokolade",
    "schnitzel": "Schnitzel",
    "pork": "Schwein",
    "potato": "Kartoffel",
    "orange": "Orange",
    "apple": "Apfel",
    "pasta": "Nudeln",
    "chicken": "Haehnchen",
    "celery": "Sellerie",
    "milk": "Milch",
    "cheese": "Kaese"
}


def translate(word):
    """Takes in a food related word in English returns German translation
    If the word is not in the dictionary, returns an error message"""
    if word in deutsch_dict:
        return deutsch_dict[word]
    else:
        return "ERROR: That word does not exist in the dictionary"

yes_in_dict = translate("potato")
print "The German word for potato is {}.".format(yes_in_dict)

not_in_dict = translate("ramen")
print "The German word for ramen is [{}].".format(not_in_dict)
