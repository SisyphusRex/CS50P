students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}


#enumerate shows the index value of object in iterable
for i, student in enumerate(sorted(students), start=1):
    print (i, student)
