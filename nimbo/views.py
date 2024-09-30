# views.py
from rest_framework import generics
from .models import Machine
from .serializers import MachineSerializer


class MachineListCreateView(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class MachineRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
