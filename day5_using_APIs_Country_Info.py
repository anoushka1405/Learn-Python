'''
What is an API?

An API (Application Programming Interface) is a mechanism that allows different software applications to communicate with each other.
It enables a program to request data or services from an external system (usually over the internet).

How APIs Work
1. A client (my Python program) sends a request to an API
2. The API processes the request
3. The API returns a response (usually in JSON format)

HTTP Methods:
Method	Purpose
GET - 	Retrieve data
POST - 	Send/Create data
PUT / PATCH	 - Update data
DELETE - Remove data

API Endpoint:
An endpoint is a specific URL used to access data from an API.

Status Codes
Code	Meaning
200	    Success
404	    Not Found
403	    Forbidden
500	    Server Error

APIs usually return data in JSON (JavaScript Object Notation) format.
API responses often contain nested data structures (lists and dictionaries).

Day 5 : 
Fetch and display country information using a public API in Python.
'''

import requests
country = input("Enter Country : ")

response = requests.get(f'https://restcountries.com/v3.1/name/{country}?fullText=true')

if response.status_code != 200:
    print("Country not found")
    exit()

data = response.json()

country_data = data[0]

print("\n--- Country Information ---\n")
print("Common Name : ",country_data["name"]["common"])
print("Capital : ",country_data["capital"][0])
print("Region : ",country_data["region"])
print("Population : ",country_data["population"])
