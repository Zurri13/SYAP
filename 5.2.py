import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

dataset = pd.read_csv('test.csv', encoding='UTF-8', sep=',')

all_data = pd.DataFrame(dataset).head(1000)

if all_data.isnull().values.any():
    print('Пропуски в данных присутствуют.')
else:
    print('Пропуски в данных отсутствуют.')

all_data['Rooms'] = all_data['Rooms'].replace(0,1)

plt.figure(figsize=(15,8))
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.subplot(2, 3, 1)
plt.title('Гистограмма Square')
sns.histplot(dataset['Square'], color='blue')

plt.subplot(2, 3, 2)
plt.title('Гистограмма LifeSquare')
sns.histplot(dataset['LifeSquare'], color='orange')
plt.xlim(0, 100)

plt.subplot(2, 3, 3)
plt.title('Гистограмма KitchenSquare')
sns.histplot(dataset['KitchenSquare'], color='green')
plt.xlim(0, 20)

plt.subplot(2, 3, 4)
plt.title('Гистограмма Ecology_1')
sns.histplot(dataset['Ecology_1'], color='purple')

plt.figure(figsize=(15,8))
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.subplot(2, 3, 1)
plt.title('Ящик с усами Square')
sns.boxplot(y=dataset['Square'], color='blue')

plt.subplot(2, 3, 2)
plt.title('Ящик с усами LifeSquare')
sns.boxplot(y=dataset['LifeSquare'], color='orange')

plt.subplot(2, 3, 3)
plt.title('Ящик с усами KitchenSquare')
sns.boxplot(y=dataset['KitchenSquare'], color='green')
plt.ylim(0, 100)

plt.subplot(2, 3, 4)
plt.title('Ящик с усами Ecology_1')
sns.boxplot(y=dataset['Ecology_1'], color='red')
plt.ylim(0, 1)

plt.subplot(2, 3, 5)
plt.title('Ящик с усами Social_2')
sns.boxplot(y=dataset['Social_2'], color='purple')

plt.show()

room_counts = dict(all_data['Rooms'].value_counts())
for key, value in sorted(room_counts.items()):
    print(f'Квартир с количеством комнат {int(key)} -- {value}')

pivot_table_result = pd.pivot_table(all_data, values='Id', index='DistrictId', columns='Rooms', aggfunc='count',
                                    fill_value=0)
pivot_table_result.columns = [f"{int(col)} room(s)" for col in pivot_table_result.columns]
pivot_table_result.to_csv('Pivot_table_lb_5.csv', index=True, sep=',')
print(pivot_table_result)

all_data.to_csv('Наумович.csv', index=False)