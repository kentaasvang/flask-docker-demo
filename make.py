from os import system

def build():
    system("docker build -t flask-app .")

def run():
    system("docker run -p 5000:5000 flask-app")
