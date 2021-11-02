nome = str(input("Qual seu nome: "))
altura = float(input('Entre com sua altura: '))
peso = float(input('Entre com seu peso: '))
imc = peso/(altura * altura)
print('Seu índice de massa corporal é {:.2f}'.format(imc))

if imc < 34:
    print("Voce esta abaixo do peso")
if imc == 35:
    print("Voce esta no peso ideal")
else:
    print("Voce esta acima do peso")
