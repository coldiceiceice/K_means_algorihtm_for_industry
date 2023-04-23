import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn import preprocessing

cust_df = pd.read_excel('proizvodsvo.xlsx')
df = cust_df.drop('Завод', axis=1)
df = df.dropna()
df = df.reset_index(drop=True)
x = df.values

x = np.nan_to_num(x)
print('Преобразование в список', '\n', x, '\n')

clus_dataset = StandardScaler().fit_transform(x)
print('Вычисление параметров стандартного отклонения:', '\n', clus_dataset, '\n')

cluster_num = 3
k_means = KMeans(init="k-means++", n_clusters= cluster_num, random_state=0,n_init=12)
k_means.fit(x)
labels = k_means.labels_
print('Кластеризация:', '\n', labels, '\n')

df['Класс'] = labels
df.groupby('Класс').mean()
print(df, '\n', '*' * 10)

df = df.replace(r'\\n', ' ', regex=True)

# Выдает нули для каждого класса
# X = df[['Выручка от ', 'Рентабельность ', 'Оборачиваемость']]
# for i in range(3):
#     X_cluster = X[labels == i].values
#     y_cluster = df['Класс'][labels == i].values
#     lda = LinearDiscriminantAnalysis()
#     lda.fit(X_cluster, y_cluster)
#
#     print(f"Кластер {i}:{lda.coef_[0][0]} * Рентабельность + {lda.coef_[0][1]} * Оборачиваемость + {lda.intercept_[0]}")
#
#     print(lda.intercept_)
#     print(lda.coef_)
#     print(lda.predict(X_cluster))

classA = df.copy(deep=True)
classB = df.copy(deep=True)
classC = df.copy(deep=True)

# Разбиение на таблицы классов
classA = classA[classA['Класс'] == 0]
classB = classB[classB['Класс'] == 1]
classC = classC[classC['Класс'] == 2]


# Вывод классов
print('Класс А', '\n', classA.head(10), '\n', '-' * 35)
print('Класс В', '\n', classB.head(10), '\n', '-' * 35)
print('Класс С', '\n', classC.head(10), '\n', '-' * 35)

# Выборка данных для дискриминантного анализа
class_x = df[['Выручка от ', 'Оборачиваемость', 'Рентабельность ']]
class_y = df['Класс']

lda = LinearDiscriminantAnalysis()
lda.fit(class_x, class_y)
# sep_functions = pd.DataFrame(lda.coef_, columns=class_x.columns, index=lda.classes_)
# print('Разделительные функции: ', '\n', sep_functions)
print()
print(f"f1= {lda.coef_[0][0]} * Выручка от + {lda.coef_[0][1]} * Рентабельность + {lda.coef_[0][2]} *"
      f" Оборачиваемость + {lda.intercept_[0]}")

print(f"f2= {lda.coef_[1][0]} * Выручка от + {lda.coef_[1][1]} * Рентабельность + {lda.coef_[1][2]} *"
      f" Оборачиваемость + {lda.intercept_[1]}")

print(f"f3= {lda.coef_[2][0]} * Выручка от + {lda.coef_[2][1]} * Рентабельность + {lda.coef_[2][2]} *"
      f" Оборачиваемость + {lda.intercept_[2]}")



# print(lda.intercept_[3])
# # print(lda.coef_)
# qwe = lda.decision_function(class_x)
# # print(qwe)

# Здесь первая версия анализа, хз работает или нет

# classA_x = classA[['Выручка от ', 'Оборачиваемость', 'Рентабельность ']]
# classA_y = classA['Класс']
# # Дискриминантный анализ
# lda = LinearDiscriminantAnalysis()
# labels = preprocessing.LabelEncoder()
# classA_y = labels.fit_transform(classA_y)
# lda.fit(classA_x, classA_y)
# coefficients = lda.coef_
# intercept = lda.intercept_
#
# # Вывод формулы
# print(f"{lda.coef_[0][0]} * Выручка от + {lda.coef_[0][1]} * Рентабельность + {lda.coef_[0][2]} * Оборачиваемость + {lda.intercept_[0]}")

