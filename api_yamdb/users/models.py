from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Пользовательская модель User.
    Содержит следующие поля:
    - username (обязательное): логин, уникальное значение
    - email (обязательное): электронная почта, уникальное значение
    - first_name: имя
    - last_name: фамилия
    - bio: биография или инное описание
    - role: роль, определяющая права доступа.

    Пароль не является обязательным.
    """

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLE_CHOICE = (
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Отображаемое имя'
    )

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Электронная почта'
    )

    first_name = models.CharField(
        max_length=150, verbose_name='Имя', blank=True
    )

    last_name = models.CharField(
        max_length=150, verbose_name='Фамилия', blank=True
    )

    bio = models.TextField(verbose_name='Биография', blank=True)

    role = models.CharField(
        max_length=15,
        default=USER,
        choices=ROLE_CHOICE,
        verbose_name='Роль'
    )

    class Meta:
        ordering = ('id',)

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moder(self):
        return self.role == self.MODERATOR
