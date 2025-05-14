import os
from data_preparation_M2 import download_answer_files, collate_answer_files
from data_extraction_M1 import extract_answers_sequence, write_answers_sequence
from data_analysis_M3 import visualize_data

def run_full_analysis():

    cloud_url = "https://drive.google.com/drive/folders/1wq4I1RFFIZ7fz0tQ9ojcBSOHFe1AX95y?usp=sharing"
    data_folder = "data/raw_answers"
    structured_folder = "data"
    collated_file_path = "output/collated_answers.txt"
    respondent_index = 25
    plot_mode = 1,2  

<<<<<<< HEAD
    print("Step 2: Extracting structured answer seq")
    for i in range(1,26):
        input_file = f"{data_folder}/answers_respondent_{i}.txt"
        answers = M1.extract_answers_sequence(input_file)
        M1.write_answers_sequence(list_answers, i)
=======
    print("="*50)
    download_answer_files(cloud_url, data_folder, respondent_index)
>>>>>>> c5105befb533baca60e6671049c49deb718e1f21

    for i in range(1, respondent_index + 1):
        input_file = os.path.join(data_folder, f"answers_respondent_{i}.txt")
        answers = extract_answers_sequence(input_file)
        write_answers_sequence(answers, i)

    collate_answer_files(structured_folder)


    visualize_data(collated_file_path, plot_mode)



if __name__ == "__main__":
    run_full_analysis()