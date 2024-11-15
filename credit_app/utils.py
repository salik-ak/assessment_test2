from .models import UserResponse, Question

def calculate_credit_score(user):
    responses = UserResponse.objects.filter(user=user)
    total_score = 0
    total_weight = 0

    # Define weightages for each question category (higher weight = more impact on credit score)
    weight_mapping = {
        "On-time Payments": 0.4,     # 40% weight
        "Industry Risk": 0.2,        # 20% weight
        "Company Age": 0.1,          # 10% weight
        "Number of Employees": 0.1,  # 10% weight
        "Profit/Loss Ratio": 0.2     # 20% weight
    }

    # Loop through user responses and calculate total weighted score
    for response in responses:
        question = response.question

        # Fetch the score for the selected option
        if response.selected_option == 'A':
            score = question.score_a
        elif response.selected_option == 'B':
            score = question.score_b
        elif response.selected_option == 'C':
            score = question.score_c
        elif response.selected_option == 'D':
            score = question.score_d
        else:
            score = 0  # Default score if no valid option is selected

        # Assign weight based on question category
        question_weight = weight_mapping.get(question.category, 0.1)
        total_weight += question_weight

        # Add the weighted score to the total
        total_score += score * question_weight

    # Normalize the total score to a range of 0 to 100
    if total_weight > 0:
        normalized_score = (total_score / total_weight) * 100
    else:
        normalized_score = 0

    return round(normalized_score, 2)

