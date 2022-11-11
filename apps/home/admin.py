# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from  .models import *

# Register your models here.

admin.site.register(Merchant)
admin.site.register(Paymant_system)
admin.site.register(Status)
admin.site.register(Card)
admin.site.register(Transaction)
admin.site.register(Tarif)
admin.site.register(Payment)
admin.site.register(Transfer)