# Generated by Django 3.1 on 2020-08-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteapp', '0002_candidate_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotedIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
    ]