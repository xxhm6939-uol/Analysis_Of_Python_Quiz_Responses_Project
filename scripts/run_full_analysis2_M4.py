import data_extraction_M1 as M1
import data_preparation_M2 as M2
import data_analysis_M3 as M3

def run_full_analysis(cloud_url, data_folder, output_folder, n=1):
    print("Step 1: Downloading and collating responses")
    M2.download_answer_files(cloud_url, data_folder, respondent_index=25) 
    M2.collate_answer_files(data_folder)

    # collated_file = f"{output_folder}/collated_answers.txt"
    collated_file = "output/collated_answers.txt"

    print("Step 2: Extracting structured answer seq")
    for i in range(1,26):
        input_file = f"{data_folder}/answers_respondent_{i}.txt"
        answers = M1.extract_answers_sequence(input_file)
        M1.write_answers_sequence(list_answers, i)

    print("Step 3: Analysing and visualising data")
    sequences = M3.m3(collated_file)
    means_sequence = M3.generate_means_sequence(sequences)
    M3.visualise_data(sequences, n)

    print("Pipeline execution complete: Results save in:", output_folder)

def collate_extracted_answers(output_path="output/collated_answers.txt", count=25):
    os.makedirs("output", exist_ok=True)
    with open(output_path, 'w') as outfile:
        for i in range(1, count + 1):
            input_path = f"answers_list_respondent_{i}.txt"
            if os.path.exists(input_path):
                with open(input_path, 'r') as infile:
                    outfile.write(infile.read())
                    outfile.write("*\n")
            else:
                print(f"⚠️ Missing extracted answer file: {input_path}")


# cloud_url = "https://drive.google.com/drive/folders/1wq4I1RFFIZ7fz0tQ9ojcBSOHFe1AX95y?usp=drive_link"
cloud_url = "https://drive.google.com/drive/folders/1wq4I1RFFIZ7fz0tQ9ojcBSOHFe1AX95y?usp=sharing"
data_folder = "data/raw_answers"
output_folder = "results/analysis_M4"
run_full_analysis(cloud_url, data_folder, output_folder, n=1) 
