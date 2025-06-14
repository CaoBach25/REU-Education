import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# Шаг 1: Загрузка и подготовка данных CIFAR-10
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Шаг 2: Предобработка данных (нормализация значений в диапазон [0, 1])
train_images, test_images = train_images / 255.0, test_images / 255.0

# Шаг 3: Построение модели CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)
])

# Шаг 4: Компиляция модели
model.compile(optimizer='adam',
              loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Шаг 5: Обучение модели
history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# Шаг 6: Оценка модели на тестовых данных
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"Точность на тестовых данных: {test_acc}")

# Шаг 7: Построение графика точности
plt.plot(history.history['accuracy'], label='Точность на обучающих данных')
plt.plot(history.history['val_accuracy'], label = 'Точность на тестовых данных')
plt.xlabel('Эпохи')
plt.ylabel('Точность')
plt.legend(loc='lower right')
plt.show()