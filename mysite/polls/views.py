from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
# def index(request):
# 	latest_question_list = Question.objects.order_by('pub_date')
# 	context = {
# 		'latest_question_list': latest_question_list,
# 	}
# 	return render(request, 'polls/index.html', context)


# def detail(request, question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.doesNotExist:
# 		raise Http404("Question does not exist")
# 	return render(request, 'polls/detail.html', {'question':question})

# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def add_question(request,question_text):
    q = Question(question_text=question_text, pub_date = timezone.now())
    q.save()
    return HttpResponse("You added the following question: {} , with the id {}".format(question_text,q.id))

def add_choice(request, question_id, choiceText):
	q = Question.objects.get(id=int(question_id))
	c = q.choice_set.create(choice_text=choiceText,votes=0)
	return HttpResponse("You added the following choice: {} , with the id {}, to the following question {}".format(c.choice_text,c.id,c.question))	

def clean_questions(request,question_id):
	print(Question.objects.values_list('id','question_text'))
	q = Question.objects.get(id=int(question_id))
	q.delete()
	return HttpResponse("Deleted question %s" %question_id)

def show_questions(request):
	return HttpResponse(Question.objects.values_list('id','question_text'))