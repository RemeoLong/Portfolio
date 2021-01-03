from django.contrib import admin
from .models import *


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'test')


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'test')
    list_filter = ('test',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'section', 'questions_text')
    list_filter = ('test', 'section')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question')
    list_filter = ('question',)


class TotalScoreAdmin(admin.ModelAdmin):
    list_display = ('User', 'test', 'section', 'score')
    list_filter = ('score', 'User', 'test', 'section')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('UserID', 'answer', 'question')
    list_filter = ('UserID',)


admin.site.register(Test, TestAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Passage)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Explanation)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(TotalScore, TotalScoreAdmin)



