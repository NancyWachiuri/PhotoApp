from django.urls import path
from . import views
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('', views.gallery, name = 'gallery'),
    path ('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/',views.addPhoto, name='add'),
    path('search/', views.search_results, name='search_results'),
    path('location/<int:location_id>/', views.location, name='location'),
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)