# Generated by Django 3.1 on 2020-08-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]