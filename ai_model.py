# ai_model.py
import sys

def process_input(input_value):
    # Return the first letter of the input
    return input_value[0] if input_value else "No input provided"

if __name__ == "__main__":
    input_value = sys.argv[1]
    print(process_input(input_value))
