#Calculadora equação de segundo grau

import math


a=float(input("Digite o valor de a: "))



if a==0:
    print('Se a=0 então não é equação.')
else:
    b=float(input("Digite o valor de b: "))
    c=float(input("Digite o valor de c: "))
    delta= b*b - (4*a*c)

    if delta < 0:
        print("Delta é menor que 0! Bye Bye")
    
    elif delta == 0:
        raiz = -b / (2*a)
        print ("Delta = 0, raiz = %.2f" % raiz)
    else:
        raiz1=((-b + math.sqrt(delta)) / (2*a))
        raiz2=((-b - math.sqrt(delta)) / (2*a))
        print(' Resultado:',"\n Delta Positivo: %.0f"% raiz1, "\n Delta negativo %.0f" % raiz2)




