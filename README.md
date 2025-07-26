# Древовидное меню для Django (тестовое задание)

Простая реализация древовидного меню, соответствующая ТЗ.

## Как это работает
### Основные компоненты

Модели:
- Menu - хранит название меню и slug
- MenuItem - элементы меню с возможностью вложенности

Template tag:
- draw_menu - отрисовывает меню по его slug
- Автоматически определяет активный пункт по URL

Админка: Стандартный интерфейс Django для управления меню

## Как использовать
1. Добавьте пункты меню через админку (/admin)
2. В шаблоне подключите тег и выведите меню:

```html
{% load draw_menu %}

{% draw_menu 'main_menu' %}
{% draw_menu 'sidebar_menu' %}
```

## Как запустить

```bash
git clone https://github.com/4frag/test_task2.git
cd test_task2
docker-compose up --build -d
```
И через пару секунд (надо подождать запуска PostgreSQL)
```bash
./restore-postgres.sh
```

зайти в админку можно по [ссылке](http://localhost/admin/)
login - test
password - test

небольшое готовое меню [тут](http://localhost/menu/main/)

