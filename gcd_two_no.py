x = int(input("insert 1st number: "))
y = int(input("insert 2nd number: "))
if x > y: 
    s = y 
else: 
    s = x 
for i in range(1, s+1): 
    if((x % i == 0) and (y % i == 0)): 
        gcd = i 
print ("gcd =",gcd )