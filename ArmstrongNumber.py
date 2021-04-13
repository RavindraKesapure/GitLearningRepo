#WAP Armstrong number or not
sum=0;count=0;temp=0;
n=int(input("Enter the number \n"))
temp=n

while(temp > 0):
         count+=1
         temp =temp // 10

temp = n
while(temp > 0):
         r = temp % 10
         arm=1
         print("r ",r)
         i=1
         while(i <= count):
                   arm = int(arm * r)   
                   i +=1
                   print(arm);
         sum =int(sum + arm)
         print("sum is ",sum)
         temp = temp //10
	 	 
if n == sum:
          print(n," is Armstrong Number ")	
else:	
          print(n," is not Armstrong Number ")
	
