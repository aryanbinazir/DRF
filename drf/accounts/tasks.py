from celery import shared_task
import random
from django.contrib.auth.models import User

@shared_task
def creating_random_users():
    word = ''
    random_number = random.randint(5,10)
    for i in range(random_number):
        random_letter = random.randint(97, 123)
        word += chr(random_letter)
    user = User.objects.create_user(
        username= word,
        password= str(123456),
        email=f'{word}@gmail.com'
    )

