with open('students.txt', 'w', encoding='utf-8') as file:
    file.write("Иванов Иван:5,4,3,5\n")
    file.write("Петров Петр:4,3,4,4\n")
    file.write("Сидорова Мария:5,5,5,5\n")

with open('students.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    name, ocenki = line.strip().split(':')
    ocenki = list(map(int, ocenki.split(',')))
    bal = sum(ocenki) / len(ocenki)
    print(f"{name}: средний балл: {bal:.2f}")

with open('students.txt', 'r', encoding='utf-8') as file:
    best_student = ""
    best_ball = 0
    for line in file:
        name, ocenki = line.strip().split(':')
        ocenki = list(map(int, ocenki.split(',')))
        bal = sum(ocenki) / len(ocenki)
        if bal > best_ball:
            best_student = name
            best_ball = bal
print(f"Студент с наивысшим баллом: {best_student} средний балл - {best_ball:.2f} ")



