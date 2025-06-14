import numpy as np
import random

# Тестовые данные о проектах
projects = [
    {"cost": 10000, "time": 30, "quality": 80},
    {"cost": 15000, "time": 25, "quality": 90},
    {"cost": 12000, "time": 35, "quality": 85},
]

# Нормализация данных
# В этом случае, чем меньше стоимость и время, тем лучше; чем выше качество, тем лучше.
def normalize_projects(projects):
    normalized = []
    costs = [p['cost'] for p in projects]
    times = [p['time'] for p in projects]
    qualities = [p['quality'] for p in projects]

    max_cost, min_cost = max(costs), min(costs)
    max_time, min_time = max(times), min(times)
    max_quality, min_quality = max(qualities), min(qualities)

    for project in projects:
        normalized.append({
            'cost': (max_cost - project['cost']) / (max_cost - min_cost),
            'time': (max_time - project['time']) / (max_time - min_time),
            'quality': (project['quality'] - min_quality) / (max_quality - min_quality)
        })
    return normalized

# Параметры алгоритма муравьиной колонии
NUM_ANTS = 10
NUM_ITERATIONS = 50
EVAPORATION_RATE = 0.5
ALPHA = 1.0  # Влияние феромонов
BETA = 2.0   # Влияние эвристической информации

# Инициализация феромонов
pheromones = [1.0 for _ in projects]

# Эвристическая информация (предпочтения муравьев)
def heuristic(project):
    return project['cost'] + project['time'] + project['quality']

# Основной алгоритм
normalized_projects = normalize_projects(projects)

def ant_colony_optimization():
    global pheromones
    best_project = None
    best_score = -float('inf')

    for iteration in range(NUM_ITERATIONS):
        scores = []

        for ant in range(NUM_ANTS):
            probabilities = []
            for i, project in enumerate(normalized_projects):
                prob = (pheromones[i] ** ALPHA) * ((heuristic(project)) ** BETA)
                probabilities.append(prob)

            # Нормализация вероятностей
            probabilities = np.array(probabilities)
            probabilities /= probabilities.sum()

            # Выбор проекта для муравья
            chosen_index = np.random.choice(len(projects), p=probabilities)
            scores.append((chosen_index, heuristic(normalized_projects[chosen_index])))

        # Обновление феромонов
        pheromones = [p * (1 - EVAPORATION_RATE) for p in pheromones]

        for chosen_index, score in scores:
            pheromones[chosen_index] += score

        # Выбор лучшего решения
        for chosen_index, score in scores:
            if score > best_score:
                best_score = score
                best_project = projects[chosen_index]

    return best_project

# Запуск алгоритма
best_project = ant_colony_optimization()
print("Лучший проект:")
print(best_project)