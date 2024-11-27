import hashlib

def hash_password(password: str) -> str:
    # Преобразуем пароль в хэш-строку с использованием SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

# Пример регистрации пользователя
stored_password_hash = hash_password("my_secure_password")  # Сохраняем хэш в базе
print(f"Хэш пароля: {stored_password_hash}")