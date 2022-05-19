def fib(n):
    a=0
    b=1
    flag=0
    for i in range(2,n):
        c=a+b
        a,b=b,c
        if c==n:
            flag+=1
    if flag==1:
        print("True")
    else:
        print("False")
n=int(input())
fib(n)