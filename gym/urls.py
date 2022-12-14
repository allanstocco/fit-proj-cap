from django.urls import path
from .views import *

app_name = 'gym'


urlpatterns = [
    # MAIL SERVICE
    path('email', EmailViewSet.as_view(
        {"post": "challengeUser"}), name="email"),

    # PROFILE PATHS
    path('profile', ProfileViewSet.as_view({'get': 'list'}), name="profile"),
    path('profile/<int:pk>',
         ProfileViewSet.as_view({'get': 'retrieve'}), name="profile"),
    path('profile/workouts/<int:pk>',
         ProfileViewSet.as_view({'get': 'user_workouts'}), name="profile_workouts"),
    path('profile/workouts/<int:pk>/active',
         ProfileViewSet.as_view({'get': 'user_workouts_active'}), name="profile_workouts_active"),
    path('profile/workouts/<int:pk>/inactive',
         ProfileViewSet.as_view({'get': 'user_workouts_inactive'}), name="profile_workouts_inactive"),


    # EXERCISES PATHS
    path('exercises', ExercisesViewSet.as_view(
        {'get': 'list'}), name="exercises"),

    # WORKOUT PATHS
    path('workout', WorkoutViewSet.as_view({'get': 'list'}), name="workout"),

    path('workout/<int:pk>',
         WorkoutViewSet.as_view({'get': 'retrieve'}), name="workout_pk"),

    path('workout/<str:str>',
         WorkoutViewSet.as_view({'get': 'pair'}), name="workout_pair"),

    path('workout/active/<int:bool>',
         WorkoutViewSet.as_view({'get': 'active'}), name="workout_active"),

    path('workout/unique_string/<str:unique_str>',
         WorkoutViewSet.as_view({'get': 'unique_string'}), name="workout_unique_string"),

    # newly added
    path('workout/new/post',
         WorkoutViewSet.as_view({'post': 'create_workout'}), name="create_workout_post"),





    # WORKOUT SESSION DAY
    path('sessions/workout/<int:pk>/sessionday',
         WorkoutExerciseSessionViewSet.as_view({'get': 'workouts_active_session'}), name="workouts_session_active"),

    path('sessions/workout/exercise/sets/post',
         WorkoutExerciseSessionViewSet.as_view({'post': 'workouts_active_session_exercises_post'}), name="workouts_active_session_exercises_post"),
    # Newly added
    path('sessions/workout/patch/<int:pk>',
         WorkoutExerciseSessionViewSet.as_view({'patch': 'update_workout_session'}), name="update_workout"),




    # WORKOUT EXERCISES
    path('exercise/all',
         WorkoutExercisesViewSet.as_view({'get': 'list'}), name="all"),




    # WORKOUT SETS
    path('sets/all',
         WorkoutExerciseSessionSetsViewSet.as_view({'get': 'list'}), name='all_sets'),
    path('sets/post',
         WorkoutExerciseSessionSetsViewSet.as_view({'post': 'session_set_exercises_post'}), name='post_sets'),
]
