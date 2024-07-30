students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

def list_comp():
#creates a list of student names if the house is gryffindor using List Comprehension
    gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]

    for gryffindor in sorted(gryffindors):
        print(gryffindor)

#returns student key-value pair if house is gryffindor
def is_gryffindor(s):
    return s["house"] == "Gryffindor"

def main():
    #filter() returns result of function if true
    #map() returns the result of the function, not subject to boolean
    gryffindors1 = filter(is_gryffindor, students)
    for gryffindor in sorted(gryffindors1, key=lambda s: s["name"]):
        print(gryffindor["name"])

if __name__ == "__main__":
    main()
