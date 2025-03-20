from termcolor import colored

def main():
    sides = [float(input(colored(f"Enter side {i+1}: ", "red"))) for i in range(3)]
    print(colored(f"The perimeter of the triangle is {sum(sides)}", "yellow"))

main()

# def main():
#     side1 = float(input("Enter the length of side 1: ")) #2 
#     side2 = int(input("Enter the length of side 2: "))
#     side3 = int(input("Enter the length of side 3: "))

#     perimeter = side1 + side2 + side3
#     print(f"The perimeter of the triangle is {perimeter}")
# main()
