def ifprime(a):
    f=1
    for i in range(2,int(a/2)+1):
        if a%i==0:
            return False
        return True   

def fact(n):
    b=1
    for i in range(n,0,-1):
        b*=i
    return b
def summ(n):
    b=0
    for i in range(n,0,-1):
        b+=i
    return b

def sub(a,b):
    print(a-b)

while True:
    n=int(input("Enter a number:"))
    if ifprime(n):
        while True:
            ch=int(input("1.SUMMATION\n2.FACTORIAL\n3.SUB(FACT-SUMM)\n0.EXIT\nEnter choice: "))            
            if ch==1:
                print(summ(n))
                print()
            elif ch==2:
                print(fact(n))
                print()
            elif ch==3:
                sub(fact(n),summ(n))
                print()
            elif ch==0:
                break
            else:
                print("Invalid choice")
                print()
    else:
        print(f"{n} is not PRIME!!")
    c=input("Again Prime no.[y/n]")
    if c in "nN":
        break 