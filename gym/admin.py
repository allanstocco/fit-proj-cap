from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from .models import *
# Register your models here.


class WorkoutModelAdmin(admin.ModelAdmin):
    list_display = ["user_profile", "timestamp", "workout_id",
                    "workout_description", "start_time", "end_time", "active"]

    class Meta:
        model = Workout

class WorkoutExerciseSessionAdmin(admin.ModelAdmin):
    list_display = ['workout_id', 'exercise']

    class Meta:
        model = WorkoutExerciseSession
        
class ExerciseSetsAdmin(admin.ModelAdmin):
    list_display = ['exercise_sets']

    class Meta:
        model = WorkoutExerciseSession
        
admin.site.register(UserProfile)
admin.site.register(Exercises)
admin.site.register(WorkoutExerciseSession, WorkoutExerciseSessionAdmin)
admin.site.register(ExerciseSets, ExerciseSetsAdmin)
admin.site.register(Workout, WorkoutModelAdmin)
