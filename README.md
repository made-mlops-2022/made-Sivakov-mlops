# Homework2
Смотри ридми в online_inference

# Homework1

## Интро к домашней работе
Очень хотелось написать красивое масштабируемое решение. В итоге вместо домашки начал делать мини-фреймворк, 
что привело к проблемам.

К сожалению, получилось далеко не все из задуманного. Я хотел написать продакшн код, но из-за нехватки времени 
дописывал уже костылями. Прошу отнестись с пониманием(

### Как запустить базовый пайплайн (состоит из всех этапов сразу)
`docker-compose build
`

`
docker-compose up
`
### Структура проекта
Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── predictions    <- Конечные предсказания моделей в .csv файлах
    │   ├── preprocessed_data   <- Обработанные данные
    │   ├── source_data      <- Начальные данные
    │   └── splitted_data            <- Поделенные данные на трейн/вал.
    │
    │
    ├── ml_project
    |   |── confs - <- Конфиги для обучения модели, для предсказания и препроцессинга. (на каждый этап пайплайна)
    |   |── models - <- Все компоненты пайплайна
    |   |── logger_conf.py - <- Настройка логгера
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    |── full_pipeline_example.py   <- Пример как может работать собранные блоки вместе


--------