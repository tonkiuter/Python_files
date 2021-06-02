lista = [1, 2, 3, 4, 5]

for num in lista:
    if num == 3:
        print('Found!!!')
        continue  #Aplica la condicional, y va para arriba del for
    print(num)


for num in lista:
    for letter in 'abc':
        print(num, letter)
print('-----------------------------')
#conteo 1 - 10 inicializando el contador
for i in range(1, 11):
    print(i)

print('----------------------------')
x = 0 

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

while True:
    print(x+2)
    x +=1
    if x > 5:
        break
