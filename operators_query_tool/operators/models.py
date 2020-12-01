from django.db import models
from django.contrib.auth.models import User

# Need clarification from Hayden about the Operator model.
# class Operator(models.Model):
#     op_id = models.IntegerField(unique=True)
#     name = models.CharField(unique=True)
#     mode = models.ManyToManyField(Modes, on_delete=models.CASCADE)
#     homepage = models.URLField()
#     api_url = models.URLField()
#     default_language = models.CharField()
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

class Modes(models.Model):
    mode_id = models.IntegerField(unique=True)
    # op_id = models.ForeignKey(Operator, on_delete=models.CASCADE)
    short_desc = models.CharField(max_length=50)
    long_desc = models.TextField()

    def __str__(self):
        return self.mode_id # short_desc might be more useful? - LT