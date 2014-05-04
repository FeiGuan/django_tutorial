from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 0

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question']}),
		('Date information', {'fields': ['pub_date']})
	]
	inlines = [ChoiceInline]

	list_display = ('question','pub_date', 'was_published_recently', '__str__')
	list_filter = ['pub_date', 'question']
	search_fields = ['question']
	

admin.site.register(Poll, PollAdmin)
