from django.db import models
from django.urls import reverse

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)


    class Meta:
        verbose_name = ("City")
        verbose_name_plural = ("Citys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("City_detail", kwargs={"pk": self.pk})

