from django.shortcuts import render


def home(request):
    name = "CodingMedved"
    current_day = "03.01.2017"



    return render(request, 'Home_page/Home_page.html', locals())

