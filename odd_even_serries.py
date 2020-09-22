n=int(input("Insert any number: "))
y = int(input("press 1 for odd and 2 for even no:"))
if y == 1:
    for i in range(0, n): 
        if i % 2 != 0: 
            print(i, end = ' ') 
elif y == 2:
    for i in range(0, n+1): 
        if i % 2 == 0: 
            print(i,end = ' ') 
