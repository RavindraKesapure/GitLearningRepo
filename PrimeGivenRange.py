#WAP prime number given Range
count=0
n=int(input("Enter the number \n"))
for i in range(2,n+1):
         for j in range(2,i):        
                  count=0  
                  if i%j==0:
                         count =count+1
                         break  
          if count==0:
                  print(i, " is prime number")
      


