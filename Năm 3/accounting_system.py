import sqlite3
from datetime import datetime

# Подключение к базе данных
def connect_db():
    return sqlite3.connect("бухгалтерия.db")

# Создание таблиц в базе данных
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Создание таблицы счетов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS счета (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            название TEXT NOT NULL,
            тип TEXT NOT NULL,
            баланс REAL DEFAULT 0
        )
    ''')

    # Создание таблицы транзакций
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS транзакции (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            дебет_счет INTEGER,
            кредит_счет INTEGER,
            сумма REAL NOT NULL,
            дата TEXT NOT NULL,
            описание TEXT,
            FOREIGN KEY(дебет_счет) REFERENCES счета(id),
            FOREIGN KEY(кредит_счет) REFERENCES счета(id)
        )
    ''')

    conn.commit()
    conn.close()

# Добавление нового счета
def add_account(name, acc_type):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO счета (название, тип)
        VALUES (?, ?)
    ''', (name, acc_type))
    conn.commit()
    conn.close()
    print(f"Счет '{name}' успешно добавлен.")

# Добавление транзакции
def add_transaction(debit_account, credit_account, amount, description=""):
    conn = connect_db()
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Добавление транзакции
    cursor.execute('''
        INSERT INTO транзакции (дебет_счет, кредит_счет, сумма, дата, описание)
        VALUES (?, ?, ?, ?, ?)
    ''', (debit_account, credit_account, amount, date, description))

    # Обновление баланса счетов
    cursor.execute('UPDATE счета SET баланс = баланс - ? WHERE id = ?', (amount, debit_account))
    cursor.execute('UPDATE счета SET баланс = баланс + ? WHERE id = ?', (amount, credit_account))

    conn.commit()
    conn.close()
    print("Транзакция успешно добавлена.")

# Генерация финансового отчета
def generate_report():
    conn = connect_db()
    cursor = conn.cursor()

    # Получение балансов счетов
    cursor.execute('SELECT id, название, тип, баланс FROM счета')
    accounts = cursor.fetchall()

    print("\n--- Финансовый отчет ---")
    for acc in accounts:
        print(f"Счет: {acc[1]} ({acc[2]}) - Баланс: {acc[3]:,.2f} руб.")
    print("-----------------------")

    conn.close()

# Меню программы
def menu():
    while True:
        print("\n--- Простая бухгалтерская система ---")
        print("1. Создать таблицы")
        print("2. Добавить новый счет")
        print("3. Добавить транзакцию")
        print("4. Сгенерировать финансовый отчет")
        print("5. Выйти")

        choice = input("Выберите опцию: ")
        if choice == "1":
            create_tables()
            print("Таблицы в базе данных успешно созданы.")
        elif choice == "2":
            name = input("Введите название счета: ")
            acc_type = input("Введите тип счета (Актив/Пассив): ")
            add_account(name, acc_type)
        elif choice == "3":
            debit_account = int(input("Введите ID дебетового счета: "))
            credit_account = int(input("Введите ID кредитового счета: "))
            amount = float(input("Введите сумму транзакции: "))
            description = input("Введите описание транзакции (необязательно): ")
            add_transaction(debit_account, credit_account, amount, description)
        elif choice == "4":
            generate_report()
        elif choice == "5":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    menu()