# Pull python image
FROM python:3.9

# Set working directory to code
WORKDIR /code

# Copy requirement.txt
COPY ./api/app/requirements.txt /code/requirements.txt

# Install required python packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy api code
COPY ./api/app /code/app

# Run Web Server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]