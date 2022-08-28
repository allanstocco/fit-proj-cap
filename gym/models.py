from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    account_id = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField()

    def __str__(self):
        return self.user.user_name


class Workout(models.Model):
    workout_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE, related_name='user_workout', related_query_name='user_workout')
    workout_description = models.CharField(
        max_length=150, null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.timestamp}'


class Exercises(models.Model):
    exercise = models.CharField(max_length=60, null=True, blank=True)
    exercise_description = models.CharField(
        max_length=512, null=True, blank=True)

    def __str__(self):
        return self.exercise



class UserWorkoutSession(models.Model):
    workout_id = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name='user_workout_session', related_query_name='user_workout_session', null=True, blank=True)
    exercise = models.ForeignKey(
        Exercises, on_delete=models.CASCADE, related_name='exercises', related_query_name='exercises')
    exercise_reps = models.IntegerField(default=0, blank=True, null=True)
    exercise_kg = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.exercise.exercise
