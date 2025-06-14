# Импортируем необходимые библиотеки
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Загрузка данных Iris
data = load_iris()

# Вывод описания данных (по-русски)
print("Описание данных Iris:")
print(data.DESCR)  # Описание данных (английский текст)

# Извлечение признаков (features) и меток (labels)
X = data.data  # Признаки: длина и ширина чашелистиков и лепестков
y = data.target  # Метки: 0 - setosa, 1 - versicolor, 2 - virginica

# Печать первых 5 строк данных (по-русски)
print("\nПримеры данных (первые 5 строк):")
print("Признаки (длина и ширина):")
print(X[:5])  # Первые 5 строк признаков
print("\nМетки (классы):")
print(y[:5])  # Первые 5 меток

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Создание и обучение модели k-NN
knn = KNeighborsClassifier(n_neighbors=3)  # k = 3
knn.fit(X_train, y_train)

# Предсказание на тестовых данных
y_pred = knn.predict(X_test)

# Оценка точности модели
accuracy = accuracy_score(y_test, y_pred)

# Вывод результатов (по-русски)
print("\nРезультаты:")
print(f"Точность классификации: {accuracy:.2f}")