d=int(input("Enter the number of numbers you want to check:"))
for i in range(d):
    n=int(input("Enter the number:"))
    f=0
    g=0
    b,c=((5*n*n)-4),((5*n*n)+4)
    if n==0 or n==1:
        print(n,"is a Fibonacci number")
    else:
        for j in range(1,b):
            if j**2==b:
                f=1
        for v in range(1,c):
            if v**2==c:
                g=1
        if f==1 or g==1:
            print(n,"is a Fibonacci number")
        else:
            print(n,"is not a Fibonacci number")
