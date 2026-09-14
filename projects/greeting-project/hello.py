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

if __name__ == "__main__":
    greet_user()
