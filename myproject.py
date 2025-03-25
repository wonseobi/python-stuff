# Project
# Calculates in % my progress for six months in the gym ;D
from time import sleep
progress = 28.22
print("Hello Won, today's date: 20/3/25")
answer = input("Did you assist today? (Y/N) ").upper()

if answer == "Y":
    print("Well done!")
    sleep(1)
    print("Updating progress...")
    sleep(3)
    progress = progress + 0.83
    progress = round(progress, 2)
    print(f"Current progress {progress}%")
    sleep(1)
    print("Remember to add a new pin!")
    sleep(1)
    print("See you tomorrow :)")
elif answer == "N":
    print("Please stay on track")
    sleep(1)
    print("Missing once is a mistake, missing twice is the start of a new habit")
    sleep(3)
    print("See you tomorrow :)")
else:
    print("Unknown input")
