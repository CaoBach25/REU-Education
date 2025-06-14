import numpy as np
import matplotlib.pyplot as plt

file_path = r"D:\Tin\Nam 3\Ki 1\Машинное обучение\RAS4\Nedvig.csv"

#Загрузка и обработка данных
data = np.genfromtxt(file_path, delimiter=',', skip_header=1, dtype=None, encoding='utf-8')

# Проверка исходных данных
print("Исходные данные (первые 5 строк):")
print(data[:5])

# Преобразование данных в числовой формат, обработка NaN
def preprocess_data(data):
    """
    Преобразование столбцов в числовой формат, замена NaN на среднее или значение по умолчанию.
    """
    numeric_data = []
    for row in data:
        row_numeric = []
        for value in row:
            try:
                # Попытка преобразовать значение в число
                row_numeric.append(float(value))
            except ValueError:
                # Замена значений, которые не удалось преобразовать, на NaN
                row_numeric.append(np.nan)
        numeric_data.append(row_numeric)
    numeric_data = np.array(numeric_data)
    
    # Обработка NaN: замена NaN в каждом столбце на среднее значение этого столбца
    for col in range(numeric_data.shape[1]):
        col_mean = np.nanmean(numeric_data[:, col])
        numeric_data[:, col] = np.where(np.isnan(numeric_data[:, col]), col_mean, numeric_data[:, col])
    
    return numeric_data

# Обработка данных
numeric_data = preprocess_data(data)
print("Данные после обработки (первые 5 строк):")
print(numeric_data[:5])

#Выбор одного столбца x и y для регрессии
x = numeric_data[:, 5]  # Столбец "General" (общая площадь)
y = numeric_data[:, -1]  # Столбец "Price" (цена)

# Реализация функций для градиентного спуска
def get_gradient_at_b(x, y, b, a):
    N = len(x)
    diff = sum((y - (a * x + b)))
    b_gradient = -(2 / N) * diff
    return b_gradient

def get_gradient_at_a(x, y, b, a):
    N = len(x)
    diff = sum(x * (y - (a * x + b)))
    a_gradient = -(2 / N) * diff
    return a_gradient

def step_gradient(x, y, b_current, a_current, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, a_current)
    a_gradient = get_gradient_at_a(x, y, b_current, a_current)
    b = b_current - (learning_rate * b_gradient)
    a = a_current - (learning_rate * a_gradient)
    return b, a

def gradient_descent(x, y, learning_rate, num_iterations):
    b = 0  # Начальное значение свободного члена
    a = 0  # Начальное значение углового коэффициента
    for _ in range(num_iterations):
        b, a = step_gradient(x, y, b, a, learning_rate)
    return b, a

#Выполнение градиентного спуска
learning_rate = 0.0001
num_iterations = 1000
b, a = gradient_descent(x, y, learning_rate, num_iterations)
print(f"Свободный член b (intercept): {b}")
print(f"Угловой коэффициент a (slope): {a}")

#Построение графика результата
y_pred = a * x + b  # Предсказанные значения
plt.scatter(x, y, color="blue", label="Фактические данные")
plt.plot(x, y_pred, color="red", label="Линия регрессии")
plt.xlabel("Общая площадь (x)")
plt.ylabel("Цена (y)")
plt.title("Линейная регрессия с использованием градиентного спуска")
plt.legend()
plt.show()