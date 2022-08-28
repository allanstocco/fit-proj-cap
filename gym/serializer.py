from rest_framework import serializers
from .models import *


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = '__all__'


class ExerciseSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseSets
        fields = '__all__'


class WorkoutExerciseSessionSerializer(serializers.ModelSerializer):
    workout_exercise_set = ExerciseSetSerializer(
        read_only=True, many=True)

    class Meta:
        model = WorkoutExerciseSession
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    user_workout_session = WorkoutExerciseSessionSerializer(
        read_only=True, many=True)

    class Meta:
        model = Workout
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    user_workout = WorkoutSerializer(read_only=True, many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
