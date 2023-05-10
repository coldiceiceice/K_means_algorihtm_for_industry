import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# Функция подсчета каждой точки класса A
def scoreCoefA(revenue, profitability, turnover):
    return round(-0.0915 * revenue - 0.8364 * profitability + 4.062 * turnover - 0.5406, 4)


# Функция подсчета каждой точки класса В
def scoreCoefB(revenue, profitability, turnover):
    return round(-6.6415 * revenue + 6.6732 * profitability + 46.3427 * turnover - 1.4697, 4)


# Функция подсчета каждой точки класса С
def scoreCoefC(revenue, profitability, turnover):
    return round(13.4356 * revenue - 11.9525 * profitability - 99.4554 * turnover - 63.3037, 4)


#   Считывание данных предприятия (excel формат)
cust_df = pd.read_excel('proizvodsvo.xlsx')
df = cust_df.drop('Завод', axis=1)  # Удаляем столбец названий, в расчетах он не нужен
df = df.dropna() # Удаляем nan значения
df = df.reset_index(drop=True)  # Сопоставляем индексы
x = df.values  # Отделяем значения таблицы

x = np.nan_to_num(x)
print('Преобразование в список', '\n', x, '\n')

clus_dataset = StandardScaler().fit_transform(x)
print('Вычисление параметров стандартного отклонения:', '\n', clus_dataset, '\n')

# Реализация кластеризации
k_means = KMeans(init="k-means++", n_clusters=3, random_state=0, n_init=12) # Настройка метода, задаем 3 класса
k_means.fit(x)
labels = k_means.labels_ # Получаем список классов
print('Кластеризация:', '\n', labels, '\n')

df['Класс'] = labels  # Создаем и добавляем новую таблицу с классами предприятий
df.groupby('Класс').mean()
print(df, '\n', '*' * 10)
df = df.replace(r'\\n', ' ', regex=True)

# Создаем отдельные таблицы для каждого класса
classA = df.copy(deep=True)
classB = df.copy(deep=True)
classC = df.copy(deep=True)

# Разбиение на таблицы классов
classA = classA[classA['Класс'] == 0]   # Худшая
classB = classB[classB['Класс'] == 1]   # Средняя
classC = classC[classC['Класс'] == 2]   # Лучшая

# Вывод классов
print('Проблемное предприятие с высоким риском банкротства:', '\n', classA.head(10), '\n', '-' * 35)
print('Рискованное предприятие:', '\n', classB.head(10), '\n', '-' * 35)
print('Предприятия с хорошим запасом финансовой устойчивости', '\n', classC.head(10), '\n', '-' * 35)

# Выборка данных для дискриминантного анализа
class_x = df[['Выручка', 'Рентабельность', 'Оборачиваемость']]
class_y = df['Класс']

# Алгоритм дискриминантного анализа
lda = LinearDiscriminantAnalysis()
lda.fit(class_x, class_y) # Вносим данные для выборки


# Вывод формул
print()
print(
    f"f1= {round(lda.coef_[0][0], 4)} * Выручка + {round(lda.coef_[0][1], 4)} * Рентабельность + {round(lda.coef_[0][2], 4)} *"
    f" Оборачиваемость + {round(lda.intercept_[0], 4)}")

print(
    f"f2= {round(lda.coef_[1][0], 4)} * Выручка + {round(lda.coef_[1][1], 4)} * Рентабельность + {round(lda.coef_[1][2], 4)} *"
    f" Оборачиваемость + {round(lda.intercept_[1], 4)}")

print(
    f"f3= {round(lda.coef_[2][0], 4)} * Выручка + {round(lda.coef_[2][1], 4)} * Рентабельность + {round(lda.coef_[2][2], 4)} *"
    f" Оборачиваемость + {round(lda.intercept_[2], 4)}")

print('\nХудший')
for i in range(classA.shape[0]):
    print(scoreCoefA(classA.iloc[i][0], classA.iloc[i][1], classA.iloc[i][2]))

print('\nСредний')
for i in range(classB.shape[0]):
    print(scoreCoefB(classB.iloc[i][0], classB.iloc[i][1], classB.iloc[i][2]))

print('\nНаилудший')
for i in range(classC.shape[0]):
    print(scoreCoefC(classC.iloc[i][0], classC.iloc[i][1], classC.iloc[i][2]))
