from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Candidate(models.Model):
    name = models.CharField(max_length=16, null=True, blank=True)
    num_challenges_solved = models.IntegerField(null=True)
    expertise_level = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    data_strs = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    algos = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    cplusplus = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    java = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    python = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    votes = models.IntegerField(default=0)


class VotedIP(models.Model):
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()
