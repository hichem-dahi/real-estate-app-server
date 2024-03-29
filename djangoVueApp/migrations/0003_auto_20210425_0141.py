# Generated by Django 3.0.4 on 2021-04-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoVueApp', '0002_user_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='beds',
        ),
        migrations.RemoveField(
            model_name='house',
            name='title',
        ),
        migrations.AddField(
            model_name='house',
            name='bathroom',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='house',
            name='daira',
            field=models.CharField(default='empty', max_length=50),
        ),
        migrations.AddField(
            model_name='house',
            name='kitchen',
            field=models.BooleanField(default=False),
        ),
    ]
