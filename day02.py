url = "data\day2.csv"


def verified():
    
    pass

with open(url) as file:
    dice = [12,13,14]
    game = [verified(line) for line in file]
    pass