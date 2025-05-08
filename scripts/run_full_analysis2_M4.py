import data_extraction_1M1 as M1
import data_preparation_M2 as M2
import data_analysis_M3 as M3

def run_full_analysis(cloud_url, data_folder, output_folder, n=1):
    print("Step 1: Downloading and collating responses")
    M2.download_answer_files(cloud_url, data_folder, respondent_index=25) 
    M2.collate_answer_files(data_folder)

    collated_file = f"{output_folder}/collated_answers.txt"

    print("Step 2: Extracting structured answer seq")
    for i in range(1,26):
        input_file = f"{data_folder}/answers_respondent_{i}.txt"
        answers = M1.extract_answers_sequence(input_file)
        M1.write_answers_sequence(answers, i)

    print("Step 3: Analysing and visualising data")
    means_sequence = M3.generate_means_sequence(collated_file)
    M3.visualise_data(collated_file, n)

    print("Pipeline execution complete: Results save in:", output_folder)

cloud_url = "https://drive.google.com/drive/folders/1wq4I1RFFIZ7fz0tQ9ojcBSOHFe1AX95y?usp=drive_link"
data_folder = "data/raw_answers"
output_folder = "results/analysis_M4"
run_full_analysis(cloud_url, data_folder, output_folder, n=1) 