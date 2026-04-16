'''
To Build a command-line diary that lets users write and view daily entries using Python.
'''
from datetime import date

n = int(input("Enter 1 for Writing a new entry\nEnter 2 for viewing old entries\n"))

if(n==1):
    file = open("diary.txt", "a")
    today = date.today().strftime("%Y-%m-%d")

    entry = input("Enter Entry : ")
    file.write(str(today)+ " : "+ entry + "\n")
    file.close()

elif(n==2):
    try:
        file = open("diary.txt", "r")
        content = file.read()
        print("\n--- Your Diary Entries ---\n")
        print(content)
        file.close()
    except FileNotFoundError:
        print("No entries found yet")

else:
    print("Invalid Choice")