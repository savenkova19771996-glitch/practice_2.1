import csv

filename = "products.csv"
products = [
    ["Название", "Цена", "Количество"],
    ["Яблоки", 100, 50],
    ["Бананы", 80, 30],
    ["Молоко", 120, 20],
    ["Хлеб", 40, 100]
]
with open(filename, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(products)

while True:
    print("1 - Да", "\n2 - Нет")
    choice = (input("Хотите ввести дополнительные данные: "))
    if choice == '1':
        nazvanie = input("Введите название товара: ")
        price = float(input("Введите цену: "))
        kolichestvo = int(input("Введите количество: "))
        with open(filename, 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nazvanie, price, kolichestvo])
            print(f"{nazvanie}, {price}, {kolichestvo} - добавлены успешно")
    if choice == '2':
        break















