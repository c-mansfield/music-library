from django.urls import path
from . import views
from django.conf import settings

app_name = 'music'

urlpatterns = [

    # /music/
    path('', views.IndexView.as_view(), name='index'),

    # /music/
    path('register/', views.UserFormView.as_view(), name='register'),

    # /music/<album_id>/
    path('<int:pk>/', views.DetailsView.as_view(), name='detail'),

    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-del')

]
