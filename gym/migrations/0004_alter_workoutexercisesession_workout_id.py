# Generated by Django 3.2.5 on 2022-08-31 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_alter_workoutexercisesession_date_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutexercisesession',
            name='workout_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_workout_session', related_query_name='user_workout_session', to='gym.workout'),
        ),
    ]
