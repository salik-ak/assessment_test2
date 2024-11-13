from .models import UserResponse, Question

def calculate_credit_score(user):
    responses = UserResponse.objects.filter(user=user)
    total_score = 0

    for response in responses:
        question = response.question
        if response.selected_option == 'A':
            total_score += question.score_a
        elif response.selected_option == 'B':
            total_score += question.score_b
        elif response.selected_option == 'C':
            total_score += question.score_c
        elif response.selected_option == 'D':
            total_score += question.score_d

    return total_score
