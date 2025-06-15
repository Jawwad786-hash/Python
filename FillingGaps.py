print("Mohd.Jawwad Ali Farooqui, USN:1AY24AI070, SEC:O")
import os
import re
def get_numbered_files(folder, prefix, extension):
    pattern = re.compile(rf'^{re.escape(prefix)}(\d+){re.escape(extension)}$')
    numbered_files = []
    
    for filename in os.listdir(folder):
        match = pattern.match(filename)
        if match:
            num = int(match.group(1))
            numbered_files.append((num, filename))
    return sorted(numbered_files)
def close_gaps(folder, prefix, extension):
    files = get_numbered_files(folder, prefix, extension)
    if not files:
        print("No matching files found.")
        return
    next_expected = 1
    for actual_num, filename in files:
        if actual_num != next_expected:
            new_name = f"{prefix}{str(next_expected).zfill(3)}{extension}"
            print(f"Renaming {filename} → {new_name}")
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
        next_expected += 1
    print("Gaps closed.")
def insert_gap(folder, prefix, extension, insert_position):
    files = get_numbered_files(folder, prefix, extension)
    if not files:
        print("No matching files found.")
        return
    for num, filename in sorted(files, reverse=True):
        if num >= insert_position:
            new_num = num + 1
            new_name = f"{prefix}{str(new_num).zfill(3)}{extension}"
            print(f"Renaming {filename} → {new_name}")
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
    print(f"Gap inserted at position {insert_position}.")
def main():
    print("Choose an operation:")
    print("1. Close gaps in numbered files")
    print("2. Insert a gap at a specific position")
    choice = input("Enter 1 or 2: ").strip()
    folder = input("Enter folder path: ").strip()
    prefix = input("Enter file prefix (e.g., spam): ").strip()
    extension = input("Enter file extension (e.g., .txt): ").strip()
    if choice == '1':
        close_gaps(folder, prefix, extension)
    elif choice == '2':
        pos = int(input("Enter position number to insert gap at (e.g., 2 for spam002): "))
        insert_gap(folder, prefix, extension, pos)
    else:
        print("Invalid choice.")
if __name__ == "__main__":
    main()
