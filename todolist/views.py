from rest_framework import viewsets
from .models import Todo, Media
from .serializers import ExpandedMediaSerializer, ExpandedTodoSerializer
from .serializers import MediaSerializer, TodoSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

class TodoViewSet(viewsets.ModelViewSet):
    model = Todo

    def change_status(self,pk,status):
        todo_check = Todo.objects.get(pk=pk)
        todo_check.status = status
        todo_check.save()
        return todo_check

    def default_return_todo(self):
        todo = self.get_object()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)


    def get_serializer_class(self):
        if self.request.method == "GET":
            return ExpandedTodoSerializer
        else:
            return TodoSerializer

    def get_queryset(self):
        queryset =  self.model.objects.all()
        return queryset


    @detail_route(methods=['get'])
    def done(self, request,pk):
        try:
            self.change_status(pk,True)
        except self.model.DoesNotExist:
            pass
        return self.default_return_todo()

    @detail_route(methods=['get'])
    def undone(self, request,pk):
        try:
            self.change_status(pk,False)
        except self.model.DoesNotExist:
            pass
        return self.default_return_todo()

