from .import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register',views.sign_up,name="register"),
  
    path('home',views.home,name="home"),
    path('',views.log_in,name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('feedback',views.mess_page),
    path('lecturs/<lecture_title>/<lecture_slug>',views.lecture_page,name="lecture_page"),
    path('test',views.test)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


