#!/usr/bin/env python3
"""
Скрипт для инициализации базы данных
"""
import os
import subprocess
import sys

def run_command(command):
    """Выполнить команду и вывести результат"""
    print(f"Выполняется: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Ошибка: {result.stderr}")
        return False
    print(f"Результат: {result.stdout}")
    return True

def main():
    """Основная функция инициализации"""
    print("Инициализация базы данных...")
    
    # Проверяем наличие переменной окружения DATABASE_URL
    if not os.getenv("DATABASE_URL"):
        print("Установка DATABASE_URL по умолчанию...")
        os.environ["DATABASE_URL"] = "postgresql://user:password@localhost:5432/organizations_db"
    
    # Создаем первую миграцию
    print("Создание первой миграции...")
    if not run_command("alembic revision --autogenerate -m 'Initial migration'"):
        print("Ошибка при создании миграции")
        return False
    
    # Применяем миграцию
    print("Применение миграции...")
    if not run_command("alembic upgrade head"):
        print("Ошибка при применении миграции")
        return False
    
    # Заполняем тестовыми данными
    print("Заполнение тестовыми данными...")
    if not run_command("python seed_data.py"):
        print("Ошибка при заполнении данными")
        return False
    
    print("Инициализация завершена успешно!")

if __name__ == "__main__":
    main()
