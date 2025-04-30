import os
import urllib.request
import shutil
def download_answer_files(cloud_url, path_to_data_folder, respondent_index):
        os.makedirs(path_to_data_folder, exist_ok=True)
        for i in range(1,respondent_index + 1):
             original_name= f"a{i}.txt"
             download_url=f"{cloud_url}/{original_name}"
             new_name = f"answers_respondent_{i}.txt"
             local_path = os.path.join(path_to_data_folder, new_name)
        try:
         file_data = urllib.request.urlopen(download_url).read()
         with open(local_path, "wb") as f:
                f.write(file_data)
         print(f"Downloaded: {new_name}")  
        except:
             
            print(f"Failed to download a{i}.txt")

        
    
def collate_answer_files(data_folder_path):
    import os
    os.makedirs("output", exist_ok=True)
    output_path = os.path.join("output", "collated_answers.txt")
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for filename in sorted(os.listdir(data_folder_path)):
            if filename.startswith("answers_respondent_") and filename.endswith(".txt"):
                file_path = os.path.join(data_folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    
                    outfile.write(infile.read())
                    outfile.write("\n*\n")

    print("Collation complete: 'collated_answers.txt' has been saved to the output/ folder.")


