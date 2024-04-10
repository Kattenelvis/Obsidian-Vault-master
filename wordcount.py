import os
import re

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Remove Markdown formatting
            text = re.sub(r'(^#+\s*)|(\*\*|__|\*|_|```.+?```)', '', text, flags=re.MULTILINE)
            words = text.split()
            return len(words)
    except Exception as e:
        print(f"Error reading file '{file_path}': {str(e)}")
        return 0

def count_words_in_files(directory):
    total_words = 0
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)
            total_words += count_words_in_file(file_path)
    return total_words

directory_path = 'Book Idea (AI Safety textbook)'
total_words = count_words_in_files(directory_path)
print("Total words in all Markdown files:", total_words)