'''
    File name: fdxb-calc.py
    Version: 1.0
    Author name: Unded Inside
    Date created: 2022-10-01
    Date modified: 2022-11-05
    Python version: 3.9.2
'''

def replaceInput(inputData):
    data = inputData.lower()
    ignoreValues = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    delimiter = data[2]
    if delimiter in ignoreValues:
        str = data
    else:
        str = data.replace(delimiter, "")
    return str

def hexToBin(toConvert):
    binaryString = ""
    for x in range(len(toConvert)):
        if toConvert[x] == "0":
            binaryString += "0000"
        elif toConvert[x] == "1":
            binaryString += "0001"
        elif toConvert[x] == "2":
            binaryString += "0010"
        elif toConvert[x] == "3":
            binaryString += "0011"
        elif toConvert[x] == "4":
            binaryString += "0100"
        elif toConvert[x] == "5":
            binaryString += "0101"
        elif toConvert[x] == "6":
            binaryString += "0110"
        elif toConvert[x] == "7":
            binaryString += "0111"
        elif toConvert[x] == "8":
            binaryString += "1000"
        elif toConvert[x] == "9":
            binaryString += "1001"
        elif toConvert[x].lower() == "a":
            binaryString += "1010"
        elif toConvert[x].lower() == "b":
            binaryString += "1011"
        elif toConvert[x].lower() == "c":
            binaryString += "1100"
        elif toConvert[x].lower() == "d":
            binaryString += "1101"
        elif toConvert[x].lower() == "e":
            binaryString += "1110"
        elif toConvert[x].lower() == "f":
            binaryString += "1111"
        else:
            raise ValueError("Invalid hexadcecimal input")
    return binaryString

def decToHex(toConvert):
    if toConvert < 10:
        return str(toConvert)
    elif toConvert == 10:
        return "A"
    elif toConvert == 11:
        return "B"
    elif toConvert == 12:
        return "C"
    elif toConvert == 13:
        return "D"
    elif toConvert == 14:
        return "E"
    elif toConvert == 15:
        return "F"

def binToDec(toConvert):
    toConvert = str(toConvert)
    bitValue = 1
    binValue = 0
    for x in range(len(toConvert)):
        if toConvert[x] == "1":
            binValue += bitValue
        bitValue = bitValue * 2
    return binValue

def outputBits(toOutput):
    output = ""
    output += toOutput[0] + "-"
    output += toOutput[1] + "-"
    if toOutput[2] == "1":
        output += "1"
    output += decToHex(binToDec(toOutput[3:7][::-1])) + "-"
    if toOutput[7] == "1":
        output += "1"
    output += decToHex(binToDec(toOutput[8:12][::-1])) + "-"
    output += decToHex(binToDec(toOutput[12:15][::-1]))
    return output

def splitData(toSplit):
    parts = []
    # Numerical ID
    parts.append(toSplit[0:38])
    # Country Code
    parts.append(toSplit[38:48])
    # Bits
    parts.append(toSplit[48:63])
    # Animal flag
    parts.append(toSplit[63])
    # Extra data
    parts.append(toSplit[64:88])
    return parts

def main():
    userInput = input("Please enter hex string.\n: ")
    # Strips delimiters
    userInput = replaceInput(userInput)
    # Checks length
    if len(userInput) != 22:
        print("Input must be 11 bytes (spaces allowed)")
        return 0
    # Splits hex to its composite parts
    dataParts = splitData(hexToBin(userInput))

    # Output numerical ID
    print("ID:", binToDec(dataParts[1]), end="-")
    # Print with leading 0s
    numerIDInt = binToDec(dataParts[0])
    print("0" * (12-len(str(numerIDInt))) + str(numerIDInt))
    # Animal flag
    if dataParts[3] == "1":
        print("Animal: Yes")
    else:
        print("Animal: No")
    # Bits
    print("Bits: " + outputBits(dataParts[2]))

main()
