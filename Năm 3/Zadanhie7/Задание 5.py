import numpy as np

# Тестовые данные о членах команды
team_members = [
    {"position": np.array([1, 2]), "velocity": np.array([1, 1])},
    {"position": np.array([3, 4]), "velocity": np.array([0, 1])},
    {"position": np.array([5, 1]), "velocity": np.array([1, 0])},
]

# Параметры алгоритма
SEPARATION_DISTANCE = 2.0  # Минимальное расстояние между членами команды
ALIGNMENT_WEIGHT = 1.0     # Вес для выравнивания скоростей
COHESION_WEIGHT = 1.0      # Вес для притяжения к центру масс
SEPARATION_WEIGHT = 1.5    # Вес для разделения
TIME_STEP = 1.0            # Временной шаг
NUM_ITERATIONS = 10        # Количество итераций

# Функция для вычисления центра масс команды
def compute_center_of_mass(team_members):
    positions = [member['position'] for member in team_members]
    return np.mean(positions, axis=0)

# Функция для разделения (разрыв тесных связей)
def separation(member, team_members):
    force = np.array([0.0, 0.0])
    for other in team_members:
        if other is not member:
            distance = np.linalg.norm(member['position'] - other['position'])
            if distance < SEPARATION_DISTANCE:
                force += member['position'] - other['position']
    return force

# Функция для выравнивания скоростей
def alignment(member, team_members):
    avg_velocity = np.mean([other['velocity'] for other in team_members], axis=0)
    return avg_velocity - member['velocity']

# Функция для притяжения к центру масс
def cohesion(member, center_of_mass):
    return center_of_mass - member['position']

# Основной алгоритм флокинга
def flocking_simulation(team_members):
    for iteration in range(NUM_ITERATIONS):
        center_of_mass = compute_center_of_mass(team_members)
        new_states = []

        for member in team_members:
            sep_force = separation(member, team_members) * SEPARATION_WEIGHT
            align_force = alignment(member, team_members) * ALIGNMENT_WEIGHT
            coh_force = cohesion(member, center_of_mass) * COHESION_WEIGHT

            # Итоговая сила
            total_force = sep_force + align_force + coh_force

            # Обновление скорости и позиции
            new_velocity = member['velocity'] + total_force * TIME_STEP
            new_position = member['position'] + new_velocity * TIME_STEP

            # Сохранение нового состояния
            new_states.append({"position": new_position, "velocity": new_velocity})

        # Обновление состояний команды
        team_members = new_states

        # Печать текущего состояния команды
        print(f"Итерация {iteration + 1}:")
        for i, member in enumerate(team_members):
            print(f"  Член команды {i + 1}: положение {member['position']}, скорость {member['velocity']}")

# Запуск алгоритма
flocking_simulation(team_members)