
from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
# Leave the rest of the views (detail, results, vote) unchanged

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)





from django.views.generic import CreateView, ListView, DetailView, DeleteView,UpdateView
from django.urls import reverse_lazy

class QuestionCreateView(CreateView):
    model = Question
    fields = ('question_text',)
    success_url = reverse_lazy('question-list')
    template_name = 'polls/question_form.html'

class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-pub_date']
    paginate_by = 5

class QuestionDetailView(DetailView):
    model = Question
    context_object_name = 'question'

class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy("question-list")
    success_message = "enquete excluída com sucesso"


    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super ().form_valid(form)

class QuestionUpdateView(UpdateView):
    model = Question
    template_name = 'polls/question_form.html'
    fields = ('question_text', )
    success_url = reverse_lazy('question_list')

   
