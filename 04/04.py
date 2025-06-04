content = ""
with open('04/input.txt', 'r') as file:
    content = file.read()

result=content.split("\n")


list1 = []
list2 = []

for line in result:
    abc = line.split("   ")
    list1.append(int(abc[0]))
    list2.append(int(abc[1]))

list1.sort()
list2.sort()

distance = 0
for i in range(len(list1)):
    distance = distance + abs(list1[i] - list2[i])

part2Result = 0 
for i in list1:
    count = 0
    for j in list2:
        if i == j:
            count += 1
    part2Result += i*count

print(part2Result)