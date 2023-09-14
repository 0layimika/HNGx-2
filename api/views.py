from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serializers import personserializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.http import JsonResponse
class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = personserializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = personserializer
    lookup_field = 'lookup_field'

    def get_object(self):

        lookup_value = self.kwargs.get(self.lookup_field)
        if lookup_value.isdigit():
            return get_object_or_404(Person, pk=lookup_value)
        else:
            return get_object_or_404(Person, name=lookup_value)