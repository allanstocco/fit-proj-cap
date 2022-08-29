from django.db import models
from django.conf import settings

goals = (
    ("CONSISTENCY", "Consistency"),
    ("PROGRESSION", "Progression"),
    ("TONNAGE", "Tonnage")
)


class UserProfile(models.Model):
    account_id = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name="profile"
    )
    in_challenge = models.BooleanField(default=False)
    bio = models.TextField()

    def __str__(self):
        return self.account_id.user_name


class Workout(models.Model):
    workout_id = models.BigAutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile,
                                     on_delete=models.CASCADE, related_name='user_workout', related_query_name='user_workout')
    workout_description = models.CharField(
        max_length=150, null=True, blank=True)
    goal = models.CharField(
        max_length=20, blank=True, choices=goals, default="OTHER")
    unique_str = models.CharField(
        max_length=150, null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_profile} - {self.workout_description}'


class Exercises(models.Model):
    exercise = models.CharField(max_length=60, null=True, blank=True)
    exercise_description = models.CharField(
        max_length=512, null=True, blank=True)

    def __str__(self):
        return self.exercise


class WorkoutExerciseSession(models.Model):
    workout_id = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name='user_workout_session', related_query_name='user_workout_session')
    exercise = models.ForeignKey(
        Exercises, on_delete=models.CASCADE, related_name='exercises', related_query_name='exercises')
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.exercise.exercise} => FROM => {self.workout_id}'


class ExerciseSets(models.Model):
    exercise_sets = models.ForeignKey(WorkoutExerciseSession, on_delete=models.CASCADE,
                                      related_name='workout_exercise_set', related_query_name='workout_exercise_set', null=True, blank=True)
    exercise_reps = models.IntegerField(default=0, blank=True, null=True)
    exercise_kg = models.IntegerField(default=0, blank=True, null=True)
