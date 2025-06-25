from django.urls import path
from . import views
from rest_framework import routers

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('user_list/', views.UserListApi.as_view()),
]

router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls