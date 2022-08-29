from django.conf import settings
from django.http import JsonResponse
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.http import HttpResponseRedirect


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
