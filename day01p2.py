path = "./data/day01.txt"

def number_collector(line):
    digits = {"twone":"21",
            "eightwo":"82",
            "eighthree":"83",
            "oneight":"18",
            "threeight":"38",
            "sevenine":"79",
            "one":"1",
            "two":"2",
            "three":"3",
            "four":"4",
            "five":"5",
            "six":"6",
            "seven":"7",
            "eight":"8",
            "nine":"9"
            }
    
    for key in digits:
        line = line.replace(key,digits[key])

    values = [letter for letter in line if letter.isdigit()]  
    values = [values[0],values[-1]]
    values = int("".join(values))

    return values

with open(path) as file:
    reader = file.readlines()
    numbers = [number_collector(line) for line in reader]
    print(sum(numbers))
