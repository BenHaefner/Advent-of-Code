total_fuel = 0

def fuelCalc(item):
    return int(item/3) - 2

with open('input.txt', 'r') as file: 
    for line in file:
        item = int(line)
        result = fuelCalc(item)
        total_fuel = total_fuel + result

print(total_fuel)
