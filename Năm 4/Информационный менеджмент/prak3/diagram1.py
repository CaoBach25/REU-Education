import matplotlib.pyplot as plt

# ИТ-процессы
processes = [
    "Управление инцидентами",
    "Управление ИТ-проектами",
    "Информационная безопасность",
    "DevOps / CI-CD процессы",
    "Управление знаниями"
]

# Важность для бизнеса (1–10)
importance = [8, 9, 8, 10, 6]

# Текущий уровень зрелости (1–5)
current = [2, 3, 1, 2, 1]

# Целевой уровень зрелости (1–5)
target = [4, 5, 3, 4, 3]

plt.figure(figsize=(10,6))
plt.title("Диаграмма зрелости ИТ-процессов компании Mundfish", fontsize=13)
plt.xlabel("Важность для бизнеса (1–10)", fontsize=11)
plt.ylabel("Уровень зрелости (1–5)", fontsize=11)

# Синие точки — текущее состояние
plt.scatter(importance, current, color='blue', label='Текущее состояние (С)', s=100)

# Красные точки — целевое состояние
plt.scatter(importance, target, color='red', label='Целевое состояние (Ц)', s=100)

# Соединяем точки каждого процесса пунктиром
for i in range(len(processes)):
    plt.plot([importance[i], importance[i]], [current[i], target[i]], 'k--', alpha=0.7)
    plt.text(importance[i]+0.15, current[i]-0.2, processes[i], fontsize=9)

plt.xlim(5,10.5)
plt.ylim(0,5.5)
plt.legend()
plt.grid(True)
plt.show()
