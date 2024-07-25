Проект сайта Kittygram для загрузки фотографий котов. Июль 2024.

![Workflow badge!](https://github.com/Knivy/kittygram_final/actions/workflows/main.yml/badge.svg)

# Команда

Код проекта предоставлен Яндекс Практикумом. 

Деплой в контейнерах и CI/CD выполнила Альбина Гилязова. 

Ревьюер: Денис Унтевский.

# Технологии

Github Actions, Docker, docker-compose

# Как запустить на удаленном сервере

На удаленном сервере установите и настройте nginx так, чтобы он перенаправлял запросы в контейнер с проектом. 

Оформите файл .env в соответствии с примером .env.example в папке kittygram.

Форкните и склонируйте репозиторий с помощью git clone. 

Настройте секреты Github Actions.

Сделайте пуш в ветку main, чтобы запустить workflow. 

Сайт должен стать доступен по адресу в настройках.

### Как запустить проект на локальном компьютере

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Knivy/kittygram_final.git
```

```
cd kittygram_final/backend
```

Cоздать и активировать виртуальное окружение:

* Если у вас Linux/macOS

    ```
    python3 -m venv env
    source env/bin/activate
    ```

* Если у вас windows

    ```
    python -m venv env
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Сайт должен стать доступен по адресу, который будет указан в выводе терминала.

# Пример запроса к API при локальном подключении

При переходе по адресу http://localhost/api/cats должен отобразиться список котов.
