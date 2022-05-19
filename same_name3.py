def spam():
    global eggs
    eggs = 'spam' #essa variável é global

def bacon():
    eggs = 'bacon' #essa variável é local

def ham():
    print(eggs) #essa variável é global

eggs = 42 #essa variável é global
spam()
print(eggs)