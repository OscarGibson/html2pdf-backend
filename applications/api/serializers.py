from rest_framework.serializers import ModelSerializer
#from applications.gallery.models import Photo
#import uuid
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = get_user_model()
