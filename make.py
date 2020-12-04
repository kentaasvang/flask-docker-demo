from os import system


def build():
    system("docker-compose build")


def run():
    system("docker-compose up --build")
