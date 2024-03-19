# Elections-Site

## Description: 
This project is a web-app which allows the user to vote for their party in the local and national elections.

## How to install:
1. Download the entire folder
2. Open your terminal and navigate to the folder
3. Create a virtual env: python -m venv venv
4. Activate the virtual env: venv\Scripts\activate
5. Run 'pip install -r requirements.txt'

## How to run:
1. Open your terminal and direct to the project folder
2. Pull the docker image: docker pull moranderee/final-elections
3. Redirect to folder with Dockerfile
4. Run the image: docker run -p 8000:8000 moranderee/final-elections

After running the server to access the application, go to http://127.0.0.1:8000/ 
Use same link when running docker containers.

Authors and version history:
Muhammad Randeree - March 2024
