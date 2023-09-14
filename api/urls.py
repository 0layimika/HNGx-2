from django.urls import path
from .views import *
urlpatterns=[
    path('',PersonListCreateView.as_view(),name='create'),
    path('<str:lookup_field>/',PersonDetailView.as_view(),name='edit')
]