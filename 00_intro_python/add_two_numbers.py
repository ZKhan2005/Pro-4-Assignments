import os
import termcolor

os.system("pip install termcolor")

def main():
    try:
        num1, num2 = int(input(termcolor.colored("Enter 1st No#: ", "light_blue"))), int(input(termcolor.colored("Enter 2nd No#: ", "light_green")))
        print(termcolor.colored(f"{num1} + {num2} = {num1 + num2}", "yellow"))
    except ValueError:
        print(termcolor.colored("Invalid Input! Please Enter Numeric Digits Only", "red"))

main()
