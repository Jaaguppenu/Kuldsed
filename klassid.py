def loe_failist_jarjend(failinimi):
    with open(failinimi, 'r', encoding='UTF-8') as file:
        jarjend = [rida.strip().split() for rida in file.readlines()]
    return jarjend

def leia_õpilane(jarjend, nimi):
    for i, rida in enumerate(jarjend):
        if nimi in rida:
            return (i, rida.index(nimi))
    return None


jarjend = loe_failist_jarjend('klass.txt')
print(jarjend)
print(leia_õpilane(jarjend, 'Jaak'))
