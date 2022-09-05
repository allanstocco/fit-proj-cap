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
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.account_id.user_name


class Workout(models.Model):
    workout_id = models.BigAutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile,
                                     on_delete=models.CASCADE, related_name='user_workout', related_query_name='user_workout')
    workout_description = models.CharField(
        max_length=150, null=True, blank=True)
    goal = models.CharField(
        max_length=20, blank=True, choices=goals)
    unique_str = models.CharField(
        max_length=150, null=True, blank=True)
    start_time = models.DateField(null=True, blank=True)
    end_time = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

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
        Workout, on_delete=models.CASCADE, null=True, blank=True, related_name='user_workout_session', related_query_name='user_workout_session')
    exercise = models.ForeignKey(
        Exercises, on_delete=models.CASCADE, null=True, blank=True, related_name='exercises', related_query_name='exercises')
    date_name = models.CharField(
        default='', max_length=20, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.exercise.exercise} => FROM => {self.workout_id}'


class ExerciseSets(models.Model):
    exercise_sets = models.ForeignKey(WorkoutExerciseSession, on_delete=models.CASCADE,
                                      related_name='workout_exercise_set', related_query_name='workout_exercise_set', null=True, blank=True)
    reps = models.IntegerField(default=0, blank=True, null=True)
    weights = models.IntegerField(default=0, blank=True, null=True)


class Email(models.Model):
    account_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="email_profile", null=True, blank=True
    )
    message_name = models.CharField(
        default='test', max_length=200, null=True, blank=False)
    message_email = models.CharField(
        default='test@test.com', max_length=200, null=True, blank=False)
    message_body = models.CharField(
        default='testing', max_length=5000, null=True, blank=False)
