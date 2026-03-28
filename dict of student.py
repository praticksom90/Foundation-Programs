
stu = {}


n = int(input("No. of students: "))

for i in range(n):
    name = input("Name: ")
    marks=[]
    print("Marks:")
    for j in range(3):
        marks.append(float(input()))
    stu[name] = marks

a = input("Enter name for average:")

if a in stu:
    mar = stu[a]
    avg = sum(mar) / len(mar)
    print(f"Average marks: {avg:.2f}")
else:
    print("error 404: not found")
