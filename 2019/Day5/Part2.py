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

def jumpTrue(index1, index2, outputIndex, senderType,):
    global index
    if senderType == 0:
        index = inputArray[index2] if inputArray[index1] != 0 else index
        if index != inputArray[index2]:
            index += 3
    else: 
        index = (inputArray[index2[0]] if index2[1] == 0 else index2[0]) if (inputArray[index1[0]] if index1[1] == 0 else index1[0]) != 0 else index
        if index != (inputArray[index2[0]] if index2[1] == 0 else index2[0]):
            index += 3

def jumpFalse(index1, index2, outputIndex, senderType,):
    global index
    if senderType == 0:
        index = inputArray[index2] if inputArray[index1] == 0 else index
        if index != inputArray[index2]:
            index += 3
    else: 
        index = (inputArray[index2[0]] if index2[1] == 0 else index2[0]) if (inputArray[index1[0]] if index1[1] == 0 else index1[0]) == 0 else index
        if index != (inputArray[index2[0]] if index2[1] == 0 else index2[0]):
            index += 3

def lessThan(index1, index2, outputIndex, senderType):
    if senderType == 0:
        inputArray[outputIndex] = 1 if inputArray[index1] < inputArray[index2] else 0
    else: 
        inputArray[outputIndex] = 1 if (inputArray[index1[0]] if index1[1] == 0 else index1[0]) < (inputArray[index2[0]] if index2[1] == 0 else index2[0]) else 0

def equals(index1, index2, outputIndex, senderType):
    if senderType == 0:
        inputArray[outputIndex] = 1 if inputArray[index1] == inputArray[index2] else 0
    else: 
        inputArray[outputIndex] = 1 if (inputArray[index1[0]] if index1[1] == 0 else index1[0]) == (inputArray[index2[0]] if index2[1] == 0 else index2[0]) else 0


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
    elif inputArray[index] is 5:
        jumpTrue(inputArray[index+1],inputArray[index+2],inputArray[index+3],0)
    elif inputArray[index] is 6:
        jumpFalse(inputArray[index+1],inputArray[index+2],inputArray[index+3],0)
    elif inputArray[index] is 7:
        lessThan(inputArray[index+1],inputArray[index+2],inputArray[index+3],0)
        index = index + 4
    elif inputArray[index] is 8:
        equals(inputArray[index+1],inputArray[index+2],inputArray[index+3],0)
        index = index + 4
    else:
        pass

def opCodeAndParams():
    global index
    inputParams, opCode = str(inputArray[index])[:-2], int(str(inputArray[index])[-2:])
    if 1 == opCode:
        addCase((inputArray[index+1], int(inputParams[-1]) if inputParams[-1] else 0 ),(inputArray[index+2], int(inputParams[-2]) if len(inputParams) > 1 else 0 ),inputArray[index+3], 1)
        index = index + 4
    elif 2 == opCode:
        multCase((inputArray[index+1], int(inputParams[-1]) if inputParams[-1] else 0 ),(inputArray[index+2], int(inputParams[-2]) if len(inputParams) > 1 else 0 ),inputArray[index+3], 1)
        index = index + 4
    elif 3 == opCode:
        index = index + 2
    elif 4 == opCode:
        singleIntOutput(inputArray[index+1], 1)
        index = index + 2
    elif 5 == opCode:
        jumpTrue((inputArray[index+1], int(inputParams[-1]) if inputParams[-1] else 0 ),(inputArray[index+2], int(inputParams[-2]) if len(inputParams) > 1 else 0 ),inputArray[index+3], 1)
    elif 6 == opCode:
        jumpFalse((inputArray[index+1], int(inputParams[-1]) if inputParams[-1] else 0 ),(inputArray[index+2], int(inputParams[-2]) if len(inputParams) > 1 else 0 ),inputArray[index+3], 1)
    elif 7 == opCode:
        lessThan((inputArray[index+1], int(inputParams[-1]) if inputParams[-1] else 0 ),(inputArray[index+2], int(inputParams[-2]) if len(inputParams) > 1 else 0 ),inputArray[index+3], 1)
        index = index + 4
    elif 8 == opCode:
        equals((inputArray[index+1], int(inputParams[-1]) if inputParams[-1] else 0 ),(inputArray[index+2], int(inputParams[-2]) if len(inputParams) > 1 else 0 ),inputArray[index+3], 1)
        index = index + 4
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
