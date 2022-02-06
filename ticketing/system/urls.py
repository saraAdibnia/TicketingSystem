from django.urls import URLPattern, path
from . import views

#URLConf
urlpatterns = [
    path('user/', views.user, name='user'),
    path('department/', views.department, name='user'),
    path('file/', views.file, name='user'),
    path('answer/', views.answer, name='user'),
    path('ticket/', views.ticket, name='user'),
]