n=int(input())
flag=0
square=n*n
while n>0:
    rem=n%10
    if(rem!=square%10):
        print("Not an Automorphic Number")
        flag=1
        break
    n=n//10
    square=square//10
if flag==0:
    print("Automorphic Number")