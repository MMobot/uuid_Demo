name = input('your name:')
gender = input('your are a boy?(y/n)')

welcome_str = 'Welcome to the matrix {prefix} {name}'
welcome_dic = {
    'prefix': 'Mr.' if gender == 'y' else 'Mrs',
    'name': name
}

print('authorizing...')
print(welcome_str.format(**welcome_dic))