import requests
url = "https://jsonplaceholder.typicode.com/users"
res = requests.get(url).json()
for data in res:
    print(data["name"])