from django.contrib import admin
from polls.models import Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
  list_display = ('question_text', 'pub_date', 'was_published_recently' )

admin.site.register(Question, QuestionAdmin)