import requests
import argparse
import json

#To access the fake data from jsonplaceholder
r = request.get("https://jsonplaceholder.typicode.com/posts/1")
print(r.json())

#to Post the data in json

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title" :"abc",
    "body" : "abjkfjhfo",
    "userId" : 1
}
response = request.post(url, json = data)

print(response.status_code)
print(response.text)
