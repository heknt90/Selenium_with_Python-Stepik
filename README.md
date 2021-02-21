# Привет, дружище)

Этот репозиторий создан в рамках выполнения задачи из курса "Автоматизация тестирования с помощью Selenium и Python"

[Ссылка на задачу](https://stepik.org/lesson/187065/step/11?unit=161976)

Но на всякий случай я оставлю здесь примеры решения других задач этого курса
Возможно они кому то пригодятся (не исключено, что и мне самому)

## Вместо документации

[Шпаргалки](docs/README.md)

## Установка драйверов

Для работы с каждым из браузеров требуется скачивание нужного драйвера.
Драйвер достаточно разместить в некоторой папке на компьютере, например

    C:\webdrivers

После чего прописать этот путь в системной переменной PATH

### Список драйверов

- для Google Chrome - [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- для Mozilla Firefox - [geckodriver](https://github.com/mozilla/geckodriver/releases)

## Настройка окружения

Для установки виртуального окружения (на Windows)

    python3 -m venv environments/selenium_env

Для активации виртуального окружения (на Windows)

    ./environments/selenium_env/Scripts/activate

## Установка библиотек

Установка библиотек (требует установленного python 3.6+).
Для запуска автоматической установки библиотек из файла, воспользуйтесь командой:

    pip install -r requirements.txt

## Запуск тестов

    pytest path-to-file
    pytest -s -v --setup-show path-to-file

запуск тестов маркированных метками (например smoke, regression)

    pytest -s -v -m <mark> path-to-file
