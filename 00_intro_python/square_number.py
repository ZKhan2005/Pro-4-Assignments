from termcolor import colored

def main():
    number = int(input(colored("Enter a number: ", "red")))
    square = number * number
    print(colored(f"The square of {number} is {square}", "yellow"))

main()
