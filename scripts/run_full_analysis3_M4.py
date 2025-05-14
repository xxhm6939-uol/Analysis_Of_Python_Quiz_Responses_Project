import data_extraction_M1 as M1
import data_preparation_M2 as M2
import data_analysis_M3 as M3
import os

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

def run_full_analysis(cloud_url, data_folder, output_folder, n=1):
    print("Step 1: Downloading raw answer files")
    M2.download_answer_files(cloud_url, data_folder, respondent_index=25)

    print("Step 2: Extracting structured answer sequences")
    for i in range(1, 26):
        input_file = f"{data_folder}/answers_respondent_{i}.txt"
        if os.path.exists(input_file):
            list_answers = M1.extract_answers_sequence(input_file)
            M1.write_answers_sequence(list_answers, i)
        else:
            print(f"⚠️ Missing file: {input_file}")

    print("Step 3: Collating extracted numeric answers")
    collate_extracted_answers(output_path="output/collated_answers.txt", count=25)

    print("Step 4: Analysing and visualising data")
    collated_file = "output/collated_answers.txt"
    sequences = M3.m3(collated_file)
    means_sequence = M3.generate_means_sequence(sequences)
    M3.visualize_data(sequences, n)

    print("✅ Pipeline complete. Results saved in:", output_folder)


# === Main Execution ===

cloud_url = "https://drive.google.com/drive/folders/1wq4I1RFFIZ7fz0tQ9ojcBSOHFe1AX95y?usp=sharing"
data_folder = "data/raw_answers"
output_folder = "results/analysis_M4"

run_full_analysis(cloud_url, data_folder, output_folder, n=1)
