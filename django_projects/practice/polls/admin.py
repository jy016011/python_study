from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    # 추가로 표시할 빈 인스턴스
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문 섹션', {'fields': ['question']}),
        ('생성일', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    readonly_fields = ['pub_date']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question', 'choice__choice_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)