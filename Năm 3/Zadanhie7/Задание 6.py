import numpy as np
from scipy.optimize import differential_evolution

# Тестовые данные
historical_data = {
    "GDP": [100, 120, 110, 130, 125],
    "Unemployment": [5, 4.5, 5.2, 4.8, 5],
    "Income": [30000, 32000, 31000, 33000, 32500],
    "Investments": [1000, 1200, 1100, 1300, 1250],
    "Education": [200, 250, 220, 240, 230],
    "Healthcare": [300, 350, 320, 340, 330]
}

# Нормализация данных
def normalize(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

# Преобразование данных в массив numpy
normalized_data = {key: normalize(np.array(value)) for key, value in historical_data.items()}

# Целевая функция
# Максимизация ВВП, минимизация безработицы, увеличение инвестиций
# Считаем это как взвешенную сумму целевых значений
def objective_function(params):
    weights = {
        "GDP": params[0],
        "Unemployment": params[1],
        "Investments": params[2]
    }

    # Подсчет взвешенной суммы
    score = 0
    score += weights["GDP"] * np.mean(normalized_data["GDP"])
    score -= weights["Unemployment"] * np.mean(normalized_data["Unemployment"])
    score += weights["Investments"] * np.mean(normalized_data["Investments"])

    # Ограничение: сумма весов должна быть равна 1
    penalty = abs(1 - sum(params))
    return -score + penalty * 10  # Чем выше штраф, тем хуже функция

# Ограничения: веса должны быть между 0 и 1
bounds = [(0, 1), (0, 1), (0, 1)]

# Запуск оптимизации
result = differential_evolution(objective_function, bounds, strategy='best1bin', maxiter=100, popsize=15)

# Оптимальные параметры
optimal_params = result.x
print("Оптимальные параметры:")
print(f"Вес ВВП: {optimal_params[0]:.2f}")
print(f"Вес Безработицы: {optimal_params[1]:.2f}")
print(f"Вес Инвестиций: {optimal_params[2]:.2f}")

# Прогнозирование (на основе оптимальных параметров)
def forecast_future(params):
    weights = {
        "GDP": params[0],
        "Unemployment": params[1],
        "Investments": params[2]
    }
    
    future_score = 0
    future_score += weights["GDP"] * np.mean(normalized_data["GDP"]) * 1.1  # Допустим, рост на 10%
    future_score -= weights["Unemployment"] * np.mean(normalized_data["Unemployment"]) * 0.95  # Снижение на 5%
    future_score += weights["Investments"] * np.mean(normalized_data["Investments"]) * 1.15  # Рост на 15%
    return future_score

future_score = forecast_future(optimal_params)
print("Ожидаемый показатель развития региона:", future_score)