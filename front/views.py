from django.http import HttpResponse
from polls.models import Poll
from django.shortcuts import render
from django.template import loader, RequestContext

def index(request):
	polls = Poll.objects.order_by('-pub_date')
	questions = []
	for poll in polls:
		questions.append(poll.question)
	
	template = loader.get_template('front/index.html')
	context = RequestContext(request, {'questions': questions,})
	return HttpResponse(template.render(context))
