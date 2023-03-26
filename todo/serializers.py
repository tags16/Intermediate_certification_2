from rest_framework import serializers
from todo.models import Todo


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['create_date', 'finish_date', 'close']


class TodoDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'measurements']


class TodosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description']

