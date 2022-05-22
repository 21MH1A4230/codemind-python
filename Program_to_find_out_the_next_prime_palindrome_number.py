def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
def rev(n):
    rev=0
    while n>0:
        r=n%10
        rev=(rev*10)+r
        n=n//10
    return rev
x=int(input())
for i in range(x+1,100000):
    if prime(i):
        revnum=rev(i)
        if revnum==i:
            print(i)
            break