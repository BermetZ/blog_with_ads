from django.conf import settings
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    phone = models.IntegerField()
    logo = models.ImageField(upload_to='logo', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Ad(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    company = models.ForeignKey(Company, related_name='company', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Ad, related_name='ad', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text
