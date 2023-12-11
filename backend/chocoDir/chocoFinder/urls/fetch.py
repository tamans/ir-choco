# from django.urls import path
# from ..view.chocolate_1 import get_choco

# urlpatterns = [
#     path("api/choco/get-choco/<str:query>/", get_choco, name="get_choco"),
    
# ]

# urls.py
from django.urls import path
# from ..views import index_and_search_chocolates
from ..view.chocolate_1 import get_choco


# urlpatterns = [
#     path("get-choco/<str:query>/", get_choco, name="index_and_search_chocolates"),
# ]

urlpatterns = [
    path("api/chocolate/get-choco/<str:query>/", get_choco, name="get_choco"),
]

# from django.urls import path
# from ..views.searchs import get_documents, get_recommended

# urlpatterns = [
#     path("get-documents/<str:query>/", get_documents, name="get-documents"),
#     path("get-recomended/", get_recommended, name="get-recommended"),
# ]
