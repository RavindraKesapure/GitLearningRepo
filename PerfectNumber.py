#WAP perfect  number or not
sum=0 
n=int(input("Enter the number \n"))
for i in range(1,n):
        if n%i==0:
               sum =int(sum+i)

if sum == n:
       print(n, " is perfect number")
else:
       print(n," is not perfect number")