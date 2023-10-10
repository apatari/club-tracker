# lib/helpers.py
from rich.console import Console
from models.club import Club
from models.student import Student
console = Console()

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    console.print(" Goodbye! ", style="dark_red on grey84 bold")
    print('')
    exit()

def add_club():
    name_ = input("Enter the name for the new club: ")
    cap = input("Enter the number of students the club can take: ")
    try: 
        cap = int(cap)
    except:
        print('Capacity must be an integer')
        return
    try:
        Club.create(name_, cap)
    except Exception as exc:
        print("Error creating club: ", exc)


def club_list():
    return Club.get_all()

def view_students():
    pass

