#!/usr/bin/env python3

import random

# Jokes taken from https://teachinglondoncomputing.org/computing-crackers/

def main():
    number = input("Pick a number between 1 and 10.\n")
    print("\n")
    if not number.isdigit():
        print("Sorry you get no joke!\n")
        return 0
    else:
        number = int(number)
    match number:
        case 1:
            print("How do robots eat pizza?\n")
            print("One byte at a time.\n")
        case 2:
            print("I have a joke about my work as a software engineer, but it only works for me.\n")
        case 3:
            print("I have a joke about recursion, but I have a joke about recursion, but I have a joke about recursion, but I have a joke about recursion, but I have a joke about recursion, but I have a joke about recursion, but I have a joke about recursion, but I …\n")
        case 4:
            print("What jungle animal has only two states - jumping out and scaring people or not.\n")
            print("A Boo-lion\n")
        case 5:
            print("[“hip”,”hip”]\n")
            print("hip hip array!\n")
        case 6:
            print("An SQL query goes into a bar, walks up to two tables and asks, “Can I join you?”\n")
        case 7:
            print("What do trees do on computers?\n")
            print("They branch out.\n")
        case 8:
            print("Why don't elephants use desktop computers?\n")
            print("They are scared of the mouse.\n")
        case 9:
            print("Why did the monkey fall off the tree?\n")
            print("Its node got deleted.\n")
        case 10:
            print("What's the object-oriented way to become wealthy?\n")
            print("Inheritance.\n")
        case _:
            print("Sorry you get no joke!\n")

        
if __name__ == "__main__":
    main()
