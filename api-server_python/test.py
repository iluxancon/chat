import requests

print (requests.post("http://127.0.0.1:5000/chat", data={"username": "illia"}).text)
print (requests.get("http://127.0.0.1:5000/chat").text)
print (requests.post("http://127.0.0.1:5000/chat", data={"username": "illia", "message": "Hi"}).text)
print (requests.get("http://127.0.0.1:5000/chat").text)

