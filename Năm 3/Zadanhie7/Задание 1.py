import numpy as np

# Данные с дополнительной вариативностью
data = {
    "ВВП": [100, 120, 110, 130, 125, 140, 150, 160],
    "Инфляция": [2, 3, 2.5, 3.5, 3.2, 4, 3.8, 4.1],
    "Уровень безработицы": [5, 4.5, 5.2, 4.8, 5, 4.7, 4.6, 4.5],
    "Доходы бюджета": [30, 35, 32, 40, 38, 42, 45, 47],
    "Расходы бюджета": [25, 30, 28, 35, 33, 36, 38, 39]
}

# Целевая функция с учетом штрафов
def objective_function(params):
    weight = [0.5, 0.2, 0.2, 0.05, 0.05]  # Весовые коэффициенты
    score = 0
    for i, key in enumerate(data.keys()):
        pred = np.mean(data[key]) + params[i]  # Прогнозируемое влияние
        real = np.mean(data[key])  # Реальное значение
        deviation = abs(pred - real)
        penalty = 0.1 if abs(params[i]) < 0.1 else 0  # Штраф для параметров около 0
        score += weight[i] * (deviation ** 2) + penalty
    return score

# Настройки PSO
num_particles = 50  # Количество частиц
num_dimensions = 5  # Количество параметров (ВВП, инфляция и т.д.)
iterations = 100  # Количество итераций
bounds = (-50, 50)  # Ограничения пространства поиска

# Инициализация
particles = np.random.uniform(bounds[0], bounds[1], (num_particles, num_dimensions))
velocities = np.zeros((num_particles, num_dimensions))
personal_best_positions = particles.copy()
personal_best_scores = np.array([objective_function(p) for p in particles])
global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
global_best_score = np.min(personal_best_scores)

# Гиперпараметры PSO
w = 0.7  # Инерция
c1 = 1.8  # Личный опыт
c2 = 1.8  # Групповой опыт

# Основной цикл PSO
for iteration in range(iterations):
    for i in range(num_particles):
        # Обновление скорости
        r1, r2 = np.random.rand(), np.random.rand()
        velocities[i] = (w * velocities[i] +
                         c1 * r1 * (personal_best_positions[i] - particles[i]) +
                         c2 * r2 * (global_best_position - particles[i]))
        
        # Обновление позиции
        particles[i] += velocities[i]
        particles[i] = np.clip(particles[i], bounds[0], bounds[1])  # Ограничение позиции

        # Оценка новой позиции
        score = objective_function(particles[i])
        if score < personal_best_scores[i]:  # Обновление личного лучшего
            personal_best_positions[i] = particles[i]
            personal_best_scores[i] = score

            # Обновление глобального лучшего
            if score < global_best_score:
                global_best_position = particles[i]
                global_best_score = score

    print(f"Итерация {iteration + 1}/{iterations}, Лучшая оценка: {global_best_score:.6f}")

# Итоговые результаты
print("\nОптимальные параметры воздействия нормативного акта:")
print(f"Влияние на ВВП: {global_best_position[0]:.2f}")
print(f"Влияние на инфляцию: {global_best_position[1]:.2f}")
print(f"Влияние на безработицу: {global_best_position[2]:.2f}")
print(f"Влияние на доходы бюджета: {global_best_position[3]:.2f}")
print(f"Влияние на расходы бюджета: {global_best_position[4]:.2f}")