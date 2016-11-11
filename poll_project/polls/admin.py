from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# 1 вариант
# admin.site.register(Question) меняется все как обычно

# 2 вариант
# class QuestionAdmin(admin.ModelAdmin):
# 	fields = ['pub_date', 'question_text'] # меняем поля местами в админке
# admin.site.register(Question, QuestionAdmin) # и собственно регистриуем наши хотелки

# 3 вариант регистрации поля Question
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}), # еще более круто
#         ('Date information', {'fields': ['pub_date']}), # еще более круто
#     ]
# admin.site.register(Question, QuestionAdmin) # регистрируем

# Простой вариант региcтрации поля Choice
# admin.site.register(Choice)

# Более крутой вариант 4 и с вопросами и с выбором
# Здесь  Choice Question

class ChoiceInline(admin.TabularInline): # а можно в стопку (admin.StackedInline)
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}), # еще более круто
        ('Date information', {'fields': ['pub_date']}), # еще более круто
    ]
    inlines = [ChoiceInline] # класс с выбором: Это говорит джанго
    # Choice объекты редактируются на странице Question. По умолчанию
    # обеспечь нам 3 выбора!

    list_display = ('question_text', 'pub_date', 'was_published_recently') # это здесь потому что изначально 
    # все выводит в стринговом формате каждый объект, но приятнее по индивидуальному полю
    # для этого используется переменная list_display с тьюплом 

    list_filter = ['pub_date'] # добавили фильтр по полю даты публикации см. админку
    search_fields = ['question_text'] # и даже теперь можно икать по вопросу!

admin.site.register(Question, QuestionAdmin) # регистрируем!