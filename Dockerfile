# Use a base image
FROM python:3.10

# Set working directory
WORKDIR /app

COPY requirements.txt .


RUN pip3 install -r requirements.txt

# Copy the entire directory
COPY . .

# Expose port
EXPOSE 8501

# Command to run the Streamlit application
ENTRYPOINT ["streamlit", "run", "/app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]