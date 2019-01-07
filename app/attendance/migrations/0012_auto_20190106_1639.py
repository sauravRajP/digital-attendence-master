# Generated by Django 2.1.5 on 2019-01-06 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0011_attends_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='t',
            new_name='t_id',
        ),
        migrations.RemoveField(
            model_name='attends',
            name='status',
        ),
        migrations.RemoveField(
            model_name='attends',
            name='time',
        ),
        migrations.RemoveField(
            model_name='class',
            name='s',
        ),
        migrations.AddField(
            model_name='class',
            name='broadcast_attendance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='class',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
