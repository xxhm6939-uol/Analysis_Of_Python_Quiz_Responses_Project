

def extract_answers_sequence(file_path):
    f = open(file_path, "r")

    lines = [line.strip() for line in f.readlines()]
    answers = []
    
    i = 0

    while i < len(lines):
        if lines[i].startswith("Question"):
                options = lines[i+1:i+5]
                answer = 0
                for j in range(4):
                    if "[x]" in options[j]:
                        answer = j+1
                        break
                answers.append(answer)
                i+=5
        else:
            i+=1
    f.close()

    return answers


def extract_answers_sequence(string_file_path):

    answers = []   # creates an empty list to store the answer values 
    current_answer = 0 

    with open(string_file_path, 'r', encoding = 'utf-8') as file:
        survey = file.read()      # opens the file to read only 
    
    text = survey[i].strip()
    i = 0 

    while i < len(survey):
        

        if text[i].startswith("Question"):
            answers.append(current_answer)
            current_answer = 0   # if a line starts with "Question", current answer remains 0 
            question_block = survey[i+1:i+5]

            k = 0

            for k in range(4):
                question = question_block.strip()
                if question.startswith('[x]'):
                    current_answer = 1 + k 
                
            answers.append(current_answer)
            i += 5
    
        else:
            i += 1

    return answers

file_name = 'data/answers_respondent_2.txt'
answers = extract_answers_sequence(file_path)
print(answers)





list_answers = extract_answers_sequence(string_file_path)
def write_answers_sequence(list_answers, int_n):
    list_answers = extract_answers_sequence(string_file_path)
    new_text_file = f"answers_list_respondent_{int_n},.txt"

    with open(new_text_file, 'w') as file:
        f.write(f"{answer}\n" for answer in list_answers)    # sets new name to the text file containing answers list
    
    print(f"Answers saved to text file!")


