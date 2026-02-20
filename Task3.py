input_ = input("Please enter your age: ")

try:
    age = int(input_)
    if age > 0 and age < 105:
        if age < 18:
            print("You qualify for the youthn plan.")
        elif age >= 18 and age < 60:
            print("You qualify for the standard plan.")
        else:
            print("You qualify for a senior plan.")
    else:
        print("Figure entered is invalid")
except ValueError:
    print("You did not enter a digit, Goodbye!")