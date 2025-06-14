import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data_path = r'D:\Tin\Nam 3\Ki 1\Машинное обучение\RAS4\boston.csv'

data = pd.read_csv(data_path)

# Разделение данных на признаки (X) и целевую переменную (y)
X = data.iloc[:, :-1].values  # Все столбцы, кроме последнего
y = data.iloc[:, -1].values   # Последний столбец — целевая переменная

#Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели Ridge
alpha = 1.0  # Параметр регуляризации
ridge = Ridge(alpha=alpha)

# Обучение модели на обучающих данных
ridge.fit(X_train, y_train)

# Прогнозирование на тестовой выборке
y_pred = ridge.predict(X_test)

#Оценка модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R2 Score:", r2)
print("Коэффициенты модели Ridge:", ridge.coef_)

# Визуализация результатов
plt.scatter(y_test, y_pred)
plt.xlabel("Истинные значения")
plt.ylabel("Предсказанные значения")
plt.title("Ridge Regression: Истинные значения vs Предсказанные значения")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'k--', lw=2)  # Референсная линия
plt.show()