import os

def count_words_in_file(file_path):
    # Implement your logic for counting words within a single file
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return len(text.split())

def count_words_in_files(directory):
    total_words = 0
    
    # Iterate over everything in the directory
    for entry in os.listdir(directory):
        path = os.path.join(directory, entry)
        
        # If it's a directory, recurse into it
        if os.path.isdir(path):
            total_words += count_words_in_files(path)
        
        # If it's a file with a .md extension, count its words
        elif entry.lower().endswith(".md"):
            total_words += count_words_in_file(path)
    
    return total_words

directory_path = 'Book Idea (AI Safety textbook)'
total_words = count_words_in_files(directory_path)
print("Total words in all Markdown files:", total_words)