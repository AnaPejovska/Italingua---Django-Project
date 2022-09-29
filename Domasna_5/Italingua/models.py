from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Lecture(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    time = models.IntegerField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    for_lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)


class QuizQuestions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quizName = models.CharField(max_length=20, default=None)
    question1 = models.CharField(max_length=100)
    question2 = models.CharField(max_length=100)


class UserPerson (models.Model):
    class Level(models.TextChoices):
        Level1 = 'Level A1'
        Level2 = 'Level A2'
        Level3 = 'Level B1'
        Level4 = 'Level B2'
        Level5 = 'Level C1'
        Level6 = 'Level C2'
        Level7 = 'Proffessional'
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=50)
    level = models.CharField(max_length=50,
                             choices=Level.choices,
                             default=Level.Level1,)

    def __str__(self):
        return self.name + " " + self.surname


class ForumQuestion(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    numberOfReplies = models.IntegerField(default=0)

    def __str__(self):
        return self.content


class Comment(models.Model):
    replyTo = models.ForeignKey(ForumQuestion, on_delete=models.CASCADE, default=None)
    commentAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment
