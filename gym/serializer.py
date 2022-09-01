from rest_framework import serializers
from .models import *


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercises
        fields = ['pk','exercise','exercise_description']


class ExerciseSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExerciseSets
        fields = ['pk', 'exercise_sets', 'reps', 'weights']


class WorkoutExerciseSessionSerializer(serializers.ModelSerializer):
    workout_exercise_set = ExerciseSetSerializer(read_only=True, many=True)
    exercise_name = serializers.CharField(
        read_only=True, source='exercise.exercise')
    class Meta:
        model = WorkoutExerciseSession
        fields = ['pk', 'workout_id', 'exercise', 'exercise_name', 'date_name',
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
        fields = ['account_id', 'in_challenge', 'bio', 'user_workout']

    def create(self, validated_data):
        var = validated_data.pop('account_id')
        return print(var)
