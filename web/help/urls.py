from django.urls import path
from django.contrib import admin
from help import views
from . import views

urlpatterns = [
    path('save-recording/', views.save_recording, name='save_recording'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('get-recordings/', views.get_recordings, name='get_recordings'),
]
