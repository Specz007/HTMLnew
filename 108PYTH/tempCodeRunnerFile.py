n=int(input("Enter the no : "))
if n==0:
    print("Enter a number greater than 0")
for i in range (1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()