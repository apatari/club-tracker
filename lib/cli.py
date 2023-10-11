# lib/cli.py


from rich import print as rprint
from rich.style import Style
from rich.console import Console
import helpers
console = Console()

from helpers import (
    exit_program,
    helper_1
)

invalid = Style( color='magenta2', bold=True)

def main():
    
    while True:
        menu()
        choice = input("> ")
        if choice == "x":
            exit_program()
        elif choice == "c":
            clubs()
        elif choice == 's':
            students()
        else:
            print("")
            console.print(f"Invalid entry: {choice}", style= invalid, highlight=False)


def menu():
    print('')
    console.print("------[blue]Main Menu[/blue]-----------------", style="dark_sea_green bold")
    print(" ")
    print("Enter c for clubs menu")
    print("Enter s for students menu")
    print("Enter x to exit the program")
    print('')

def students():
    while True:
        student_list = students_menu()
        choice = input('> ')

        if choice == 'x':
            exit_program()
        elif choice == 'b':
            break
        elif choice == 'a':
            print('TODO: create new student and assign them to a club')
        else:
            try:
                picked_student = student_list[int(choice) - 1]
                student_details(picked_student)
            except:
                print("")
                console.print(f"Invalid entry: {choice}", style= invalid, highlight=False)
        

def students_menu():
    list = helpers.student_list()

    print('')
    console.print("------[blue]Students Menu[/blue]-----------------", style="dark_sea_green bold")
    print("")
    print('All Students:')
    for i, student in enumerate(list):
        console.print(i + 1, student.name, style='orange3')
    print('')
    print('Enter any student\'s number for details and additional options')
    print("Enter a to create a new student and assign them to a club")
    print("Enter b to go back to main menu")
    print("Enter x to exit the program")
    print("")
    return list

def student_details(student):
    print('')
    print(f'Student: {student.name}, Club: TODO')
    print('')
    input("Press Enter to continue")



def clubs():
    while True:
        clubs_list = clubs_menu()
        choice = input("> ")
        
        if choice == "x":
            exit_program()
        elif choice == 'b': 
            break
        elif choice == 'a':
            helpers.add_club()
        else:
            try:
                picked_club = clubs_list[int(choice) - 1]
                club_details(picked_club)
            except:
                print("")
                console.print(f"Invalid entry: {choice}", style= invalid, highlight=False)

            

def clubs_menu():

    list = helpers.club_list()

    print('')
    console.print("------[blue]Clubs Menu[/blue]-----------------", style="dark_sea_green bold")
    print("")
    print('All Clubs:')
    for i, club in enumerate(list):
        console.print(i + 1, club.name, style='light_steel_blue')
    print('')
    print('Enter any club\'s number for details and additional options')
    print("Enter a to add a new club")
    print("Enter b to go back to main menu")
    print("Enter x to exit the program")
    print("")
    return list

def club_details(club):

    while True:
        club_details_menu(club)
        choice = input("> ")
        if choice == 's':
            helpers.view_students(club)
        elif choice == 'n':
            helpers.add_student(club)
        elif choice == 'r':
            helpers.remove_student(club)
        elif choice == 'u':
            helpers.update_club(club)
        elif choice == 'd':
            next = helpers.delete_club(club) 
            if next == 1:
                break
        elif choice == 'b':
            break
        else:
            print('')
            console.print(f"Invalid entry: {choice}", style= invalid, highlight=False)
        
def club_details_menu(club):
    print('')
    console.print("------[blue]Club Details[/blue]-----------------", style="dark_sea_green bold")
    print('')
    print('Club Name: ', club.name)
    print('Current enrollment: ', club.student_count())
    print('Maximum capacity:   ', club.capacity)
    # TODO more details, such as students and limit
    print('')
    
    print('Enter s to view all students in this club')
    print('Enter n to add a new student')
    print('Enter r to remove a student')
    print('Enter u to update this club\'s name and capacity')
    print('Enter d to delete this club and its students')
    print('')
    print("Enter b to go back to clubs menu")
    

if __name__ == "__main__":
    print("")
    console.print(" Welcome to the Club Tracker! ", style = "dark_green on white bold")
    print("")
    main()

