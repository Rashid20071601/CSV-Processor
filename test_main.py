# Импорты
import pytest
import sys
from main import filter_rows, aggregate_column, main



# Тестовые данные
rows = [
    {"name": "iphone", "brand": "apple", "price": "999", "rating": "4.9"},
    {"name": "galaxy", "brand": "samsung", "price": "1199", "rating": "4.8"},
    {"name": "poco", "brand": "xiaomi", "price": "299", "rating": "4.4"},
]



# Проверка фильтрации по условию price > 750
def test_filter_price_gt():
    result = filter_rows(rows, "price>750")
    assert len(result) == 2


# Проверка фильтрации по условию price < 750
def test_filter_price_lt():
    result = filter_rows(rows, "price<750")
    assert len(result) == 1
    assert result[0]["name"] == "poco"


# Проверка фильтрации по полю name
def test_filter_name():
    result = filter_rows(rows, "name=iphone")
    assert result[0]["brand"] == "apple"


# Проверка фильтрации по полю brand
def test_filter_brand():
    result = filter_rows(rows, "brand=samsung")
    assert result[0]["name"] == "galaxy"



# Проверка агрегации: среднее значение price
def test_aggregate_avg():
    rows = [
        {"price": "100"},
        {"price": "200"},
        {"price": "300"},
    ]
    result = aggregate_column(rows, "price=avg")
    assert result == 200


# Проверка агрегации: минимальное значение price
def test_aggregate_min():
    rows = [
        {"price": "100"},
        {"price": "200"},
        {"price": "300"},
    ]
    result = aggregate_column(rows, "price=min")
    assert result == 100


# Проверка агрегации: максимальное значение price
def test_aggregate_max():
    rows = [
        {"price": "100"},
        {"price": "200"},
        {"price": "300"},
    ]
    result = aggregate_column(rows, "price=max")
    assert result == 300



# Интеграционный тест: проверка полного запуска скрипта с агрегацией
def test_main_output(monkeypatch, capsys):
    # Эмулируем аргументы командной строки
    monkeypatch.setattr(sys, "argv", ["main.py", "data.csv", "--aggregate", "price=avg"])

    # Запускаем main
    main()

    # Захватываем вывод в консоль
    capture = capsys.readouterr()

    # Проверяем, что вывод содержит нужные строки
    assert "Aggregate" in capture.out
    assert "Value" in capture.out
    assert any(char.isdigit() for char in capture.out)
