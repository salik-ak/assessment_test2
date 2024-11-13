
from django.shortcuts import render, redirect
from .models import Question, UserResponse
from .utils import calculate_credit_score
from django.contrib.auth.models import User

def index(request):
    questions = Question.objects.all()
    return render(request, 'credit_app/index.html', {'questions': questions})

def submit_responses(request):
    if request.method == 'POST':
        user = request.user
        for question in Question.objects.all():
            selected_option = request.POST.get(str(question.id))
            if selected_option:
                UserResponse.objects.create(
                    user=user,
                    question=question,
                    selected_option=selected_option
                )
        score = calculate_credit_score(user)
        return render(request, 'credit_app/result.html', {'score': score})
    return redirect('index')

