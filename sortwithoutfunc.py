def max3(a,b,c):
    if a>b and a>c:
        print("a is big")
        return
    elif b>c:
        print("b is big")
        return
    else:
        print("c is big")
        return
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
max3(a,b,c)
