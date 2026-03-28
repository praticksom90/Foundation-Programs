#2


ALL=[]
for i in range(5):
    a=input("Enter word:")
    ALL.append(a)

#1

def PUSHNV(N):
    novowel=[]
    v="aeiouAEIOU"
    for i in N:
        f=0
        for j in i:
            if j in v:
                f=1
                break
        if f!=1:
            novowel.append(i)

#3

    for i in range(len(novowel)):
        print(novowel.pop())
    print("empty stack")
PUSHNV(ALL)
