from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(UserWorkout)
admin.site.register(Exercises)
admin.site.register(UserWorkoutSession)
