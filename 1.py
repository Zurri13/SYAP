# Задание 1
number = int(input("Введите натуральное число: "))
even_sum = 0
while number > 0:
    digit = number % 10
    if digit % 2 == 0:
        even_sum += digit
    number //= 10
if even_sum == 0:
    print("Четных цифр в числе нет (0)")
else:
    print("Сумма четных цифр:", even_sum)

# Задание 2
text = input("Введите строку текста: ")
# Разделение строки на слова и нахождение самого длинного слова
words = text.split()
longest_word = max(words, key=len)
converted_text = ""
for char in text:
    if char.islower():
        converted_text += char.upper()
    elif char.isupper():
        converted_text += char.lower()
    else:
        converted_text += char
# Подсчет суммы цифр в строке
digit_sum = sum(int(char) for char in text if char.isdigit())
print("Самое длинное слово:", longest_word)
print("Текст с перевернутым регистром:", converted_text)
print("Сумма цифр в строке:", digit_sum)

# Задание 3
n = int(input("Введите натуральное число: "))
divisors = []
# Находим делители числа n и добавляем их в список
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
# Находим максимальный и минимальный элементы в списке
if len(divisors) == 0:
    print("Число", n, "не имеет делителей.")
else:
    max_divisor = max(divisors)
    min_divisor = min(divisors)

    print("Список делителей числа", n, ":", divisors)
    print("Максимальный делитель:", max_divisor)
    print("Минимальный делитель:", min_divisor)

# Задание 4
my_dict = {'a': 12, 'b': 13, 'c': 56, 'd': 400, 'e': 58, 'f': 20}
print("Исходный словарь:", my_dict)
# Используем функцию sorted() с параметром key для сортировки элементов словаря
# в порядке убывания значений и затем используем срез [0:3] для выбора трех верхних элементов
top_keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print("Три ключа с самыми высокими значениями:")
for key in top_keys:
    print(key)

# Задание 6
my_tuple = (5, -3, 8, -2, 4, 7)
print("Исходный кортеж:", my_tuple)
# Преобразуем кортеж в список
my_list = list(my_tuple)
# Ищем первый отрицательный элемент и удаляем его
for i, num in enumerate(my_list):
    if num < 0:
        del my_list[i]
        break  # Выходим из цикла после удаления первого отрицательного элемента
# Преобразуем список обратно в кортеж
my_tuple = tuple(my_list)
print("Измененный кортеж:", my_tuple)
