# Generated by Django 4.1.3 on 2022-11-14 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='calorie',
            new_name='calorie_per_one_quantity',
        ),
        migrations.RemoveField(
            model_name='food',
            name='person_of',
        ),
        migrations.RemoveField(
            model_name='food',
            name='quantity',
        ),
    ]