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

collate_extracted_answers()