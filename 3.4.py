import json

my_dict = {}
average_profit = 0
with open("firm.txt", "r", encoding='utf-8') as file:
    for line in file:
        line = line.split()
        profit = int(line[2]) - int(line[3])
        my_dict[line[0]] = profit
for i in my_dict:
    average_profit += my_dict.get(i)
my_dict1 = {"average_profit": average_profit}
list = [my_dict, my_dict1]
print(list)

with open("file.json", "w") as fil:
    json.dump(list,fil)
