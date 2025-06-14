import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

# Загрузка данных из файла diabetes.csv
file_path = r"D:\Tin\Nam 3\Ki 1\Машинное обучение\RAS1\diabetes.csv"
data = pd.read_csv(file_path)

# Вывод информации о данных
print("Информация о данных:")
print(data.info())
print("\nПервые 5 строк данных:")
print(data.head())

# Разделение данных на обучающую и тестовую выборки
X = data.iloc[:, :-1].values  # Независимые переменные (все столбцы, кроме последнего)
y = data.iloc[:, -1].values   # Зависимая переменная (последний столбец)

# Разделение на обучающую (80%) и тестовую выборки (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели логистической регрессии
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Оценка модели
# Предсказание на тестовой выборке
y_pred = model.predict(X_test)

# Метрики качества
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification = classification_report(y_test, y_pred)
roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])

print(f"\nТочность (Accuracy): {accuracy:.2f}")
print("\nМатрица ошибок (Confusion Matrix):")
print(conf_matrix)
print("\nОтчет о классификации (Classification Report):")
print(classification)
print(f"\nПоказатель ROC-AUC: {roc_auc:.2f}")

# Визуализация матрицы ошибок

plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["No", "Yes"], yticklabels=["No", "Yes"])
plt.xlabel("Предсказания")
plt.ylabel("Истинные значения")
plt.title("Матрица ошибок")
plt.show()