# Проект Foodgram, "Продуктовый помощник"

![foodgram_workflow](https://github.com/shogun500/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)


## Как запустить проект:

##
- Склонировать репозиторий:

```
bash
git clone <название репозитория>
```
##

### Создайте в .env-файл в папке infra и заполните по образцу.
```
DB_ENGINE=<...>
DB_NAME=<...>
POSTGRES_USER=<...>
POSTGRES_PASSWORD=<...>
DB_HOST=<...>
DB_PORT=<...>
SECRET_KEY=<...>
```
### Собрать и запустить контейнер с помощью Docker-compose
```
docker-compose up --build
```
### Выполнить миграции через Docker-compose
```
docker-compose exec web python manage.py migrate
```
### Собрать через Docker-compose статику
```
docker-compose exec web python manage.py collectstatic --no-input
```
### Создать суперпользователя
```
docker-compose exec web python manage.py createsuperuser
```
### Заполнить базу начальными данными
```
docker-compose exec backend python3 manage.py load_data
```
### Доступ к ресурсы
```
Проект доступен по адресу: http://http://84.201.154.23/recipes
```

## Используемые технологии
![Alt-Текст](https://img.shields.io/badge/python-3.8-blue)
![Alt-Текст](https://img.shields.io/badge/django-2.2.20-blue)
![Alt-Текст](https://img.shields.io/badge/djangorestframework-3.12.4-blue)
![Alt-Текст](https://img.shields.io/badge/docker-20.10.16-blue)
![Alt-Текст](https://img.shields.io/badge/nginx-1.21.3-blue)
![Alt-Текст](https://img.shields.io/badge/gunicorn-20.0.4-blue)

## Автор

<a href=https://github.com/shogun500>Sergey Pavlov</a>