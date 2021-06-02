student = {'name': 'Okaru', 'age': 23, 'courses': ['DataStructures, Algoritmia, Hipermedia']}

student['genre'] = 'Male'

print(student)

print(student['name'])

print(student.get('phone', 'Not Found'))

student.update({'name': 'Alvaro'})

print(student)

del student['age']  #or age = student.pop('age')

print(student) 

print('--------------------------------- \n')
print('Metodos de acceso a diccionarios \n')
print('Longitud',len(student))

print('Keys',student.keys())

print('Values',student.values())

print('Items',student.items())

print('--------------------------------- \n')
print("Iteracion de Diccionario")
for key, value in student.items():
    print(key, value)