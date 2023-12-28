import os
import subprocess
from datetime import datetime, timedelta

class Animal:
    def __init__(self, name, command, birth_date):
        self.name = name
        self.command = command
        self.birth_date = birth_date

class PetRegistry:
    def __init__(self):
        self.animals = []
        self.counter = 0

    def add_animal(self, name, command, birth_date):
        new_animal = Animal(name, command, birth_date)
        self.animals.append(new_animal)
        self.counter += 1

    def show_animals(self):
        for animal in self.animals:
            print(f"Name: {animal.name}, Command: {animal.command}, Birth Date: {animal.birth_date}")

    def teach_animal(self, name, new_command):
        for animal in self.animals:
            if animal.name == name:
                animal.command = new_command
                print(f"{name} has learned a new command: {new_command}")
                break
        else:
            print(f"Animal with name {name} not found.")

    def menu(self):
        while True:
            print("\nPet Registry Menu:")
            print("1. Add new animal")
            print("2. Show animals")
            print("3. Teach an animal a new command")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                name = input("Enter the name of the animal: ")
                command = input("Enter the command of the animal: ")
                birth_date = input("Enter the birth date of the animal (YYYY-MM-DD): ")
                self.add_animal(name, command, birth_date)
            elif choice == "2":
                self.show_animals()
            elif choice == "3":
                name = input("Enter the name of the animal you want to teach a new command: ")
                new_command = input("Enter the new command: ")
                self.teach_animal(name, new_command)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

class Counter:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.value > 0:
            raise Exception("Resource leak: Counter was not properly closed.")
            
# Пример использования

def main():
    # Создаем реестр животных
    registry = PetRegistry()

    # Создаем счетчик для отслеживания "Завести новое животное"
    with Counter() as counter:
        registry.menu()

if __name__ == "__main__":
    main()
