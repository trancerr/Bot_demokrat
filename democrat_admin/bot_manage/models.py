from django.db import models

"""
Класс модели обязательных колонок создания и апдейта записи
"""


class TimeBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""
Класс модели пользователей
"""


class User(TimeBaseModel):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, default=1, verbose_name='ID пользователя телеграм')
    name = models.CharField(max_length=250, verbose_name='Имя пользователя', null=True)
    user_name = models.CharField(max_length=150, verbose_name='Username телеграм')
    user_email = models.CharField(max_length=100, verbose_name='Email', null=True)


"""
Класс модели текущих акций
"""


class CurrentStocks(TimeBaseModel):
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Текущие акции'

    id = models.AutoField(primary_key=True)
    stock_name = models.CharField(max_length=250, verbose_name='Заголовок акции')
    stock_description = models.TextField(max_length=500, verbose_name='Описание акции')
    stock_image = models.TextField(max_length=250, verbose_name='ID изображения акции')


"""
Класс модели рассылки
"""


class Mailing(TimeBaseModel):
    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    id = models.AutoField(primary_key=True)
    mailing_name = models.CharField(max_length=250, verbose_name='Заголовок рассылки')
    mailing_description = models.TextField(max_length=500, verbose_name='Описание рассылки')
    mailing_image = models.TextField(max_length=250, verbose_name='ID изображения рассылки')
