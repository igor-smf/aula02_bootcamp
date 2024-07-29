CONSTANTE_BUNUS = 1000

nome = input("Digite o seu nome: ")

if nome.isdigit():
    print("Você digitou seu nome errado.")
    exit()
elif len(nome) == 0:
    print("Você não digitou nada.")
    exit()
elif nome.isspace():
    print("Você digitou só espaço.")

try:
    salario = float(input("Digite o seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")

try:
    bonus = float(input("Digite o seu bonus: "))
    if bonus < 0:
        print("Por favor, digite um valor positivo para o bonus.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")


valor_bonus = CONSTANTE_BUNUS + (salario * bonus)

print(f"Olá {nome}, o seu valor bônus foi de {valor_bonus}")