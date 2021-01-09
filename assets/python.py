import re

print("Python Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def math_calculation():
    global previous
    global run
    equation = ""
    if previous == 0:
        equation = input('Enter equation:')
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    math_calculation()


