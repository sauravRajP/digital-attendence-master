# Generated by Django 2.1.5 on 2019-06-06 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='associated',
            old_name='clas_id',
            new_name='class_id',
        ),
    ]