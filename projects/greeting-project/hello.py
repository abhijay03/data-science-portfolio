# My first Python project in GitHub
from datetime import datetime

def greet_user():
    name = input("Enter your name: ")
    hour = datetime.now().hour
    
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    
    print(f"{greeting}, {name}! Welcome to Data Science.")


def greet_user():
    name = input("Enter your name: ")
    major = input("What's your major? ")
    year = input("What year are you in? ")
    
    print("Hello, {name}! ")
    print("It's great to meet a {year}-year {major} major. ")
    print("Welcome to Data Science.")
