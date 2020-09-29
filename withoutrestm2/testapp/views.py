from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from testapp.utils import is_json
from testapp.mixins import HttpResponseMixin, SerilizeMixin
from testapp.models import Student
from testapp.forms import StudentForm
import json

# Create your views here.

#For CSRF Desabling from the form
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class StudentCRUDCBV(HttpResponseMixin, SerilizeMixin, View):
    def get_object_by_id(self, id):
        try:
            std = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return None
        return std

    def get(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg': 'Please send valid json data'})
            return self.render_to_http_response(json_data, status=400)

        data = json.loads(data)
        id = data.get('id', None)

        if id is None:
            qs = Student.objects.all()
            json_data = self.serialize(qs)
            return self.render_to_http_response(json_data)

        std = self.get_object_by_id(id)
        if std is None:
            json_data = json.dumps({'msg': 'Please Provide valid Id, Resource not Found'})
            return self.render_to_http_response(json_data, status=400)
        json_data = self.serialize([std])
        return self.render_to_http_response(json_data)


    def post(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg': 'Please send json data only'})
            return self.render_to_http_response(json_data, status=400)

        stdData = json.loads(data)
        forms = StudentForm(stdData)

        if forms.is_valid():
            forms.save()
            json_data = json.dumps({'msg': 'Data saved Successfully'})
            return self.render_to_http_response(json_data)

        if forms.errors:
            json_data = json.dumps(forms.errors)
            return self.render_to_http_response(json_data, status=400)

    def put(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg': 'Please provide valid json data only'})
            return self.render_to_http_response(json_data, status=400)

        provided_data = json.loads(data)
        id = provided_data.get('id', None)

        if id is None:
            json_data = json.dumps({'msg': 'For updation id must be required!'})
            return self.render_to_http_response(json_data, status=400)

        std_data = self.get_object_by_id(id)

        if std_data is None:
            json_data = json.dumps({'msg': 'Provided id is invalid, Please provide valid id!'})
            return self.render_to_http_response(json_data, status=400)

        orig_data = {
            'name' : std_data.name,
            'rollno': std_data.rollno,
            'marks': std_data.marks,
            'gf': std_data.gf,
            'bf': std_data.bf
        }
        orig_data.update(provided_data)

        form = StudentForm(orig_data, instance=std_data)

        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg': 'Updated successfully'})
            return self.render_to_http_response(json_data)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def delete(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            json_data = json.dumps({'msg': 'Please provide valid json data only'})
            return self.render_to_http_response(json_data, status=400)

        provided_data = json.loads(data)
        id = provided_data.get('id', None)

        if id is None:
            json_data = json.dumps({'msg': 'For Deletion id must be required!'})
            return self.render_to_http_response(json_data, status=400)

        std_data = self.get_object_by_id(id)
        if std_data is None:
            json_data = json.dumps({'msg': 'Provided id is invalid, Please provide valid id!'})
            return self.render_to_http_response(json_data, status=400)

        status, deleted_item = std_data.delete()

        if status == 1:
            json_data = json.dumps({'msg': 'Resource Deleted Successfully'})
            return self.render_to_http_response(json_data, status=200)

        json_data = json.dumps({'msg': 'Unable to delete, Please Try Again'})
        return self.render_to_http_response(json_data, status=400)








