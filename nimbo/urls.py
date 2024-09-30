# urls.py
from django.urls import path
from .views import MachineListCreateView, MachineRetrieveUpdateDestroyView

urlpatterns = [
    path('machines/', MachineListCreateView.as_view(), name='machine-list-create'),
    path('machines/<int:pk>/', MachineRetrieveUpdateDestroyView.as_view(),
         name='machine-detail'),
]
