/* Lesson of CS50: Introduction to Computer Science, Harvard University course in Brazil

from cs50 import get_string

people = {
    "Brian": "3481-0056",
    "David": "99875-8517"
}

nome = get_string("Nome: ")
if nome in people:
    print(f'Number: {people[nome]}')
