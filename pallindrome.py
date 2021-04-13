#WAP Number is pallindrome or not
sum=0
n=int(input("Enter the number \n"))
temp=n
while(temp > 0):	
           r=temp%10
           sum =sum*10+r
           temp =temp // 10
           print(sum ,"  ",temp)


if sum==n:
       print(n," number is pallindrome")
else:
       print(n," number is not pallindrome");