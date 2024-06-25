from django.shortcuts import render
from datetime import date
from .customFunc import dataReform


def mainPageView(request):
  dataNow = date.today()

  data = {'Title': 'Главная страница',
          'iterations': range(10),
          'iterationsBrands': range(6),
          'dataDay': dataNow.day, 'dataMonth': dataReform.monthReform(dataNow.month), 'dataYear': dataNow.year
          }

  return render(request, 'perfomanse/MainPage.html', context=data)
