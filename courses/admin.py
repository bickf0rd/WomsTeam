from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


class TaskAdmin(SummernoteModelAdmin):
    text = ('text', 'code', 'correct_answer', 'answer')


admin.site.register(Category)
admin.site.register(Courses)
admin.site.register(Task, TaskAdmin)
