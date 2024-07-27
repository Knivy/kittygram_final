Проект сайта Kittygram для загрузки фотографий котов. Июль 2024.

![Workflow badge!](https://github.com/Knivy/kittygram_final/actions/workflows/main.yml/badge.svg)

# Команда

Код проекта предоставлен Яндекс Практикумом. 

Деплой в контейнерах и CI/CD выполнила Альбина Гилязова. 

Ревьюер: Денис Унтевский.

Наставники: Николай Минякин, Ритис Бараускас.

# Технологии

Github Actions, Docker, docker-compose, Nginx, Django, Redis

# Как запустить на удаленном сервере

На удаленном сервере установите и настройте nginx так, чтобы он перенаправлял запросы в контейнер с проектом. 

Оформите файл .env в соответствии с примером .env.example в папке kittygram.

Форкните и склонируйте репозиторий с помощью git clone. 

Настройте секреты Github Actions.

Сделайте пуш в ветку main, чтобы запустить workflow. 

Сайт должен стать доступен по адресу в настройках.

# Как запустить проект на локальном сервере

Установить и запустить Docker Desktop на Windows/Mac или docker и docker compose на Linux
Склонировать проект
```
git clone https://github.com/Knivy/kittygram_final.git
```

В терминале в корне проекта выполнить:

```
docker compose up
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/  
```

Проект будет доступен по адресу http://localhost:9000

# Пример запроса к API при локальном подключении

При переходе по адресу http://localhost:9000/api/cats должен отобразиться список котов.
