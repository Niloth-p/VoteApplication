from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# class IntegerRangeField(models.IntegerField):

#     def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
#         self.min_value, self.max_value = min_value, max_value
#         models.IntegerField.__init__(self, verbose_name, name, **kwargs)

#     def formfield(self, **kwargs):
#         defaults = {'min_value': self.min_value, 'max_value':self.max_value}
#         defaults.update(kwargs)
#         return super(IntegerRangeField, self).formfield(**defaults)

class Candidate(models.Model):
    name = models.CharField(max_length=16, null=True, blank=True)
    num_challenges_solved = models.IntegerField(null=True)
    # expertise_level = models.IntegerRangeField(min_value=1, max_value=5)
    expertise_level = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    data_strs = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    algos = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    cplusplus = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    java = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    python = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    votes = models.IntegerField(default=0)
