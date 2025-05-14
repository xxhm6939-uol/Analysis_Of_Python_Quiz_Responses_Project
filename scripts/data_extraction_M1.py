

def extract_answers_sequence(string_file_path):

    answers = []   # creates an empty list to store the answer values 
    current_answer = 0 
    i = 0 

    with open(string_file_path, 'r', encoding = 'utf-8') as file:
        survey = file.readlines()      # opens the file to read only 
    

    while i < len(survey):
        text = survey[i].strip()

        if text.startswith("Question"):
            current_answer = 0   # if a line starts with "Question", current answer remains 0 
            question_block = survey[i+1:i+5]

            k = 0

            for answer_line in question_block:
                answer_line = answer_line.strip()
                if answer_line.startswith('[x]'):
                    current_answer = 1 + k 
                    break
                k +=1

            answers.append(current_answer)
            i += 5
    
        else:
            i += 1

    return answers






def write_answers_sequence(list_answers, i):
    new_text_file = f"answers_list_respondent_{i}.txt"

    with open(new_text_file, 'w') as file:
        file.writelines(f"{answer}\n" for answer in list_answers)    # sets new name to the text file containing answers list
    
    print(f"Answers saved to text file!")


