from django.db import models


class Advert(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField()
    counter = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title