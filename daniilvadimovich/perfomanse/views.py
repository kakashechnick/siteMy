import base64

from django.shortcuts import (
  render,
  get_object_or_404
)

from datetime import date
from .customFunc import dataReform
from perfomanse.models import Brand, Goods


def mainPageView(request):
  dataNow = date.today()

  brands = Brand.objects.all()

  data = {'Title': 'Купить хайповое шмотье | Магазин ebatKakStilno.ru',
          'iterations': range(10),
          'image_data': brands,
          'dataDay': dataNow.day, 'dataMonth': dataReform.monthReform(dataNow.month), 'dataYear': dataNow.year,
          }

  return render(request, 'perfomanse/MainPage.html', context=data)


def thisBrand(request, brand_slug):
  post = get_object_or_404(Brand, slug=brand_slug)

  id_numeric = Brand.objects.filter(slug=brand_slug)
  allGoodsForThisBrand = Goods.objects.filter(brand_id=id_numeric[0].pk)

  data = {'Title': post.title,
          'image_goods': allGoodsForThisBrand
          }

  return render(request, 'perfomanse/thisBrandPage.html', context=data)


def allBrand(request):
  brands = Brand.objects.all()

  data = {'Title': 'Брэнды | Магазин ebatKakStilno.ru',
          'image_data': brands}

  return render(request, 'perfomanse/allBrands.html', context=data)


def goods(request, goods_slug, sku_counter):
  post2 = get_object_or_404(Goods, slug=goods_slug)

  data = {'Title': post2.title, }

  return render(request, 'perfomanse/thisGoodsPage.html', context=data)
