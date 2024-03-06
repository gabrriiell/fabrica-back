from.import views
from django.urls import path

urlpatterns = [
    path('cep/<str:cep',views.get_cep_info)
]
