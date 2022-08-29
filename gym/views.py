from django.http import JsonResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework import status, permissions, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

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
        return HttpResponseRedirect(reverse("gym:email"))
    else:
        return render(request, "email.html")


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk):
        profile = get_object_or_404(self.queryset, pk=pk)
        serialize = UserSerializer(profile)
        return Response(serialize.data)


class ExercisesViewSet(viewsets.ModelViewSet):
    queryset = Exercises.objects.all()
    serializer_class = ExerciseSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def retrieve(self, request, str):
        user_workout = Workout.objects.filter(workout_description=str)
        serialize = WorkoutSerializer(user_workout, many=True)
        return Response(serialize.data)
