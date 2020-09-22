n=int(input("Enter a Number: "))
p=0
temp=n
while(temp > 0):
    p = p+1
    temp = temp // 10

sum=0
temp=n
while(temp > 0):
    rem = temp % 10
    sum = sum + (rem**p)
    temp = temp // 10

if(n==sum):
    print("Armstrong")
else:
    print("Not Armstrong")