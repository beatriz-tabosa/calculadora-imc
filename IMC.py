# IMC simplificado

nome = ''
altura = 0.
peso = 0
imc = 0.

def ler_dados():
    global nome
    global altura
    global peso



    while True:
        try:
            nome = str(input ('Digite seu primeiro nome: '))
            if (not nome.isalpha()):
                print('Seu nome apenas com letras <3')
                continue
        except ValueError:
            print ('Seu nome apenas com letras <3')
            continue
        break

    while True:
        try:
            altura = float(input('Digite sua altura: '))
            if altura <= 0:
                print ('Sua altura não pode ser menor ou igual a 0')
                continue
        except ValueError:
            print ('Sua altura em metros. Se não funcionou tente com um ponto ao em vez de vírgula <3')
            continue
        break

    while True:
        try:
            peso = float(input('Digite seu peso: '))
            if peso <= 0:
                print ('Seu peso não pode ser menor ou igual a 0')
                continue
        except ValueError:
            print ('Seu peso em kilogramas. Se não funcionou tente com um ponto ao em vez de vírgula <3')
            continue
        break
            

def calcula_imc():
    global peso
    global altura

    imc = peso / pow(altura, 2)
    return round(imc, 2)

def avalia_imc():
    imc = calcula_imc()
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc >= 18.5 and imc < 25:
        return 'Peso normal'
    else:
        return 'Sobrepeso'
        
ler_dados()
imc = calcula_imc()
msg = avalia_imc()
nome = nome.capitalize()
print(f'\n {nome} seu resultado é: \n \n IMC = {imc} \n Status = {msg} \n')