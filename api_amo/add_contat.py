from amocrm.v2 import Lead as _Lead, custom_field
from api_amo.connect_api_amo import connect_amo
from asgiref.sync import sync_to_async


class Lead(_Lead):
    Source_phone = custom_field.TextCustomField("Source_phone")


@sync_to_async()
def add_contact(name: str, phone: str):
    connect_amo()
    create_contact = Lead.objects.create(name=name)
    create_contact.Source_phone = phone
    create_contact.save()

