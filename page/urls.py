from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'page'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('who/', views.who, name='who'),
    path('merge/', views.merge, name='merge'),
    path('mixed/<str:name>', views.mixed, name='mixed'),
    path('mixed_all/<str:name1>/<str:name2>/<str:name3>', views.mixed_all, name='mixed_all'),
    path('photo_list',views.photo_list,name='photo_list'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)