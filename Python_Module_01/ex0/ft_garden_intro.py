#!/usr/bin/env python3

def ft_garden_intro():
    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age}days \n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()

# '#!' → means “use the following interpreter”
# /usr/bin/env python3 → tells the system to run the script using Python 3
# So instead of doing:
# python3 script.py
# You can do:
# ./script.py
# the OS already knows to use Python.

# what is: if __name__ == "__main__":  ???
# It stops your code from running when the file is imported.
# eg: file: main.py -> import (filename)
# You DIDN’T call anything yet in main.py
# but it still prints the functions output in (filename) straight away
# Because Python runs the whole file when you import it
# so use: if __name__ == "__main__":
# to run the imported function only when the main file is executed.
