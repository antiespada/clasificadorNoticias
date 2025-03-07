import sys

if len(sys.argv) < 2:
    print("No input file provided")
    sys.exit(1)

input_filename = sys.argv[1]
try:
    with open(input_filename, 'r', encoding='utf-8') as file:
        text = file.read().strip()
except FileNotFoundError:
    print(f"File {input_filename} not found.")
    sys.exit(1)

if not text.strip():
    print("The file is empty.")
    sys.exit(1)

# No llamamos a retorn_class, asumimos que text ya es el resultado
processed_text = f"Processed: {text}"
print(processed_text)
