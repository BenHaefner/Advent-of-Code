total_fuel = 0

with open('input.txt', 'r') as file: 
    for line in file:
        item = int(line)
        check = 1
        while check > 0:
            item = int(item/3) - 2
            total_fuel = total_fuel + item
            check = int(item/3) - 2

print(total_fuel)
