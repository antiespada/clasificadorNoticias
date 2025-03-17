# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first for better caching
COPY requirements.txt /app/

# Upgrade pip and install dependencies (these will be baked into the image)
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of your code
COPY . /app/

# Default command: run your analysis script
CMD ["python", "ai_model.py", "input.txt"]
