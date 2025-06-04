content = ""
with open('input.txt', 'r') as file:
    content = file.read().replace("\n", "")

#Split "mul"
def splitFile(string):
    result=string.split("mul")
    return result
lines = splitFile(content)


# Remove strings which dont start "("
def removeStrings(list):
    tempList = []
    for line in list:
        if len(line) > 0 and line[0] == "(":
            line = line[1:]
            tempList.append(line)
    return tempList

lines = removeStrings(lines)

# Split by comma
def splitComma(string):
    return string.split(",")
for i in range(len(lines)):
    lines[i] = splitComma(lines[i])



#  Check the first number
def checkFirstNumber(string):
    if string.isdigit():
        number = int(string)
        if number < 1000:
            return number
    return 0 

# Check 2nd number
def checkSecondNumber(string):
    if ')' in string:
        result = string.split(")")
        if result[0].isdigit():
            number = int(result[0])
            if number < 1000:
                return number
    return 0

result = 0      
for line in lines:
    if len(line) > 1: 
        mul = checkFirstNumber(line[0]) * checkSecondNumber(line[1])
        result = result + mul
print(result)

