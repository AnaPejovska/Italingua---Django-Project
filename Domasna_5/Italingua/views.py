from django.shortcuts import render, redirect
from .models import Lecture, QuizQuestions, Quiz, UserPerson, User, ForumQuestion, Comment
from .forms import QuestionForm, ReplyForm
# Create your views here.


def home(request):
    person = UserPerson.objects.filter(user=request.user)
    context = {"person": person}
    return render(request, 'home.html', context=context)


def test(request):
    person = UserPerson.objects.filter(user=request.user)
    context = {"person": person}
    return render(request, 'test.html', context=context)


def lectures(request):
    person = UserPerson.objects.filter(user=request.user)
    lectures_all = Lecture.objects.all().order_by('name').values()
    context = {'lectures': lectures_all, 'person': person}
    return render(request, 'lectures.html', context)


def profile(request):
    person = UserPerson.objects.filter(user=request.user)
    context = {"person": person}
    return render(request, "profile.html", context=context)


def practice(request):
    person = UserPerson.objects.filter(user=request.user)
    quizzes = Quiz.objects.all()
    context = {"quizzes": quizzes, "person": person}
    return render(request, 'practice.html', context=context)


def congratulations(request):
    person = UserPerson.objects.filter(user=request.user)
    context = {"person": person}
    return render(request, 'congratulations.html', context=context)


def choose(request):
    person = UserPerson.objects.filter(user=request.user)
    context = {"person": person}
    return render(request, 'choose.html', context=context)


def forum(request):
    person = UserPerson.objects.filter(user=request.user)
    questions = ForumQuestion.objects.all()
    context = {"questions": questions, "person": person}
    return render(request, 'forum.html', context)


def addQuestion(request):
    person = UserPerson.objects.filter(user=request.user)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("forum")
    else: #ako ne e post, daj ja stranata so forma
        context = {"person": person, "form": QuestionForm}
        return render(request, 'addQuestion.html', context=context)


def reply(request):
    person = UserPerson.objects.filter(user=request.user)
    if (request.method == "POST"):
        form = ReplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("forum")
    context = {"person": person, "form": ReplyForm}
    return render(request, "reply.html", context=context)


def replies(request):
    person = UserPerson.objects.filter(user=request.user)
    all = Comment.objects.all()
    context = {'person': person, 'replies': all}
    return render(request, "replies.html", context=context)


def quiz(request):
    prasanja = QuizQuestions.objects.all()
    context = {"prasanja": prasanja}
    return render(request, 'quiz.html', context)
