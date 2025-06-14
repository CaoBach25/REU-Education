import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs  # Генерация тестовых данных

# 1. Генерация тестовых данных (вы можете заменить эти данные на реальные данные о клиентах)
X, y = make_blobs(n_samples=300, centers=4, random_state=42)

# 2. Масштабирование данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Применение алгоритма K-Means
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X_scaled)

# 4. Получение меток кластеров
labels = kmeans.labels_

# 5. Построение графика кластеров
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200)  # Центры кластеров
plt.title('Сегментация клиентов с использованием алгоритма K-Means')
plt.xlabel('Признак 1')
plt.ylabel('Признак 2')
plt.colorbar(label='Кластер')
plt.show()

# 6. Вывод центров кластеров и меток
print(f"Центры кластеров: \n{kmeans.cluster_centers_}")
print(f"Метки: \n{labels}")