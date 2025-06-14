import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz
from statsmodels.api import OLS, GLS, add_constant
import seaborn as sns

# Укажите путь к папке с файлами CSV
directory = r'D:\Tin\Nam 3\Ki 1\Машинное обучение\RAS4'

# Генерация данных с автокорреляцией
np.random.seed(42)
n = 100  # Количество наблюдений
x1 = np.random.normal(0, 1, n)  # Первая независимая переменная
x2 = np.random.normal(0, 1, n)  # Вторая независимая переменная
phi = 0.5  # Коэффициент автокорреляции
residuals = np.zeros(n)
for t in range(1, n):
    residuals[t] = phi * residuals[t - 1] + np.random.normal(0, 1)

# Зависимая переменная
beta0, beta1, beta2 = 2, 1.5, -1.0
y = beta0 + beta1 * x1 + beta2 * x2 + residuals
X_b = pd.DataFrame({'const': np.ones(len(x1)), 'x1': x1, 'x2': x2})

# Модель OLS
model_OLS = OLS(y, X_b).fit()
print("Результаты OLS:")
print(model_OLS.summary())

# Остатки из OLS
residuals_OLS = model_OLS.resid

# Оценка коэффициента автокорреляции
resid_fit = OLS(
    np.asarray(residuals_OLS)[1:],
    add_constant(np.asarray(residuals_OLS)[:-1])
).fit()
rho = resid_fit.params[1]
print(f"\nКоэффициент автокорреляции rho: {rho}")

# Построение матрицы Toeplitz для GLS
order = toeplitz(range(len(residuals_OLS)))
sigma_matrix = rho ** order

# Модель GLS
model_GLS = GLS(y, X_b, sigma=sigma_matrix).fit()
print("\nРезультаты GLS:")
print(model_GLS.summary())

#Графики остатков OLS и GLS
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(residuals_OLS, label='OLS Остатки')
plt.title('OLS Остатки')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(model_GLS.resid, label='GLS Остатки')
plt.title('GLS Остатки')
plt.legend()

plt.tight_layout()
plt.show()

# Анализ данных boston.csv
file_path = f'{directory}\\boston.csv'

# Загрузка данных
df = pd.read_csv(file_path)
print("\nДанные Boston:")
print(df.head())

# Корреляционная матрица
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr().round(1), annot=True, cbar=False)
plt.title('Корреляционная матрица')
plt.show()

# Разделение данных на X и y
X_boston = df[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']]
y_boston = df['MEDV']
X_boston = add_constant(X_boston)

# Модель OLS для Boston
model_boston_ols = OLS(y_boston, X_boston).fit()
print("\nРезультаты OLS для Boston:")
print(model_boston_ols.summary())

# Модель GLS для Boston
n_boston = len(y_boston)
rho_boston = 0.3  # Предположим коэффициент автокорреляции
omega_boston = toeplitz(rho_boston ** np.arange(n_boston))
model_boston_gls = GLS(y_boston, X_boston, sigma=omega_boston).fit()
print("\nРезультаты GLS для Boston:")
print(model_boston_gls.summary())