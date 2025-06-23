import requests

res=requests.get("http://localhost:8000/meinserver.py")
print(f"{res.text=}")
response=requests.post("http://localhost:8000/meinserver.py",data={"name":"Anna","age":10})
print(f"{response.text=}")