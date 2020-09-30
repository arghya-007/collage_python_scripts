str1 = input("Enter string : ")
t = 1
i = 0

while(i < len(str1)):
    if(str1[i] == ' '):
        t = t + 1
    i = i + 1

print(" Words in this String = ", t)