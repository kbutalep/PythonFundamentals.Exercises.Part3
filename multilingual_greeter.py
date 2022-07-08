
language = input("Please choose your language: English, French, Spanish")

def greet(language):
    if (language == "English"):
            name = input("What is your name? ")
            print("Hello " + name)
    elif(language == "French"):
            name = input("Quel est ton nom? ")
            print("Bonjour " + name)
    elif(language == "Spanish"):
            name = input("¿Cuál es su nombre? ")
            print("Hola " + name)

greet(language)

