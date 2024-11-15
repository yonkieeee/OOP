import requests

res = requests.delete("http://127.0.0.1:5000/api/main/courses/2")
print(res.json())