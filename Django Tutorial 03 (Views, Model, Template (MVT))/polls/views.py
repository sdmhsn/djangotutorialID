from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    """ output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output) """

    """ template = loader.get_template('polls/index.html')
    context = {
        'latest_question': latest_question_list,
    }
    data_response = template.render(context, request)
    return HttpResponse(data_response) """

    """ context = {'latest_question': latest_question_list}
    return render(request, 'polls/index.html', context) """

    return render(
        request,
        template_name='polls/index.html',
        context={'latest_question': latest_question_list}
    )


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)

    # return HttpResponse(f"You're looking at question {question_id}")

    """ try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist!!!")
    return render(request, 'polls/detail.html', {'question': question}) """

    # question = Question.objects.get(pk=question_id)

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
