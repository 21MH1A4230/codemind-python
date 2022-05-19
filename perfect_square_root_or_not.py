n=int(input())
import math
s=math.sqrt(n)
round(s,2)
if int(s+0.5)**2==n:
    print("True")
else:
    print("False")