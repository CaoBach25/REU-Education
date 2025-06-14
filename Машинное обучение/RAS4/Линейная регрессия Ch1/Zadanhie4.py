import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

file_path = r"D:\Tin\Nam 3\Ki 1\Машинное обучение\RAS4\Nedvig.csv"

# Загрузка данных
data = np.genfromtxt(file_path, delimiter=',', skip_header=1, dtype=None, encoding='utf-8')

# Обработка данных: преобразование столбцов в числовые и обработка NaN
def preprocess_data(data):
    numeric_data = []
    for row in data:
        row_numeric = []
        for value in row:
            try:
                row_numeric.append(float(value))
            except ValueError:
                row_numeric.append(np.nan)
        numeric_data.append(row_numeric)
    numeric_data = np.array(numeric_data)

    # Замена NaN на среднее значение столбца
    for col in range(numeric_data.shape[1]):
        col_mean = np.nanmean(numeric_data[:, col])
        numeric_data[:, col] = np.where(np.isnan(numeric_data[:, col]), col_mean, numeric_data[:, col])
    return numeric_data

# Предварительная обработка данных
numeric_data = preprocess_data(data)

# Выбор переменных x и y
X = numeric_data[:, 5].reshape(-1, 1)  # Столбец "General" (общая площадь)
y = numeric_data[:, -1]  # Столбец "Price" (цена)

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание модели
model = LinearRegression()

# Обучение модели на обучающем наборе
model.fit(X_train, y_train)

# Прогноз на тестовом наборе
y_pred = model.predict(X_test)

# Вывод коэффициентов регрессии
print(f"Коэффициент наклона (slope): {model.coef_[0]}")
print(f"Свободный член (intercept): {model.intercept_}")

# Оценка модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Среднеквадратичная ошибка (MSE): {mse}")
print(f"Коэффициент детерминации (R²): {r2}")

# Использование statsmodels для сравнения

# Добавление константного столбца в X_train для построения линейной регрессии
X_train_sm = sm.add_constant(X_train)
model_sm = sm.OLS(y_train, X_train_sm).fit()

# Коэффициенты из statsmodels
print("\nКоэффициенты регрессии из Statsmodels:")
print(model_sm.params)

# Сравнение результатов
print("\nСравнение коэффициентов:")
print(f"Scikit-learn - Коэффициент наклона: {model.coef_[0]}, Свободный член: {model.intercept_}")
print(f"Statsmodels - Коэффициент наклона: {model_sm.params[1]}, Свободный член: {model_sm.params[0]}")

# Построение графика
plt.scatter(X_test, y_test, color="blue", label="Фактические данные")
plt.plot(X_test, y_pred, color="red", label="Линия регрессии")
plt.xlabel("Общая площадь (x)")
plt.ylabel("Цена (y)")
plt.title("Линейная регрессия с использованием Scikit-learn")
plt.legend()
plt.show()