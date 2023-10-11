# lib/helpers.py
from rich.console import Console
from rich.style import Style
from models.club import Club
from models.student import Student
console = Console()
invalid = Style( color='magenta2', bold=True)

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

def student_list():
    return Student.get_all()

def view_students(club):
    list = club.students()
    print('')
    if list:
        print(f'Students in {club.name}:')
        for i, student in enumerate(list):
            console.print(i + 1, student.name, style='orange3')
    else:
        console.print(f'No students are enrolled in {club.name}', style='orange3')
    print('')
    input('Press Enter to return to Club Details')

def add_student(club):
    print('')
    name = input("Enter the student's name: ")
    try:
        Student.create(name, club.id)
        print('')
        console.print('Student created successfully', style = 'green3')
    except Exception as exc:
        print('')
        console.print("Error creating student: ", exc, style=invalid)

def remove_student(club):
    list = club.students()
    print('')
    if list:
        print(f'Students in {club.name}:')
        for i, student in enumerate(list):
            console.print(i + 1, student.name, style='orange3')
            
        print('')
        choice = input("Enter the number for the student to delete: ")

        try:
                picked_student = list[int(choice) - 1]
                print('')
                console.print(f"Delete {picked_student.name}? Enter y to confirm, anything else to cancel")
                confirmation = input("> ")
                if confirmation == 'y':
                    picked_student.delete()
                    print('')
                    console.print(f'{picked_student.name} was deleted', style = 'green3')
                else:
                    print('')
                    console.print('Action canceled', style='yellow')
        except:
            print("")
            console.print(f"Invalid entry: {choice}", style= invalid, highlight=False)
    else:
        console.print(f'No students are enrolled in {club.name}', style='orange3')

def update_club(club):
    print('')
    tmp = club.name
    try:
        name = input('Enter the name for the updated club: ')
        club.name = name
        capacity = int(input('Enter the capacity for the updated club: '))
        club.capacity = capacity
        club.update()
        print('')
        console.print('Update successful', style = 'green3')
    except Exception as exc:
        club.name = tmp
        console.print("Error updating club: must enter a valid name and number", style=invalid)

def delete_club(club):
    print('')
    console.print(f'Delete {club.name} and all its students? Enter y to confirm, anything else to cancel')
    confirm = input("> ")
    if confirm != 'y':
        print('')
        console.print('Action canceled', style='yellow')
        return 0
    else:
        for student in club.students():
            student.delete()
        club.delete()
        print('')
        console.print('Club and students deleted', style='green3')
        return 1
    
def create_student():
    print('')
    name = input("Enter student name: ")
    print('')

    club_list = [club for club in Club.get_all() if club.student_count() < club.capacity]

    print('Clubs with room for another student:')
    for i, club in enumerate(club_list):
        console.print(i + 1, club.name, style='light_steel_blue')
    
    choice = input('Enter the number of the club for the new student: ')

    try:
        picked_club = club_list[int(choice) - 1]
        Student.create(name, picked_club.id)
        print('')
        console.print("Student created", style='green')
    except:
        print("")
        console.print(f"Error creating student: must enter a valid name and number", style= invalid, highlight=False)



def find_student(name):
    return Student.find_by_name(name)

def club_name_from_id(id):
    return Club.find_by_id(id).name

def update_student(student):
    print('')
    tmp = student.name
    try:
        name_ = input("Enter student name: ")
        student.name = name_
        print('')

        try:
            club_list = [club for club in Club.get_all() if club.student_count() < club.capacity]

            print('Clubs with room for another student:')
            for i, club in enumerate(club_list):
                console.print(i + 1, club.name, style='light_steel_blue')
            
            choice = input('Enter the number of the club for the new student: ')

            picked_club = club_list[int(choice) - 1]
            student.club_id = picked_club.id
            student.update()
            print('')
            console.print("Student updated", style='green')
        except:
            print('')
            console.print(f"Error updating student: must enter valid club number", style= invalid)
            student.name = tmp


    except Exception as exc:
        print("")
        console.print(f"Error updating student: ", exc, style= invalid, highlight=False)

    
def delete_student(student):
    print('')
    console.print(f'Delete {student.name}? Enter y to confirm, anything else to cancel')
    confirm = input("> ")
    if confirm != 'y':
        print('')
        console.print('Action canceled', style='yellow')
        return 0
    else:
        student.delete()
        print('')
        console.print('Student deleted', style='green3')
        return 1
    
