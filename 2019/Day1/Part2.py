total_fuel = 0

def fuelCalc(item):
    return int(item/3) - 2

with open('input.txt', 'r') as file: 
    for line in file:
        item = int(line)
        check = fuelCalc(item)
        while check > 0:
            item = check
            check = fuelCalc(item)
            total_fuel = total_fuel + item

print(total_fuel)
