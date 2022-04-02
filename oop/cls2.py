from locale import format_string


some_string='Hello world'
print('testing a string')
print('_'* 20)
print('some string',some_string)
print("some_string.startswith('H')",some_string.startswith('H'))
print("some_string.startswith('h')",some_string.startswith('h'))
print("some_string.endswith('d')",some_string.endswith('d'))
print("some_string.istitle()",some_string.istitle())
print("some_string.isupper()",some_string.isupper())
print("some_string.islower()",some_string.islower())
print("some_string.isalpha()",some_string.isalpha())

print('String conversion')
print('_'* 20)
print('some_string.upper()',some_string.upper())
print('some_string.lower()',some_string.lower())
print('some_string.title()',some_string.title)
print('some_string.swapcase()',some_string.swapcase())
print('start leading, trailing',"xyz".strip())

# 2
# print(format_string='Hello {}')
# print(format_string.format('Phoebe'))
# 3

name="Adam"
age=20
print("{} is years old".format(name,age))

# 4
format_string="{artist} sang {song} in {year}"
print(format_string.format(artist='Palona Faith',song='Guilty',year='2017'))


# 5
print('|{:<25}|'.format('left aligned'))
print('|{:^25}|'.format('Centerd'))
print('|{:>25}|'.format('right aligned'))

# 6
print('{:,}'.format(1234567890))
print('{:,}'.format(1234567890.0))