n=int(input("Enter the number"))
count=0
for i in range(2,n):
       if  n%i==0:
            count +=1;
            break;
if count == 0:
     print( n," no is prime")
else:
     print( n ," no is not prime")