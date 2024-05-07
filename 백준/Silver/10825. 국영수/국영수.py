students = []

for _ in range(int(input())):
    name, kor, eng, mat = input().split()
    students.append((int(kor), int(eng), int(mat), name))

students.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for student in students:
    print(student[3])