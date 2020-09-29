from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

class EmployeeDetails(View):
    def get(self, request, *args, **kwargs):
        emp = self.get_element_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg' : 'Please give proper id'})
            return HttpResponse(json_data, status=404)
        return HttpResponse(emp)