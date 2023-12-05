import csv

url = "data\day1.csv"

def number_collector(line):
    values = [letter for letter in line[0] if letter.isdigit()]
    values = [values[0],values[-1]]
    values = int("".join(values))
    print(values)
    return values

with open(url) as file:
    reader = csv.reader(file)
    numbers = [number_collector(line) for line in reader]
    print(sum(numbers))
