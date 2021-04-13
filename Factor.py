#WAP Factor of number
n=int(input("Enter the number \n"))
print(" factor of ",n)
for i in range(1,n+1):
        if n%i==0:
               print(i)
