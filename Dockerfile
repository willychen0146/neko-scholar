# Use an official Python runtime as the base image
FROM python:3.11.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt /code/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt
# RUN pip install -r requirements.txt

# Copy project
COPY . /code/

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]