from rest_framework import serializers
from testapp.models import Employee


def multiple_of_1000(value):
    if value % 1000 != 0:
        raise serializers.ValidationError('Salary Should be multiple of 1000')


# Model Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[multiple_of_1000])

    def validate_esal(self, value):
        if value < 5000:
            raise serializers.ValidationError('Employee salary should be minimum 5000')
        return value

    def validate(self, data):
        if(self.instance is not None):
            ename = data.get('ename', self.instance.ename)
            esal = data.get('esal', self.instance.esal)
        else:
            ename = data.get('ename')
            esal = data.get('esal')
        # import pdb #DEBUG
        # pdb.set_trace()
        if ename.lower() == 'sunny':
            if esal < 50000:
                raise serializers.ValidationError('For sunny salary should be greater minimum 50,000')
        return data

    class Meta:
        model = Employee
        fields = '__all__'

# class EmployeeSerializer(serializers.Serializer):
#     eno = serializers.IntegerField()
#     ename = serializers.CharField(max_length=64)
#     esal = serializers.FloatField(validators=[multiple_of_1000])
#     eaddr = serializers.CharField(max_length=64)
#
#     def validate_esal(self, value):
#         if value < 5000:
#             raise serializers.ValidationError('Employee salary should be minimum 5000')
#         return value
#
#     def validate(self, data):
#         if(self.instance is not None):
#             ename = data.get('ename', self.instance.ename)
#             esal = data.get('esal', self.instance.esal)
#         else:
#             ename = data.get('ename')
#             esal = data.get('esal')
#         # import pdb #DEBUG
#         # pdb.set_trace()
#         if ename.lower() == 'sunny':
#             if esal < 50000:
#                 raise serializers.ValidationError('For sunny salary should be greater minimum 50,000')
#         return data
#
#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.eno = validated_data.get('eno', instance.eno)
#         instance.ename = validated_data.get('ename', instance.ename)
#         instance.esal = validated_data.get('esal', instance.esal)
#         instance.eaddr = validated_data.get('eaddr', instance.eaddr)
#         instance.save()
#         return instance
