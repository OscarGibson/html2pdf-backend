from rest_framework import serializers
from .models import Project

class ProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('pk','name')

class ProjectDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('html','css','pk','name')
