import matplotlib.pyplot as plt
import numpy as np

data = {
    'Асинхронный': 2.17,
    'Многопоточный': 2.16,
    'Многопроцессный': 1.61
}

methods = list(data.keys())
times = list(data.values())

fig, ax = plt.subplots()
rects = ax.bar(methods, times, 0.5)


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects)

ax.set_ylabel('Время выполнения (секунды)')
ax.set_title('Время вычисления квадратного корня')
ax.set_xticks(np.arange(len(methods)))
ax.set_xticklabels(methods)


fig.tight_layout()
plt.show()