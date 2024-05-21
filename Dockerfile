# Use Python base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /elastic-app/

COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create directories for static and template files
RUN mkdir -p /elastic-app/static
RUN mkdir -p /elastic-app/templates

# Copy the HTML, CSS, and JavaScript files into the container
COPY templates/*.html /elastic-app/templates
COPY static/*.css /elastic-app/static
COPY static/*.js /elastic-app/static
COPY . /elastic-app/

# Expose port 5001 to the outside world
EXPOSE 5001

# Run Python app
CMD ["python3", "main.py"]

