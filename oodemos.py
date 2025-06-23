class Person:
    number_instances: int = 0

    def __getattribute__(self, item):
        print(f"{item=}")
        """
         if item == "income":
            raise AttributeError("income not allowed")
        """

        return object.__getattribute__(self, item)

    """
            def __getattr__(self, item):
                print(f"{item=} not exists")
                return item
    """

    def __init__(self, name, age, sleepy):
        self.name: str = name
        self.age: int = age
        self.__sleepy: bool = sleepy
        Person.number_instances += 1


p1: Person = Person("Hans", 42, True)
p2: Person = Person("Max", 7, True)

print(f"{Person.number_instances=}")

print(f"{p1.name}")
Person.name = "Hans"
print(f"{Person.name=}")
print(f"{p1.name=}")
print(f"{p1.__dir__()}")
print(f"{Person.__dir__(Person)}")
# print(f"{p1.income=}")
print(f"{p1.__dict__}")
print(f"{Person.__dict__}")
print(f"{p1._Person__sleepy}")
print(f"{hash(p1)}")
from dataclasses import dataclass


@dataclass(unsafe_hash=True,eq=True,repr=True,init=True)
class Address:
    street: str
    city: str


address1: Address = Address(street="", city="")
print(f"{hash(address1)}")
address1.city="Vienna"
print(f"{hash(address1)}")
address2:Address=Address("linzerstreet","vienna")
print(f"{address2.city=}")
