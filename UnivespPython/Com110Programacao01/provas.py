##
def vogal(string):
    vogais = []
    string.lower()
    for i in string:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vogais.append(i)
    print("Vogais: ", vogais)


vogal('univesp')
