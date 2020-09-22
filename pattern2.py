n = int(input("Enter Height : "))

if(n%2==0):
    print("Invalid Input")
else:
    half = n//2

    for i in range(half+1):
        for j in range(i+1):
            print("*",end="")
        print()

    for i in range(half):
        for j in range(half-i):
            print("*",end="")
        print()