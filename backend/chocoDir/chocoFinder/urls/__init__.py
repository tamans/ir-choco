from django.urls import path, include

urlpatterns= [
    #everytime i see this path i know i will ned to call this fetch
    path("choco/", include("chocoFinder.urls.fetch"), name="get-choco"),
]