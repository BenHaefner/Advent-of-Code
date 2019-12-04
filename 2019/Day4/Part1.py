start = 138307
end = 654504
passwordCount = 0

def checkValidity(number):
    global passwordCount
    digit= []
    for index in range(0,6):
        digit.append(int(number[index]))
    if( digit[0] <= digit[1] <= digit[2] <= digit[3]<= digit[4] <= digit[5]):
        if(digit[0] == digit[1] or digit[1] == digit[2] or digit[2] == digit[3] or digit[3] == digit[4] or digit[4] == digit[5]):
            passwordCount = passwordCount + 1

for index in range(start, end):
    checkValidity(str(index))

print(passwordCount)