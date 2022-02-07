from django.urls import URLPattern, path,include
from . import views

#URLConf
urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
]