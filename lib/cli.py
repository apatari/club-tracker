# lib/cli.py


from rich import print as rprint
from rich.style import Style
from rich.console import Console
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


def clubs():
    while True:
        clubs_list = clubs_menu()
        choice = input("> ")
        #TODO: add the option to create or delete clubs
        if choice == "x":
            exit_program()
        elif choice == 'b': 
            break
        else:
            try:
                picked_club = clubs_list[int(choice) - 1]
                club_details(picked_club)
            except:
                print("")
                console.print(f"Invalid entry: {choice}", style= invalid, highlight=False)

            

def clubs_menu():

    # TODO: this is a fake list for initial debugging, add real helper later
    list = [{'id': 1, 'name':'Skiing'}, {'id':2, 'name': 'Chess'}]

    print('')
    console.print("------[blue]Clubs Menu[/blue]-----------------", style="dark_sea_green bold")
    print("")
    print('All Clubs:')
    for i, club in enumerate(list):
        console.print(i + 1, club['name'], style='light_steel_blue')
    print('')
    print('Enter a club\'s number for details and additional options')
    print("Enter b to go back to main menu")
    print("Enter x to exit th program")
    print("")
    return list

def club_details(club):

    while True:
        club_details_menu(club)
        choice = input("> ")
        if choice == 'a':
            print('TODO: add student')
        elif choice == 'r':
            print('TODO: remove student')
        elif choice == 'b':
            break
        else:
            print('')
            console.print(f"Invalid entry: {choice}", style= invalid, highlight=False)
        
def club_details_menu(club):
    print('')
    console.print("------[blue]Club Details[/blue]-----------------", style="dark_sea_green bold")
    print('')
    print('Club Name: ', club['name'])
    # TODO more details, such as students and limit
    print('')
    print('Enter a to add a student')
    print('Enter r to remove a student')
    print('')
    print("Enter b to go back to clubs menu")
    

if __name__ == "__main__":
    print("")
    console.print(" Welcome to the Club Tracker! ", style = "dark_green on white bold")
    print("")
    main()

