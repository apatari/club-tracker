# lib/helpers.py
import os
import sys
from rich.console import Console
console = Console()

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    console.print(" Goodbye! ", style="dark_red on grey84 bold")
    print('')
    
    
    # sys.exit()
    # # os.abort()
    exit()

