import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

file_path = r"D:\Tin\Nam 3\Ki 1\Машинное обучение\RAS4\Nedvig.csv"
data = np.genfromtxt(file_path, delimiter=',', skip_header=1)

print("Исходные данные:\n", data)
print("Размер исходных данных:", data.shape)

# Обработка значений NaN
if np.isnan(data).any():
    print("Количество NaN до обработки:", np.isnan(data).sum())
    # Замена NaN на среднее значение по каждому столбцу
    col_means = np.nanmean(data, axis=0)
    data = np.where(np.isnan(data), col_means, data)
    print("Количество NaN после обработки:", np.isnan(data).sum())

# Разделение данных на X и y
X = data[:, :-1]  # Независимые переменные
y = data[:, -1]   # Зависимая переменная

# Удаление столбцов с нулевой дисперсией
stds = np.std(X, axis=0)
X = X[:, stds > 0]  # Оставляем только столбцы с дисперсией > 0
print("Размер X после удаления столбцов с нулевой дисперсией:", X.shape)

# Проверка данных после обработки
if X.shape[0] == 0 or X.shape[1] == 0:
    print("Нет валидных данных. Проверьте исходный файл!")
    exit()

#Линейная регрессия с использованием NumPy
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Добавляем столбец 1 (свободный член)
theta_best = np.linalg.pinv(X_b.T @ X_b) @ X_b.T @ y
print("\nКоэффициенты линейной регрессии (NumPy):", theta_best)

# Линейная регрессия с использованием scikit-learn
lr = LinearRegression()
lr.fit(X, y)
y_pred_sklearn = lr.predict(X)
print("\nКоэффициенты линейной регрессии (scikit-learn):")
print(f"  Intercept: {lr.intercept_}")
print(f"  Coefficients: {lr.coef_}")

# Линейная регрессия с использованием statsmodels
X_b_sm = sm.add_constant(X)  # Добавляем столбец 1 (свободный член)
model = sm.OLS(y, X_b_sm).fit()
print("\nКоэффициенты линейной регрессии (statsmodels):")
print(model.params)

# Построение графика: Сравнение фактических и прогнозируемых значений
plt.figure(figsize=(8, 6))
plt.scatter(y, y_pred_sklearn, label="Прогноз vs Фактические значения", alpha=0.7)
plt.plot([min(y), max(y)], [min(y), max(y)], color="red", linestyle="-", label="Идеальная линия")
plt.xlabel("Фактические значения (y)")
plt.ylabel("Прогнозируемые значения (\u017Cy\u0302)")
plt.title("Сравнение фактических и прогнозируемых значений")
plt.legend()
plt.grid()
plt.show()

# Построение графиков рассеяния для каждой переменной
for i in range(X.shape[1]):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, i], y, label="Фактические данные", alpha=0.7)
    plt.plot(X[:, i], y_pred_sklearn, color="red", label="Линейная регрессия")
    plt.xlabel(f"X{i+1}")
    plt.ylabel("y")
    plt.title(f"График рассеяния X{i+1} и y")
    plt.legend()
    plt.grid()
    plt.show()