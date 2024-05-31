# Overview: Practice finding elements in a list.

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10",
    "Raphael 2"
]

youngest_people = []
youngest_age = 999

for person in people:
    person = person.strip().split(" ")
    name = person[0]
    age = int(person[1])

    if age < youngest_age:
        youngest_age = age
        youngest_people = [name]  
    elif age == youngest_age:
        youngest_people.append(name)  

print(f"The youngest age is {youngest_age}")

if len(youngest_people) == 1:
    print(f"The person with the youngest age is: {youngest_people[0]}")
else:
    print("The people with the youngest age are:")
    for person in youngest_people:
        print(person)