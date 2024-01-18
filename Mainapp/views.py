from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login,logout
import random
from django.contrib.auth.models import User
from .models import Question, QuestionAssignment
def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            question_1 = QuestionAssignment.objects.filter(user=User.objects.get(username='acm_team_1'), solved=True).order_by('order')
            print(question_1)
            question_2 = QuestionAssignment.objects.filter(user=User.objects.get(username='acm_team_2'), solved=True).order_by('order')
            question_3 = QuestionAssignment.objects.filter(user=User.objects.get(username='acm_team_3'), solved=True).order_by('order')
            question_4 = QuestionAssignment.objects.filter(user=User.objects.get(username='acm_team_4'), solved=True).order_by('order')
            question_5 = QuestionAssignment.objects.filter(user=User.objects.get(username='acm_team_5'), solved=True).order_by('order')
            question_6 = QuestionAssignment.objects.filter(user=User.objects.get(username='acm_team_6'), solved=True).order_by('order')
            question_7 = QuestionAssignment.objects.filter(user=User.objects.get(username='acm_team_7'), solved=True).order_by('order')
            question_8 = QuestionAssignment.objects.filter(user=User.objects.get(username='acm_team_8'), solved=True).order_by('order')
            question_9 = QuestionAssignment.objects.filter(user=User.objects.get(username='acm_team_9'), solved=True).order_by('order')
            question_10 = QuestionAssignment.objects.filter(user=User.objects.get(username='acm_team_10'), solved=True).order_by('order')
            return render(request,'Mainapp/acm.html',context={'question_1':question_1,'question_2':question_2,'question_3':question_3,'question_4':question_4,'question_5':question_5,'question_6':question_6,'question_7':question_7,'question_8':question_8,'question_9':question_9,'question_10':question_10})
        else:
            question = QuestionAssignment.objects.filter(user=request.user, solved=False).order_by('order')
            return render(request,'Mainapp/home.html',context={'questions':question})
    return loginMe(request)

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            print("success")
            return JsonResponse({'data':'success'})
        else:
            return HttpResponse(status=401)
    return HttpResponse(status=404)

def logoutPage(request):
    logout(request)
    return home(request)

def loginMe(request):
    return render(request,'Mainapp/login.html')

def assign(request):
    if request.user.is_superuser:
        QuestionAssignment.objects.all().delete()
        # Assuming you have a list of questions (queryset)
        questions = Question.objects.all()
        # Get all custom users
        users = User.objects.all()
        users = users.exclude(username='acm')
        # Iterate over each user
        for user in users:
            # Get questions excluding the 7th question
            random_questions = questions.exclude(id=7).order_by('?')[:6]
            # Get the 7th question
            seventh_question = questions.get(id=7)

            print(random_questions)
            # Create QuestionAssignment instances
            for order, question in enumerate(random_questions, start=1):
                QuestionAssignment.objects.create(user=user, question=question, order=order)
            QuestionAssignment.objects.create(user=user, question=seventh_question, order=7)

        return JsonResponse({"data":"this is data"})
    else:
        return HttpResponse(status=404)

def code(request):
    print("found")
    if request.method=='POST':
        code = request.POST.get('code')
        question = request.POST.get('question_id')
        print(code,question)
        question = Question.objects.get(id=question)
        if question.code == code:
            questionAssignment = QuestionAssignment.objects.get(user=request.user,question=question)
            questionAssignment.solved = True
            questionAssignment.save()
            question.save()
            return JsonResponse({'data':'success'})
        else:
            question.save()
            return HttpResponse(status=500)
    return HttpResponse(status=404)
