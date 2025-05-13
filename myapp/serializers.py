from rest_framework import serializers
from myapp.models import Remind
class RemindSerializer(serializers.ModelSerializer):
    class Meta:
        model=Remind
        fields=['id','date','time','message','method']
