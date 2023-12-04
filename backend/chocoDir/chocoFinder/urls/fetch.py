from django.urls import path
from ..views.chocolate_1 import get_choco

urlpatterns = [
    path("get-chocolates/<str:query>/", get_choco, name = "get-choco"),
    
]