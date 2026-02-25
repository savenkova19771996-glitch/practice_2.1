with open('file_3.txt', 'w', encoding='utf-8') as file:
    file.write("Привет, мир!\n")
    file.write("Вторая строка\n")
    file.write("Строчка номер три\n")
    file.write("Это очень длинная строка\n")
    file.write("Строка пять\n")

with open('file_3.txt', 'r', encoding='utf-8') as file:
    stroki = file.readlines()
    count = len(stroki)
    print(f"Количество строк в файле: {count}")

with open('file_3.txt', 'r', encoding='utf-8') as file:
    k = file.readlines()
words_count = 0
for strok in k:
    words = strok.split()
    words_count += len(words)
print(f"Общее количество слов: {words_count}")

with open('file_3.txt', 'r', encoding='utf-8') as file:
    vse_stroki = file.readlines()
    vse_stroki = [strok.strip() for strok in vse_stroki]
longest_strok = ""
for strok in vse_stroki:
    if len(strok) > len(longest_strok):
        longest_strok = strok
print(f"Самая длинная строка файла: {longest_strok}")



