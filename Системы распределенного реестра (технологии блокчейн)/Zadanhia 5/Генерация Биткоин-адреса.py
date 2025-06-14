import hashlib
from random import randint
from ecdsa import SECP256k1, SigningKey
from ripemd.ripemd160 import ripemd160
from base58 import b58encode

# Устанавливаем верхнюю границу для закрытого ключа
UPPER_LIMIT = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# Шаг 1: Генерация случайного 32-байтового закрытого ключа
privkey = bytes.fromhex(hex(randint(1, UPPER_LIMIT))[2:].zfill(64))
print(f"Закрытый ключ: {privkey.hex()}")

# Шаг 2: Генерация открытого ключа
s = SigningKey.from_string(privkey, curve=SECP256k1)
v = bytes.fromhex("04") + s.verifying_key.to_string()
print(f"Открытый ключ: {v.hex()}")

# Шаг 3: Вычисление SHA-256 хэша от открытого ключа
a = hashlib.sha256(v).digest()
print(f"SHA-256 хэш: {a.hex()}")

# Шаг 4: Вычисление RIPEMD-160 хэша от SHA-256 хэша
b = ripemd160(a)
print(f"RIPEMD-160 хэш: {b.hex()}")

# Шаг 5: Добавление версии (0x00 для основной сети)
c = bytes.fromhex("00") + b
print(f"С добавленной версией: {c.hex()}")

# Шаг 6: Первое SHA-256 хэширование
d = hashlib.sha256(c).digest()
print(f"SHA-256 (шаг 1): {d.hex()}")

# Шаг 7: Второе SHA-256 хэширование
e = hashlib.sha256(d).digest()
print(f"SHA-256 (шаг 2): {e.hex()}")

# Шаг 8: Добавление контрольной суммы
f = c + e[:4]
print(f"С контрольной суммой: {f.hex()}")

# Шаг 9: Кодирование в формате Base58
address = b58encode(f)
print(f"Bitcoin-адрес: {address.decode()}")