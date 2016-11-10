from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone
# from django.template import loader # for not good way
# Create your views here.


# вариант с БОЛЬШИМ количеством кода для понимания
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	# template = loader.get_template('polls/index.html') not good way
# 	context = {'latest_question_list': latest_question_list,}
# 	# return HttpResponse(template.render(context, request)) not good way
# 	return render(request, 'polls/index.html', context)
	
# def detail(request, question_id):
# 	# not fast way!
# 	# try:
# 		# question = Question.objects.get(pk=question_id)
# 	# except Question.DoesNotExist:
# 		# raise Http404('Question does not exist')

# 	question = get_object_or_404(Question, pk=question_id) # get_list_or_404 (не гет, а фильтр если хочешь!)
# 	return render(request, 'polls/detail.html', {'question': question})

# 	return HttpResponse('You are looking at question {}.'.format(question_id))

# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	context = {'question': question} # можно просто в ретерн рендер в конце забахать
# 	return render(request, 'polls/results.html', context)

# вариант с МЕНЬШИМ количеством кода лучше

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self): 
		"""Вернет последние 5 вопросов c нормальным условием по времени!"""
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
        Исключает вопросы которые еще не опубликованы.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', 
			{'question': question, 'error_message': 'You did not select a choice.',})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Всегда возврщай HttpResponseRedirect после того как получил
        # POST данные. Это поможет избежать случаев повторного (неверного) получения данных
        # если пользователь нажмет "назад".

	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
