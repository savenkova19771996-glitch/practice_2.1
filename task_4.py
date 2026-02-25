from datetime import datetime
import os

log_file = "calculator.log"
print("Последние 5 операций: ")
if os.path.exists(log_file):
    with open(log_file, "r", encoding='utf-8') as f:
        lines = f.readlines()

        for line in lines[-5:]:
            print(line.strip())
else:
    print("Операций не найдено")
while True:
    print("Команды\n", "1 - +\n", "2 - -\n", "3 - *\n", "4 - /\n", "5 - очистить лог\n", "6 - выход\n")

    choice = int(input("Выберите команду: "))
    if choice == 6:
        break

    elif choice == 5:
        open(log_file, 'w', encoding='utf-8').close()
        print("Лог - файл очищен")
        continue

    elif choice == 1:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        result = a + b
        print(f"{a} + {b} = {result}")
        now = datetime.now()
        zapis = now.strftime("%Y/%m/%d %H:%M:%S")
        file = open(log_file, "a", encoding='utf-8')
        file.write(f"[{zapis}] {a} + {b} = {result}\n")
        file.close()

    elif choice == 2:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        result = a - b
        print(f"{a} - {b} = {result}")

        now = datetime.now()
        zapis = now.strftime("%Y/%m/%d %H:%M:%S")
        file = open(log_file, "a", encoding='utf-8')
        file.write(f"[{zapis}] {a} - {b} = {result}\n")
        file.close()

    elif choice == 3:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        result = a * b
        print(f"{a} * {b} = {result}")

        now = datetime.now()
        zapis = now.strftime("%Y/%m/%d %H:%M:%S")
        file = open(log_file, "a", encoding='utf-8')
        file.write(f"[{zapis}] {a} * {b} = {result}\n")
        file.close()

    elif choice == 4:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))

        if b == 0:
            print("Ошибка деления на ноль")
            continue
        result = a / b
        print(f"{a} / {b} = {result}")
        now = datetime.now()
        zapis = now.strftime("%Y/%m/%d %H:%M:%S")
        file = open(log_file, "a", encoding='utf-8')
        file.write(f"[{zapis}] {a} / {b} = {result}\n")
        file.close()







