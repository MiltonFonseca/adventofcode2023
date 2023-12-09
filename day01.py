path = "./data/day1.txt"

def number_collector(line):
    values = [letter for letter in line if letter.isdigit()]  
    values = [values[0],values[-1]]
    values = int("".join(values))

    print(values)
    return values

with open(path) as file:
    reader = file.readlines()
    numbers = [number_collector(line) for line in reader]
    print(sum(numbers))
