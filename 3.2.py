with open('products.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print("Товары со стоимостью от 10 до 50 рублей:")
for line in lines:
    parts = line.split()
    if len(parts) == 2:
        product, price = parts
        price = float(price)
        if 10 <= price <= 50:
            print(f"{product}: {price} руб.")

total_price = sum(float(parts[1]) for parts in (line.split() for line in lines) if len(parts) == 2)
average_price = total_price / len(lines)

print(f"\nСредняя стоимость всех товаров: {average_price} руб.")
