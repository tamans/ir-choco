# urls.py
from django.urls import path
from ..view.chocolate_1 import get_choco


urlpatterns = [
    path("api/chocolate/get-choco/<str:query>/", get_choco, name="get_choco"),
]