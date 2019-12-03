inputArray = []

def addCase(index1, index2, outputIndex):
    inputArray[outputIndex] = inputArray[index1] + inputArray[index2]

def multCase(index1, index2, outputIndex):
    inputArray[outputIndex] = inputArray[index1] * inputArray[index2]

with open('input.txt', 'r') as file: 
    for line in file:
        inputArray = [int(x) for x in line.split(',')]

inputArray[1] = int(input('What was in position 1? Integers only please! '))
inputArray[2] = int(input('What was in position 2? Integers only please! '))

index = 0
while True:
    if inputArray[index] is 1:
        addCase(inputArray[index+1],inputArray[index+2],inputArray[index+3])
    elif inputArray[index] is 2:
        multCase(inputArray[index+1],inputArray[index+2],inputArray[index+3])
    elif inputArray[index] is 99:
        break
    else:
        print('Something went wrong')
        break
    index = index + 4

print(inputArray[0])
