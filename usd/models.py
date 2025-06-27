from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.code


class CurrencyRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    time = models.DateTimeField()
    value = models.FloatField()

    class Meta:
        ordering = ('-time',)
        # unique_together = ('currency', 'time')

    def __str__(self):
        return f'{self.currency}: {self.value} @ {self.time}'
