print("Mohd.Jawwad Ali Farooqui, USN:1AY24AI070, SEC:O")
import re
def mad_libs(input_filename, output_filename):
    # Read the content of the file
    with open(input_filename, 'r') as file:
        content = file.read()
    placeholders = re.findall(r'\b(ADJECTIVE|NOUN|VERB|ADVERB)\b', content)
    for word in placeholders:
        article = "an" if word[0] in "AEIOU" else "a"
        user_input = input(f"Enter {article.lower()} {word.lower()}: ")
        # Replace only the first occurrence each time
        content = content.replace(word, user_input, 1)
    print("\nGenerated Mad Libs:\n")
    print(content)
    with open(output_filename, 'w') as file:
        file.write(content)
    print(f"\nSaved to '{output_filename}'")
input_file = input("Enter the path to your Mad Libs template file: ").strip()
output_file = "madlib_result.txt"
mad_libs(input_file, output_file)
