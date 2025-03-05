import sys
from predictor import *

# Ensure a filename is provided
if len(sys.argv) < 2:
    print("No input file provided")
    sys.exit(1)

# Read the file content
input_filename = sys.argv[1]
with open(input_filename, 'r') as file:
    text = file.read()
clase = retorn_class(text)
# Process the text as needed (this example just echoes it)
processed_text = f"Processed: {clase}"

print(processed_text)
