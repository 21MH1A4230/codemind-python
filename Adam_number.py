def rev(n):
    rev=0
    while n>0:
        r=n%10
        rev=(rev*10)+r
        n=n//10
    return rev
n=int(input())
sqr=n*n
rn=rev(n)
sqr1=rn*rn
sqrev=rev(sqr1)
if sqrev==sqr:
    print("True")
else:
    print("False")