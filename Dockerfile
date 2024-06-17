# Use the official Python image from Docker Hub
FROM python:3.11

# Set the working directory
WORKDIR /usr/src/app

# Copy requirements.txt first to leverage Docker caching
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port
EXPOSE 8000

# Command to run the application with Gunicorn
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
