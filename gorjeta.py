print("Calculadora de Conta e Gorjeta")
Conta = float(input("Qual o valor total da conta?\n"))
Porcentagem = float(input("Qual porcetagem em gorjeta você deseja dar?\n"))
Pessoas = float(input("Quantas pessoas vão dividir a conta?\n"))

Porcentagem1 = Porcentagem / 100 * Conta
Gorjeta = Porcentagem1 / Pessoas

Conta1 = Conta / Pessoas - Gorjeta
Gorjeta2 = Gorjeta / Pessoas

print("Cada pessoa pagará: " + str(round(Conta1,2)))
print("O valor da gorjeta será: " + str(round(Gorjeta2,2)))

enter = input("Aperte Enter para fechar")