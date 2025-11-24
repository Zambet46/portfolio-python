from random import randint

print("Seja bem-vindo ao nosso sistema de sorteios!\n Por favor digite o número de pessoas para que seja realizado o sorteio: ")

try:
    # Tenta converter a entrada para inteiro
    entrada = int(input())
    
    # Verifica se o número é logicamente válido
    if entrada <= 0:
        print("Erro: O número de participantes deve ser positivo.")
    else:
        # Só executa o sorteio se a entrada for válida
        numero_sorteado = randint(1, entrada)
        print(f"O número sorteado foi: {numero_sorteado}, parabéns você foi sorteado!")

except ValueError:
    # Captura o erro se a conversão para int falhar
    print("Erro: O valor digitado não é um número válido. Por favor, tente novamente.")