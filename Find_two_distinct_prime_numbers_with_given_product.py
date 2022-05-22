def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
            return True
n=int(input())
flag=0
for i in range(2,n):
    for j in range(2,n):
        if prime(j) and prime(i):
            if i<j:
                if i*j==n:
                    print(i,j)
                    flag=1
                    break
if flag!=1:
    print("-1")