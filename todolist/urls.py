from .views import TodoViewSet
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet, 'todo')

urlpatterns = [
    url(r'^', include(router.urls)),
]
