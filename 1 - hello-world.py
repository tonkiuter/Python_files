#shift + alt down arrow to duplicate a line

my_message = 'Hello Python'

print(my_message)

print(my_message[:5])

print(my_message[6:])

#tamanio de la variable
print(len(my_message))

#minusculas
print(my_message.lower())

#mayusculas
print(my_message.upper())

#cuenta el numero de letras de acuerdo al parametro dado.
print(my_message.count('l'))

#busca en que index se encuentra la cadena dada.
print(my_message.find('thon'))

#reemplaza una cadena por otra
new_message = my_message.replace('Python', 'Anaconda')

print(new_message)

name = 'Okaru'

greeting = 'Hello'

#concatenar variables sin ningun metodo
message = greeting + ', ' + name

#Formato con metodo
message = '{}, {} . Welcome!'.format(greeting, name)

print(message)

print(dir(name))
