from rest_framework import serializers
from .models import *


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = '__all__'

class ExerciseSetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExerciseSets
        fields = ['pk','reps', 'weights']

class WorkoutExerciseSessionSerializer(serializers.ModelSerializer):
    workout_exercise_set = ExerciseSetSerializer(
        read_only=True, many=True)
    exercise_name = serializers.CharField(source='exercise.exercise')

    class Meta:
        model = WorkoutExerciseSession
        fields = ['pk','workout_id','exercise', 'exercise_name', 'date_name',
                  'date', 'complete', 'workout_exercise_set']


class WorkoutSerializer(serializers.ModelSerializer):
    user_workout_session = WorkoutExerciseSessionSerializer(
        read_only=True, many=True)
    
    class Meta:
        model = Workout
        fields = ['workout_id', 'user_profile', 'workout_description', 'unique_str', 'goal', 'active',
                  'start_time', 'end_time', 'created_at', 'user_workout_session']


class UserSerializer(serializers.ModelSerializer):
    user_workout = WorkoutSerializer(read_only=True, many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
