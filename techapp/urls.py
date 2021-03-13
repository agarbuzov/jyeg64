from django.urls import path
from .views import DataCreate, DataRead

urlpatterns = [
    path('create/', DataCreate.as_view(), name='DataCreate'),
    path('read/', DataRead.as_view(), name='DataRead'),
]
