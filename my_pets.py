my_pets = ['zophie','pooka','fat-tail']
name = input('Enter a pet name: ')
if name not in my_pets:
    print(f'I do not have a pet named {name}!')
else:
    print(f'{name} is my pet.')