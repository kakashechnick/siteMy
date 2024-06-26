from django.db import models


class Brand(models.Model):
  title = models.CharField(max_length=200)
  image = models.TextField(default='_')
