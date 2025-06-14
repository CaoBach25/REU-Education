import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Путь к файлу
file_path = r"D:\Tin\Nam 3\Ki 1\Машинное обучение\RAS4\Nedvig.csv"

# Загрузка данных
data = np.genfromtxt(file_path, delimiter=',', skip_header=1, dtype=None, encoding='utf-8')

# Предобработка данных
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

    # Замена NaN на средние значения
    for col in range(numeric_data.shape[1]):
        col_mean = np.nanmean(numeric_data[:, col])
        numeric_data[:, col] = np.where(np.isnan(numeric_data[:, col]), col_mean, numeric_data[:, col])
    return numeric_data

# Предобработка данных
numeric_data = preprocess_data(data)

# Выбор признаков x и y
X = numeric_data[:, 5].reshape(-1, 1)  # Общая площадь
y = numeric_data[:, -1]  # Цена

# Разделение на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказания на тестовых данных
y_pred = model.predict(X_test)

# Расчет R2
r2 = r2_score(y_test, y_pred)

# Вывод результатов
print(f"Коэффициент детерминации (R²) для тестового набора данных: {r2}")

# Визуализация
plt.scatter(X_test, y_test, color="blue", label="Фактические данные")
plt.plot(X_test, y_pred, color="red", label="Прогноз модели")
plt.xlabel("Общая площадь (x)")
plt.ylabel("Цена (y)")
plt.title("Линейная регрессия с использованием Scikit-learn")
plt.legend()
plt.show()