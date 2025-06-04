from django.db import models


class USD(models.Model):
    time = models.CharField(max_length=40)
    value = models.FloatField()

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return str(self.value)
