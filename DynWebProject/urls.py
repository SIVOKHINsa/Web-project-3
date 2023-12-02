from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_home, name='homepage'),
    path('about', views.about, name='aboutpage'),
    path('contacts', views.contacts, name='contacts'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.newsdetailview.as_view(), name='detail'),
    path('<int:pk>/update', views.newsupdateview.as_view(), name='update'),
    path('<int:pk>/delete', views.newsdeleteview.as_view(), name='delete')
]
