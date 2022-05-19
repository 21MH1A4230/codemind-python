num=int(input())
sqr=num*num
sumofdigit=0
while sqr>0:
    sumofdigit=sumofdigit+sqr%10
    sqr=sqr//10
if (num==sumofdigit):
    print("Neon Number")
else:
    print("Not Neon Number")
