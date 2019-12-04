import numpy as np

line1Path = []
line2Path = []
line1Visted= []
line2Visted= []

def traversePathLine1(path):
    x = 0
    y = 0
    print('Traversing line 1...')
    for instruction in path:
        dirc = instruction[0]
        dist = int(instruction[1:])
        if dirc == 'R':
            for _ in range(dist): 
                x = x + 1
                line1Visted.append((x,y))

        elif dirc == 'L':
            for _ in range(dist): 
                x = x - 1
                line1Visted.append((x,y))

        elif dirc == 'U':
            for _ in range(dist): 
                y = y + 1
                line1Visted.append((x,y))

        elif dirc == 'D':
            for _ in range(dist): 
                y = y - 1
                line1Visted.append((x,y))

def traversePathLine2(path):
    x = 0
    y = 0
    print('Traversing line 2...')
    for instruction in path:
        dirc = instruction[0]
        dist = int(instruction[1:])
        if dirc == 'R':
            for _ in range(dist): 
                x = x + 1
                line2Visted.append((x,y))

        elif dirc == 'L':
            for _ in range(dist): 
                x = x - 1
                line2Visted.append((x,y))
        elif dirc == 'U':
            for _ in range(dist): 
                y = y + 1
                line2Visted.append((x,y))
        elif dirc == 'D':
            for _ in range(dist): 
                y = y - 1
                line2Visted.append((x,y))

def findIntersections(): 
    intersections = set(line1Visted) & set(line2Visted)
    manDist = abs(list(intersections)[0][0]) + abs(list(intersections)[0][1])
    for coords in intersections:
        currentDist = abs(coords[0]) + abs(coords[1])
        if currentDist < manDist:
            manDist = currentDist
    print(manDist)


with open('input.txt', 'r') as file: 
    line1Path = file.readline().split(',')
    line2Path = file.readline().split(',')

traversePathLine1(line1Path)
traversePathLine2(line2Path)
findIntersections()
