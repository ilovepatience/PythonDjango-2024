from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.page1, name='Main'),
    path('aboutpage/', views.page2, name='About'),
    path('', views.article_list, name='article_list'),
    path('article/new/', views.article_create, name='article_create'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
    path('article/edit/<int:id>/', views.edit_article, name='edit_article')
]
