#Você foi contratado(a) como cientista de dados de uma associação de skate. 
#Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano,
#você precisa criar um código que calcula a pontuação dos(as) atletas.
# Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

#Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor
# pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram.
# Retorne a média para apresentar o texto: "Nota da manobra: [media]"

notas = []
while len(notas) < 5:
    try:
        nota_digitada = float(input(f"Digite uma nota {len(notas)+1} entre 0 e 10: "))
        if 0 <= nota_digitada <= 10:
            notas.append(nota_digitada)
        else:
            print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

def calcular_notas(lista_de_notas: list) -> float:
    notas_copia = lista_de_notas.copy()
    notas_copia.remove(max(notas_copia))
    notas_copia.remove(min(notas_copia))
    media = sum(notas_copia) / len(notas_copia)
    return media

media = calcular_notas(notas)
print(f"Nota da manobra: {media:.2f}")
