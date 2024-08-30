from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('api/', GetData.as_view(), name='api')
]