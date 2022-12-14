# Проект YaMDb

### Описание проекта

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории, например, «Книги», «Фильмы», «Музыка». Список категорий может быть меняться администратором.
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр из списка предустановленных. Новые жанры может создавать только администратор.
Пользователи могут оставлять к произведениям текстовые отзывы и ставить произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.


### Настройка проекта

1. Установить виртуальное окружение: python3 -m venv venv
2. Активировать виртуальное окружение: source venv/bin/activate
3. Установить зависимости: pip install -r requirements.txt
4. Выполнить миграции: python3 api_yamdb/manage.py migrate


### Пользовательские роли

1. Пользователь: может просматривать списки категорий, жанров, а также изучать информацию о произведениях. Также может писать отзывы на произведения и комментарии к отзывам. Может редактировать и/или удалять собственные отзывы и комментарии.
2. Модератор: обладает теми же правами, что и пользователь, но дополнительно имеет права на изменение и/или удаление отзывов и комментариев любых других пользователей.
3. Администратор: в дополнение к правам модератора может добавлять/удалять категории и жанры, добавлять/удалять произведения, регистрировать и удалять новых пользователей, менять роли пользователям.


### Ресурсы

1. Ресурс auth (auth/): аутентификация.
2. Ресурс users (users/): пользователи.
3. Ресурс categories (categories/): категории (типы) произведений («Фильмы», «Книги», «Музыка»).
4. Ресурс genres (genres/): жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
5. Ресурс titles (titles/): произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
6. Ресурс reviews (titles/id/reviews/): отзывы на произведения. Отзыв привязан к определённому произведению.
7. Ресурс comments (titles/id/reviews/id/comments/): комментарии к отзывам. Комментарий привязан к определённому отзыву.


### Регистрация авторизация

1. Пользователь отправляет POST-запрос с параметрами "email" и "username" на эндпоинт /api/v1/auth/signup/.
2. Сервис YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на указанный адрес email.
3. Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).


### Технологии

* PYTHON
* DJANGO
* DJANGO REST FRAMEWORK
* JWY


### Документация к API

ReDoc/