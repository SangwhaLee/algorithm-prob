from django.shortcuts import render, redirect

from .models import Question, Comment
from .forms import QuestionForm, CommentForm
from random import choice
# Create your views here.

def index(request):
    questions = Question.objects.order_by('pk')
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)


def detail(request, pk):
    question = Question.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = question.comment_set.all()
    count_a = comments.filter(pick="RED TEAM").count()
    count_b = comments.filter(pick="BLUE TEAM").count()
    total_count = count_a + count_b
    if total_count != 0:
        per_a = round(count_a / total_count * 100, 2)
        per_b = round(count_b / total_count * 100, 2)
    else:
        per_a = 0
        per_b = 0
    context = {
        'question': question,
        'comment_form':comment_form,
        'comments':comments,
        'count_a': count_a,
        'count_b': count_b,
        'per_a': per_a,
        'per_b': per_b,
    }
    return render(request, 'eithers/detail.html', context)



def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('eithers:detail', question.pk)
    else:
        form = QuestionForm()
    context = {
        'form':form,
    }
    return render(request, 'eithers/create.html', context)

def comment_create(request, pk):
    question = Question.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.question = question
        comment.save()
    return redirect('eithers:detail', question.pk)


def random(request):
    question = choice(Question.objects.all())
    comment_form = CommentForm()
    comments = question.comment_set.all()
    count_a = comments.filter(pick="RED TEAM").count()
    count_b = comments.filter(pick="BLUE TEAM").count()
    total_count = count_a + count_b
    if total_count != 0:
        per_a = round(count_a / total_count * 100, 2)
        per_b = round(count_b / total_count * 100, 2)
    else:
        per_a = 0
        per_b = 0
    context = {
        'question': question,
        'comment_form':comment_form,
        'comments':comments,
        'count_a': count_a,
        'count_b': count_b,
        'per_a': per_a,
        'per_b': per_b,
    }
    return render(request, 'eithers/detail.html', context)