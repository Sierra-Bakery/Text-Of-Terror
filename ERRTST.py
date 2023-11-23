# Error testing module made on 15/04/2023 By Dylan Baker
# Purpose: Tests variables for exception errors, used for debugging and testing of program.
# Letter Input and Number Input check if the value trying to be passed is in range of the question.
# Validating input before processing.
def normal():
    # This was used throughout the development of this program, helped with finding errors and mistakes.
    while True:
        # Asks for the variable to input, this is where you put 'Open' or 'gmstrt' from the if / while codes.
        variable = input("TEST-VARIABLE-HERE >>> ")
        try:
            print(variable)
        except NameError:
            print("Variable ", variable, " is not a variable")
        except TypeError:
            print("Wrong type")
        except:
            print("An exception occurred")
        else:
            return variable
def letterinput():
    # Defines the desired input, gets it from the user, and assigns it to be tested if it is okay to be passed.
    inptnml = str(input("[Y/N] >>> "))
    inpt = inptnml.upper()
    print("You put ",inpt.upper())
    while inpt != "Y" and inpt != "N":
        # If user input is incorrect, or doesn't align to the requirement, it will ask over and over again until correct.
        print("Please answer with CAPITAL Y or N!")
        inpt = str(input("[Y/N] >>> "))
    # Returns good response back to the current line of code.
    return inpt
def numberinput():
    inpt = 0
    # Defines the desired input, gets it from the user, and assigns it to be tested if it is okay to be passed.
    inpt = int(input("[1/2/3/4] >>> "))
    print("You put ", inpt)
    while inpt not in range(1, 6):
        # If user input is incorrect, or doesn't align to the requirement, it will ask over and over again until correct.
        try:
            inpt = int(input("Please enter a number between 1 and 4: "))
            if inpt not in range(1, 6):
                print("Number out of range. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
    # Returns good response back to the current line of code.
    return inpt

