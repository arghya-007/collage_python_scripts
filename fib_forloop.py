t = int(input("enter terms: "))
n1=0
n2=1
for n in range(0, t):
           if(n <= 1):
                      x = n
           else:
                      x = n1 + n2
                      n1 = n2
                      n2 = x
           print(x)