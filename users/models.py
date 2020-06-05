from django.db import models
from django.contrib.auth.models import User

class Resultado(models.Model):
    perspicuidad = models.FloatField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return "Resultado {}".format(self.perspicuidad)