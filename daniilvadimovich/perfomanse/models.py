import base64

from django.db import models
from django.urls import reverse


class Brand(models.Model):   # Брэнды
  title = models.CharField(max_length=200)
  image = models.TextField(default='_')
  slug = models.SlugField(max_length=200, db_index=True, unique=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('brand', kwargs={'brand_slug': self.slug})


class Sex(models.Model):  # Под какой пол товар
  title = models.CharField(max_length=10)
  name = models.CharField(max_length=10)


class tags(models.Model):
  tile = title = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200, null=True, default=' ')


class Goods(models.Model):  # Товар
  title = models.CharField(max_length=200)
  image = models.TextField(default='_')
  quantity = models.PositiveIntegerField(default=0)  # Остаток
  price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
  code = models.TextField(max_length=200, null=True)  # Артикул
  slug = models.SlugField(max_length=200, db_index=True, unique=True, default=' ')

  brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True)
  forSex = models.ForeignKey(Sex, on_delete=models.PROTECT, null=True)
  tags = models.ManyToManyField(tags, related_name='tags', blank=True)

  def __str__(self):
    return base64.b64encode(self.image).decode()

  def get_absolute_url(self):
    return reverse('thisGoods', kwargs={
      'goods_slug': self.slug,
      'sku_counter': self.quantity
    })
