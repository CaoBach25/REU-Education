import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Binarizer
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report

# 1. Чтение и исследование данных
df = pd.read_csv('D:\\Tin\\Nam 3\\Ki 1\\Машинное обучение\\jupyter-jupyter-bi19_nguen_k_b.csv')

# Просмотр первых 5 строк данных
print("Первые 5 строк данных:")
print(df.head())

# Информация о данных (типы данных и наличие пропусков)
print("\nИнформация о данных:")
print(df.info())

# 2. Проверка на пропущенные значения
print("\nПроверка на пропущенные значения:")
print(df.isnull().sum())

# 3. Анализ взаимосвязей между переменными
print("\nМатрица корреляции:")
correlation_matrix = df.corr()

# Построение тепловой карты корреляции
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Корреляция между переменными")
plt.show()

# 4. Построение модели для предсказания (Линейная регрессия)
# Разделение данных на признаки (X) и результат (y)
X = df.drop(columns=['Result'])  # Замените 'Result' на название целевой переменной в вашем наборе данных
y = df['Result']  # Замените 'Result' на название целевой переменной

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Инициализация модели линейной регрессии
model = LinearRegression()

# Обучение модели
model.fit(X_train, y_train)

# Прогнозирование
y_pred = model.predict(X_test)

# Оценка модели
print("\nОценка модели линейной регрессии:")
print(f'Среднеквадратичная ошибка: {mean_squared_error(y_test, y_pred)}')
print(f'Коэффициент детерминации (R2): {r2_score(y_test, y_pred)}')

# 5. Моделирование для классификации (например, случайный лес)
# Преобразование переменной 'Result' в классы (высокий/низкий)
binarizer = Binarizer(threshold=20)  # Установка порога для классификации
y_class = binarizer.fit_transform(y.values.reshape(-1, 1))

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y_class, test_size=0.2, random_state=42)

# Инициализация модели случайного леса
classifier = RandomForestClassifier()

# Обучение модели
classifier.fit(X_train, y_train)

# Прогнозирование и оценка модели
y_pred_class = classifier.predict(X_test)

print("\nОценка модели классификации (Случайный лес):")
print(f'Точность модели: {accuracy_score(y_test, y_pred_class)}')
print(classification_report(y_test, y_pred_class))

# 6. Сохранение обработанных данных в новый CSV файл
df.to_csv('processed_data.csv', index=False)
print("\nДанные успешно сохранены в файл 'processed_data.csv'")