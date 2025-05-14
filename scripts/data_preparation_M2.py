import os
import subprocess

import sys

# dowmload gdown
subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown"])
def download_answer_files(cloud_url, path_to_data_folder, respondent_index):

    os.makedirs(path_to_data_folder, exist_ok=True)

    

    # gdown --folder URL -O path
    command = [
        "gdown",
        "--folder",
        cloud_url,
        "-O",
        path_to_data_folder
    ]

    try:
        subprocess.run(command, check=True)
        print(" Download complete.")
    except Exception as e:
        print(f" Download failed: {e}")
        return

    # a1.txt rename to answers_respondent_1.txt 
    for i in range(1, respondent_index + 1):
        original = os.path.join(path_to_data_folder, f"a{i}.txt")
        renamed = os.path.join(path_to_data_folder, f"answers_respondent_{i}.txt")
        if os.path.exists(original):
            os.rename(original, renamed)
            print(f" Renamed {original} → {renamed}")
        else:
            print(f" File missing: {original}")


def collate_answer_files(data_folder_path):
    
    os.makedirs("output", exist_ok=True)
    output_path = os.path.join("output", "collated_answers.txt")

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for filename in sorted(os.listdir(data_folder_path)):
            if filename.startswith("answers_list_respondent_") and filename.endswith(".txt"):
                file_path = os.path.join(data_folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write("*\n")

    print(f"Collation complete: {output_path}")
    print(" Collate function has run.")
from data_preparation_M2 import collate_answer_files
collate_answer_files("data")