student = {'name':"Alice","age":20,"major":"Computer Science"}
print(student)

Sname = student["name"]; print(Sname)
Age = student["age"]; print(f'age = {Age}')
print(f'major = {student["major"]}')

student["age"] = 21

student["grade"] = "A"; print(student)

del student["age"]; print(f'after remove: =>{student}')