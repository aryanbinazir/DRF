from rest_framework import serializers
from .models import Question, Answer
from .models import Car


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        extra_kwargs = {
            'country': {'write_only': True}
        }

class QuestionSerializers(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self, obj):
        result = obj.qanswers.all()
        return AnswerSerializers(instance=result, many=True).data

class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'