from django.urls import path
from .views import *

app_name = 'gym'


urlpatterns = [
    path('profile', ProfileViewSet.as_view({'get': 'list'}), name="profile"),
    path('exercises', ExercisesViewSet.as_view({'get': 'list'}), name="exercises"),
    path('workout', WorkoutViewSet.as_view({'get': 'list'}), name="workout"),
    path('workout/<int:id>', WorkoutViewSet.as_view({'get': 'retrieve'}), name="workout"),
]