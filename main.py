from math import sqrt, sin
c = 0 
l = []
sides = int(input("Quantos lados tem sua figura: "))


if sides == 3:
    while c < 3:
        x = float(input("Insira as medidas dos lados do triangulo: "))
        l.append(x)
        c += 1
    p = sum(l)/2
    a= l[0]
    b = l[1]
    c = l[2]
    heron = sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"A area do triangulo é {heron:.2f} metros quadrados")


if sides == 4:
    print("Sua figura é um quadrilatero. Selecione abaixo qual o tipo:")
    tipo = int(input('''
                        [ 1 ] - Quadrado
                        [ 2 ] - Retangulo
                        [ 3 ] - Paralelogramo
                        [ 4 ] - Losango
'''))
    
    if tipo == 1:
        x = float(input("Insira as medidas dos lados do quadrilatero: "))
        print(f"A area do quadrado é {x**2:.2f} metros quadrados")
    
    if tipo == 2:
        l1 = float(input("Insira o valor da base: "))
        l2 = float(input("Insira o valor da altura: "))
        area = l1 * l2
        print(f"A area do retangulo é {area:.2f} metros quadrados")

    if tipo == 3:
        l1 = float(input("Insira o valor do par de lados horizontais: "))
        l2 = float(input("Insira o valor do par de lados verticais: "))
        angulo = int(input("Qual o valor do angulo entre os lados "))
        altura = l2 * sin(angulo)
        area = l1 * altura
        if area < 0: area = area * (-1)
        print(f"A area do paralelogramo é {area:.2f} metros quadrados")

    if tipo == 4:
        l1 = float(input("Insira o valor dos lados "))
        angulo = int(input("Qual o valor do angulo entre os lados "))
        area = (l1 ** 2) * sin(angulo)
        if area < 0: area = area * (-1)
        print(f"A area do losango é {area:.2f}")

    