import sys
from predictor import *

# Ensure a filename is provided
if len(sys.argv) < 2:
    print("No input file provided")
    sys.exit(1)

# Read the file content
input_filename = sys.argv[1]
try:
    with open(input_filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print(f"File {input_filename} not found.")
    sys.exit(1)

# Check if the file is empty
if not text.strip():
    print("The file is empty.")
    sys.exit(1)

# Call retorn_class function and handle any errors
try:
    clase = retorn_class(text)
except Exception as e:
    print(f"Error while classifying text: {e}")
    sys.exit(1)

# Process the text as needed
processed_text = f"Processed: {clase}"

# Output the result
print(processed_text)
