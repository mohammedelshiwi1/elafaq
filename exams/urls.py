from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .import views




urlpatterns = [path('quiz/<quiz_name>/<quiz_id>',views.quiz_detail,name="quiz_page")]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
