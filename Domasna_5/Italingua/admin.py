from django.contrib import admin
from .models import Lecture, Quiz, QuizQuestions, UserPerson, ForumQuestion, Comment


# Register your models here.
class Lectures(admin.ModelAdmin):
    list_display = ("name", "description")

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Lecture, Lectures)
#######################################

class UserPersons(admin.ModelAdmin):
    list_display = ("name", "surname", "level")


admin.site.register(UserPerson, UserPersons)
#########################################

class Questions(admin.ModelAdmin):
    list_display = ("quiz", "quizName", "question1", "question2")


admin.site.register(QuizQuestions, Questions)
##########################################


class QuizAdmin (admin.ModelAdmin):
    list_display = ("name", "for_lecture")


admin.site.register(Quiz, QuizAdmin)
##########################################


class ForumAdmin (admin.ModelAdmin):
    list_display = ("content", "author", "numberOfReplies")


admin.site.register(ForumQuestion, ForumAdmin)
#########################################


class CommentAdmin(admin.ModelAdmin):
    list_display = ("commentAuthor", "comment")

admin.site.register(Comment, CommentAdmin)