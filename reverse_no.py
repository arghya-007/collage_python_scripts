n = int(input("Insert any number: "))
r = 0
  
while n > 0: 
    a = n % 10
    r = r * 10 + a 
    n = int(n / 10)
      
print(r) 