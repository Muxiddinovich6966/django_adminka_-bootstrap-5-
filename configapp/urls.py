from django.urls import path,include
from configapp.views import *

urlpatterns = [
    path('app/',app )
]
