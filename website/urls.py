from django.urls import path
from .views import *
from django.urls import include
urlpatterns = [
    path('items', IotItemsView.as_view(), name='iot_list'),
    path('items/<int:port>', IotItemsView.as_view()),
    path('arduino', arduino_get)
]