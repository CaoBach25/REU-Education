import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

train_file_path = r"D:\Tin\Nam 3\Ki 1\Машинное обучение\RAS4\Nedvig.csv"
test_file_path = r"D:\Tin\Nam 3\Ki 1\Машинное обучение\RAS4\Nedvig_test.csv"

# Загрузка и обработка обучающих данных (Nedvig.csv)
data_train = np.genfromtxt(train_file_path, delimiter=',', skip_header=1)
print("Исходные обучающие данные:", data_train)

# Обработка NaN и Inf
if np.isnan(data_train).any() or np.isinf(data_train).any():
    print("Количество NaN до обработки:", np.isnan(data_train).sum())
    print("Количество Inf до обработки:", np.isinf(data_train).sum())
    # Для столбцов, содержащих только NaN, заменяем на 0
    for i in range(data_train.shape[1]):
        if np.all(np.isnan(data_train[:, i])):
            data_train[:, i] = 0  # Заменяем на 0, если все значения NaN
        else:
            col_mean = np.nanmean(data_train[:, i])  # Среднее по столбцу
            data_train[:, i] = np.where(np.isnan(data_train[:, i]), col_mean, data_train[:, i])  # Заменяем NaN на среднее

    # Заменяем Inf на максимальное значение без Inf в столбце
    for i in range(data_train.shape[1]):
        max_value = np.max(data_train[:, i][~np.isinf(data_train[:, i])])  # Максимум без Inf
        data_train[:, i] = np.where(np.isinf(data_train[:, i]), max_value, data_train[:, i])

    print("Количество NaN после обработки:", np.isnan(data_train).sum())
    print("Количество Inf после обработки:", np.isinf(data_train).sum())

# Разделение данных на X_train и y_train
X_train = data_train[:, :-1]  # Независимые переменные
y_train = data_train[:, -1]   # Зависимая переменная

# Добавление столбца с единицами в X_train для константы
X_train_sm = sm.add_constant(X_train)

# Проверка на наличие NaN или Inf
if np.isnan(X_train_sm).any() or np.isinf(X_train_sm).any():
    print("Ошибка: X_train_sm содержит NaN или Inf!")
    exit()

# Построение модели линейной регрессии с использованием statsmodels
model = sm.OLS(y_train, X_train_sm)
results = model.fit()

# Общий отчет о модели
print(results.summary())

# Загрузка и обработка тестовых данных (Nedvig_test.csv)
data_test = np.genfromtxt(test_file_path, delimiter=',', skip_header=1)
print("Исходные тестовые данные:", data_test)

# Обработка NaN и Inf в тестовых данных
if np.isnan(data_test).any() or np.isinf(data_test).any():
    for i in range(data_test.shape[1]):
        if np.all(np.isnan(data_test[:, i])):
            data_test[:, i] = 0  # Заменяем на 0, если все значения NaN
        else:
            col_mean = np.nanmean(data_test[:, i])
            data_test[:, i] = np.where(np.isnan(data_test[:, i]), col_mean, data_test[:, i])

    for i in range(data_test.shape[1]):
        max_value = np.max(data_test[:, i][~np.isinf(data_test[:, i])])
        data_test[:, i] = np.where(np.isinf(data_test[:, i]), max_value, data_test[:, i])

# Разделение данных на X_test и y_test
X_test = data_test[:, :-1]
y_test = data_test[:, -1]

# Добавление столбца с единицами в X_test для константы
X_test_sm = sm.add_constant(X_test)

# Проверка на наличие NaN или Inf
if np.isnan(X_test_sm).any() or np.isinf(X_test_sm).any():
    print("Ошибка: X_test_sm содержит NaN или Inf!")
    exit()

# Прогнозирование значений y_test с использованием обученной модели
y_pred = results.predict(X_test_sm)

# Сравнение фактических и прогнозируемых значений
plt.scatter(y_test, y_pred, label="Прогноз vs Фактические значения", alpha=0.7)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color="red", linestyle="-", label="Линия регрессия")
plt.xlabel("Фактические значения (y_test)")
plt.ylabel("Прогнозируемые значения (ŷ)")
plt.title("Сравнение фактических и прогнозируемых значений")
plt.legend()
plt.show()

# Оценка качества модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Среднеквадратичная ошибка (MSE): {mse}")
print(f"Коэффициент детерминации (R²): {r2}")

# Заключение о качестве модели
if r2 >= 0.7:
    print("Модель имеет хорошую точность.")
elif 0.4 <= r2 < 0.7:
    print("Модель имеет среднюю точность.")
else:
    print("Модель имеет низкую точность.")