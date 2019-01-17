from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
	# halls = serializers.StringRelatedField(many=True)
	class Meta:
		model = Job
		fields = "__all__"