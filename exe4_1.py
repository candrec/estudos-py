def frutas(spam):
    frase = ''
    for i in range(len(spam)):
        frase = frase + str(spam[i]) + ', '
        
    print(type(frase))
    return frase

spam = ['apples','bananas','tofu','cats']
lista_de_frutas = frutas(spam)
print(lista_de_frutas)
