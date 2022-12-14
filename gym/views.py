from django.conf import settings
from rest_framework import status, viewsets
from rest_framework.response import Response
from datetime import date
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.shortcuts import render
import json


from user.serializer import *
from .serializer import *
from .models import *
import json


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def challengeUser(self, request):
        data = request.data
        serializer = EmailSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            data = serializer.validated_data
            message_name = data.get('message_body')
            message_email = data.get('message_email')
            message_body = data.get('message_body')

            send_mail(
                message_name,
                message_body,
                settings.EMAIL_HOST_USER,
                [message_email],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk):
        profile = get_object_or_404(self.queryset, pk=pk)
        serialize = UserSerializer(profile)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def user_workouts(self, request, pk):
        user_workouts = Workout.objects.filter(user_profile=pk)
        serialize = WorkoutSerializer(user_workouts, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def user_workouts_active(self, request, pk):
        user_workouts_active = Workout.objects.filter(
            user_profile=pk, active=True)
        serializer = WorkoutSerializer(user_workouts_active, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def user_workouts_inactive(self, request, pk):
        user_workouts_active = Workout.objects.filter(
            user_profile=pk, active=False)
        serializer = WorkoutSerializer(user_workouts_active, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExercisesViewSet(viewsets.ModelViewSet):
    queryset = Exercises.objects.all()
    serializer_class = ExerciseSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def pair(self, request, str):
        user_workout = Workout.objects.filter(workout_description=str)
        serialize = WorkoutSerializer(user_workout, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        user_workout = get_object_or_404(self.queryset, pk=pk)
        serialize = WorkoutSerializer(user_workout)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def active(self, request, bool):
        active_workout = Workout.objects.filter(active=bool)
        serialize = WorkoutSerializer(active_workout, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def create_workout(self, request):
        data = request.data
        serializer = WorkoutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def unique_string(self, request, unique_str):
        workout_unique = Workout.objects.filter(unique_str=unique_str)
        serialize = WorkoutSerializer(workout_unique, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)


class WorkoutExerciseSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutExerciseSession.objects.all()
    serializer_class = WorkoutExerciseSessionSerializer

    def workouts_active_session(self, request, pk):
        today = date.today()
        user_workouts_active = WorkoutExerciseSession.objects.filter(
            workout_id=pk, date=today)
        serialize = WorkoutExerciseSessionSerializer(
            user_workouts_active, many=True)
        print(serialize)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def workouts_active_session_exercises_post(self, request):
        data = request.data
        serializer = WorkoutExerciseSessionSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def update_workout_session(self, request, pk):
        if request.method == 'PATCH':
            workout = WorkoutExerciseSession.objects.get(pk=pk)
            serializer = WorkoutExerciseSessionSerializer(workout,
                                                          data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class WorkoutExercisesViewSet(viewsets.ModelViewSet):
    queryset = Exercises.objects.all()
    serializer_class = ExerciseSerializer


class WorkoutExerciseSessionSetsViewSet(viewsets.ModelViewSet):
    queryset = ExerciseSets.objects.all()
    serializer_class = ExerciseSetSerializer

    def session_set_exercises_post(self, request):
        data = request.data
        serializer = ExerciseSetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
