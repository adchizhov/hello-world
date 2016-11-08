from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from with_forms.forms import MyForm


def index(request):
    if request.method == "GET":
        return HttpResponse('Hello!')

class MyView(View):
    def get(self, request):
        form = MyForm()
        c = {'form': form}
        return render(request, 'with_forms/form.html', c)

    def post(self, request):
        form = MyForm(data=request.POST)
        if form.is_valid():
            messages.success(request, form.cleaned_data['name'])
        else:
            messages.error(request, 'Error')
        c = {'form': form}
        return render(request, 'with_forms/form.html', c)