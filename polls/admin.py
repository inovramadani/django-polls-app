from django.contrib import admin

from .models import Question, Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

# add a fieldset with header
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Date information', {'fields': ['pub_date']}),
		(None, {'fields': ['question_text']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)



# # re-ordering the displayed field
# class QuestionAdmin(admin.ModelAdmin):
# 	fields = ['pub_date', 'question_text']

# admin.site.register(Question, QuestionAdmin)

# # show default forms
# admin.site.register(Question)
# admin.site.register(Choice)
