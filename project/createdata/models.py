from django.db import models
from django.utils import timezone

class SimpleData(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

class OptionalData(models.Model):
    simpleData = models.ForeignKey(SimpleData, on_delete=models.CASCADE)
    optionalContent = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.optionalContent
