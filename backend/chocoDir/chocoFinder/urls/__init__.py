from django.urls import path, include

urlpatterns= [
    #everytime i see this path i know i will ned to call this fetch
    path("chocolate/", include("chocoFinder.urls.fetch"), name="index_and_search_chocolates"),

]