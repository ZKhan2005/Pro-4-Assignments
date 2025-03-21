from termcolor import colored

def main():
    while True:
        prompt = input(colored("What's Your Favorite Animal? ", "blue"))
        if prompt.isalpha():
            print(colored(f"My Favorite Animal Is Also {prompt}!", "green"))
            break
        print(colored("Error: Only alphabetic characters are allowed!", "red"))

main()