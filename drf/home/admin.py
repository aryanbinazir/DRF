from django.contrib import admin
from .models import Car, Question, Answer

admin.site.register(Car)
admin.site.register(Answer)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}