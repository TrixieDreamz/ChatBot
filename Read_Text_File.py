# Step 1: Open the text file
file_path = 'path/to/your/book.txt'  # Replace 'path/to/your/book.txt' with the actual path to your text file
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # Step 2: Read the contents
        book_content = file.read()
        print("File successfully read!")
        # Step 3: Close the file (not necessary due to 'with' statement)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print(f"Error occurred: {e}")
