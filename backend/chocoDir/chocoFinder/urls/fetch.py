# from django.urls import path
# from ..view.chocolate_1 import get_choco

# urlpatterns = [
#     path("api/choco/get-choco/<str:query>/", get_choco, name="get_choco"),
    
# ]

# urls.py
from django.urls import path
from ..views import index_and_search_chocolates

urlpatterns = [
    path("search-chocolates/<str:query>/", index_and_search_chocolates, name="index_and_search_chocolates"),
    # Add other urlpatterns as needed
]
