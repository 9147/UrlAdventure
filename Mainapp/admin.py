from django.contrib import admin
from .models import Question, QuestionAssignment

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','text','code')

@admin.register(QuestionAssignment)
class QuestionAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id','user','question','order','solved')
