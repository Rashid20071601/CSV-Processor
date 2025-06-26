# Импорты
import csv
import argparse
import pytest
from tabulate import tabulate



def main():
    # Разбор аргументов командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Путь к csv файлу")
    parser.add_argument("--where", help="Фильтрация")
    parser.add_argument("--aggregate", help="Агрегация")
    args = parser.parse_args()

    rows = csv_reader("data.csv")
    
    # Применение фильтрации, если передан аргумент --where
    if args.where:
        rows = filter_rows(rows, args.where)

    # Применение агрегации, если передан аргумент --aggregate
    if args.aggregate:
        result = aggregate_column(rows, args.aggregate)
        print(tabulate([["Aggregate", result]], headers=["Column", "Value"]))
    else:
        print(tabulate(rows, headers="keys"))



def csv_reader(filename: str) -> list[dict[str: str]]:
    # Чтение CSV-файла и преобразование в список словарей
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)



def filter_rows(rows: list[dict[str: str]], condition: str) -> list[dict[str: str]]:
    result = []

    # Определение операторов и разбивка строк на колонку и значение
    for op in ("=", ">", "<"):
        if op in condition:
            column, value = condition.split(op)
            break

    # Применение фильтраций по условию
    for row in rows:
        if op == "=" and row[column] == value:
            result.append(row)
        elif op == ">" and float(row[column]) > float(value):
            result.append(row)
        elif op == "<" and float(row[column]) < float(value):
            result.append(row)

    return result



def aggregate_column(rows: list[dict[str: str]], instruction: str) -> float:
    column, operation = instruction.split('=')

    # Преобразование значений колонки в числа
    try:
        values = [float(row[column]) for row in rows]
    except ValueError:
        raise ValueError(f"Невозможно агрегировать столбец '{column}': содержит нечисловые значения")

    # Выполние агрегаций
    operations = ['avg', 'min', 'max']
    if operation in operations:
        if operation == 'avg':
            return sum(values) / len(values)
        elif operation == 'min':
            return min(values)
        elif operation == 'max':
            return max(values)
    else:
        raise ValueError(f"Неизвестная операция: {operation}")



if __name__ == "__main__":
    main()
