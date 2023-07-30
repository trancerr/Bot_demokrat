from django.contrib import admin

from .models import User, Referral, CurrentStocks, Mailing


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'user_name', 'created_at')


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('id', 'referrer_id', 'created_at')


@admin.register(CurrentStocks)
class CurrentStocksAdmin(admin.ModelAdmin):
    list_display = ('id', 'stock_name', 'stock_description', 'stock_image', 'created_at')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'mailing_name', 'mailing_description', 'mailing_image', 'created_at')
