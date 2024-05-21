# app/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),  # Örnek bir URL tanımı
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blogs/<str:categori>/', views.detail_categori, name='detail_categori'),
    # path('blog_details/', views.blog_details, name='blog_details'),
    path("blog_details/<int:question_id>/", views.detail, name="detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)