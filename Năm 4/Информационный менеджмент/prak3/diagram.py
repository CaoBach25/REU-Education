import matplotlib.pyplot as plt

# --- Dữ liệu hệ thống và màu sắc ---
systems = {
    "Forge Platform": "#1f77b4",   # Xanh lam
    "AtomConnect CRM": "#2ca02c",  # Xanh lá
    "Help Desk 2.0": "#ff7f0e",    # Cam
    "AtomChain Web3": "#9467bd"    # Tím
}

# --- Tọa độ cho từng năm ---
data_2025 = {
    "Forge Platform": (4, 7),
    "AtomConnect CRM": (3, 6),
    "Help Desk 2.0": (2, 5),
    "AtomChain Web3": (2, 4)
}

data_2027 = {
    "Forge Platform": (9, 9),
    "AtomConnect CRM": (8, 8),
    "Help Desk 2.0": (7, 7),
    "AtomChain Web3": (7, 6)
}

# --- Kích thước vòng tròn (bubble size) ---
sizes_2025 = [200, 180, 150, 130]
sizes_2027 = [300, 250, 220, 200]

plt.figure(figsize=(10, 6))
plt.title("Диаграмма текущего и планируемого состояния ИТ-сервисов (Mundfish)", fontsize=12)
plt.xlabel("Важность для бизнеса (1–10)", fontsize=11)
plt.ylabel("Уровень зрелости (1–10)", fontsize=11)

# --- Vẽ các điểm ---
for i, (system, color) in enumerate(systems.items()):
    x2025, y2025 = data_2025[system]
    x2027, y2027 = data_2027[system]
    
    # Hình tròn cho năm 2025
    plt.scatter(x2025, y2025, s=sizes_2025[i], color=color, alpha=0.5, label=f"{system} 2025")
    
    # Hình vuông cho năm 2027
    plt.scatter(x2027, y2027, s=sizes_2027[i], color=color, marker='s', alpha=0.7, label=f"{system} 2027")

# --- Thiết lập khung ---
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(title="Системы", loc='lower right', fontsize=8, frameon=False)
plt.tight_layout()
plt.show()
