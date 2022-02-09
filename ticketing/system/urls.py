from django.urls import URLPattern, path,include
from . import views

#URLConf
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('tickets/', views.my_tickets_view, name='my_tickets_view'),
    path('tickets/', views.department_tickets_view, name='.department_tickets_view'),
    path('tickets/', views.operator_tickets_view, name='operator_tickets_view')
]