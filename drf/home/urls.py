from django.urls import path
from . import views
from rest_framework import routers

app_name = 'home'
urlpatterns =[
    path('questions/', views.QuestionListView.as_view()),
    path('questions/create/', views.QuestionCreateView.as_view()),
    path('questions/update/<int:pk>/', views.QuestionUpdateView.as_view()),
    path('questions/delete/<int:pk>/', views.QuestionDeleteView.as_view()),
]

router = routers.SimpleRouter()
router.register('', views.CarViewSet, basename='car')
urlpatterns += router.urls