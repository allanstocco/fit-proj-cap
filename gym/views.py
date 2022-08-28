from django.http import JsonResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework import status, permissions, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from user.serializer import *
from .serializer import *
from .models import *


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class ExercisesViewSet(viewsets.ModelViewSet):
    queryset = Exercises.objects.all()
    serializer_class = ExerciseSerializer
    

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
        
