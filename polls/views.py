 
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Option

# Create your views here.
def home(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "index.html", context)

# get question and display result
def result(request, question_id):
    selected_question = Question.objects.get(pk=question_id)
    return render(request, "result.html", {'question': selected_question})

# to show a specific question and choices
def detail(request, question_id):
    try:
        selected_question = Question.objects.get(pk=question_id)
    except:
        return HttpResponse('Question not found')
    return render(request, "detail.html", {'question': selected_question})

# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.option_set.get(pk=request.POST['choice'])
    except (KeyError, Option.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('result', args=(question.id,)))
