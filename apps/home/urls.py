# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home.views import index, transfers, pay_history


app_name = 'home'
urlpatterns = [

    # The home page
    path('', index, name='home'),
    path('transfers/', transfers, name='transfers'),
    path('pay_history/', pay_history, name='paymant_history'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
