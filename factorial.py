quit=str(input())
while(quit=="y"):
    print("you have exited, if want to calculate press any key another than y")
else:
    n=int(input())
    fac=1
    if(n<=0):
        print("sorry factorial cant be calcualated for negative number or zero")
    else:
        for i in range(1,n+1):
            fac=fac*i
    print("factorial of number",n,"is",fac)



