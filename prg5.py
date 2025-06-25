def greatest(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greatest")
    elif(b>a and b>c):
        print(f"{b} is greatest")
    elif(c>a and c>b):
        print(f"{c} is greatest")


a=int(input("enter a :- "))
b=int(input("enter b :- "))
c=int(input("enter c :- "))
greatest(a,b,c)
