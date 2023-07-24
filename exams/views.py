from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Quiz,Question,Option,StudentAttempt
# Create your views here.

@login_required
def quiz_detail(request,quiz_id,quiz_name):
    quiz=get_object_or_404(Quiz,pk=quiz_id,name=quiz_name)
    questions=Question.objects.filter(quiz=quiz)
    context={'quiz':quiz,'questions':questions}
    return render(request,"exams/quizz_page.html",context)

@login_required
def submit_quiz(request,quiz_id):
    if request.method == 'POST' and request.is_ajax():
        user = request.user
        quiz = get_object_or_404(Quiz, pk=quiz_id)

        # Check if the user has attempted the quiz before
        student_attempt = StudentAttempt.objects.filter(user=user, quiz=quiz).first()
        if student_attempt:
            return JsonResponse({
                'message': 'Sorry, you have already attempted this quiz before.',
                'score': student_attempt.score
            }, status=403)

        selected_answers = request.POST.getlist('selected_answers[]', [])
        questions = Question.objects.filter(quiz=quiz)

        # Calculate the score based on selected answers
        score = 0
        for question in questions:
            correct_option = question.option_set.filter(is_correct=True).first()
            selected_option_id = int(selected_answers.get(str(question.id), -1))
            if selected_option_id == correct_option.id:
                score += 1

        # Save the student attempt
        student_attempt = StudentAttempt(user=user, quiz=quiz, score=score)
        student_attempt.save()

        return JsonResponse({'score': score}, status=200)

    return JsonResponse({'message': 'Bad Request'}, status=400)