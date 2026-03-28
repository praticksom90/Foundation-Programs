#stack
l=[]

def push(l):
    a=input("Enter an name:")
    b=int(input("Enter marks"))
    l.append([a,b])
    print("Data has been inserted in the stack.\n")

def pop(l):
    if len(l)==0:
        print("EMPTY STACK\n")
    else:
        print(l.pop(), "has been removed from the stack.\n")

def peek(l):
    if len(l)==0:
        print("EMPTY STACK\n")
    else:
        print(l[-1],"\n")

def disp(l):
    if len(l)==0:
        print("EMPTY STACK\n")
    else:
        m=l[::-1]
        for i in m:
            print(f"|\t{i}\t|")
        print()

while True:

    ch=int(input("1. PUSH\n2. POP\n3. PEEK\n4. DISPLAY\n5. EXIT\n\nENTER CHOICE:"))

    if ch==1:
        push(l)
    elif ch==2:
        pop(l)
    elif ch==3:
        peek(l)
    elif ch==4:
        disp(l)
    elif ch==5:
        break
    else:
        print("INVALID\n")