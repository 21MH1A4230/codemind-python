def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
x=int(input())
y=int(input())
sum=x+y
i=1
sum+=1
while sum>0:
    if prime(sum):
        print(i)
        break
    i+=1
    sum+=1