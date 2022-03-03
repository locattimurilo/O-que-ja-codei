horas_mes=float(input("Digite quantas horas trabalha por mês: "))
valor_hora=float(input("Digite aqui quanto recebe por hora: "))
sal=(horas_mes * valor_hora)


if sal <= 900:
    INSS=(sal*0.10)
    FGTS=(sal*0.11)
    sf= (sal-INSS)
    print("Seu salário bruto é: %.2f" % sal)
    print("(-) IR: ISENTO")
    print("(-) INSS: %.2f" % INSS)
    print("    FGTS: %.2f" % FGTS)
    print(" Total de descontos: %.2f" % INSS)
    print("Salário líquido: %.2f" % sf)



elif sal <= 1500:
    IR=(sal*0.05)
    INSS=(sal*0.10)
    FGTS=(sal*0.11)
    sf= (sal-INSS-IR)
    print("Seu salário bruto é: %.2f" % sal)
    print("(-) IR: %.2f" % IR)
    print("(-) INSS: %.2f" % INSS)
    print("    FGTS: %.2f" % FGTS)
    print(" Total de descontos: %.2f" % (INSS+IR))
    print("Salário líquido: %.2f" % sf)

elif sal <= 2500:
    IR=(sal*0.10)
    INSS=(sal*0.10)
    FGTS=(sal*0.11)
    sf= (sal-INSS-IR)
    print("Seu salário bruto é: %.2f" % sal)
    print("(-) IR: %.2f" % IR)
    print("(-) INSS: %.2f" % INSS)
    print("    FGTS: %.2f" % FGTS)
    print("Total de descontos: %.2f" % (INSS+IR))
    print("Salário líquido: %.2f" % sf)

elif sal >= 2500:
    IR=(sal*0.10)
    INSS=(sal*0.10)
    FGTS=(sal*0.11)
    sf= (sal-INSS-IR)
    print("Seu salário bruto é: %.2f" % sal)
    print("(-) IR: %.2f" % IR)
    print("(-) INSS: %.2f" % INSS)
    print("    FGTS: %.2f" % FGTS)
    print(" Total de descontos: %.2f" % (INSS+IR))
    print("Salário líquido: %.2f" % sf)

elif horas_mes or valor_hora == str:
    print("Digite apenas números")

else:
    print("Tente novamente")
    


