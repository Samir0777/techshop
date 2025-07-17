from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sign_in/', views.sign_in, name='sign_in'),    # <--- добавили
    path('sign_up/', views.sign_up, name='sign_up'),    # <--- добавили
    path('sign_out/', views.sign_out, name='sign_out'), # <--- если нужно выйти
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
