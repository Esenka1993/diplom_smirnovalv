import matplotlib.pyplot as plt
import numpy as np

# Данные о времени выполнения
data = {
    'Одно изображение': {
        'Обычное выполнение': 0.28,
        'Многопоточное': 0.17,
        'Многопроцессное': 0.41
    },
    'Десять изображений': {
        'Обычное выполнение': 0.40,
        'Многопоточное': 0.17,
        'Многопроцессное': 0.51
    }
}

# Данные для графика
labels = ['Одно изображение', 'Десять изображений']
methods = ['Обычное выполнение', 'Многопоточное', 'Многопроцессное']

x = np.arange(len(methods)) # Позиции столбцов на оси x
width = 0.2 # Ширина столбцов

fig, ax = plt.subplots()

# Создаем столбцы для одного изображения
rects1 = ax.bar(x - width, [data['Одно изображение'][m] for m in methods], width, label='Одно изображение')

# Создаем столбцы для десяти изображений
rects2 = ax.bar(x, [data['Десять изображений'][m] for m in methods], width, label='Десять изображений')


# Функция для добавления подписей к столбцам
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

# Настройка графика
ax.set_ylabel('Время выполнения (секунды)')
ax.set_title('Время выполнения обработки изображений')
ax.set_xticks(x)
ax.set_xticklabels(methods) #Изменено: подписи по методам
ax.legend()

fig.tight_layout()
plt.show()