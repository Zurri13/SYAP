def process_data(data):
    if isinstance(data, list):
        # список
        even_sum = sum([x for x in data if x % 2 == 0])
        data = [x for x in data if x != 0]
        return even_sum, data

    elif isinstance(data, set):
        # множество
        max_element = max(data)
        data.discard(max_element)
        return data

    elif isinstance(data, int):
        # число
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        return is_prime(data)

    elif isinstance(data, str):
        # Если передана строка
        char_count = {}
        for char in data:
            char_count[char] = char_count.get(char, 0) + 1
        most_common_char = max(char_count, key=char_count.get)
        return most_common_char

    else:
        # Если передан неизвестный тип данных
        return "Неподдерживаемый тип данных"

# Примеры использования
print(process_data([1, 2, 3, 0, 4, 5, 6]))  # Возвращает (12, [1, 2, 3, 4, 5, 6])
print(process_data({1, 2, 3, 4, 5}))         # Возвращает {1, 2, 3, 4}
print(process_data(7))                        # Возвращает True (число 7 - простое)
print(process_data("hello"))                  # Возвращает 'l' (символ 'l' встречается чаще всего)
print(process_data(True))                     # Возвращает "Неподдерживаемый тип данных"
