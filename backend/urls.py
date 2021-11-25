from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('',views.home, name='homepage'),
    path('index/',views.index, name='index'),
    path('home/',views.home, name='homepage'),
    path('single/<slug:slug>',views.single, name='single'),
    path('about/', views.about, name='about' ),
    path('Direktor/', views.Direktor, name='Direktor' ),
    path('home/Direktor/', views.Direktor, name='Direktor' ),
    path('Rahbariyat/', views.Rahbariyat, name='Rahbariyat' ),
    path('home/Rahbariyat/', views.Rahbariyat, name='Rahbariyat' ),
    path('IT_ticher/', views.IT_ticher, name='IT_ticher' ),
    path('home/IT_ticher/', views.IT_ticher, name='IT_ticher' ),
]