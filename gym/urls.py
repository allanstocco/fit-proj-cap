from django.urls import path
from .views import *

app_name = 'gym'


urlpatterns = [
    # MAIL SERVICE
    path('email', challengeUser, name="email"),

    # PROFILE PATHS
    path('profile', ProfileViewSet.as_view({'get': 'list'}), name="profile"),
    path('profile/<int:pk>',
         ProfileViewSet.as_view({'get': 'retrieve'}), name="profile"),

    # EXERCISES PATHS
    path('exercises', ExercisesViewSet.as_view(
        {'get': 'list'}), name="exercises"),

    # WORKOUT PATHS
    path('workout', WorkoutViewSet.as_view({'get': 'list'}), name="workout"),
    path('workout/<int:pk>',
         WorkoutViewSet.as_view({'get': 'retrieve'}), name="workout_pk"),
    path('workout/<str:str>',
         WorkoutViewSet.as_view({'get': 'pair'}), name="workout_pair"),

]
