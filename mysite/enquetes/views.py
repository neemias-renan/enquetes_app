from unicodedata import category
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy,reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'enquetes/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'enquetes/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'enquetes/results.html'

def createView(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')

        questionCreation = Question.objects.create(question_text = title, category = category)
        choiceOneCreation = Choice.objects.create(question = questionCreation, choice_text = option1)
        choiceTwoCreation = Choice.objects.create(question = questionCreation, choice_text = option2)
        choiceThreeCreation = Choice.objects.create(question = questionCreation, choice_text = option3)
        return HttpResponseRedirect(reverse('enquetes:index'))

    return render(request, "enquetes/create.html")


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'enquetes/detail.html', {
            'question': question,
            'error_message': "Escolha uma alternativa.",
        })
    else:
        questionId = Question.objects.get(pk=question_id)
        questionId.all_votes += 1
        questionId.save()
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('enquetes:results', args=(question.id,)))
