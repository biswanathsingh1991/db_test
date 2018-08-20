
from django.contrib import admin
from django.urls import path, include
from .views import Test1, Allalbum, AllAlbumApi


app_name = "db_app"
urlpatterns = [

    path('', Test1.as_view(), name="test1"),
    path('allalbum/', Allalbum.as_view(), name="allalbum"),
    path('allalbumapi/', AllAlbumApi.as_view(), name="allalbumapi"),


]
