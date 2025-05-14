

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
                if '[x]' in answer_line:
                    current_answer = 1 + k 
                    break
                k +=1

            answers.append(current_answer)
            i += 5
    
        else:
            i += 1

    return answers



#list_answers = extract_answers_sequence("data/raw_answers/answers_respondent_1.txt")
def write_answers_sequence(list_answers, int_n):
    new_text_file = f"data/answers_list_respondent_{int_n}.txt"
    with open(new_text_file, 'w') as file:
        file.writelines(f"{answer}\n" for answer in list_answers)    # sets new name to the text file containing answers list
    
    print(f"Answers saved to text file!")

for i in range(1, 26):
    input_path = f"data/raw_answers/answers_respondent_{i}.txt"
    answers = extract_answers_sequence(input_path)
    print(f"Respondent {i}: extracted {len(answers)} answers")
    write_answers_sequence(answers, i)
answers = extract_answers_sequence("data/raw_answers/answers_respondent_2.txt")
print(answers)