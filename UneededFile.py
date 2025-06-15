print("Mohd.Jawwad Ali Farooqui, USN:1AY24AI070, SEC:O")
import os
def find_large_files(folder_path, size_threshold_mb=100):
    size_threshold_bytes = size_threshold_mb * 1024 * 1024
    large_files_found = 0
    print(f"\nScanning for files larger than {size_threshold_mb}MB in:\n{os.path.abspath(folder_path)}\n")
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            try:
                file_path = os.path.join(foldername, filename)
                file_size = os.path.getsize(file_path)
                if file_size > size_threshold_bytes:
                    size_mb = file_size / (1024 * 1024)
                    print(f"{os.path.abspath(file_path)} - {size_mb:.2f} MB")
                    large_files_found += 1
            except (PermissionError, FileNotFoundError):
                continue
    if large_files_found == 0:
        print("No files larger than the specified size were found.")
    else:
        print(f"\nTotal large files found: {large_files_found}")
folder = input("Enter the path to the folder to scan: ").strip()
find_large_files(folder)
