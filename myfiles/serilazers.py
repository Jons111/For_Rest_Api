from rest_framework.serializers import ModelSerializer
from myfiles.models import Teacher
class Api_Serializer(ModelSerializer):
    class Meta:
        fields = ('id','name','last_name','age')
        model = Teacher
