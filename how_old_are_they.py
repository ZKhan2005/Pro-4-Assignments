from termcolor import colored

def main():
    zara = 21
    saba = zara + 6
    hania = saba + 20

    print(colored(f"Zara is {zara} years old", "blue"))
    print(colored(f"Saba is {saba} years old", "green"))
    print(colored(f"Hania is {hania} years old", "yellow"))

main()