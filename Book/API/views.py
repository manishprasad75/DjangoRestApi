from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.
# Function Based Views
def emp_data_view(request):
    emp_data = dict(eno=100, ename='Sunny', esal=1000, eaddr='Delhi')
    # json_data = json.dumps(emp_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(emp_data)


# Class Based Views

from django.views.generic import View
from .mixins import HttpResponseMixin


class JsonCBV(HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):
        emp_data = {
            'eno': 101,
            'ename': 'Leone',
            'esal': 10000,
            'eaddr': 'Mumbai',
        }
        json_data = json.dumps(emp_data)
        # return HttpResponse(json_data, content_type='application/json')
        return self.render_to_http_response(json_data) #mixins
        # return JsonResponse(emp_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from post route'})
        # return HttpResponse(json_data, content_type='application/json')
        return self.render_to_http_response(json_data)  # mixins

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from put route'})
        # return HttpResponse(json_data, content_type='application/json')
        return self.render_to_http_response(json_data)  # mixins

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from delete route'})
        # return HttpResponse(json_data, content_type='application/json')
        return self.render_to_http_response(json_data)  # mixins
