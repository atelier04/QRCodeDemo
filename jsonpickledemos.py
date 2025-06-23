import json

words = ["Hallo", "Wie"]
json_words = json.dumps(words)
print(f"{json_words=}")
word = "Hi"
json_word = json.dumps(word)
print(f"{json_word=}")
print(json.loads(json_word))
number1 = 1
print(f"{number1=}")
json_number = json.dumps(number1)
print(f"{json_number=}")
print(f"{type(json_number)=}")
print(f"{json.loads(json_words)=}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {"name": self.name, "age": self.age}

    def __str__(self):
        return f"name:{self.name} age:{self.age}"


json_person = json.dumps(Person("Alex", 12).to_dict())
print(f"{json_person=}")
person_alex = json.loads(json_person)
print(f"{type(person_alex)=}")
print(f"{person_alex}")
import pickle

pickle_person2 = pickle.dumps(Person("Max", 6))
print(f"{type(pickle_person2)=}")
person2: Person = pickle.loads(pickle_person2)
print(type(person2))
print(f"{person2.__str__()}")

with open("person.json", "w") as fh:
    json.dump(Person("Markus", 54).to_dict(), fh)

with open("person.json", "r") as fh:
    load_json = json.load(fh)
    print(f"{load_json=}")

with open("personen.json", "w") as fh:
    json.dump([Person("Markus", 54).to_dict(), Person("Max", 7).to_dict()], fh)

with open("person.pickle", "wb") as fh:
    pickle.dump(Person("Hans", 10), fh)

with open("person.pickle", "rb") as fh:
    person_load: Person = pickle.load(fh)
    print(person_load.name)
    print(person_load.age)
import requests

posts = requests.get("https://jsonplaceholder.typicode.com/posts")
print(type(posts))
posts = posts.json()
print(f"{type(posts)=}")
print(f"{posts=}")
res = requests.post("https://jsonplaceholder.typicode.com/posts",
                    data={
                        "userId": 1,
                        "id": 1,
                        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
                    })
print(res.json())
res = requests.get("http://localhost:8000/personen.json")
print(f"{res.json()=}")
result=requests.post("http://localhost:8000/personen.json", data={"name": "Anna", "age": 10})
print(f"{result=}")

res = requests.post("https://jsonplaceholder.typicode.com/todos",
                    {
                        "userId": 10,
                        "id": 1,
                        "title": "hallo 10",
                        "completed": False
                    },
                    )



