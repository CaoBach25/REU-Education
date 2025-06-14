import requests
from datetime import datetime
import time

# Преобразование даты в метку времени (в миллисекундах)
def get_timestamp(date):
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d")
        return int(date_object.timestamp() * 1000)
    except ValueError:
        print("Неверный формат даты. Используйте ГГГГ-ММ-ДД.")
        return None

# Получение списка блоков за указанную дату
def get_blocks(date):
    timestamp = get_timestamp(date)
    if not timestamp:
        return None
    url = f"https://blockchain.info/blocks/{timestamp}?format=json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Не удалось загрузить данные блоков.")
            return None
    except requests.RequestException as e:
        print(f"Ошибка сети: {e}")
        return None

# Получение деталей блока
def get_block_details(block_hash):
    url = f"https://blockchain.info/rawblock/{block_hash}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Не удалось получить данные для блока {block_hash}.")
            return None
    except requests.RequestException as e:
        print(f"Ошибка сети: {e}")
        return None

# Анализ данных
def analyze_data(date):
    print(f"Загрузка данных за {date}...")
    blocks = get_blocks(date)
    if not blocks:
        print("Данные за эту дату отсутствуют.")
        return

    # Инициализация переменных
    total_transactions = 0
    blockchain_size_start = None
    blockchain_size_end = None
    block_times = []
    fifth_block_fees = None

    # Обход каждого блока
    for index, block in enumerate(blocks[:50]):  # Ограничение в 50 блоков
        block_details = get_block_details(block['hash'])
        if not block_details:
            continue

        # Подсчет общего числа транзакций
        total_transactions += len(block_details.get('tx', []))

        # Размер блокчейна
        if index == 0:
            blockchain_size_start = block_details['size']
        blockchain_size_end = block_details['size']

        # Время блока
        block_times.append(block_details['time'])

        # Средняя комиссия в пятом блоке
        if index == 4:  # Пятый блок
            transactions = block_details.get('tx', [])
            if transactions:
                fees = [tx.get('fee', 0) for tx in transactions]
                fifth_block_fees = sum(fees) / len(fees) if fees else "Нет данных"
            else:
                fifth_block_fees = "Нет данных"

        time.sleep(1)  # Пауза между запросами к API

    # Увеличение размера блокчейна
    size_increase = blockchain_size_end - blockchain_size_start if blockchain_size_start and blockchain_size_end else 0

    # Среднее время генерации блока
    if len(block_times) > 1:
        block_times.sort()
        average_time = (block_times[-1] - block_times[0]) / (len(block_times) - 1)
    else:
        average_time = "Недостаточно данных"

    # Вывод результатов
    print("\nРезультаты анализа:")
    print(f"Всего транзакций: {total_transactions}")
    print(f"Средняя комиссия в 5 блоке: {fifth_block_fees if fifth_block_fees else 'Недостаточно данных'}")
    print(f"Прирост размера блокчейна: {size_increase} байт")
    print(f"Среднее время генерации блока: {average_time if isinstance(average_time, float) else average_time}")
    print("Информация о майнерах недоступна в API Blockchain.info. (Ограничение API)")

# Ввод даты от пользователя
date_input = input("Введите дату (ГГГГ-ММ-ДД): ")
analyze_data(date_input)