print("Mohd.Jawwad Ali Farooqui, USN:1AY24AI070, SEC:O")
import os
import re
def search_txt_files(folder_path, user_regex):
    regex = re.compile(user_regex)
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_num, line in enumerate(file, start=1):
                        if regex.search(line):
                            print(f"Match in {filename}, Line {line_num}: {line.strip()}")
            except Exception as e:
                print(f"Could not read {filename}: {e}")
folder = input("Enter the path to the folder: ").strip()
pattern = input("Enter the regular expression to search: ").strip()
search_txt_files(folder, pattern)
