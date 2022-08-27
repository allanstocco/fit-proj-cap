from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField()

    def __str__(self):
        return self.user.user_name


class UserWorkout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    user_workout_session = models.ForeignKey(
        'UserWorkoutSession', on_delete=models.CASCADE, related_name='workout_session', related_query_name='workout_session', null=True, blank=True)


class Exercises(models.Model):
    exercise = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.exercise


class UserWorkoutSession(models.Model):
    user_workout_id = models.ForeignKey(
        UserWorkout, on_delete=models.CASCADE, related_name='comments', related_query_name='comment', null=True, blank=True)
    exercise = models.ForeignKey(
        Exercises, on_delete=models.CASCADE, related_name='exercises', related_query_name='exercises')
    exercise_reps = models.IntegerField(default=0, blank=True, null=True)
    exercise_kg = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.exercise.exercise
