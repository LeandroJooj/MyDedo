def shaper(x):
    lista = []
    for i in range(1,(x)):
        
        if x%i == 0:
            lista.append(i)
    return round(lista[1])

