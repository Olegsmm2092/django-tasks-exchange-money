# django-tasks-exchange-money

<!-- python -m pip install -U pip -->
<!-- pip install -r requirements.txt -->

django-admin startproject app
django-admin startapp exchange_money

mkdir -pv templates/exchange_money/index.html

<!-- base.html -->
+shift +d

<!-- model -->
nano /app/exchange_money/urls.py
+c +v at site urls.py

add - from .views import def

<!-- nano /app/setting.py -->
INSTALLED_APPS = [
    'exchange_money.apps.ExchangeMoneyConfig',

<!-- shell -->
>>> check
>>> migrate
