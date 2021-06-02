#Todo de listas :3

courses = ['history', 'math', 'science','philosofy']
courses_2 = ['literatura', 'robotica']
#se inserta al final
courses.append('Art')

courses.insert(0,'calculus')
#si usamos insert para insertar un alista en otra lista se agrega el objeto lista, no solo los valores
courses.extend(courses_2)

print(courses)

print('-------------------------------------------')
print(courses[0])

print('-------------------------------------------')
print(courses[:2])
print('-------------------------------------------')
#eliminamos el ultimo elemento de la lista
#al usar pop podemos almacenar el valor en una variable
popped = courses.pop()

#remover un valor especifico
courses.remove('science')

#voltea la lista
courses.reverse()

print(courses)

#sort ordena la lista en orden alfabetico
courses.sort()
print('-------------------------------------------')
print(courses)

#sorted no modifica la lista original pero podemos ponerla en una variable
sorted_courses = sorted(courses)
print('-------------------------------------------')
print(sorted_courses)

#buscar el indice de la lista por index

print(courses.index('math'))
print('-------------------------------------------')
num = [1,2,3,4,5]

print(max(num))

print('-------------------------------------------')

#Separar los elementos de la lista por comas
courses_str = ',' .join(courses)

print(courses_str)

print('-------------------------------------------')

new_list = courses_str.split(' - ')

print(new_list)