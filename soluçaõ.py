def resolve_2grau(a,b,c):
    delta = b**2 - 4*a*c
    frase =""
    if delta<0:
        frase += f"Não há raizes pois delta = {delta}"
    elif delta == 0:
        x = -b/(2*a)
        frase += f"ambas as raizes são iguais a {x}"
    else:
        x1 = (-b+delta**0.5)/(2*a)
        x2 = (-b-delta**0.5)/(2*a)
        frase += f"a primeira raiz vale {x1} e a segunda {x2}"
    xv =  -b/(2*a)
    yv = -delta/(4*a)
    frase += f"e o vertice está em xv={xv} e yv={yv}"
    return frase

a = 1
b=5
c=6


resultado = resolve_2grau(a,b,c)
print(resultado)

