
import os 

def extract_answers_sequence(string_file_path):

    answers = []

    with open(string_file_path, 'r', 'utf-8') as file:
        survey = file.read()
        current_answer = 0
        
        for text in survey:
            text = survey.strip('.')
            
            if text.startswith('**Question'):
                answers.append(current_answer)
                current_answer = 0            
     
            elif text.startswith('[x]'):
                try:
                    answer_box = answer_box.split('.')
                    answer_number = int(answer_box[1][0])
                    answers[current_answer] = answer_number
                except (ValueError):
                    current_answer = 0
        answers.append(current_answer)
        return answers[1:]

list_answers = extract_answers_sequence(string_file_path)
def write_answers_sequence(list_answers, int_n):
    list_answers = extract_answers_sequence(string_file_path)
    new_text_file = f"answers_list_respondent_{int_n},.txt"

    with open(new_text_file, 'w') as file:
        f.write(f"{answer}\n" for answer in list_answers)
    
    print(f"Answers saved to text file!")





