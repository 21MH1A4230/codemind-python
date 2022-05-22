def prime(n):
    for i in range(2,n):
        if n%i==0:
            return(False)
    else:
        return(True)
def rev(a):
    revnum=0
    while a>0:
        r=a%10
        revnum=(revnum*10)+r
        a=a//10
    return revnum
n=int(input())
if prime(n):
    if prime(rev(n)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")