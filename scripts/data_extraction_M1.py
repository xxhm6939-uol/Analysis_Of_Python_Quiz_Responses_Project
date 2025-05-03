
import os 

def extract_answers_sequence(string_file_path):

    answers = [] # create an empty list to store the answer values 

    with open(string_file_path, 'r', 'utf-8') as file:
        survey = file.read() # opens the file to read only
        current_answer = 0 
        
        for text in survey: 
            text = survey.strip('.') # splits each line into "strips"
            
            if text.startswith('Question'):
                answers.append(current_answer)
                current_answer = 0  # if a line starts with "Question", our current answer remains 0          
     
            elif text.startswith('[x]'): # if line starts with "[x]", it will split again at a fullstop '.'
                try:
                    answer_box = answer_box.split('.')
                    answer_number = int(answer_box[1][0]) # extracts the first digit after the fullstop (number of the answer)
                    answers[current_answer] = answer_number # changes the current answer's value from 0 to answer number
                except (ValueError):
                    current_answer = 0 # exception ensures that if the above process fails, our default answer will remain 0 
        answers.append(current_answer) # creates a list of all answer numbers
        return answers[1:]

list_answers = extract_answers_sequence(string_file_path)
def write_answers_sequence(list_answers, int_n):
    list_answers = extract_answers_sequence(string_file_path) # finds the list of answer numbers 
    new_text_file = f"answers_list_respondent_{int_n},.txt" 

    with open(new_text_file, 'w') as file:
        f.write(f"{answer}\n" for answer in list_answers) # sets new name to the text file containing answers list
    
    print(f"Answers saved to text file!")





