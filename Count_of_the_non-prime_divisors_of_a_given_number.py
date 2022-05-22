def prime(n):
    for i in range(2,n):
        if n%i==0:
            return True
    else:
        return False
n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i):
            count+=1
print(count+1)