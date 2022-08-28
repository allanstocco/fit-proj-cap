from rest_framework import serializers
from .models import *


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = '__all__'


class UserWorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkoutSession
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    user_workout_session = UserWorkoutSessionSerializer(
        read_only=True, many=True)

    class Meta:
        model = Workout
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    user_workout = WorkoutSerializer(read_only=True, many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
