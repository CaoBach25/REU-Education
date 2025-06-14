import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data_path = r'D:\Tin\Nam 3\Ki 1\Машинное обучение\RAS4\boston.csv'
data = pd.read_csv(data_path)

# Разделение данных на признаки (X) и целевую переменную (y)
X = data.iloc[:, :-1].values  # Все колонки, кроме последней
y = data.iloc[:, -1].values   # Последняя колонка — целевая переменная

# 2. Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Ridge Regression
alpha_ridge = 1.0  # Параметр регуляризации
ridge = Ridge(alpha=alpha_ridge)

# Обучение Ridge
ridge.fit(X_train, y_train)

# Прогнозирование Ridge
y_pred_ridge = ridge.predict(X_test)

# Оценка Ridge
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
r2_ridge = r2_score(y_test, y_pred_ridge)

print("=== Ridge Regression ===")
print("Mean Squared Error (MSE):", mse_ridge)
print("R2 Score:", r2_ridge)
print("Коэффициенты модели Ridge:", ridge.coef_)

# 4. Lasso Regression
alpha_lasso = 0.1  # Параметр регуляризации
lasso = Lasso(alpha=alpha_lasso)

# Обучение Lasso
lasso.fit(X_train, y_train)

# Прогнозирование Lasso
y_pred_lasso = lasso.predict(X_test)

# Оценка Lasso
mse_lasso = mean_squared_error(y_test, y_pred_lasso)
r2_lasso = r2_score(y_test, y_pred_lasso)

print("\n=== Lasso Regression ===")
print("Mean Squared Error (MSE):", mse_lasso)
print("R2 Score:", r2_lasso)
print("Коэффициенты модели Lasso:", lasso.coef_)

# 5. Визуализация Ridge
plt.scatter(y_test, y_pred_ridge)
plt.xlabel("Истинные значения")
plt.ylabel("Предсказанные значения")
plt.title("Ridge Regression: Истинные значения vs Предсказанные значения")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'k--', lw=2)
plt.show()

# 6. Визуализация Lasso
plt.scatter(y_test, y_pred_lasso)
plt.xlabel("Истинные значения")
plt.ylabel("Предсказанные значения")
plt.title("Lasso Regression: Истинные значения vs Предсказанные значения")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'k--', lw=2)
plt.show()