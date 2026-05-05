nomes = ["Leo", "Ju", "Caio", "Ana"]

nomes.append("cleber")

for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        for k in range(j + 1, len(nomes)):
            print(f"{nomes[i]} , {nomes[j]} e {nomes[k]} são um trio")