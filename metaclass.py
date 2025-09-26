class AutoStr(type):

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)

        def __str__(self):
            attributes = {k: v for k, v in self.__dict__.items() if not k.startswith('__')}
            return f"{self.__class__.__name__} {attributes}"

        new_class.__str__ = __str__

        return new_class
if __name__ == "__main__":
    class Person(metaclass=AutoStr):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    print(Person("Alex", 20))