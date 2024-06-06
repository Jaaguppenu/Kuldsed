def sõnastikuks(failinimi):
    sõnastik = {}
    with open(failinimi, 'r', encoding='UTF-8') as file:
        for rida in file:
            maakond, arv = rida.strip().split(',')
            sõnastik[maakond] = int(arv)
    return sõnastik


failinimi = "liiklusõnnetused.txt"
liiklusõnnetused = sõnastikuks(failinimi)
    
kriitiline_arv = int(input("Sisesta kriitiline õnnetuste arv: "))
print("Kriitilised piirkonnad on:")
    
for maakond, arv in liiklusõnnetused.items():
    if arv > kriitiline_arv:
        print(f"{maakond} {arv} juhtumiga.")