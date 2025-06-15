print("Mohd.Jawwad Ali Farooqui, USN:1AY24AI070, SEC:O")
import os
import shutil
def copy_files_with_extension(source_folder, destination_folder, file_extension):
    os.makedirs(destination_folder, exist_ok=True)
    file_extension = file_extension.lower()
    count = 0
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.lower().endswith(file_extension):
                source_path = os.path.join(foldername, filename)
                destination_path = os.path.join(destination_folder, filename)
                if os.path.exists(destination_path):
                    base, ext = os.path.splitext(filename)
                    i = 1
                    while os.path.exists(destination_path):
                        destination_path = os.path.join(destination_folder, f"{base}_{i}{ext}")
                        i += 1
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} → {destination_path}")
                count += 1
    print(f"\nTotal files copied: {count}")
source = input("Enter the path to the source folder: ").strip()
destination = input("Enter the path to the destination folder: ").strip()
extension = input("Enter the file extension to search for (e.g., .pdf, .jpg): ").strip()
copy_files_with_extension(source, destination, extension)
