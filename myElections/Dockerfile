FROM python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# create a working directory
WORKDIR /app

# copies whole folder into app
COPY . /app 

# Copy requirements.txt to the container
COPY requirements.txt .

# sets up the environment to run app
RUN pip install -r requirements.txt

# Copy the rest of the app's code to the container
COPY . .

# execute py files in order
# After starting container, use this port to run the server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["python", "manage.py", "runserver"]

# runserver runs locally on http://127.0.0.1:8000/

# Specify port for docker to use
EXPOSE 8000