'''
Goal
Take all files in a folder and rename them like:
photo.jpg → 2026-04-13_photo.jpg
notes.txt → 2026-04-13_notes.txt

This project has only 3 ideas:

1. Get files from folder
→ list everything inside a directory

2. Get today’s date
→ format like YYYY-MM-DD

3. Rename files
→ old name → new name
'''

import os
from datetime import date

today = date.today().strftime("%Y-%m-%d")

files = os.listdir(".")

for file in files:
    if not os.path.isfile(file):
        continue
    
    if file == "day1_add_date_to_filenames.py":
        continue
    
    new_name = f"{today}_{file}"
    os.rename(file,new_name)

    print(f"Renamed: {file}->{new_name}")


