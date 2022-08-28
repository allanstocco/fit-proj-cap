from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from .models import *
# Register your models here.


class WorkoutModelAdmin(admin.ModelAdmin):
    list_display = ["user", "timestamp", "workout_id",
                    "workout_description", "start_time", "end_time", "status"]

    class Meta:
        model = Workout


admin.site.register(UserProfile)
admin.site.register(Exercises)
admin.site.register(UserWorkoutSession)
admin.site.register(Workout, WorkoutModelAdmin)
