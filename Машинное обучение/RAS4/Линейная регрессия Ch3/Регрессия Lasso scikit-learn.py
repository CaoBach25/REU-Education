import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data_path = r'D:\Tin\Nam 3\Ki 1\Машинное обучение\RAS4\boston.csv'

data = pd.read_csv(data_path)

# Разделение данных на признаки (X) и целевую переменную (y)
X = data.iloc[:, :-1].values  # Все столбцы, кроме последнего
y = data.iloc[:, -1].values   # Последний столбец — целевая переменная

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели Lasso
alpha = 0.1  # Параметр регуляризации
lasso = Lasso(alpha=alpha)

# Обучение модели на обучающих данных
lasso.fit(X_train, y_train)

# Прогнозирование на тестовой выборке
y_pred = lasso.predict(X_test)

# Оценка модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error (MSE):", mse)
print("R2 Score:", r2)

# Вывод коэффициентов модели
print("Коэффициенты модели Lasso:", lasso.coef_)

#Визуализация результатов (необязательно, для анализа)
import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel("Истинные значения")
plt.ylabel("Предсказанные значения")
plt.title("Lasso Regression: Истинные значения vs Предсказанные значения")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'k--', lw=2)  # Референсная линия
plt.show()