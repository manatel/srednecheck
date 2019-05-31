from django.shortcuts import render


def landing(request):
    name = "CodingMedved"
    current_day = "03.01.2017"



    return render(request, 'landing/landing.html', locals())

