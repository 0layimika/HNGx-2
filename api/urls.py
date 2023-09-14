from django.urls import path
from .views import *
urlpatterns=[
    path('',PersonListCreateView.as_view(),name='create'),
    path('<int:pk>/',PersonDetailView.as_view(),name='edit')
]