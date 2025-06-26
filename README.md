# CSV Processor

Скрипт для обработки CSV-файлов с поддержкой фильтрации и агрегации.

## 📦 Установка

```bash
pip install -r requirements.txt
```

## Примеры запуска
Фильтрация и агрегация:

```bash
python main.py data.csv --where "price>500" --aggregate "rating=avg"
```


Только фильтрация:

```bash
python main.py data.csv --where "brand=xiaomi"
```


Только агрегация:

```bash
python main.py data.csv --aggregate "price=max"
```


## Поддерживаемые опции

| Аргумент      | Описание                                            |
| ------------- | --------------------------------------------------- |
| `filename`    | Путь к CSV-файлу                                    |
| `--where`     | Условие фильтрации (>, <, =)                        |
| `--aggregate` | Агрегация: `column=avg`, `column=min`, `column=max` |
