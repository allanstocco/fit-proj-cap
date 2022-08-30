from django.conf import settings
from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from datetime import date

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from user.serializer import *
from .serializer import *
from .models import *


def challengeUser(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_body = request.POST['message_body']
        print(message_name)

        send_mail(
            subject=message_name,
            message=message_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['allanstocco@gmail.com'],
            fail_silently=False,
        )
        return render(request, "email.html", {
            'msg': 'Mail sent successfully!'
        })
    else:
        return render(request, "email.html", {
            'msg': 'Something went wrong =('
        })


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
        if request.method == 'POST':
            data = request.POST
            print(data)


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
            filter = data.pop('workout_id')
            serializer.create(filter)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
