n=int(input())
sum=0
product=1
while(n>0):
    rem=n%10
    sum=sum+(rem)
    product=product*(rem)
    n=n//10
if(sum==product):
    print("Spy Number")
else:
    print("Not Spy Number")