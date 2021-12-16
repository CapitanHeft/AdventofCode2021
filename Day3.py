import time
def arraytoInt(array):
    string = [str(integer) for integer in array]
    concatstr = "".join(string)
    binary = int(concatstr)
    return(binaryToDecimal(binary))

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return(decimal)


txtfile = open("D:\Downloads\AdventCodeDay3Input.txt", "r")
txtfile = open("D:\Downloads\AdventCodeDay3test.txt", "r")

horizontalPos = 0
depth = 0
aim = 0


length = len(txtfile.readline())
txtfile.close()
txtfile = open("D:\Downloads\AdventCodeDay3Input.txt", "r")
txtfile = open("D:\Downloads\AdventCodeDay3test.txt", "r")

modeList = [0] * length
Epsilon = [0] * length
Gamma = [0] * length
LinesArray = []

for line in txtfile:
    index = 0
    LinesArray.append(line[0:length-1])
    for character in line:
        #time.sleep(.25)
        if character == "0":
            modeList[index] = modeList[index] - 1
        else:
           modeList[index] = modeList[index] + 1
        index = index + 1
print(LinesArray)
index = 0
for answerCharacter in modeList:
    if answerCharacter > 0:
        Epsilon[index] = 1
    else:
        Gamma[index] = 1

    index = index + 1
#Epsilon is the most common bit
Epsilon.pop()
Gamma.pop()

index = 0
co2array = LinesArray
oxygenarray = LinesArray

while index < length -1:
    mode = 0
    for num in co2array:
        if num[index] == "1":
            mode = mode + 1
        else:
            mode = mode - 1
    for num in co2array[:]:
        if mode < 0:
            if num[index] == "0":
                co2array.remove(num)
        else:
            if num[index] == "1":
                co2array.remove(num)
    if len(co2array) == 1:
        break
    index = index + 1

while index < length -1:

    mode = 0
    for num in oxygenarray:
        if num[index] == "1":
            mode = mode + 1
        else:
            mode = mode - 1
    for num in oxygenarray[:]:
        if mode < 0:
            if num[index] == "0":
                oxygenarray.remove(num)
        else:
            if num[index] == "1":
                oxygenarray.remove(num)
    if len(oxygenarray) == 1:
        break
    index = index + 1

print("CO2: ", co2array)
print("O2: ", oxygenarray)





EpsilonAns = arraytoInt(Epsilon)
GammaAns = arraytoInt(Gamma)
print("Power Consumption: ", EpsilonAns*GammaAns)


txtfile.close()