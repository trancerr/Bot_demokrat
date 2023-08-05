from typing import List

from democrat_admin.bot_manage.models import User, CurrentStocks, Referral, Mailing
from asgiref.sync import sync_to_async

"""Команды управления пользователями"""


@sync_to_async
def select_user(user_id: int):
    user = User.objects.filter(user_id=user_id).first()
    return user


@sync_to_async
def add_user(user_id, full_name, username):
    try:
        return User(user_id=int(user_id), name=full_name, user_name=username).save()
    except Exception:
        return select_user(int(user_id))


@sync_to_async
def select_all_users():
    users = User.objects.all()
    return users


@sync_to_async
def count_users():
    return User.objects.all().count()


"""Команды управления акциями"""


@sync_to_async()
def select_all_stocks():
    stocks = CurrentStocks.objects.all()
    return stocks


@sync_to_async()
def select_stock(id: int):
    stock = CurrentStocks.objects.filter(id=id).first()
    return stock


@sync_to_async()
def get_name_stocks() -> List[CurrentStocks]:
    return CurrentStocks.objects.distinct("name")


"""
Команды управления рассылками
"""


@sync_to_async()
def select_all_mailings():
    mailings = Mailing.objects.all()
    return mailings


@sync_to_async()
def select_mailing(id: int):
    mailing = Mailing.objects.filter(id=id).first()
    return mailing


@sync_to_async()
def add_mailing(mailing_name, mailing_description, mailing_image, date_of_publication):
    return Mailing(mailing_name=mailing_name,
                   mailing_description=mailing_description,
                   mailing_image=mailing_image,
                   date_of_publication=date_of_publication
                   ).save()
