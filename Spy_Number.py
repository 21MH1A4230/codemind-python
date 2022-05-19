n=int(input())
sum=0
product=1
while n>0:
    r=n%10
    sum=sum+r
    product=product*r
    n=n//10
if sum==product:
    print("Spy Number")
else:
    print("Not Spy Number")