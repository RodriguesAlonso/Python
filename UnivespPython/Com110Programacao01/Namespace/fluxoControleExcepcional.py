##


def safeOpen(arquivo, modo):
    try:
        entrada = open(arquivo, modo, encoding='UTF-8')
        return entrada
    except:
        return 'none'

