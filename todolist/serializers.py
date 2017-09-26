from .models import Todo, Media
from rest_framework import serializers


class ExpandedMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'





class ExpandedTodoSerializer(serializers.ModelSerializer):
    attachments = MediaSerializer(read_only=True)
    class Meta:
        model = Todo
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
