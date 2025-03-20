from termcolor import colored

def main():
    fahrenheit = int(input(colored("Enter temperature in Fahrenheit: ", "blue")))
    celsius = (fahrenheit - 32) * 5.0 / 9.0 
    print(colored(f"Temperature {fahrenheit}F = {celsius:.2f}C", "green"))

main()
