from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from testapp.models import Employee
from testapp.mixins import SerilizeMixin, HttpResponseMixin
import json

from django.core.serializers import serialize  # To convert Python object into Json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from testapp.utils import is_json

from testapp.forms import EmployeeForm


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(HttpResponseMixin, SerilizeMixin, View):
    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg': 'Please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        data = json.loads(data)
        id = data.get('id', None)

        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg': 'The requested resources not available'})
                return self.render_to_http_response(json_data, status=404)
            else:
                json_data = self.serialize([emp])
                return self.render_to_http_response(json_data)
        qs = Employee.objects.all()
        json_data = self.serialize(qs)  # Mixin
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg': 'please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource created successfully'})
            return self.render_to_http_response(json_data)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def put(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg': 'Please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        data = json.loads(data)
        id = data.get('id', None)

        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg': 'The requested resource does not exist'})
                return self.render_to_http_response(json_data, status=404)
            data = request.body
            if not is_json(data):
                json_data = json.dumps({'msg': 'please send valid json data only'})
                return self.render_to_http_response(json_data, status=400)
            provided_data = json.loads(data)
            original_data = dict(eno=emp.eno, ename=emp.ename, esal=emp.esal, eaddr=emp.eaddr)
            original_data.update(provided_data)

            form = EmployeeForm(original_data, instance=emp)
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({'msg': 'Update successfully'})
                return self.render_to_http_response(json_data)

            if form.errors:
                json_data = json.dumps(form.errors)
                return self.render_to_http_response(json_data, status=400)
        json_data = json.dumps({'msg': 'For update Id, is mandatory'})
        return self.render_to_http_response(json_data, status=400)

    def delete(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg': 'Please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        data = json.loads(data)
        id = data.get('id', None)

        if id is None:
            json_data = json.dumps({'msg': 'For Deletion, id must be required'})
            return self.render_to_http_response(json_data, status=400)
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'The requested resource does not exist'})
            return self.render_to_http_response(json_data, status=404)

        status, deleted_item = emp.delete()

        if status == 1:
            json_data = json.dumps({'msg': 'Resource Deleted Successfully'})
            return self.render_to_http_response(json_data, status=200)

        json_data = json.dumps({'msg': 'Unable to delete, Please Try Again'})
        return self.render_to_http_response(json_data, status=400)







# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetailCBV(HttpResponseMixin, SerilizeMixin, View):
    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self, request, id, *args, **kwargs):
        # fetch id = 1
        # emp = Employee.objects.get(id=id)
        # emp_data = {
        #     'eno': emp.eno,
        #     'ename': emp.ename,
        #     'esal': emp.esal,
        #     'eaddr': emp.esal
        # }
        # json_data = json.dumps(emp_data)
        # json_data = serialize('json', [emp], fields=('eno', 'ename', 'eaddr'))
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resources not available'})
            return self.render_to_http_response(json_data, status=404)
        else:
            json_data = self.serialize([emp])
            return self.render_to_http_response(json_data)

    def put(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'The requested resource does not exist'})
            return self.render_to_http_response(json_data, status=404)
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg': 'please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        provided_data = json.loads(data)
        original_data = dict(eno=emp.eno, ename=emp.ename, esal=emp.esal, eaddr=emp.eaddr)
        original_data.update(provided_data)

        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Update successfully'})
            return self.render_to_http_response(json_data)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def delete(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'The requested resource does not exist'})
            return self.render_to_http_response(json_data, status=404)

        status, deleted_item = emp.delete()

        if status == 1:
            json_data = json.dumps({'msg': 'Resource Deleted Successfully'})
            return self.render_to_http_response(json_data, status=200)

        json_data = json.dumps({'msg': 'Unable to delete, Please Try Again'})
        return self.render_to_http_response(json_data, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(HttpResponseMixin, SerilizeMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)  # Mixin
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg': 'please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource created successfully'})
            return self.render_to_http_response(json_data)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)
