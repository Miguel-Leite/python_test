from django.contrib import admin
from .models import Account, Moviment, Deposit


admin.site.register(Account)
admin.site.register(Moviment)
admin.site.register(Deposit)