import matplotlib.pyplot as plt
import numpy as np

data = {
    'Пять': {
        'asyncio': 0.00,
        'threading': 0.00,
        'multiprocessing': 0.24
    },
    'Тридцать': {
        'asyncio': 0.00,
        'threading': 0.01,
        'multiprocessing': 0.32
    }
}

labels = ['Пять', 'Тридцать']
methods = ['asyncio', 'threading', 'multiprocessing']

x = np.arange(len(methods))
width = 0.2

fig, ax = plt.subplots()

rects1 = ax.bar(x - width, [data['Пять'][m] for m in methods], width, label='Пять файлов')
rects2 = ax.bar(x, [data['Тридцать'][m] for m in methods], width, label='Тридцать файлов')


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

ax.set_ylabel('Время выполнения (секунды)')
ax.set_title('Время чтения текстовых файлов')
ax.set_xticks(x)
ax.set_xticklabels(methods)
ax.legend()

fig.tight_layout()
plt.show()