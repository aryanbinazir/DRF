
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CarSerializers, QuestionSerializers
from .models import Car, Question
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

class CarViewSet(viewsets.ViewSet):
    serializer_class = CarSerializers

    def list(self, request):
        """
        for list cars model
        """
        cars = Car.objects.filter(score__gt=7)
        ser_cars = CarSerializers(instance=cars, many=True)
        return Response(ser_cars.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        for create a car model
        """
        ser_cars = CarSerializers(data=request.POST)
        if ser_cars.is_valid():
            ser_cars.save()
            return Response(ser_cars.data)
        return Response(ser_cars.errors)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
class QuestionListView(APIView):
   # permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Question.objects.all()
        ser_questions = QuestionSerializers(instance=questions, many=True)
        return Response(ser_questions.data, status=status.HTTP_200_OK)

class QuestionCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ser_question = QuestionSerializers(data=request.POST)
        if ser_question.is_valid():
            ser_question.save()
            return Response(ser_question.data, status=status.HTTP_201_CREATED)
        return Response(ser_question.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        ser_question = QuestionSerializers(instance=question, data=request.data, partial=True)
        if ser_question.is_valid():
            ser_question.save()
            return Response(ser_question.data, status=status.HTTP_201_CREATED)
        return Response(ser_question.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        question.delete()
        return Response({'message': f'{question.title} has deleted'})

