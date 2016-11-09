from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
# from django.template import loader # for not good way
# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html') not good way
	context = {'latest_question_list': latest_question_list,}
	# return HttpResponse(template.render(context, request)) not good way
	return render(request, 'polls/index.html', context)
	
def detail(request, question_id):
	# not fast way!
	# try:
		# question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
		# raise Http404('Question does not exist')

	question = get_object_or_404(Question, pk=question_id) # get_list_or_404 (не гет, а фильтр если хочешь!)
	return render(request, 'polls/detail.html', {'question': question})

	return HttpResponse('You are looking at question {}.'.format(question_id))

def results(request, question_id):
	response = 'You are looking at the results of question %s.'
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse('You are voting on question {}.'.format(question_id))
