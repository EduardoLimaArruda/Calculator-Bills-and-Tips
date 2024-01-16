print("Bill and Tip Calculator")
Conta = float(input("What is the total value of the bill?\n"))
Porcentagem = float(input("What percentage of tip do you want to give?\n"))
Pessoas = float(input("How many people will split the bill?\n"))

Porcentagem1 = Porcentagem / 100 * Conta
Gorjeta = Porcentagem1 / Pessoas

Conta1 = Conta / Pessoas - Gorjeta
Gorjeta2 = Gorjeta / Pessoas

print("Each person will pay: " + str(round(Conta1,2)))
print("The tip amount will be: " + str(round(Gorjeta2,2)))

enter = input("Press Enter to close")