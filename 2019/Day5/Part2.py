inputArray = []
testingArray = []

def addCase(index1, index2, outputIndex):
    testingArray[outputIndex] = testingArray[index1] + testingArray[index2]

def multCase(index1, index2, outputIndex):
    testingArray[outputIndex] = testingArray[index1] * testingArray[index2]

with open('input.txt', 'r') as file: 
    for line in file:
        inputArray = [int(x) for x in line.split(',')]

for noun in range(100):
    for verb in range(100):
        testingArray = inputArray.copy()
        testingArray[1] = noun
        testingArray[2] = verb
        index = 0
        while True:
            if testingArray[index] == 1:
                addCase(testingArray[index+1],testingArray[index+2],testingArray[index+3])
            elif testingArray[index] == 2:
                multCase(testingArray[index+1],testingArray[index+2],testingArray[index+3])
            elif testingArray[index] == 99:
                break
            else:
                break
            index = index + 4
        
        if testingArray[0] == 19690720:
            print(100*noun+verb)