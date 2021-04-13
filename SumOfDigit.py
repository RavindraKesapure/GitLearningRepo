sum=0
n=int(input("Enter the digit \n"))
temp=n
while n > 0:
           r=n%10
           sum=int(sum+r)
           n=n/10

print(temp ," sum is ",int(sum))