inputArray = []
index = 0
def addCase(index1, index2, outputIndex, senderType):
    if senderType == 0:
        inputArray[outputIndex] = inputArray[index1] + inputArray[index2]
    else:
        inputArray[outputIndex] = (inputArray[index1[0]] if index1[1] == 0 else index1[0]) + (inputArray[index2[0]] if index2[1] == 0 else index2[0])

def multCase(index1, index2, outputIndex, senderType):
    if senderType == 0:
        inputArray[outputIndex] = inputArray[index1] * inputArray[index2]
    else:
        inputArray[outputIndex] = (inputArray[index1[0]] if index1[1] == 0 else index1[0]) * (inputArray[index2[0]] if index2[1] == 0 else index2[0])

def singleIntInput(address):
    inputArray[address] = int(input("Whats the input value: ")) 

def singleIntOutput(addressValue, senderType):
    if senderType == 0:
        print(inputArray[addressValue])
    else:
        print(addressValue)

def opCodeOnly():
    global index
    if inputArray[index] is 1:
        addCase(inputArray[index+1],inputArray[index+2],inputArray[index+3],0)
        index = index + 4
    elif inputArray[index] is 2:
        multCase(inputArray[index+1],inputArray[index+2],inputArray[index+3], 0)
        index = index + 4
    elif inputArray[index] is 3:
        singleIntInput(inputArray[index + 1])
        index = index + 2
    elif inputArray[index] is 4:
        singleIntOutput(inputArray[index+1], 0)
        index = index + 2
    else:
        pass

def opCodeAndParams():
    global index
    inputParams, opCode = str(inputArray[index])[:-2], int(str(inputArray[index])[-2:])
    if 1 == opCode:
        addCase((inputArray[index+1], int(inputParams[-1]) if inputParams[-1] else 0 ),(inputArray[index+2], int(inputParams[-2]) if len(inputParams) > 1 else 0 ),inputArray[index+3], 1)
        index = index + 4
    elif 2 == opCode:
        print(inputParams)
        multCase((inputArray[index+1], int(inputParams[-1]) if inputParams[-1] else 0 ),(inputArray[index+2], int(inputParams[-2]) if len(inputParams) > 1 else 0 ),inputArray[index+3], 1)
        index = index + 4
    elif 3 == opCode:
        index = index + 2
    elif 4 == opCode:
        singleIntOutput(inputArray[index+1], 1)
        index = index + 2
    else:
        pass

with open('input.txt', 'r') as file: 
    for line in file:
        inputArray = [int(x) for x in line.split(',')]

while True:
    if inputArray[index] is 99:
        break
    if len(str(inputArray[index])) > 2:
        opCodeAndParams()
    else:
        opCodeOnly()
print('Program Ended')
