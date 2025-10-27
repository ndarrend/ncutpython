t1 = ('red','green','blue')
print(t1[0])
for color in t1:
    print(color)

t2 = (1,3,5)
t3 = t1 + t2
print(f't3 = {t3}')

t4 = t1 * 2
print(f't4 = {t4}')

person = ('Alice',25,'Engineer')
name,age,job = person
print(f'name = {name}, Age = {age}, Job = {job}')