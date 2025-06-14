# Импорт необходимых библиотек
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.datasets import fetch_california_housing  # Thay vì load_boston
import matplotlib.pyplot as plt

# Загрузка набора данных California Housing
california = fetch_california_housing()
X = california.data  # Признаки
y = california.target  # Целевая переменная (цена жилья)

# Разделение данных на обучающую и тестовую выборки (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Инициализация модели линейной регрессии
model = LinearRegression()

# Обучение модели
model.fit(X_train, y_train)

# Прогнозирование на тестовой выборке
y_pred = model.predict(X_test)

# Вычисление средней абсолютной ошибки (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f"Средняя абсолютная ошибка (MAE): {mae}")

# Построение графика сравнения реальных и предсказанных значений
plt.scatter(y_test, y_pred)
plt.xlabel("Реальные значения")
plt.ylabel("Предсказанные значения")
plt.title("Сравнение реальных и предсказанных значений")
plt.show()