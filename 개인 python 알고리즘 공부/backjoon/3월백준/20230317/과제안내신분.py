student = [x for x in range(1,31)]
while True:
    try:
        a = int(input())
        student.remove(a)
    except:
        break

for i in student:
    print(i)
