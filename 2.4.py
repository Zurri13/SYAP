def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Результат деления: {result}")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    finally:
        print("Этот блок выполняется всегда, не важно было исключение или нет.")


divide_numbers( 10, 3)
divide_numbers( 5, 0)

