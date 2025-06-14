from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

# Данные о покупках
data = {
    'Молоко': [1, 1, 0, 0, 1],
    'Хлеб': [1, 1, 1, 0, 0],
    'Масло': [0, 1, 1, 1, 1],
    'Яйца': [1, 0, 1, 1, 1]
}

# Преобразуем данные в DataFrame
df = pd.DataFrame(data)

# Преобразуем все значения в тип boolean (True/False)
df = df.astype(bool)

# Применяем алгоритм Apriori для поиска частых наборов товаров (min_support=0.5)
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)

# Выводим частые наборы
print("Частые наборы товаров:")
print(frequent_itemsets)

# Генерируем ассоциативные правила с минимальной поддержкой 0.5 и минимальной уверенностью 0.7
# Добавляем параметр num_itemsets
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7, num_itemsets=2)

# Выводим ассоциативные правила
print("\nАссоциативные правила:")
print(rules)