from .views import TodoViewSet
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet, 'todo_rest')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^$', views.home, name='home'),
]
