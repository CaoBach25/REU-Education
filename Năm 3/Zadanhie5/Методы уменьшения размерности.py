import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import datasets

# Загрузка набора данных MNIST
digits = datasets.load_digits()
X = digits.data  # Данные (признаки)
y = digits.target  # Метки классов (цифры от 0 до 9)

# Применение метода главных компонент (PCA) для уменьшения размерности
pca = PCA(n_components=2)  # Уменьшаем до 2D
X_pca = pca.fit_transform(X)  # Применяем PCA

# Визуализация данных в 2D-пространстве
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
plt.title('Визуализация данных после уменьшения размерности с использованием PCA')
plt.xlabel('Первая главная компонента')
plt.ylabel('Вторая главная компонента')

# Добавление цветовой легенды
plt.colorbar(scatter)

# Показать график
plt.show()