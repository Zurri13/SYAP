def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y !=0:
        return x / y
    else:
        raise ValueError("Деление на ноль")

while True:
        try:
            operation = input("Веберите операцию (+,-,*,/) или введите ноль для завершения: ")

            if operation == '0':
                print("Программа завершена.")
                break

            if operation not in ('+', '-', '*', '/'):
                print("Некорректная операция. Веберите операцию +,-,*,/ или введите ноль для завершения. ")
                continue

            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = substract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)

            print("Результат: ", result)

        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")