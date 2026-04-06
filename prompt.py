import requests

url = "http://127.0.0.1:8000/generate"

prmpt = input("Enter a prompt: ")
role = input("Enter a role: ")

messages = [
    {"role": role
     ,"content" : prmpt},
]

res = requests.post(url, json={"messages": messages})
print(res.json())