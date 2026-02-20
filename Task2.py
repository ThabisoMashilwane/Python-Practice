#Task 2 - Safe Casting
age = input("Please enter your age: ")

try:
    if type(int(age)) == int:
        if int(age) < 0 or int(age) > 120:
            print("Age out of range!")
        else:
            print("Next year you will be age "+ str(age + 1))
except ValueError:
    try:
        print("Please enter a digit!")
        age = int(input("Please enter your age: "))
        print("Next year you will be age "+ str(age + 1))
    except ValueError:
        print("GoodBye!")
    
