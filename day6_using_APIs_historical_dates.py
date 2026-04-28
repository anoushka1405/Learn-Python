'''
Create a Python command-line interface that prompts for a date, fetches historical events 
via a no-key API, parses the JSON response, and prints each event's year, description, and link.
'''
import requests

print("\n Historical Events Finder")
print("----------------------------")

month = input("Enter Month :  ")
day = input("Enter Day : ")

if not month.isdigit() or not day.isdigit():
    print("Please enter valid digits")
    exit()

month = int(month)
day = int(day)

if month<1 or month>12:
    print("Invalid Month!")
    exit()
if day<1 or day>31:
    print("Invalid day!")
    exit()

response = requests.get(f'https://byabbe.se/on-this-day/{month}/{day}/events.json')

if response.status_code != 200:
    print("Failed to fetch data")
    exit()

data = response.json()

required = data['events']

if not required:
    print("No historical events found")
    exit()

for req in required[:5]:
    print('Year : ', req['year'])
    print('Event : ', req['description'])
    
    wiki = req.get("wikipedia", [])

    if wiki:
        print('Read more about it : ', wiki[0].get("wikipedia", "No link"))
    else:
        print('Read more about it : No link')
    print('--------------------------------')