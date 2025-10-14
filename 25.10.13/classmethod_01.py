class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def how_many(cls):
        return cls.count
    
p1 = Person("alcls")
p2 = Person("tlqkf")
p3 = Person("qudtls")

print(Person.how_many())
print(Person.count)
