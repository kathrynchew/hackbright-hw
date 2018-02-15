### Find all animals in the list that start with K ###
animals = ["Scarabaeus sacer", "Chrysaora quinquicirrha", "Aneides lugubris", "Australopithecus boisei", "Cordylobia anthropophaga", "Solpugassa furcifera", "Kalyptodoras bahiensis", "Anabrus simplex", "Kluyvera cryocrescens"]


def find_k_animals():
    """Loops through a list of animals, finds all animals that start with k"""
    k_list = []

    for item in animals:
        if item[0].lower() == "k":
            k_list.append(item)

    return k_list

print find_k_animals()
