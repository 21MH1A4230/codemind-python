n=int(input())
sum=0
import math
sqr=math.pow(n,2)
while(sqr>0):
    rem=sqr%10
    sum=sum+rem
    sqr=sqr//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")