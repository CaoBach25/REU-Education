import numpy as np

# Данные проектов и задач
projects = {
    "Проект 1": [("Задача 1", 5, 10), ("Задача 2", 3, 5)],
    "Проект 2": [("Задача 1", 4, 7), ("Задача 2", 2, 3)],
    "Проект 3": [("Задача 1", 6, 12), ("Задача 2", 4, 8)],
}

# Увеличиваем общее количество доступных ресурсов
total_resources = 25  # Увеличено с 15 до 25

# Параметры ACO
num_ants = 20
iterations = 50
evaporation_rate = 0.5
alpha = 1  # Влияние феромонов
beta = 2  # Влияние эвристики
pheromone_init = 1.0

# Инициализация феромонов
tasks = sum([len(projects[p]) for p in projects], 0)
pheromone = np.full((tasks, total_resources + 1), pheromone_init)

# Эвристическая информация
def heuristic(resource_allocation, resources_needed, time_needed):
    if resource_allocation < resources_needed:
        return 1e-5  # Очень маленькое значение вместо 0
    return 1 / (time_needed / resource_allocation + resources_needed)  # Учитываем потребность в ресурсах

# Оценка решения
def evaluate_solution(solution):
    total_time = 0
    total_allocated_resources = 0
    for project in projects.values():
        project_time = 0
        for task, resources, time in project:
            allocated_resources = solution.pop(0)
            total_allocated_resources += allocated_resources
            if allocated_resources >= resources:
                project_time += time / allocated_resources
            else:
                project_time += time * 2  # Увеличенный штраф за нехватку ресурсов
        total_time += project_time
    # Штраф за превышение общего количества ресурсов
    if total_allocated_resources > total_resources:
        total_time += (total_allocated_resources - total_resources) * 50  # Меньший штраф
    return total_time

# Обновление феромонов
def update_pheromones(pheromone, all_solutions, evaporation_rate, best_solution):
    pheromone *= (1 - evaporation_rate)
    for solution, time in all_solutions:
        pheromone_contribution = 1 / (time + 1e-5)
        for i, allocation in enumerate(solution):
            pheromone[i][allocation] += pheromone_contribution
    for i, allocation in enumerate(best_solution):
        pheromone[i][allocation] += 2  # Усиление феромонов для лучшего решения
    return pheromone

# Основной цикл ACO
best_solution = None
best_time = float('inf')

for iteration in range(iterations):
    all_solutions = []
    for ant in range(num_ants):
        solution = []
        total_allocated_resources = 0
        for i, project in enumerate(projects.values()):
            for j, task in enumerate(project):
                resources, time = task[1], task[2]
                probabilities = []
                for r in range(total_resources + 1):
                    if total_allocated_resources + r <= total_resources:  # Учитываем общий ресурс
                        prob = (pheromone[i][r] ** alpha) * (heuristic(r, resources, time) ** beta)
                        probabilities.append(prob)
                    else:
                        probabilities.append(0)  # Невозможное решение
                probabilities = np.array(probabilities)
                probabilities /= probabilities.sum() if probabilities.sum() > 0 else 1
                allocation = np.random.choice(range(total_resources + 1), p=probabilities)
                solution.append(allocation)
                total_allocated_resources += allocation
        total_time = evaluate_solution(solution.copy())
        all_solutions.append((solution, total_time))
        if total_time < best_time:
            best_solution = solution
            best_time = total_time
    if best_solution is not None:
        pheromone = update_pheromones(pheromone, all_solutions, evaporation_rate, best_solution)
    print(f"Итерация {iteration + 1}/{iterations}, Лучшая оценка: {best_time:.2f}")

# Итоговый результат
if best_solution is not None:
    print("\nОптимальное распределение ресурсов:")
    index = 0
    for project_name, tasks in projects.items():
        print(f"{project_name}:")
        for task_name, resources, time in tasks:
            print(f"  {task_name}: {best_solution[index]} ресурсов (необходимо {resources})")
            index += 1
    print(f"\nМинимальное время выполнения всех проектов: {best_time:.2f}")
else:
    print("Не удалось найти допустимое решение.")