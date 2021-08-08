from django.urls import path
from . import views

urlpatterns = [
    path('', views.universite_listele, name='universite_listele'),
    path('<int:pk>/', views.universite_goster, name='universite_goster'),
    path('<int:pk>/duzenle/', views.universite_duzenle, name='universite_duzenle'),
    path('yeni/', views.universite_yeni, name='universite_yeni'),
]
