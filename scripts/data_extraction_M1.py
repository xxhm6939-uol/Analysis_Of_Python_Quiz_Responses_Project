def extract_answers_sequence(string_file_path):
    answers = []

    with open(file_path, 'r') as file:
        survey = file.read()

    survey_questions = survey.split('.')
    question_number = survery_questions[0]


    for answer_box in survey.split('\n'):
        answer_box = answer_box.split()
        if '[x]' in answer_box.split():
            answer_number = answer_box[1]
            answers.append(answer_number)

    print(f"Answers collected!")
    


