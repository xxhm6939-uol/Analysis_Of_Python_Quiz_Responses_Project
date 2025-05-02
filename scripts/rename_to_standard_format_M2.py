import os

folder = "data/quiz_answers_named_a1_to_a25"

for i in range(1, 26):
    old_name = f"a{i}.txt"
    new_name = f"answers_respondent_{i}.txt"
    old_path = os.path.join(folder, old_name)
    new_path = os.path.join("data", new_name)

    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} → {new_name}")
    else:
        print(f"{old_name} not found")