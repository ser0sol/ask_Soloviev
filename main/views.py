from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.models import Question, Answer, Tag, Profile
import json

# questions = []
# for i in xrange(1,100):
# 	questions.append({
# 		'title' : 'title {}'.format(i),
# 		'id' : i,
# 		'text' : 'some text {}'.format(i),
# 	})

# answers = []
# for i in xrange(1,100):
# 	answers.append({
# 		'text' : 'my opinion {}'.format(i),
# 	})

def pagination(element, page, elements_count):
	pager = Paginator(element, elements_count)
	try:
		qlist = pager.page(page or 1)
	except EmptyPage:
		qlist = pager.page(pager.num_pages)
	except PageNotAnInteger:
		#qlist = pager.page(pager.num_pages)
		qlist = pager.page(1)
	return qlist

def index(request, page=None):
	questions = Question.objects.all()
	qlist = pagination(questions, page, 5)
	q = Question.objects.get(pk = 1)
	tag = q.tags.name
	return render(request,'index.html', {
		'questions' : qlist,
	    'page' : page,
	    'tag' : tag,
	})

def question(request, question_id, page):
	question = Question.objects.get(id = question_id)
	answers = question.answer_set.all()
	qlist = pagination(answers, page, 2)
	return render(request,'question.html', {
		'question' : question,
		'answers' : qlist,
	})
	#return HttpResponse("aaa %s" %question_id )


def hot(request, page=None):
	questions = Question.objects.hot()
	qlist = pagination(questions, page, 5)
	return render(request,'index.html', {
		'questions' : qlist,
	    'page' : page,
	})

def tag(request, tagname, page):
	tag = Tag.objects.get(name = tagname)
	questions = tag.question_set.all()
	qlist = pagination(questions, page, 3)
	return render(request,'index.html', {
	'tag' : tag,
	'questions' : qlist,
	})


def newest(request, page=None):
	questions = Question.objects.newest()
	qlist = pagination(questions, page, 5)
	return render(request,'index.html', {
		'questions' : qlist,
	})
def ask(request):
	return render(request,'ask.html')

def signin(request):
	return render(request,'login.html')

def reg(request):
	return render(request,'registration.html')

def getparametrs(request):
	return render(request,'GetParametrs.html')

def search(request):
	if request.GET.get('q'):
		message = "You searched for: %s " %request.GET['q']
	else:
		message = "Form is empty"

	return HttpResponse(message)
# Create your views here.
