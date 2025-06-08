content = ""
with open('02/input.txt', 'r') as file:
    content = file.read()

result=content.split("\n")

count = 0
for report in result: 
    list = report.split(" ")
    for i in range(len(list)):
        list[i] = int(list[i])

    safe = 0 
    for level in range(len(list)-1):
        if abs(list[level] - list[level+1]) < 1 or abs(list[level] - list[level+1]) > 3:
            safe += 1
    
     
    orderDesc = 0 
    for level in range(len(list)-1):
        if list[level] < list[level+1]:
            orderDesc += 1 
    
    orderAsc = 0 
    for level in range(len(list)-1):
        if list[level] > list[level+1]:
            orderAsc += 1 
    
    
    if (safe == 1 and (orderAsc == 0 or orderDesc == 0)) or (safe == 0 and (orderAsc <= 1 or orderDesc <= 1)) :
        count += 1 
        print(safe, end = " ")
        print(orderDesc, end = " ")
        print(orderAsc)
    
        
        
        
print(count)


 

