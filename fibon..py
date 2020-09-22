t = int(input("enter terms: "))
n1=0
n2=1
c = 0
if t == 1:
   print(n1)
else:
   while c < t:
       print(n1)
       x = n1 + n2
       n1 = n2
       n2 = x
       c = c+1