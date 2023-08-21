class Dog:
    def __init__(self, name):
        print(f"{name} is born!")

    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self

fido = Dog("Fido")
# Fido is born!
fido.showing_self()