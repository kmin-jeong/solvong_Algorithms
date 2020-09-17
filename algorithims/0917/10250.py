for k in range(int(input())):
    h,w,num = map(int,input().split(" "))
    x=1
    y=0
    while num > h:
        x=x+1
        num = num-h
    y = num
    if x<10:
        print(y,end="")
        print("0",end="")
        print(x)
    else:
        print(y,end="")
        print(x)
