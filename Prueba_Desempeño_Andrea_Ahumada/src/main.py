# Main entry point for inventory system
from validations import getOption
from menu import menu
from services import choose

student_list = []  # In-memory inventory: list of dicts

print("Welcome to the student list")

while True:
    try:
        option = getOption(menu)
        choose(option, student_list)
        if option == 8:
            break
    except KeyboardInterrupt:
        break
