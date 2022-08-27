from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from .models import *
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Exercises)
admin.site.register(UserWorkoutSession)
admin.site.register(UserWorkout)
