with open('F1.txt', 'w') as f1:
    print("Введите строки для записи в файл F1. Для окончания ввода оставьте строку пустой:")
    while True:
        line = input()
        if not line:
            break
        f1.write(line + '\n')

second_word = input("Введите второе слово: ")
with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    for line in f1:
        words = line.split()
        if len(words) >= 2 and second_word in words[1]:
            f2.write(line)

with open('F2.txt', 'r') as f2:
    lines = f2.readlines()
    if lines:
        last_line = lines[-1]
        digit_count = sum(c.isdigit() for c in last_line)
        print(f"Количество цифр в последней строке файла F2: {digit_count}")
    else:
        print("Файл F2 пуст.")
