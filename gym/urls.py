from django.urls import path
from .views import *

app_name = 'gym'


urlpatterns = [
    path('profile', ProfileViewSet.as_view({'get': 'list'}), name="profile"),
    path('exercises', ExercisesViewSet.as_view({'get': 'list'}), name="exercises"),
]
