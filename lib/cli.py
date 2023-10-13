# lib/cli.py

from rich.style import Style
from rich.console import Console
import helpers
console = Console()


invalid = Style( color='magenta2', bold=True)

def main():
    
    while True:
        menu()
        choice = input("> ")
        if choice == "x":
            helpers.exit_program()
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
        students_menu()
        choice = input('> ')

        if choice == 'x':
            helpers.exit_program()
        elif choice == 'b':
            break
        elif choice == 'a':
            helpers.create_student()
        elif choice == 'v':
            all_students()
        elif choice == 'f':
            find_student()
        else:
            print("")
            console.print(f"Invalid entry: {choice}", style= invalid, highlight=False)
        

def students_menu():
    
    print('')
    console.print("------[blue]Students Menu[/blue]-----------------", style="dark_sea_green bold")
    print("")
    print('Enter v to view all students')
    print('Enter f to find a student by name')
    print("Enter a to add a new student and assign them to a club")
    print("Enter b to go back to main menu")
    print("Enter x to exit the program")
    print("")

def student_details(student):
    while True:
        student_details_menu(student)
        choice = input("> ")

        if choice == 'b':
            break
        elif choice == 'u':
            helpers.update_student(student)
        elif choice == 'd':
            next = helpers.delete_student(student) 
            if next == 1:
                break
        else:
            print("")
            console.print(f"Invalid entry: {choice}", style= invalid, highlight=False)

def student_details_menu(student):
    print('')
    console.print(f'Student: {student.name}, Club: {helpers.club_name_from_id(student.club_id)}', style='orange3')
    print('')
    print("Press u to update this student's name and/or club")
    print("Press d to delete this student")
    print("Press b to go back to previous menu")
    

def all_students():
    while True:
        student_list = all_students_menu()
        choice = input("> ")

        if choice == 'x':
            helpers.exit_program()
        elif choice == 'b':
            break
        elif choice == 'a':
            helpers.create_student()
        else:
            try:
                picked_student = student_list[int(choice) - 1]
                student_details(picked_student)
            except:
                print("")
                console.print(f"Invalid entry: {choice}", style= invalid, highlight=False)
        
def find_student():
    print('')
    name = input('Enter name of student (case sensitive): ')
    student = helpers.find_student(name)
    if student:
        student_details(student)
    else:
        print('')
        console.print(f"No student with name {name} in database", style= invalid, highlight=False)

def all_students_menu():
    
    list = helpers.student_list()
    print('')
    console.print("------[blue]All Students[/blue]-----------------", style="dark_sea_green bold")
    print("")
    for i, student in enumerate(list):
        console.print(i + 1, student.name, style='orange3')
    print('')
    print('Enter any student\'s number for details and additional options')
    print("Enter a to add a new student and assign them to a club")
    print("Enter b to go back to students menu")
    print("Enter x to exit the program")
    print("")
    return list

def clubs():
    while True:
        clubs_list = clubs_menu()
        choice = input("> ")
        
        if choice == "x":
            helpers.exit_program()
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

