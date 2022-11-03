def transforma_base (entrada): 
    saida = {}
    for item in entrada:
        nivel = item['nivel']
        if nivel not in saida:
            saida[nivel] = []
        saida[nivel].append(item)
    return saida
