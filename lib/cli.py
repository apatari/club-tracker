# lib/cli.py


from rich import print as rprint
from rich.style import Style
from rich.console import Console
console = Console()

from helpers import (
    exit_program,
    helper_1
)

invalid = Style( color='magenta2', bold=True )

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
            console.print("Invalid entry", style= invalid)


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
        clubs_menu()
        choice = input("> ")
        if choice == "x":
            exit_program()
        elif choice == "m":
            main()
        else:
            print("")
            console.print("Invalid entry", style= invalid)

def clubs_menu():
    print('')
    console.print("------[purple]Clubs Menu[/purple]-----------------", style="dark_sea_green bold")
    print("")
    print("Enter m to return to main menu")
    print("Enter x to exit the program")
    print("")

if __name__ == "__main__":
    print("")
    console.print("Welcome to the Club Tracker!", style = "dark_orange on white bold")
    print("")
    main()

