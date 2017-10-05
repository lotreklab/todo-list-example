from django.conf.urls import url, include
from rest_framework import routers

from .views import TodoViewSet

print(TodoViewSet)

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet, 'todo_rest')

urlpatterns = [
    url(r'^', include(router.urls)),
]
