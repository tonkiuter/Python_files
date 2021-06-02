#Tuplas
#Tuplas no se pueden modificar (Inmutable)

from typing import Tuple


tuple_1 = ('History', 'Math', 'Physics', 'Science')
tuple_2 = tuple_1

print (tuple_1)
print (tuple_2)

#las tuplas no se pueden modificar
#tuple_1[0] = 'Art'

#Sets
#Sets dont care about order
#There are not duplicates
set_courses = {'History', 'Math', 'Physics', 'Science'}
set_2_courses = {'History', 'Math', 'Art', 'Design'}

#Intersection podemos comparar los dos sets y ver que elemntos tienen en comun
print("Cursos que contienen los 2 sets:")
print(set_courses.intersection(set_2_courses))

#difference podemos ver que es lo que tienen de diferente
print("Cursos diferentes respecto primer set:")
print(set_courses.difference(set_2_courses))

#fusion de los 2 sets (union)
print("Fusion de los 2 sets:")
print(set_courses.union(set_2_courses))


#Empty Lists
empty_list = []
empty_list = list()

#Empty tuple
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets
empty_set = set()