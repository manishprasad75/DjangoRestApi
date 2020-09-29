from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import NameSerializer


# Create your views here.
class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        colors = ['Yello', 'Green', 'Blue', 'Red']
        return Response({'msg': 'Happy Coding :)', 'colors': colors})

    def post(self, request, *args, **kwargs):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello, {}, Happy Coding!!!'.format(name)
            return Response({'msg': msg})
        return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        return Response({'msg': 'This is from put method of APIView'})

    def patch(self, request, *args, **kwargs):
        return Response({'msg': 'This is from patch method of APIView'})

    def delete(self, request, *args, **kwargs):
        return Response({'msg': 'This is from Delete method of APIView'})


from rest_framework.viewsets import ViewSet


class TestViewSet(ViewSet):
    def list(self, request):
        colors = ['Yello', 'Green', 'Blue', 'Red']
        return Response({'msg': 'Happy Coding :)', 'colors': colors})

    def create(self, request):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello, {}, Happy Coding!!!'.format(name)
            return Response({'msg': msg})
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        return Response({'msg': 'This is from retrieve method'})

    def update(self, request, pk=None):
        return Response({'msg': 'This is from update method'})

    def partial_update(self, request, pk=None):
        return Response({'msg': 'This is from partial_update method'})

    def destroy(self, request, pk=None):
        return Response({'msg': 'This is from destroy method'})



