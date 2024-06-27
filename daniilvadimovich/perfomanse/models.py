from django.db import models
from django.urls import reverse


class Brand(models.Model):
  title = models.CharField(max_length=200)
  image = models.TextField(default='_')
  slug = models.SlugField(max_length=200, db_index=True, unique=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('brand', kwargs={'brand_slug': self.slug})
