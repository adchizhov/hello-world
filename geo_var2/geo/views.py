from django.shortcuts import render

# Create your views here.


def my_view(request):
    return render(
        request,
        'geo/index2.html',
    )
