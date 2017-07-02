from rest_framework import routers
from applications.api.viewsets import UserViewSet


api_router = routers.SimpleRouter()
api_router.register('user', UserViewSet)
