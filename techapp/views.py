from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Data
from .forms import JSONForm
from django.views import View
from django.urls import reverse
import json


class DataCreate(View):

    def get(self, request):
        form = JSONForm()
        return render(request, 'base.html', context={'form': form})

    def post(self, request):
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        name = json.dumps(data)
        Data.objects.create(name=name)
        return HttpResponseRedirect(reverse('DataCreate'))


class DataRead(View):

    def get(self, request):
        data = Data.objects.all()
        return HttpResponse(json.dumps([json.loads(value.name) for value in data]), content_type='application/json')
