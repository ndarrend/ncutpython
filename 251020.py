s1 = "this is my first string in double quotes"
s2 = 'string in single quotes'
long_string = """ASCII stands for American Standard Code
Code fo Information Interchange.
Computers can only understand numbers, so an ASCII code
is the numerical representation of a character such
as "a" or "@" or an action of some sort."""

print('long_string =', long_string)
print(s1)
print(s2)
print("This is \"President\" quoted")
print('This is "President" quoted')
iNum=20
print(f'The iNum is {iNum}')
s = input("please give me an integer:")
print(f'Your number is {s}')
week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(f'weekday:{week[0,5]}')
print(f'weekday:{week[5,7]}')