import numpy as np

# Данные сценариев и рисков
scenarios = {
    "Сценарий 1": [("Риск 1", 0.2, 1000), ("Риск 2", 0.3, 2000)],
    "Сценарий 2": [("Риск 3", 0.4, 3000), ("Риск 4", 0.5, 4000)],
    "Сценарий 3": [("Риск 5", 0.6, 5000), ("Риск 6", 0.7, 6000)],
}

# Параметры алгоритма пчелиной колонии
num_bees = 30
num_scouts = 10
num_selected_sites = 5
elite_sites = 2
neighborhood_size = 0.2  # Увеличено для лучшего исследования
max_iterations = 50
penalty_factor = 1.2  # Уменьшено для баланса

# Целевая функция для оценки риска
def evaluate_risk(strategy):
    total_risk = 0
    for scenario, risks in scenarios.items():
        scenario_risk = 0
        for i, (risk_name, probability, cost) in enumerate(risks):
            if strategy[scenario][i]:  # Если риск минимизируется
                scenario_risk += probability * cost
            else:  # Штраф пропорционален стоимости и вероятности
                scenario_risk += penalty_factor * (0.5 * probability * cost)
        total_risk += scenario_risk
    return total_risk

# Генерация случайной стратегии
def generate_strategy():
    return {scenario: [np.random.choice([0, 1]) for _ in risks] for scenario, risks in scenarios.items()}

# Мутирование стратегии
def mutate_strategy(strategy):
    return {
        scenario: [
            1 - risk if np.random.rand() < neighborhood_size else risk
            for risk in risks
        ]
        for scenario, risks in strategy.items()
    }

# Алгоритм пчелиной колонии
def bee_algorithm():
    population = [generate_strategy() for _ in range(num_bees)]
    best_strategy = None
    best_risk = float("inf")

    for iteration in range(max_iterations):
        risks = [evaluate_risk(strategy) for strategy in population]
        sorted_indices = np.argsort(risks)
        population = [population[i] for i in sorted_indices]
        risks = [risks[i] for i in sorted_indices]

        if risks[0] < best_risk:
            best_strategy = population[0]
            best_risk = risks[0]

        elite_population = population[:elite_sites]
        selected_population = population[elite_sites:num_selected_sites]
        scout_population = [generate_strategy() for _ in range(num_scouts)]

        for i in range(elite_sites):
            for _ in range(3):
                new_strategy = mutate_strategy(elite_population[i])
                new_risk = evaluate_risk(new_strategy)
                if new_risk < risks[i]:
                    elite_population[i] = new_strategy
                    risks[i] = new_risk

        for i in range(num_selected_sites - elite_sites):
            idx = elite_sites + i
            for _ in range(2):
                new_strategy = mutate_strategy(selected_population[i])
                new_risk = evaluate_risk(new_strategy)
                if new_risk < risks[idx]:
                    selected_population[i] = new_strategy
                    risks[idx] = new_risk

        population = elite_population + selected_population + scout_population
        print(f"Итерация {iteration + 1}/{max_iterations}, Лучшая оценка риска: {best_risk:.2f}")

    return best_strategy, best_risk

# Запуск алгоритма
best_strategy, best_risk = bee_algorithm()

# Вывод результатов
print("\nОптимальная стратегия минимизации рисков:")
for scenario, risks in best_strategy.items():
    print(f"{scenario}: {[f'Риск {i + 1}: {"Минимизировать" if risk == 1 else "Игнорировать"}' for i, risk in enumerate(risks)]}")
print(f"\nМинимальный риск: {best_risk:.2f}")