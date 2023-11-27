from django.urls import path

urlpatterns = [
    path("get-chocolates/<str:query>/", get_choco, name = "get-choco"),
]