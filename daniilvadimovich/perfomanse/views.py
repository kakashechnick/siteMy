from django.shortcuts import render
from datetime import date
from .customFunc import dataReform
from perfomanse.models import Brand


def mainPageView(request):
  dataNow = date.today()

  brands = Brand.objects.all()

  data = {'Title': 'Главная страница',
          'iterations': range(10),
          'iterationsBrands': range(6),
          'image_data': brands,
          'dataDay': dataNow.day, 'dataMonth': dataReform.monthReform(dataNow.month), 'dataYear': dataNow.year,
          }

  return render(request, 'perfomanse/MainPage.html', context=data)


def thisBrand(request, brand_slug):
  return render(request, 'perfomanse/thisBrandPage.html')
