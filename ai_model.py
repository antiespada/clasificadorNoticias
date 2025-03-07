import sys
from predictor import *

if len(sys.argv) < 2:
    print("No input file provided")
    sys.exit(1)

input_filename = sys.argv[1]
try:
    with open(input_filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print(f"File {input_filename} not found.")
    sys.exit(1)

if not text.strip():
    print("The file is empty.")
    sys.exit(1)

try:
    clase = retorn_class(text)
except Exception as e:
    print(f"Error while classifying text: {e}")
    sys.exit(1)

processed_text = f"Processed: {clase}"
print(processed_text)
