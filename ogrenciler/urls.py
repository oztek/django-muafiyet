from django.urls import path
from . import views

urlpatterns = [
    path('', views.ogrenci_listele, name='ogrenci_listele'),
    #path('', views.ogrenci_goster, name='ogrenci_goster'),
    path('ogrenci/goster/', views.ogrenci_goster, name='ogrenci_goster'),
    path('ogrenci/ayrinti/<int:pk>', views.ogrenci_ayrinti, name='ogrenci_ayrinti'),
    path('ogrenci/duzenle/<int:pk>/', views.ogrenci_duzenle, name='ogrenci_duzenle'),
    path('ogrenci/yeni/', views.ogrenci_yeni, name='ogrenci_yeni'),
    path('ogrenci/ders/ekle/<int:pk>/', views.ogrenci_ders_ekle, name='ogrenci_ders_ekle'),
    path('bos', views.ogrenci_bos, name='ogrenci_bos'),
    #path('universite/<int:pk>/', views.universite_goster, name='universite_goster'),
    #path('universite/<int:pk>/duzenle/', views.universite_duzenle, name='universite_duzenle'),
    #path('universite/yeni/', views.universite_yeni, name='universite_yeni'),
]