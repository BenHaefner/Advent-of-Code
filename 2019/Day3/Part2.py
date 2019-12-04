line1Path = []
line2Path = []
line1Visted= []
line2Visted= []
line1Dict = {}
line2Dict = dict({})

def traversePathLine1(path):
    x = 0
    y = 0
    steps = 0
    print('Traversing line 1...')
    for instruction in path:
        dirc = instruction[0]
        dist = int(instruction[1:])
        if dirc == 'R':
            for _ in range(dist): 
                x = x + 1
                steps = steps+1
                line1Visted.append((x,y))
                line1Dict[(x,y)] = steps
        elif dirc == 'L':
            for _ in range(dist): 
                x = x - 1
                steps = steps+1
                line1Visted.append((x,y))
                line1Dict[(x,y)] = steps
        elif dirc == 'U':
            for _ in range(dist): 
                y = y + 1
                steps = steps+1
                line1Visted.append((x,y))
                line1Dict[(x,y)] = steps
        elif dirc == 'D':
            for _ in range(dist): 
                y = y - 1
                steps = steps+1
                line1Visted.append((x,y))
                line1Dict[(x,y)] = steps

def traversePathLine2(path):
    x = 0
    y = 0
    steps = 0
    print('Traversing line 2...')
    for instruction in path:
        dirc = instruction[0]
        dist = int(instruction[1:])
        if dirc == 'R':
            for _ in range(dist): 
                x = x + 1
                steps = steps+1
                line2Visted.append((x,y))
                line2Dict[(x,y)] = steps
        elif dirc == 'L':
            for _ in range(dist): 
                x = x - 1
                steps = steps+1
                line2Visted.append((x,y))
                line2Dict[(x,y)] = steps

        elif dirc == 'U':
            for _ in range(dist): 
                y = y + 1
                steps = steps+1
                line2Visted.append((x,y))
                line2Dict[(x,y)] = steps

        elif dirc == 'D':
            for _ in range(dist): 
                y = y - 1
                steps = steps+1
                line2Visted.append((x,y))
                line2Dict[(x,y)] = steps

def findIntersections(): 
    intersections = set(line1Visted) & set(line2Visted)
    lowestSteps = line1Dict.get(list(intersections)[0]) + line2Dict.get(list(intersections)[0])
    for coords in intersections:
        currentSteps1 = line1Dict.get(coords)
        currentSteps2 = line2Dict.get(coords)
        currentSteps = currentSteps1 + currentSteps2
        if currentSteps < lowestSteps:
            lowestSteps = currentSteps
    print(lowestSteps)


with open('input.txt', 'r') as file: 
    line1Path = file.readline().split(',')
    line2Path = file.readline().split(',')

traversePathLine1(line1Path)
traversePathLine2(line2Path)
findIntersections()
