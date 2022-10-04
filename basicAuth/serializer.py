from basicAuth.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    # name_city = serializers.ReadOnlyField('name_city')
    name_city = serializers.SerializerMethodField('get_name_city')
    def get_name_city(self,obj):
        return obj.name + ' ' + obj.city
    class Meta:
        model = Student
        fields = ['id','name','roll','city','name_city']
