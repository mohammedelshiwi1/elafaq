from django.contrib import admin
from .models import Quiz,Question,Option,StudentAttempt

# Register your models here.
admin.site.register(StudentAttempt)
class optionInline(admin.TabularInline):
    model=Option
    extra=4

class questionInline(admin.TabularInline):
    model=Question
    inlines=[optionInline]
    extra=1
class quizAdmin(admin.ModelAdmin):
    inlines=[questionInline]

admin.site.register(Quiz,quizAdmin)
admin.site.register(Question)
admin.site.register(Option)